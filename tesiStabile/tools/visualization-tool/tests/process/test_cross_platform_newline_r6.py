"""Ensure renderer output is byte-identical on Windows and POSIX."""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class CrossPlatformNewlineTests(unittest.TestCase):
    def test_renderer_all_text_outputs_force_lf(self):
        tree = ast.parse((ROOT / "src/ddta_process.py").read_text(encoding="utf-8"))
        calls = [node for node in ast.walk(tree)
                 if isinstance(node, ast.Call)
                 and isinstance(node.func, ast.Attribute)
                 and node.func.attr == "write_text"]
        self.assertEqual(5, len(calls), "Review added write_text calls for Windows LF stability")
        for node in calls:
            values = {kw.arg: kw.value for kw in node.keywords}
            self.assertIn("newline", values, f"write_text at line {node.lineno} must choose LF explicitly")
            self.assertIsInstance(values["newline"], ast.Constant)
            self.assertEqual("\n", values["newline"].value)

    def test_packaged_reference_is_lf_only(self):
        for path in (ROOT / "output/r7_candidate").rglob("*"):
            if path.is_file() and path.suffix in (".json", ".md", ".mmd"):
                self.assertNotIn(b"\r\n", path.read_bytes(), str(path))

if __name__ == "__main__":
    unittest.main()
