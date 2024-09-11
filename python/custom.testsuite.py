import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def run_translator(self, input_str):
        # Split the input string into a list of arguments
        command = ['python3', 'translator.py'] + input_str.split()
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()

    def test_sentence_with_caps_and_num(self):
        input_str = "Order 123 Shirt"
        expected_output = ".....OO..OO.O.OOO.OO.O..O..O..O.OOO........O.OOOO.....O.O...OO...............O.OO.O.O.OO...OO...O.OOO..OOOO."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_simple_mixed(self):
        input_str = "Shopify Store"
        expected_output = ".....O.OO.O.O.OO..O..OO.OOO.O..OO...OOO...OO.OOO...........O.OO.O..OOOO.O..OO.O.OOO.O..O.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_simple_num(self):
        input_str = "123423"
        expected_output = ".O.OOOO.....O.O...OO....OO.O..O.O...OO...."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_all_lower_case(self):
        input_str = "i love shopify"
        expected_output = ".OO.........O.O.O.O..OO.O.O.OOO..O.........OO.O.O.OO..O..OO.OOO.O..OO...OOO...OO.OOO"
        self.assertEqual(self.run_translator(input_str), expected_output)
    
    def test_all_upper_case(self):
        input_str = "ALL CAPS TEST"
        expected_output = ".....OO..........OO.O.O......OO.O.O............OOO.........OO..........OOOO.O......O.OO.O............O.OOOO......OO..O.......O.OO.O......O.OOOO."
        self.assertEqual(self.run_translator(input_str), expected_output)
    
    def test_mixed_case_with_num(self):
        input_str = "MiXeD CaSe 2 TeSt 23432"
        expected_output = ".....OOO..O..OO........OOO..OOO..O.......OOO.O.............OOO....O..........O.OO.O.O..O.........O.OOOO.O..............O.OOOO.O..O.......O.OO.O..OOOO........O.OOOO.O...OO....OO.O..OO....O.O..."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def multiple_nums(self):
        input_str = "123 456 789 232 121424"
        expected_output = ".O.OOOO.....O.O...OO...........O.OOOOO.O..O..O..OOO..........O.OOOOOOO..O.OO...OO..........O.OOOO.O...OO....O.O..........O.OOOO.....O.O...O.....OO.O..O.O...OO.O.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def complex_sentence(self):
        input_str = "b2 b2 b2 target4 2024 ShOPiFY"
        expected_output = "O.O....O.OOOO.O.........O.O....O.OOOO.O.........O.O....O.OOOO.O..........OOOO.O.....O.OOO.OOOO..O..O...OOOO..O.OOOOO.O.........O.OOOO.O....OOO..O.O...OO.O.............O.OO.O.O.OO.......OO..OO......OOOO.O..OO........OOOO........OOO.OOO"
        self.assertEqual(self.run_translator(input_str), expected_output)

if __name__ == '__main__':
    unittest.main()

