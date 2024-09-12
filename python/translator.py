import sys

# Lookup tables for Braille to English and vice versa
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '....OO': 'number', '......': ' ',
    # Add letters with corresponding Braille
}

english_to_braille = {v: k for k, v in braille_to_english.items() if v != 'capital' and v != 'number'}


def is_braille(input_string):
    return all(c in ['O', '.'] for c in input_string)


def braille_to_text(braille_string):
    result = []
    braille_chars = [braille_string[i:i + 6] for i in range(0, len(braille_string), 6)]
    capital_next = False
    number_next = False

    for char in braille_chars:
        if char == '.....O':
            capital_next = True
        elif char == '....OO':
            number_next = True
        else:
            english_char = braille_to_english.get(char, '?')
            if capital_next:
                english_char = english_char.upper()
                capital_next = False
            result.append(english_char)

    return ''.join(result)


def text_to_braille(text_string):
    result = []
    for char in text_string:
        if char.isupper():
            result.append('.....O')  # Capital follows
            result.append(english_to_braille[char.lower()])
        else:
            result.append(english_to_braille.get(char, '......'))  # Default to space if not found
    return ''.join(result)


def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text_or_braille>")
        return

    input_string = sys.argv[1]

    if is_braille(input_string):
        print(braille_to_text(input_string))
    else:
        print(text_to_braille(input_string))


if __name__ == '__main__':
    main()
