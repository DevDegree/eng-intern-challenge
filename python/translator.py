
import sys
from typing import List


english_to_braille = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    ' ': "......",
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
    'CAPITAL': ".....O",
    'NUMBER': ".O.OOO"
}


braille_to_english = {
    "O.....": 'a1',
    "O.O...": 'b2',
    "OO....": 'c3',
    "OO.O..": 'd4',
    "O..O..": 'e5',
    "OOO...": 'f6',
    "OOOO..": 'g7',
    "O.OO..": 'h8',
    ".OO...": 'i9',
    ".OOO..": 'j0',
    "O...O.": 'k',
    "O.O.O.": 'l',
    "OO..O.": 'm',
    "OO.OO.": 'n',
    "O..OO.": 'o',
    "OOO.O.": 'p',
    "OOOOO.": 'q',
    "O.OOO.": 'r',
    ".OO.O.": 's',
    ".OOOO.": 't',
    "O...OO": 'u',
    "O.O.OO": 'v',
    ".OOO.O": 'w',
    "OO..OO": 'x',
    "OO.OOO": 'y',
    "O..OOO": 'z',
    "......": ' ',
    ".....O": 'CAPITAL',
    ".O.OOO": 'NUMBER'
}

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

def translate_to_english(braille: str) -> str:
    splitted_chars = split_into_letters(braille)
    english_letters = ''
    next_letter_uppercase = False
    next_chars_number = False
    for braille_sequence in splitted_chars:
        braille_symbol = braille_to_english[braille_sequence]
        if braille_symbol == 'CAPITAL':
            next_letter_uppercase = True
        elif braille_symbol == 'NUMBER':
            next_chars_number = True
        elif braille_symbol == ' ':
            english_letters += ' '
            if next_chars_number:
                next_chars_number = False
        else:
            if len(braille_symbol) > 1:
                if next_chars_number:
                    english_letters += braille_symbol[1]
                else:
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
        if char.isupper():
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
