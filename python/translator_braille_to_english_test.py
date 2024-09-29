import unittest
import subprocess
from translator import braille_to_english  # Import the braille_to_english function

class TestTranslator(unittest.TestCase):
    def test_braille_to_english(self):

        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        expected_output = "Abc 123 xYz"
        
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_hello_world(self):
        command = ["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]
        
        result = subprocess.run(command, capture_output=True, text=True)
             
        expected_output = "Hello world"

        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_empty_input(self):
        command = ["python3", "translator.py"]
        
        result = subprocess.run(command, capture_output=True, text=True)
             
        expected_output = ""

        self.assertEqual(result.stdout.strip(), expected_output)

    def test_numbers(self):
        command = ["python3", "translator.py", ".O.OOOOO.O..O.O..."]
        
        result = subprocess.run(command, capture_output=True, text=True)
             
        expected_output = "42"

        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_single_letter_and_decimal(self):
        command = ["python3", "translator.py", ".....OO............O.OOOO......O...OO.O..."]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        expected_output = "A 1.2"

        self.assertEqual(result.stdout.strip(), expected_output)


    def test_special_characters(self):

        test = ".OO..O" + "......" + "O....." + "......" + "..OOO."
        command = ["python3", "translator.py", test]

        result = subprocess.run(command, capture_output=True, text=True)

        expected_output = "< a !"


        self.assertEqual(result.stdout.strip(), expected_output)



if __name__ == '__main__':
    unittest.main()
