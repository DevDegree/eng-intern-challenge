# Test Cases file for translator.py
# Michael Han
# September 09 20


import unittest

from translator import english_to_braille_translation, braille_to_english_translation
class michael_han_dev_test(unittest.TestCase):
    #test the english to braille translation with numbers, should translate numbers to braille output
    def test_multiple_number(self):
        user_input = "42"
        result = english_to_braille_translation(user_input)
        
        expected_output = ".O.OOOOO.O..O.O..."
        self.assertEqual(result, expected_output, f"Failed on input '{user_input}': Expected '{expected_output}', but got '{result}'")
    
    #test the english to braille translation with words, should translate letters to braille output
    def test_multiple_word(self):
        user_input = "Shopify"
        result = english_to_braille_translation(user_input)
        
        expected_output = ".....O.OO.O.O.OO..O..OO.OOO.O..OO...OOO...OO.OOO"
        self.assertEqual(result, expected_output, f"Failed on input '{user_input}': Expected '{expected_output}', but got '{result}'")

    #test the braille to english translation, should translate braille to english output
    def test_braille_to_english_translation(self):
        user_input = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        result = braille_to_english_translation(user_input)
        
        expected_output = "Abc 123"
        self.assertEqual(result, expected_output, f"Failed on input '{user_input}': Expected '{expected_output}', but got '{result}'")
    
if __name__ == '__main__':
    unittest.main()       