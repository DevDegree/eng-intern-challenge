import unittest
import subprocess

from translator import (isValidBraille, translateToBraille, translateToEnglish)

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_is_valid_braille(self):
        # Test valid braille
        self.assertTrue(isValidBraille(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"))
        
        # Test invalid braille length
        self.assertFalse(isValidBraille("...."))
        
        # Test invalid braille symbol
        self.assertFalse(isValidBraille("OOOOOO"))
        
        # Test invalid braille character
        self.assertFalse(isValidBraille("0....."))
        
        # Test valid braille symbol
        self.assertTrue(isValidBraille("O....."))
        
    def test_translate_to_braille(self):
        # Test capital letter
        self.assertEqual(translateToBraille("A"), ".....OO.....")
        
        # Test lowercase letter
        self.assertEqual(translateToBraille("a"), "O.....")
        
        # Test number
        self.assertEqual(translateToBraille("1"), ".O.OOOO.....")
        
        # Test space
        self.assertEqual(translateToBraille(" "), "......")
            
        # Test base cases
        self.assertEqual(translateToBraille("Hello world"), ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")
        self.assertEqual(translateToBraille("42"), ".O.OOOOO.O..O.O...")
        self.assertEqual(translateToBraille("Abc 123"), ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")

        # Validate all braille alphabet chars and numbers
        self.assertEqual(translateToBraille("abcdefghijklmnopqrstuvwxyz"), "O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO")
        self.assertEqual(translateToBraille("1234567890"), ".O.OOOO.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..")

        # Test invalid character
        with self.assertRaises(Exception):
            translateToBraille("!")

    def test_translate_to_english(self):
        # Test capital letter
        self.assertEqual(translateToEnglish(".....OO....."), "A")
        
        # Test lowercase letter
        self.assertEqual(translateToEnglish("O....."), "a")
        
        # Test number
        self.assertEqual(translateToEnglish(".O.OOOO....."), "1")
        
        # Test space
        self.assertEqual(translateToEnglish("......"), " ")
        
        # Test lowercase letter follows
        self.assertEqual(translateToEnglish(".....OO.....O....."), "Aa")
        
        # Test number follows
        self.assertEqual(translateToEnglish(".O.OOOO.....O....."), "11")
        
        # Test number follows letter
        self.assertEqual(translateToEnglish("O......O.OOOO....."), "a1")
        
        # Test letter follows number
        self.assertEqual(translateToEnglish(".O.OOOO...........O....."), "1 a")
            
        # Test base cases
        self.assertEqual(translateToEnglish(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."), "Hello world")
        self.assertEqual(translateToEnglish(".O.OOOOO.O..O.O..."), "42")
        self.assertEqual(translateToEnglish(".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."), "Abc 123")
                
        # Test invalid character
        with self.assertRaises(Exception):
            translateToEnglish("!")

        # Validate all braille alphabet chars and numbers
        self.assertEqual(translateToEnglish("O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO"), "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(translateToEnglish(".O.OOOO.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO.."), "1234567890")

if __name__ == '__main__':
    unittest.main()
