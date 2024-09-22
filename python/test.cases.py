import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def run_translator(self, input_str):
        # Split the input string into a list of arguments
        command = ['python3', 'translator.py'] + input_str.split()
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()

    def test_basic_test(self):
        input_str = "Hello Mic Check 123"
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............OOO..O..OO...OO...............OOO....O.OO..O..O..OO....O...O........O.OOOO.....O.O...OO...."
        self.assertEqual(self.run_translator(input_str), expected_output)
    
    def test_basic_test_reverse(self):
        input_str = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............OOO..O..OO...OO...............OOO....O.OO..O..O..OO....O...O........O.OOOO.....O.O...OO...."
        expected_output = "Hello Mic Check 123"
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_all_nums(self):
        input_str = "202409213567800"
        expected_output = ".O.OOOO.O....OOO..O.O...OO.O...OOO...OO...O.O...O.....OO....O..O..OOO...OOOO..O.OO...OOO...OOO.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_all_nums_reverse(self):
        expected_output = "202409213567800"
        input_str = ".O.OOOO.O....OOO..O.O...OO.O...OOO...OO...O.O...O.....OO....O..O..OOO...OOOO..O.OO...OOO...OOO.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_all_uppercase(self):
        input_str = "I AM NOT YELLING"
        expected_output = ".....O.OO..............OO..........OOO..O............OOO.OO......OO..OO......O.OOOO............OOO.OOO.....OO..O.......OO.O.O......OO.O.O......O.OO........OOO.OO......OOOOO.."
        self.assertEqual(self.run_translator(input_str), expected_output)
    
    def test_all_uppercase_reverse(self):
        expected_output = "I AM NOT YELLING"
        input_str = ".....O.OO..............OO..........OOO..O............OOO.OO......OO..OO......O.OOOO............OOO.OOO.....OO..O.......OO.O.O......OO.O.O......O.OO........OOO.OO......OOOOO.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_mixed_case(self):
        input_str = "tHE QuiCk broWn foX juMPs over the lazy DOG"
        expected_output = ".OOOO......OO.OO.......OO..O.............OOOOOO.O...OO.OO........OOO....O...O.......O.O...O.OOO.O..OO......O.OOO.OOO.OO.......OOO...O..OO......OOO..OO.......OOO..O...OO.....OOO..O......OOOO.O..OO.O.......O..OO.O.O.OOO..O..O.OOO........OOOO.O.OO..O..O........O.O.O.O.....O..OOOOO.OOO...........OOO.O.......OO..OO......OOOOO.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_mixed_case_reserse(self):
        expected_output = "tHE QuiCk broWn foX juMPs over the lazy DOG"
        input_str = ".OOOO......OO.OO.......OO..O.............OOOOOO.O...OO.OO........OOO....O...O.......O.O...O.OOO.O..OO......O.OOO.OOO.OO.......OOO...O..OO......OOO..OO.......OOO..O...OO.....OOO..O......OOOO.O..OO.O.......O..OO.O.O.OOO..O..O.OOO........OOOO.O.OO..O..O........O.O.O.O.....O..OOOOO.OOO...........OOO.O.......OO..OO......OOOOO.."
        self.assertEqual(self.run_translator(input_str), expected_output)

if __name__ == '__main__':
    unittest.main()