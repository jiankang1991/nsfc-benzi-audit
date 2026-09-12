"""Check source retrieval and snapshot boundaries on realistic Markdown shapes."""

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "nsfc-benzi-audit/scripts/review_index.py"
SPEC = importlib.util.spec_from_file_location("review_index", SCRIPT)
review_index = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(review_index)


class ReviewIndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="nsfc-index-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "材料/申请.md"
        self.source.parent.mkdir()
        self.output = self.root / "work/index.json"

    def build(self, text, limit=120):
        self.source.write_text(text, encoding="utf-8")
        return review_index.build([self.source], self.output, limit)["sources"][0]

    def test_every_line_is_retrievable_exactly_once(self):
        text = "# 正文\n\n" + "\n\n".join(f"第{i}段：" + "证据内容" * 20 for i in range(8))
        indexed = self.build(text)
        lines = text.splitlines(keepends=True)
        covered = []
        for chunk in indexed["chunks"]:
            covered.extend(range(chunk["start_line"], chunk["end_line"] + 1))
            retrieved = review_index.read_chunk(self.output, chunk["id"]).split("\n", 1)[1]
            expected = "".join(f"{i}: {lines[i-1]}" for i in range(chunk["start_line"], chunk["end_line"] + 1))
            self.assertEqual(retrieved, expected)
        self.assertEqual(covered, list(range(1, len(lines) + 1)))

    def test_fenced_headings_are_not_indexed_or_split(self):
        text = "# 正文\n\n```text\n# 不是标题\n\n" + "x" * 300 + "\n```\n\n## 附件\n内容\n"
        indexed = self.build(text)
        self.assertEqual([h["title"] for h in indexed["headings"]], ["正文", "附件"])
        code = next(c for c in indexed["chunks"] if c["start_line"] <= 3 <= c["end_line"])
        self.assertGreaterEqual(code["end_line"], 7)
        self.assertTrue(code["oversized"])

    def test_table_stays_together_and_oversize_is_visible(self):
        text = "# 表\n\n| 样本 | 组别 |\n| --- | --- |\n" + "| X | 训练 |\n" * 30 + "\n后文\n"
        indexed = self.build(text)
        table = next(c for c in indexed["chunks"] if c["start_line"] <= 3 <= c["end_line"])
        self.assertGreaterEqual(table["end_line"], 34)
        self.assertTrue(table["oversized"])

    def test_frontmatter_and_nested_heading_context(self):
        indexed = self.build("---\ntitle: 示例\n# YAML 注释\n---\n# 一级\n\n## 二级\n说明\n\n### 三级\n证据\n", limit=15)
        self.assertEqual([h["title"] for h in indexed["headings"]], ["一级", "二级", "三级"])
        self.assertEqual(indexed["headings"][-1]["context"], ["一级", "二级", "三级"])

    def test_leading_separator_without_metadata_closer_keeps_headings(self):
        indexed = self.build("---\n\n# 正文\n说明\n\n## 科学问题\n研究关系\n\n## 验证\n证据\n", limit=15)
        self.assertEqual([h["title"] for h in indexed["headings"]], ["正文", "科学问题", "验证"])
        self.assertGreater(len(indexed["chunks"]), 1)

    def test_source_change_blocks_verify_and_read(self):
        indexed = self.build("# 文本\n原证据\n")
        self.source.write_text("# 文本\n新证据\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Source changed"):
            review_index.load_verified(self.output)
        with self.assertRaisesRegex(ValueError, "Source changed"):
            review_index.read_chunk(self.output, indexed["chunks"][0]["id"])

    def test_relative_paths_survive_moving_bundle(self):
        self.build("# 文本\n证据\n")
        destination = self.root / "moved"
        destination.mkdir()
        shutil.move(str(self.source.parent), destination / "材料")
        shutil.move(str(self.output.parent), destination / "work")
        _, sources = review_index.load_verified(destination / "work/index.json")
        self.assertEqual(sources["S01"][0], destination / "材料/申请.md")

    def test_identical_basenames_remain_distinct(self):
        self.source.write_text("# 主稿\n", encoding="utf-8")
        other = self.root / "旧稿/申请.md"
        other.parent.mkdir()
        other.write_text("# 历史\n", encoding="utf-8")
        index = review_index.build([self.source, other], self.output)
        self.assertNotEqual(index["sources"][0]["path"], index["sources"][1]["path"])
        self.assertEqual([s["id"] for s in index["sources"]], ["S01", "S02"])

    def test_bom_crlf_and_final_line_without_newline(self):
        self.source.write_bytes(b"\xef\xbb\xbf" + "# 标题\r\n\r\n末行".encode())
        index = review_index.build([self.source], self.output)
        output = review_index.read_chunk(self.output, index["sources"][0]["chunks"][0]["id"])
        self.assertTrue(output.endswith("3: 末行"))
        self.assertIn("1: # 标题\r\n", output)

    def test_sources_and_existing_index_are_never_overwritten(self):
        self.source.write_text("source", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "cannot replace"):
            review_index.build([self.source], self.source)
        review_index.build([self.source], self.output)
        original = self.output.read_bytes()
        with self.assertRaisesRegex(ValueError, "already exists"):
            review_index.build([self.source], self.output)
        self.assertEqual(self.output.read_bytes(), original)
        self.assertEqual(self.source.read_text(), "source")

    def test_empty_input_and_invalid_chunk(self):
        indexed = self.build("")
        self.assertEqual(indexed["chunks"], [])
        with self.assertRaisesRegex(ValueError, "Unknown chunk"):
            review_index.read_chunk(self.output, "S01-C999")

    def test_binary_input_is_rejected_without_output(self):
        self.source.write_bytes(b"binary\0data")
        with self.assertRaisesRegex(ValueError, "plain text"):
            review_index.build([self.source], self.output)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
