import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output(self):
        arg_and_expected_output_dict = {
            "Hello world": ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..",
            "42": ".O.OOOOO.O..O.O...",
            ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....": "Abc 123"
        }
        
        for arg, expected_output in arg_and_expected_output_dict.items():
            result = subprocess.run(["python3", "translator.py", arg], capture_output=True, text=True)
            self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
