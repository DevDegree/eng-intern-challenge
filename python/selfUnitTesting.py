import unittest
import subprocess


# Personal Unit Testing
def run_command(*args):
    command = ["python3", "translator.py"] + list(args)
    return subprocess.run(command, capture_output=True, text=True)


class TestTranslator(unittest.TestCase):
    """
    Tests translating a Braille input to English.
    """

    def test_braille_translation(self):
        """Test translating simple braille word to English"""
        result = run_command("O.....O.O...")
        expected_output = "ab"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_translation_hello_word(self):
        """Test translating braille word with space to English"""
        result = run_command("O.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")
        expected_output = "hello world"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_translation_capsLock(self):
        """Test translating braille word with CapsLock to English"""
        result = run_command(".....OO.OO..")
        expected_output = "H"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_translation_number_and_capslock(self):
        """Test translating braille word with CapsLock Numbers Letters and Spaces to English"""
        result = run_command(".....OO.OO.........O.OOOO................OO................OO.O...")
        expected_output = 'H 1 A B'
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_translation_letters_and_num(self):
        """Test from the Readme"""
        result = run_command(".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
        expected_output = "Abc 123"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_translation_to_english_word_mixed_case(self):
        """Test translating a mixed Braille Word to English"""
        result = run_command(".....OOOO.O.OO.OOO.....O.OOOO.O.OO.......OO..OO.OO.OO.")
        expected_output = "PyThOn"
        self.assertEqual(result.stdout.strip(), expected_output)

    """
    Test translating a English to Braille.
    """

    def test_english_translation_short_word(self):
        """Test translating a very simple english input to Braille."""
        result = run_command("hello")
        expected_output = "O.OO..O..O..O.O.O.O.O.O.O..OO."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_translation_longer_word_with_space(self):
        """Test translating an english word with space to Braille."""
        result = run_command("hello world")
        expected_output = "O.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_translation_capsLock(self):
        """Test translating an English word with Capslock to Braille."""
        result = run_command("H")
        expected_output = ".....OO.OO.."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_translation_Hello_World(self):
        """Test from Readme"""
        result = run_command("Hello world")
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_translation_space_and_number_and_capslock(self):
        """Test translating English word with Letter Number Space and Capslock to braille"""
        result = run_command("H 1 A B")
        expected_output = ".....OO.OO.........O.OOOO................OO................OO.O..."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_translation_letters_and_num(self):
        result = run_command("Abc 123")
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_translation_empty_string(self):
        """Test translating an empty string to Braille."""
        result = run_command("")
        expected_output = ""
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_translation_multiple_spaces(self):
        """Test translating a string with multiple spaces to Braille."""
        result = run_command("   ")
        expected_output = ".................."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_translation_mixed_case(self):
        """Test translating a mixed case word to Braille."""
        result = run_command("PyThOn")
        expected_output = ".....OOOO.O.OO.OOO.....O.OOOO.O.OO.......OO..OO.OO.OO."
        self.assertEqual(result.stdout.strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
