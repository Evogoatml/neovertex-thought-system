import json
from pathlib import Path
import tempfile
import unittest

from nexus_forge.config import ForgeConfig


class ForgeConfigTests(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(ForgeConfig(), ForgeConfig("deep", 1, "structured", 3))

    def test_rejects_invalid_controls(self):
        for kwargs in (
            {"mode": "unknown"},
            {"hardening": -1},
            {"hardening": True},
            {"output": "verbose"},
            {"think_depth": 6},
        ):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                ForgeConfig(**kwargs)

    def test_loads_json_and_rejects_unknown_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "settings.json"
            path.write_text(json.dumps({"mode": "quick", "hardening": 0}), encoding="utf-8")
            self.assertEqual(ForgeConfig.from_json_file(path), ForgeConfig("quick", 0))
            path.write_text('{"api_key":"do-not-accept"}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unknown config key"):
                ForgeConfig.from_json_file(path)


if __name__ == "__main__":
    unittest.main()
