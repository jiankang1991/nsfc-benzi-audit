"""Exercise structural checks with disposable repositories, without network access."""

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from validate_repo import validate


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="nsfc-validator-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("LICENSE", "Example license\n")
        self.write("nsfc-benzi-audit/LICENSE", "Example license\n")
        self.write("nsfc-benzi-audit/SKILL.md", "---\nname: nsfc-benzi-audit\ndescription: Example\n---\n")
        self.write("资料/说明.md", "# 研究 条件\n\n## 重复\n\n## 重复\n")
        self.write("README.md", "[中文](资料/说明.md#研究-条件)\n[重复](资料/说明.md#重复-1)\n\n```text\n[示例](absent.md)\n```\n")

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def assert_error(self, expected, **kwargs):
        errors = validate(self.root, **kwargs)["errors"]
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_valid_unicode_anchors_duplicate_headings_and_fenced_examples(self):
        self.assertEqual(validate(self.root)["errors"], [])

    def test_frontmatter_name_and_description_length(self):
        self.write("nsfc-benzi-audit/SKILL.md", f"---\nname: other\ndescription: {'x' * 1025}\n---\n")
        self.assert_error("differs from directory")
        self.assert_error("exceeds 1024")

    def test_missing_file(self):
        self.write("README.md", "[附件](missing.md)\n")
        self.assert_error("Missing link")

    def test_missing_heading(self):
        self.write("README.md", "[附件](资料/说明.md#不存在)\n")
        self.assert_error("Missing heading")

    def test_unclosed_fence(self):
        self.write("README.md", "```text\nunfinished\n")
        self.assert_error("Unclosed code fence")

    def test_invalid_json(self):
        self.write("record.json", "{unfinished")
        self.assert_error("Cannot parse record.json")

    def test_license_mismatch(self):
        self.write("nsfc-benzi-audit/LICENSE", "Different license\n")
        self.assert_error("LICENSE differs")

    def test_manifest_detects_changed_and_missing_input(self):
        relative = "资料/说明.md"
        expected = hashlib.sha256((self.root / relative).read_bytes()).hexdigest()
        manifest = self.write("manifest.json", json.dumps({relative: expected}))
        self.assertEqual(validate(self.root, manifest)["errors"], [])
        self.write(relative, "Changed\n")
        self.assert_error("Snapshot mismatch", manifest=manifest)
        (self.root / relative).unlink()
        self.assert_error("Snapshot mismatch", manifest=manifest)


if __name__ == "__main__":
    unittest.main()
