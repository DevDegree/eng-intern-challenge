import unittest
import translator
class TestTranslatorMethods(unittest.TestCase):

    def test_isBraille(self):
        self.assertTrue(translator.isBraille(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."))
        self.assertFalse(translator.isBraille("Hello world"))
        self.assertFalse(translator.isBraille(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O."))
        
    
    def test_translateBraille(self):
        self.assertEqual(translator.translateBraille(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."), "Hello world")
        self.assertEqual(translator.translateBraille(".O.OOOO.....O.O...OO....OO.O..O..O...O...OOOO...OOOO..O.OO...OO....OOO.."), "12345.67890")

    def test_translateEnglish(self):
        self.assertEqual(translator.translateEnglish("Hello world"), ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")
        self.assertEqual(translator.translateEnglish("12345.67890"), ".O.OOOO.....O.O...OO....OO.O..O..O...O...OOOO...OOOO..O.OO...OO....OOO..")

if __name__ == "__main__":
    unittest.main()