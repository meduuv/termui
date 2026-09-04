import unittest

from termui.core import box, color, gradient, progress, table, visible_len


class TermUITests(unittest.TestCase):
    def test_gradient_preserves_visible_text_width(self):
        self.assertEqual(visible_len(gradient("APEIRON")), len("APEIRON"))

    def test_color_code_is_validated(self):
        with self.assertRaises(ValueError):
            color("x", 999)

    def test_progress_is_clamped(self):
        self.assertIn("100.0%", progress(200, 100, 10))
        self.assertIn("0.0%", progress(-5, 100, 10))

    def test_table_contains_headers_and_rows(self):
        output = table(["NAME", "VALUE"], [["alpha", 1]])
        self.assertIn("NAME", output)
        self.assertIn("alpha", output)

    def test_box_renders_title(self):
        self.assertIn("status", box("status", ["online"], width=20))


if __name__ == "__main__":
    unittest.main()
