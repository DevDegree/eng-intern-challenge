import unittest

from translator import Braille_Translator

class BrailleTest(unittest.TestCase):

    def test_is_braille(self):
        """
        Test the 'is_braille' method.
        """
        braille = Braille_Translator()

        test_cases = [
            (".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..", True),
            ("Hello world", False),
            ("42", False),
            (".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", True),
            ("OOOOOOOOOO", False),
            ("OOOOOO", False)
        ]

        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                # When
                actual = braille.is_braille(input)

                # Then
                self.assertEqual(actual, expected)



    def test_eng_to_braille(self):
        """
        Test the 'eng_to_braille' method.
        """
        braille = Braille_Translator()

        test_cases = [
            ("Hello world", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."),
            ("42", ".O.OOOOO.O..O.O...")
        ]

        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                # When
                actual = braille.eng_to_braille(input)

                # Then
                self.assertEqual(actual, expected)

    

    def test_braille_to_eng(self):
        """
        Test the 'braille_to_eng' method.
        """
        braille = Braille_Translator()

        test_cases = [
            (".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", "Abc 123"),
            (".O.OOOOO.O..O.O...", "42"),
            (".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..", "Hello world")
        ]

        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                # When
                actual = braille.braille_to_eng(input)

                # Then
                self.assertEqual(actual, expected)


    
    def test_translate(self):
        """
        Test the 'translate' method.
        """
        braille = Braille_Translator()

        test_cases = [
            (".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..", "Hello world"),
            ("Hello world", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."),
            ("42", ".O.OOOOO.O..O.O..."),
            (".O.OOOOO.O..O.O...", "42")
        ]

        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                # When
                actual = braille.translate(input)

                # Then
                self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()