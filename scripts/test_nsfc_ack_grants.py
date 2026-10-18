"""Offline check of grant-number extraction for nsfc_ack_grants.py."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "nsfc-benzi-audit" / "scripts"))
from nsfc_ack_grants import grants, render  # noqa: E402

NSFC = "https://openalex.org/F4320321001"
WORKS = [
    {"title": "A", "publication_year": 2025, "authorships": [], "awards": [
        {"funder_id": NSFC, "funder_award_id": "42374018"},          # 2023, kept
        {"funder_id": NSFC, "funder_award_id": "41974006"},          # 2019, out of range
        {"funder_id": NSFC, "funder_award_id": "RCYX20210706092140076"},  # not a 批准号
        {"funder_id": "https://openalex.org/F1", "funder_award_id": "62271234"},  # other funder
    ]},
    {"title": "B", "publication_year": 2024, "authorships": [], "awards": [
        {"funder_id": NSFC, "funder_award_id": "42374018"},
        {"funder_id": NSFC, "funder_award_id": "U2239202"},          # joint fund, 2022
    ]},
]


class AckGrantTests(unittest.TestCase):
    def test_extraction(self):
        found = grants(WORKS, 2021, 2025)
        self.assertEqual(sorted(found), ["42374018", "U2239202"])
        self.assertEqual(len(found["42374018"]), 2)

    def test_partial_scan_is_marked_lower_bound(self):
        text = render("InSAR", "2023-01-01", grants(WORKS, 2021, 2025), 2, 10)
        self.assertIn("计数为下限", text)
        self.assertIn("| 42374018 | 2023 | 2 |", text)


if __name__ == "__main__":
    unittest.main()
