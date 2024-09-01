import unittest

from translator import is_braille, english_to_braille, braille_to_english

class TestBrailleDetection(unittest.TestCase):
    # Ambiguous Input Detection
    def test_decimal_input(self):
        self.assertEqual(is_braille("O.O"), False)

    # Detection of Braille Input
    def test_detection_of_braille(self):
        self.assertEqual(is_braille("O..O.O.O.O.O..O.....O...O.O.OO"), True)

    # Detection of English Input
    def test_detection_of_english(self):
        self.assertEqual(is_braille("Hello"), False)

    def test_detection_of_ambiguous_braille(self):
        self.assertEqual(is_braille("O.O.O."), True)

    def test_detection_of_fake_braille(self):
        self.assertEqual(is_braille("O.O.O"), False)

    def test_detection_of_braille_with_spaces(self):
        self.assertEqual(is_braille("O..O.O.O.O.O..O.....O...O.O.OO      "), False)

class TestBrailleTranslator(unittest.TestCase):
    # Given Examples
    def test_given1(self):
        self.assertEqual(english_to_braille("Hello world"), ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")

    def test_given2(self):
        self.assertEqual(english_to_braille("42"), ".O.OOOOO.O..O.O...")

    def test_given3(self):
        self.assertEqual(braille_to_english(".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."), "Abc 123")

    # Reverse given Examples
    def test_given4(self):
        self.assertEqual(braille_to_english(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."), "Hello world")
    
    def test_given5(self):
      self.assertEqual(braille_to_english(".O.OOOOO.O..O.O..."), "42")

    def test_given6(self):
        self.assertEqual(english_to_braille("Abc 123"), ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")

    # New cases
    def test_simple_english_to_braille(self):
        self.assertEqual(english_to_braille("Hello"), ".....OO.OO..O..O..O.O.O.O.O.O.O..OO.")

    def test_braille_to_english(self):
        self.assertEqual(braille_to_english(".....OO.OO..O..O..O.O.O.O.O.O.O..OO."), "Hello")

    def test_single_capital_letter(self):
        self.assertEqual(english_to_braille("A"), ".....OO.....")

    def test_multiple_capital_letters(self):
        self.assertEqual(english_to_braille("HELLO"), ".....OO.OO.......OO..O.......OO.O.O......OO.O.O......OO..OO.")

    def test_numbers(self):
        self.assertEqual(english_to_braille("123"), ".O.OOOO.....O.O...OO....")

    def test_mixed_letters_numbers(self):
        self.assertEqual(english_to_braille("A1B2;"), ".....OO......O.OOOO..........OO.O....O.OOOO.O.....O.O.")

    def test_punctuation(self):
        self.assertEqual(english_to_braille(",!?."), "..O.....OOO...O.OO..OO.O")

    def test_decimal_swapping(self):
        self.assertEqual(english_to_braille("Hello. 12.34 a"), ".....OO.OO..O..O..O.O.O.O.O.O.O..OO...OO.O.......O.OOOO.....O.O....O...OOO....OO.O........O.....")

    def test_empty_input(self):
        self.assertEqual(english_to_braille(""), "")

    def test_unsupported_characters(self):
        self.assertEqual(english_to_braille("Hi$"), ".....OO.OO...OO...")

    def test_invalid_input(self):
        self.assertEqual(english_to_braille("%%%%"), "")

    def test_invalid_braille_input(self):
        self.assertEqual(braille_to_english(""), "")

    def test_long_sequence(self):
        long_string = "O.O.O." * 50
        expected_output = "l" * 50
        self.assertEqual(braille_to_english(long_string), expected_output)

    def test_long_non_num(self):
        self.assertEqual(braille_to_english("O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O."), "abcdefghijk")

    def test_long_num2(self):
        self.assertEqual(braille_to_english(".O.OOOO.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO.."), "1234567890")

    def test_ambiguous_o_braille(self):
        self.assertEqual(english_to_braille("12>34 eod"), ".O.OOOO.....O.O...O..OO..O.OOOOO....OO.O........O..O..O..OO.OO.O..")

    def test_ambiguous_o_english(self):
        self.assertEqual(braille_to_english(".O.OOOO.....O.O...O..OO..O.OOOOO....OO.O........O..O..O..OO.OO.O.."), "12>34 eod")

    # Conversions made simpler by going 2 depth.
    def test_multi_depth(self):
        strings_list = ["Hello World", "1234567890", "A quick brown fox jumps over 13 lazy dogs.", "What?! Thats amazing; truly outstanding.", "Welcome to the year 2024!", "Happy New Year!", "CIBC at 9:00 A.M. - Important Meeting.", "1.23 or 0.5? Which is larger?", "N.Y.C., L.A., and S.F.", "U.S.A. number 1 in medals.", "Python3.8 vs. JavaScript", "Good morning, Dr. Smith.", "The cost is 20.00 dollars (incl. taxes).", "(123) 456-7890", "Hello-world123", "Hello", "A", "123", "Abc 123", "42", "Abc 123 xYz", "A1B2;", ",!?.", "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"]

        for string in strings_list:
            self.assertEqual(braille_to_english(english_to_braille(string)), string)


if __name__ == '__main__':
    unittest.main()