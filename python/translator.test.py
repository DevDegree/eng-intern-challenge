import unittest
import subprocess
from translator import *

class TestTranslator(unittest.TestCase):
    
    def test_output(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...."
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    
    def test_translate_to_braille(self):
        self.assertEqual(translate_to_braille('Abc'), 
                        '.....OO.....O.O...OO....')
        self.assertEqual(translate_to_braille('42'), '.O.OOOOO.O..O.O...')
        self.assertEqual(
            translate_to_braille('Abc 123 xYz'), 
                '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO'
            )

if __name__ == '__main__':
    unittest.main()
