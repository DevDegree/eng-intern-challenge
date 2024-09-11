from typing import Dict, Union
import sys

NUMBER_FOLLOWS = '.O.OOO'
CAPITAL_FOLLOWS = '.....O'

char_to_braille: Dict[str, str] = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}
number_to_braille: Dict[str, str] = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_to_char: Dict[str, str] = {braille: char for char, braille in char_to_braille.items()}
braille_to_number: Dict[str, str] = {braille: number for number, braille in number_to_braille.items()}

def is_braille(word: str) -> bool:
    return all(char in {'.', 'O'} for char in word)

def braille_to_english(words: str) -> str:
    english = []
    digit = False
    capital = False
    i = 0
    while i < len(words):
        char = words[i:i+6]
        if char == NUMBER_FOLLOWS:
            digit = True
        elif char == CAPITAL_FOLLOWS:
            capital = True
        elif char in braille_to_char:
            if braille_to_char[char] == ' ':
                digit = False
                english.append(' ')
            elif digit:
                english.append(braille_to_number[char])
            else:
                letter = braille_to_char[char]
                english.append(letter.upper() if capital else letter)
                capital = False
        i += 6
    return ''.join(english)

def english_to_braille(words: str) -> str:
    braille = []
    digit_mode = False
    for char in words:
        if char.isdigit():
            if not digit_mode:
                braille.append(NUMBER_FOLLOWS)
                digit_mode = True
            braille.append(number_to_braille[char])
        elif char.isalpha():
            if digit_mode:
                digit_mode = False
            if char.isupper():
                braille.append(CAPITAL_FOLLOWS)
            braille.append(char_to_braille[char.lower()])
        elif char == ' ':
            digit_mode = False
            braille.append(char_to_braille[char])
    return ''.join(braille)

def translate(text: str) -> str:
    return braille_to_english(text) if is_braille(text) else english_to_braille(text)

def main():
    args = ' '.join(sys.argv[1:])
    print(translate(args))

if __name__ == "__main__":
    main()
