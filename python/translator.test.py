import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    
    def test_english_to_braille(self):
        # Command to run translator.py script with English input
        command = ["python3", "translator.py", "Abc", "123", "xYz"]

        result = subprocess.run(command, capture_output=True, text=True)
   
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
 
        self.assertEqual(result.stdout.strip(), expected_output, "English to Braille translation did not match expected result.")
        

        if result.stderr:
            self.fail(f"Script produced errors: {result.stderr.strip()}")

    def test_braille_to_english(self):
        # Command to run translator.py script with Braille input
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
  
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected English output
        expected_output = "Abc 123 xYz"  # Replace with actual expected English text
        
        self.assertEqual(result.stdout.strip(), expected_output, "Braille to English translation did not match expected result.")
        
        if result.stderr:
            self.fail(f"Script produced errors: {result.stderr.strip()}")

if __name__ == '__main__':
    unittest.main()