import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        # expected_output = ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO"

        # I think this should be the expected output... your translation of 123 doesnt seem quite right based on the image on github
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # print("Actual Output:", repr(result.stdout.strip()))
        # print("Expected Output:", repr(expected_output.strip()))


        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    # MY UNIT TESTS
    def test_braille_to_english(self):
        # Braille string to be converted back to English
        braille_input = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # Command to run translator.py script with Braille input
        command = ["python3", "translator.py", braille_input]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected English output
        expected_output = "Abc 123 xYz"
        
        # Check translation from Braille back to English
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_helloworld(self):
        # Braille string to be converted back to English
        braille_input = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        
        # Command to run translator.py script with Braille input
        command = ["python3", "translator.py", braille_input]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected English output
        expected_output = "Hello world"
        
        # Check translation from Braille back to English
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_42(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "42"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        # expected_output = ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO"

        # I think this should be the expected output... your translation of 123 doesnt seem quite right based on the image on github
        expected_output = ".O.OOOOO.O..O.O..."
        
        # print("Actual Output:", repr(result.stdout.strip()))
        # print("Expected Output:", repr(expected_output.strip()))


        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
