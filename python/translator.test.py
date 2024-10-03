import unittest
import subprocess

import os
print(os.getcwd())
class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script
        #command = ["python3", "/Users/hansonzhliu/Documents/shopify-take-home/eng-intern-challenge/python/translator.py", "Abc", "123", "xYz"]
        command = ["python3", "translator.py", ".....OO.....O.O...OO....", ".O.OOOO.....O.O...OO....", "OO..OO.....OOO.OOOO..OOO"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        #expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        expected_output = "Abc 123 xYz"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()

    