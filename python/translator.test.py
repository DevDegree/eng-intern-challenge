import unittest
import subprocess


class TestTranslator(unittest.TestCase):
    def translate(self, command, expected_output):
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output(self):
        self.translate(["python3", "translator.py", "Abc", "123", "xYz"],
                       ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")
        self.translate(["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."],
                       "Hello world")
        self.translate(["python3", "translator.py", ".O.OOOOO.O..O.O..."],
                       "42")
        self.translate(["python3", "translator.py", "I have 20.5 eggs!"],
                       ".....O.OO.........O.OO..O.....O.O.OOO..O.........O.OOOO.O....OOO...O...OO..O........O..O..OOOO..OOOO...OO.O...OOO.")
        self.translate(["python3", "translator.py",  ".....O.OO.........O.OO..O.....O.O.OOO..O.........O.OOOO.O....OOO...O...OO..O........O..O..OOOO..OOOO...OO.O...OOO."],
                      "I have 20.5 eggs!")
        self.translate(["python3", "translator.py",  "1> o"],
                      ".O.OOOO.....O..OO.......O..OO.")
        self.translate(["python3", "translator.py",  "O..OO........O.OOOO.....O..OO."],
                      "o 1>")


if __name__ == '__main__':
    unittest.main()
