import unittest

class TestBackspaceReplacer(unittest.TestCase):
    def setUp(self):
        self.backspace_replacer = BackspaceReplacer()

    def test_replace_stars_no_stars(self):
        input_string = "abcdef"
        result = self.backspace_replacer.replace_stars(input_string)
        self.assertEqual(result, input_string)

    def test_replace_stars_one_star_at_beginning(self):
        input_string = "*abc"
        result = self.backspace_replacer.replace_stars(input_string)
        self.assertEqual(result, "abc")

    def test_replace_stars_one_star_in_middle(self):
        input_string = "abc*d"
        result = self.backspace_replacer.replace_stars(input_string)
        self.assertEqual(result, "ad")

    def test_replace_stars_one_star_at_end(self):
        input_string = "abc*"
        result = self.backspace_replacer.replace_stars(input_string)
        self.assertEqual(result, "abc")

    def test_replace_stars_two_stars_consecutive(self):
        input_string = "abc**def"
        result = self.backspace_replacer.replace_stars(input_string)
        self.assertEqual(result, "def")

    def test_replace_stars_two_stars_non_consecutive(self):
        input_string = "abc*def*ghi"
        result = self.backspace_replacer.replace_stars(input_string)
        self.assertEqual(result, "adefghi")

    def test_replace_stars_empty_string(self):
        input_string = ""
        result = self.backspace_replacer.replace_stars(input_string)
        self.assertEqual(result, "")

    def test_replace_stars_none_input(self):
        result = self.backspace_replacer.replace_stars(None)
        self.assertEqual(result, "")

    def test_replace_stars_non_string_input(self):
        with self.assertRaises(TypeError):
            self.backspace_replacer.replace_stars(123)

if __name__ == "__main__":
    unittest.main()
