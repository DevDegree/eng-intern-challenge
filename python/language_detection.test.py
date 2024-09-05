import unittest

from translator import Braille, English, LanguageDetector

class TestBrailleValidator(unittest.TestCase):
    def test_contain_only_O_or_dot(self):
        input = "0..a.."
        assert not Braille(input).contain_only_O_or_dot()

    def test_not_multiple_of_6(self):
        input = "O......"
        assert not Braille(input).is_multiple_of_6()
    
    def test_invalid_sequence(self):
        input = "OOOOOO"
        assert not Braille(input).is_valid_sequence()

    def test_valid_sequence(self):
        input = "O....."
        assert Braille(input).is_valid_sequence()
    
    def test_valid_braille(self):
        input = "O....."
        assert Braille(input).valid()
    
    def test_invalid_braille(self):
        input = "O.a..."
        assert not Braille(input).valid()

class TestEnglishValidator(unittest.TestCase):
    def test_valid_english(self):
        input = "aB37"
        assert English(input).all_valid_character()
    
    def test_invalid_english(self):
        # Not in list of supported characters
        input = "*[]*&&%$"
        assert not English(input).all_valid_character()
    
    def test_invalid_english_2(self):
        input = "*[]*&&%$"
        assert not English(input).valid()

class TestLanguageDecoder(unittest.TestCase):
    def test_both_invalid(self):
        input = "*[]*&&%$"
        with self.assertRaises(ValueError):
            LanguageDetector(input).detect_language()

if __name__ == "__main__":
    unittest.main()