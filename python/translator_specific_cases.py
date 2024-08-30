import unittest
import subprocess

class TestTranslatorSpecificCases(unittest.TestCase):

    def run_translator(self, input_string):
        # Command to run translator.py script
        command = ["python3", "translator.py", input_string]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        # Return the stripped output for comparison
        return result.stdout.strip()

    def test_hello_world(self):
        input_string = "Hello world"
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        output = self.run_translator(input_string)
        self.assertEqual(output, expected_output, f"Failed for input '{input_string}': Expected '{expected_output}', but got '{output}'")

    def test_42(self):
        input_string = "42"
        expected_output = ".O.OOOOO.O..O.O..."
        output = self.run_translator(input_string)
        self.assertEqual(output, expected_output, f"Failed for input '{input_string}': Expected '{expected_output}', but got '{output}'")

    def test_braille_to_text(self):
        input_string = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        expected_output = "Abc 123"
        output = self.run_translator(input_string)
        self.assertEqual(output, expected_output, f"Failed for input '{input_string}': Expected '{expected_output}', but got '{output}'")

if __name__ == '__main__':
    unittest.main()
