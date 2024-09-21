import sys
import unittest

letter_to_braille = dict(zip('abcdefghijklmnopqrstuvwxyz ', 
    ['O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 
     'O.OO..', '.OO...', '.OOO..', 'O...O.', 'O.O.O.', 'OO..O.', 'OO.OO.', 
     'O..OO.', 'OOO.O.', 'OOOOO.', 'O.OOO.', '.OO.O.', '.OOOO.', 'O...OO', 
     'O.O.OO', '.OOO.O', 'OO..OO', 'OO.OOO', 'O..OOO', '......']))

num_to_braille = dict(zip('1234567890', 
    ['O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 
     'O.OO..', '.OO...', '.OOO..']))

misc_braille = {'capital_next': '.....O', 'number_next': '.O.OOO'}
braille_to_letter = {v: k for k, v in letter_to_braille.items()}
braille_to_number = {v: k for k, v in num_to_braille.items()}

def is_braille(s: str) -> bool:
    return all(c in ".O" for c in s) and len(s) % 6 == 0

def to_braille(s: str) -> str:
    braille, digit_mode = "", False
    for char in s:
        if char.isupper():
            braille += misc_braille['capital_next'] + letter_to_braille[char.lower()]
            digit_mode = False
        elif char.isdigit():
            if not digit_mode: braille += misc_braille['number_next']
            braille += num_to_braille[char]; digit_mode = True
        else:
            braille += letter_to_braille[char]; digit_mode = False
    return braille

def to_english(s: str) -> str:
    english, digit_mode, capital_mode = "", False, False
    for i in range(0, len(s), 6):
        braille = s[i: i+6]
        if braille == misc_braille['capital_next']: 
            capital_mode, digit_mode = True, False
        elif braille == misc_braille['number_next']: 
            digit_mode, capital_mode = True, False
        elif braille == letter_to_braille[' ']:  # Handle space separately
            english += " "
            digit_mode, capital_mode = False, False
        else:
            if digit_mode: 
                english += braille_to_number.get(braille, "")
            else: 
                letter = braille_to_letter.get(braille, "")
                english += letter.upper() if capital_mode else letter
            capital_mode = False
    return english


class TestBrailleConversion(unittest.TestCase):

    def test_to_braille_basic(self):
        self.assertEqual(to_braille("hello"), "O.OO..O..O..O.O.O.O.O.O.O..OO.")

    def test_to_braille_with_capitals(self):
        self.assertEqual(to_braille("Hello World"), ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O..")

    def test_to_braille_with_numbers(self):
        self.assertEqual(to_braille("abc123"), "O.....O.O...OO.....O.OOOO.....O.O...OO....")

    def test_to_english_basic(self):
        self.assertEqual(to_english("O.OO..O..O..O.O.O.O.O.O.O..OO."), "hello")

    def test_to_english_with_numbers(self):
        self.assertEqual(to_english("O.....O.O...OO.....O.OOOO.....O.O...OO....OO.O.."), "abc1234")


def main():
    args = sys.argv[1:]
    unittest.main()
    string = " ".join(args)
    if is_braille(string):
        print(to_english(string))
    else:
        print(to_braille(string))


if __name__ == '__main__':
    main()
