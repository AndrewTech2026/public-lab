#!/usr/bin/env python3
"""Stdlib tests for the research-brief fixture (no pytest required)."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import brief  # noqa: E402


class BriefTests(unittest.TestCase):
    def test_render_drops_noise_and_orders_top(self):
        data = json.loads((ROOT / "events.json").read_text(encoding="utf-8"))
        text = brief.render(data)
        self.assertIn("cooler than consensus", text)
        self.assertIn("L2 fee spike", text)
        self.assertNotIn("unverified rumor", text)
        self.assertIn("No orders", text)
        self.assertNotIn("api_key", text.lower())

    def test_cli_exit_0(self):
        r = subprocess.run(
            [sys.executable, str(ROOT / "brief.py"), "--events", str(ROOT / "events.json")],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Research brief", r.stdout)

    def test_bad_json_exits_1(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            f.write("{not-json")
            bad = f.name
        r = subprocess.run(
            [sys.executable, str(ROOT / "brief.py"), "--events", bad],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(r.returncode, 1)


if __name__ == "__main__":
    unittest.main()
