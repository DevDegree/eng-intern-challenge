import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # First test case: "Hello world"
        command = ["python3", "translator.py", "Hello", "world"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)
        
        # Second test case: "42"
        command = ["python3", "translator.py", "42"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".O.OOOOO.O..O.O..."
        self.assertEqual(result.stdout.strip(), expected_output)
        
        # Third test case: "Abc 123"
        command = ["python3", "translator.py", "Abc", "123"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
