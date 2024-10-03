"""
Author: Jasraj Johal johalj11@mcmaster.ca

This script translates Braille to English and vice versa.

Functions:
- `braille_to_english_letters` and `braille_to_english_numbers`: These dictionaries map Braille characters to their English equivalents (letters and numbers).
- `english_to_braille_letters` and `english_to_braille_numbers`: Reverse mappings to convert English letters and numbers to Braille.

- `isBraille(text)`: Checks if the input text contains only Braille characters ('O' and '.').

- `braille_to_english(text)`: Converts Braille to English. Handles capital letters, numbers, and spaces based on special indicators.

- `english_to_braille(text)`: Converts English to Braille. Adds indicators for capital letters and numbers as needed.
"""

import sys

# Braille to English dictionary for letters
braille_to_english_letters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.OOOO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z'
}

# Braille to English dictionary for numbers
braille_to_english_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
    '.OO...': '9', '.OOO..': '0'
}

# Reverse mappings for English to Braille conversion
english_to_braille_letters = {v: k for k,
                              v in braille_to_english_letters.items()}
english_to_braille_numbers = {v: k for k,
                              v in braille_to_english_numbers.items()}


def isBraille(text):
    """Check if the input string is Braille (only contains 'O' and '.')."""
    return all(c in 'O.' for c in text)


def braille_to_english(text):
    """Convert Braille to English."""
    result = []
    number_mode = False  # Flag for number mode
    capital_follows = False  # Flag for capitalization

    for i in range(0, len(text), 6):
        braille_char = text[i:i+6]

        if braille_char == '.....O':  # Capital letter indicator
            capital_follows = True
            continue
        if braille_char == '.O.OOO':  # Number mode indicator
            number_mode = True
            continue
        if braille_char == '......':  # Space
            number_mode = False
            result.append(' ')
            continue

        if number_mode:
            result.append(braille_to_english_numbers[braille_char])
        else:
            letter = braille_to_english_letters[braille_char]
            if capital_follows:
                result.append(letter.upper())  # Capitalize next letter
                capital_follows = False
            else:
                result.append(letter)

    return ''.join(result)


def english_to_braille(text):
    """Convert English to Braille."""
    result = []
    number_mode = False  # Flag for number mode

    for char in text:
        if char == ' ':
            result.append('......')  # Space in Braille
            number_mode = False  # Space ends number mode
            continue

        if char.isupper():
            result.append('.....O')  # Capital letter indicator
            char = char.lower()

        elif char.isdigit() and not number_mode:
            result.append('.O.OOO')  # Number mode indicator
            number_mode = True

        if number_mode and char.isdigit():
            result.append(english_to_braille_numbers[char])
        else:
            result.append(english_to_braille_letters[char])

    return ''.join(result)


def main():
    """Main function to handle input and decide translation direction."""
    input_text = ' '.join(sys.argv[1:])
    # print(f"Input text: {input_text}")
    if isBraille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))


if __name__ == '__main__':
    main()
