import sys

from typing import List
from english import braille_to_english
from braille import english_to_braille


def args_is_braille(args: List[str]) -> bool:
    return len(args) == 2 and all(char in 'O.' for char in args[1])


def split_into_letters(braille: str) -> List[str]:
    letters = []
    lettre = ''
    iterator = 1
    for char in braille:
        lettre += char
        iterator += 1
        if iterator == 7:
            letters.append(lettre)
            iterator = 1
            lettre = ''
    return letters
    # return [braille[i:i+6] for i in range(0, len(braille), 6)]


def translate_to_english(braille: str) -> str:
    splitted_chars = split_into_letters(braille)
    english_letters = ''
    next_letter_uppercase = False
    next_chars_number = False
    for braille_sequence in splitted_chars:
        # TODO : Make a separate function for these instructions
        braille_symbol = braille_to_english[braille_sequence]
        # Verifies if the Braille symbole is 'capital follows'
        if braille_symbol == 'CAPITAL':
            next_letter_uppercase = True
        # Verifies if the Braille symbole is 'number follows'
        elif braille_symbol == 'NUMBER':
            next_chars_number = True
        elif braille_symbol == ' ':
            english_letters += ' '  # Append the space character
            # We encountered a space si if the next chars were set as numbers, we turn it off
            if next_chars_number:
                next_chars_number = False
        else:  # It means it's a normal character
            # Determine whether the symbol has multiple characters associated
            if len(braille_symbol) > 1:
                if next_chars_number:
                    # Append the number (2nd char in the symbol mapping)
                    english_letters += braille_symbol[1]
                else:  # Append the letter (1st char in the symbol mapping)
                    # Determine whether it's an upper/lowercase
                    if next_letter_uppercase:
                        braille_symbol = braille_symbol[0].upper()
                        next_letter_uppercase = False
                    english_letters += braille_symbol[0]
            else:
                if next_letter_uppercase:
                    braille_symbol = braille_symbol.upper()
                    next_letter_uppercase = False
                english_letters += braille_symbol
    return english_letters


def translate_word_to_braille(english_word: str) -> str:
    braille_symbol = ''
    if english_word.isdecimal():
        braille_symbol += english_to_braille['NUMBER']
    for char in english_word:
        if char.isupper():  # Verifies if the char is an uppercase letter
            # Append the symbol that tells that the next letter is an uppercase
            braille_symbol += english_to_braille['CAPITAL']
        braille_symbol += english_to_braille[char.lower()]
    return braille_symbol


def translate_to_braille(english_words: List[str]) -> str:
    braille_sequence = ''
    for index, english_word in enumerate(english_words):
        braille_sequence += translate_word_to_braille(english_word)
        if index != len(english_words) - 1:
            braille_sequence += english_to_braille[' ']
    return braille_sequence.strip()


def main():
    if args_is_braille(sys.argv):
        print(translate_to_english(sys.argv[1]))
    else:
        print(translate_to_braille(sys.argv[1:]))


if __name__ == "__main__":
    main()

# Tests English to Braille :

# .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
# .....OO.....O.O...OO...........O.OOOO.....O.O...OO....

# .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
# .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..

# .O.OOOOO.O..O.O...
# .O.OOOOO.O..O.O...

# Tests Braille to English

# Hello world
# Hello world

# 42
# 42

# Abc 123
# Abc 123

# Abc 123 xYz
# Abc 123 xYz
