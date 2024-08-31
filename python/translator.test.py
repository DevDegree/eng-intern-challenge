import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script
        tests = [
            ["Abc", "123", "xYz", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"],
            [".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO", "Abc 123 xYz"],
            ["Hello world", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."],
            [".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..", "Hello world"],
            ["42", ".O.OOOOO.O..O.O..."],
            [".O.OOOOO.O..O.O...", "42"],
            ["Abc 234", ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O.."],
            [".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..", "Abc 234"],
            ["A", ".....OO....."],
            [".....OO.....", "A"],
            ["", ""],
        ]

        for test in tests:
            # add python command to the beginning of the list
            test_input = test
            test_input.insert(0, "python3")
            test_input.insert(1, "translator.py")
            print(test_input[:-1])

            # Run the command and capture output
            result = subprocess.run(test_input[:-1], capture_output=True, text=True)
            
            # Expected output without the newline at the end
            expected_output = test[-1]
            
            # Strip any leading/trailing whitespace from the output and compare
            self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
