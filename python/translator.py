from collections import defaultdict
from enum import Enum
from typing import List
import sys

# Special control characters
CAPITAL_FOLLOWS = '*'
NUMBER_FOLLOWS = '#'

# Global character to character maps
braille_to_eng_char = defaultdict(str)
braille_to_eng_dig = defaultdict(str)
eng_to_braille = defaultdict(lambda: '??????', {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    ' ': '......',
    CAPITAL_FOLLOWS: '.....O',
    NUMBER_FOLLOWS: '.O.OOO',
})

def init_braille_to_eng() -> None:
    """
      Initialize a hash map that maps
      Braille to English. If a character is a number, use the digit hash map, otherwise use the character hashmap.
    """

    for k, v in eng_to_braille.items():
        if k.isdigit():
            braille_to_eng_dig[v] = k
        else:
            braille_to_eng_char[v] = k


def split_chars_in_six(s: str) -> List[str]:
    """
      Splits a string, s, into a list of six characters
      If the length of string is not a multiple of 6,
      return an empty list.

      Returns:
          List[str]: a list of six characters
    """

    # An edge case where the length is not divisible by 6.
    if len(s) % 6:
        return []

    sixes = []
    for start in range(0, len(s), 6):
        six = s[start:start + 6]
        sixes.append(six)
    return sixes


def is_braille(s: str) -> bool:
    """
      Checks if the input string, s, is composed entirely of '.' or 'O'

      Returns:
          bool: True if all characters are '.' or 'O', otherwise False
    """
    for ch in s:
        if ch not in ('.', 'O'):
            return False
    return True


def translate_braille_to_eng(s: str) -> str:
    """
      Translate a string in Braille to English

      Returns:
          str: a string in English
    """

    translation = []
    number_follows, capital_follows = False, False

    # Input is not proper Braille (group of 6)
    if len(s) % 6:
        return ""

    # Split Braille into groups of 6
    braille = split_chars_in_six(s)

    for six in braille:
        ch = braille_to_eng_dig[six] if number_follows else braille_to_eng_char[six]
        if ch:
            if ch == CAPITAL_FOLLOWS:
                capital_follows = True
                continue
            elif ch == NUMBER_FOLLOWS:
                number_follows = True
                continue
            elif number_follows and ch.isdigit():  # digit
                translation.append(ch)
            elif capital_follows and ch.islower():  # capital
                translation.append(ch.upper())
                capital_follows = False
                number_follows = False
            else:
                if ch == ' ':
                    # assume all following symbols are numbers until the next
                    # space symbol
                    number_follows = False
                translation.append(ch)
                # For an edge case where the previous char is not lower
                capital_follows = False

    return ''.join(translation)


def translate_eng_to_braille(s: str) -> str:
    """
      Translate a string in English to Braille

      Returns:
          str: a string in Braille
    """

    translation = []
    number_follows = False

    for ch in s:
        if ch.isupper():
            translation.append(eng_to_braille[CAPITAL_FOLLOWS])
            ch = ch.lower()
        if ch.isdigit():
            if not number_follows:
                translation.append(eng_to_braille[NUMBER_FOLLOWS])
                number_follows = True
        else:
            number_follows = False

        if ch in eng_to_braille:
            translation.append(eng_to_braille[ch])
        else:
            return ""  # Contains an invalid character; don't translate.abs

    return ''.join(translation)


def main():
    """
      Main function, it is designed to print an empty string if an input is invalid
    """
    init_braille_to_eng()
    sentence = " ".join(sys.argv[1:])
    if is_braille(sentence):  # Braille to English
        print(translate_braille_to_eng(sentence))
    else:  # English to Braille
        print(translate_eng_to_braille(sentence))


if __name__ == "__main__":
    main()
