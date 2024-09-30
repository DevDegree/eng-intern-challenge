import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def run_translator(self, input_string):
        # Command to run translator.py script
        command = ["python3", "translator.py", input_string]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip()

    def test_abc(self):
        input_string = "Abc"
        expected_output = ".....O.O...O..O.OOO"  # Adjust based on actual expected Braille output
        output, error = self.run_translator(input_string)
        self.assertEqual(output, expected_output)
        self.assertEqual(error, "")

    def test_numbers(self):
        input_string = "123"
        expected_output = ".O.OOOO.O.O.OO..O.OO"  # Adjust based on actual expected Braille output
        output, error = self.run_translator(input_string)
        self.assertEqual(output, expected_output)
        self.assertEqual(error, "")

    def test_mixed_case(self):
        input_string = "xYz"
        expected_output = "OO..O.OOO..OO..OO"  # Adjust based on actual expected Braille output
        output, error = self.run_translator(input_string)
        self.assertEqual(output, expected_output)
        self.assertEqual(error, "")

if __name__ == '__main__':
    unittest.main()
