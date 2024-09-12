import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def translate(self, input: str) -> str:
        command1 = ["python3", "translator.py"] + input.split(" ")
        result1 = subprocess.run(command1, capture_output=True, text=True).stdout.strip()

        # we want to make sure it returns back to what it was
        command2 = ["python3", "translator.py"] + result1.split(" ")
        result2 = subprocess.run(command2, capture_output=True, text=True).stdout.strip()
        self.assertEqual(input, result2)

        return result1
        
    def test_example1(self):
        result = self.translate("Hello world")
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result, expected_output)

    def test_example2(self):
        result = self.translate("42")
        expected_output = ".O.OOOOO.O..O.O..."
        self.assertEqual(result, expected_output)

    def test_example3(self):
        result = self.translate(".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
        expected_output = "Abc 123"
        self.assertEqual(result, expected_output)

    def test_empty(self):
        result = self.translate("")
        expected_output = ""
        self.assertEqual(result, expected_output)
    
    def test_all_chars(self):
        result = self.translate("abcd efgh ijkl mnop qrst uvwx yz12 345 678 90")
        expected_output = "O.....O.O...OO....OO.O........O..O..OOO...OOOO..O.OO.........OO....OOO..O...O.O.O.O.......OO..O.OO.OO.O..OO.OOO.O.......OOOOO.O.OOO..OO.O..OOOO.......O...OOO.O.OO.OOO.OOO..OO......OO.OOOO..OOO.O.OOOO.....O.O..........O.OOOOO....OO.O..O..O.........O.OOOOOO...OOOO..O.OO.........O.OOO.OO....OOO.."
        self.assertEqual(result, expected_output)

    def test_capital(self):
        result = self.translate(".....OO.....O.O........OOO....OO.O..O..O..O..O..OOO........OOOOO.......OOOOO..OOOO..O.OO..O.....OO.O..O......OO.O.OO.O.......OO......O.OOOO.....OO.O..O..O.........O.OOOO.....O.....O.....")
        expected_output = "AbCdeefGGghadasdA145 111"
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
