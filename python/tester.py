import unittest
from translator import BrailleTranslator

class TestTranslator(unittest.TestCase):
    def test_output(self):
        translator = BrailleTranslator()
        # Test the translation of the string "Abc 123 xYz"
        self.assertEqual(translator.translate("Abc 123 xYz"), ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")
        
if __name__ == '__main__':
    unittest.main()