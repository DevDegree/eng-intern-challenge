import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def run_translator(self, input_text):
        command = ["python3", "translator.py", input_text]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()

    def test_text_to_braille(self):
        test_cases = [
            ("Abc 123", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."),
            ("Hello World!", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O...OO.O."),
            ("42.5", ".O.OOOOO.O..O.O.....O.O...O..O.."),
            ("CAPITAL", ".....O.....O.O..O.....OO.O...O.....OO....O..O.....OO.O.O.O."),
            ("MixEd CaSe", ".....OO.OO..O......O..O.....O.O..........OO.....O.....O.O..O.....O.O.O...O..O.."),
            ("a,b:c;d-e/f", "O.......O....O.O.....O.O...OO.....OO...OO.O.....O..O....O..O..OOO.....O..O."),
            ("(1+2)*3=9", ".OO.OO.O.OOOO.....O.O....O...O..OO.O...O.OOOO.....OO.......O.OOO.OO..."),
        ]

        for input_text, expected_output in test_cases:
            with self.subTest(input_text=input_text):
                self.assertEqual(self.run_translator(input_text), expected_output)

    def test_braille_to_text(self):
        test_cases = [
            (".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", "Abc 123"),
            (".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O...OO.O.", "Hello world!"),
            (".O.OOOOO.O..O.O.....O.O...O..O..", "42.5"),
            (".....O.....O.O..O.....OO.O...O.....OO....O..O.....OO.O.O.O.", "Capital"),
            (".....OO.OO..O......O..O.....O.O..........OO.....O.....O.O..O.....O.O.O...O..O..", "Mixed case"),
            ("O.......O....O.O.....O.O...OO.....OO...OO.O.....O..O....O..O..OOO.....O..O.", "a,b:c;d-e/f"),
            (".OO.OO.O.OOOO.....O.O....O...O..OO.O...O.OOOO.....OO.......O.OOO.OO...", "(1+2)*3=9"),
        ]

        for input_braille, expected_output in test_cases:
            with self.subTest(input_braille=input_braille):
                self.assertEqual(self.run_translator(input_braille), expected_output)

if __name__ == '__main__':
    unittest.main()
