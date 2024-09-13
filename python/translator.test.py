import unittest
import subprocess
import random
import string

class TestTranslator(unittest.TestCase):
    def run_translator(self, input_text: str) -> str:
        command = ["python3", "translator.py"] + input_text.split()
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()
    
    def test_simple_1(self):
        english = "Hello world"
        braille = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)
        
    def test_simple_2(self):
        english = "42"
        braille = ".O.OOOOO.O..O.O..."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)
        
    def test_simple_3(self):
        english = "Abc 123"
        braille = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)
    
    def test_all_letters(self):
        english = "abcdefghijklmnopqrstuvwxyz"
        braille = "O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO"
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)
        
    def test_all_digits(self):
        english = "1234567890"
        braille = ".O.OOOO.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO.."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)
    
    def test_lower_letter(self):
        english = "a"
        braille = "O....."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)
        
    def test_upper_letter(self):
        english = "A"
        braille = ".....OO....."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)
        
    def test_mixed_letter(self):
        english = "aAaaA"
        braille = "O..........OO.....O.....O..........OO....."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)
        
    def test_letters_with_space(self):
        english = "a a"
        braille = "O...........O....."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)    
    
    def test_single_digit(self):
        english = "0"
        braille = ".O.OOO.OOO.."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)
        
    def test_digits_with_space(self):
        english = "0 0"
        braille = ".O.OOO.OOO.........O.OOO.OOO.."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)
        
    def test_mixed_letter_digit(self):
        english = "a0"
        braille = "O......O.OOO.OOO.."
        self.assertEqual(self.run_translator(english), braille)
        self.assertEqual(self.run_translator(braille), english)

    def test_random_letter_input(self):
        for _ in range(10):
            input = []
            for _ in range(6): 
                random_letters = "".join(random.choices(string.ascii_letters, k=5))
                input.append(random_letters)
            input_text = " ".join(input)
            braille_output = self.run_translator(input_text)
            english_output = self.run_translator(braille_output)
            self.assertEqual(
                input_text, 
                english_output, 
                f"Input: {input_text}\nbraille_output: {braille_output}\nenglish_output: {english_output}",
            )
            
    def test_random_number_input(self):
        for _ in range(10):
            input = []
            for _ in range(6): 
                random_numbers = "".join(random.choices(string.digits, k=5))
                input.append(random_numbers)
            input_text = " ".join(input)
            braille_output = self.run_translator(input_text)
            english_output = self.run_translator(braille_output)
            self.assertEqual(
                input_text, 
                english_output, 
                f"Input: {input_text}\nbraille_output: {braille_output}\nenglish_output: {english_output}",
            )        
                
    def test_random_mixed_input(self):
        for _ in range(10):
            input = []
            for _ in range(6): 
                random_numbers = "".join(random.choices(string.digits, k=5))
                random_letters = "".join(random.choices(string.ascii_letters, k=5))
                input.append(random.choice([random_letters, random_numbers]))
            input_text = " ".join(input)
            braille_output = self.run_translator(input_text)
            english_output = self.run_translator(braille_output)
            self.assertEqual(
                input_text, 
                english_output, 
                f"Input: {input_text}\nbraille_output: {braille_output}\nenglish_output: {english_output}",
            )

if __name__ == '__main__':
    unittest.main()