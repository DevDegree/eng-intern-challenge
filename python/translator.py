

import sys

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' ',
    # Add letters with corresponding Braille
}
letters_to_num = {
    "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"
}

english_to_braille = {v: k for k, v in braille_to_english.items() if v != 'capital' and v != 'number'}
num_to_letters = {v: k for k, v in letters_to_num.items()}


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
        elif char == '.O.OOO':
            number_next = True
        else:
            english_char = braille_to_english.get(char, '?')
            if capital_next:
                english_char = english_char.upper()
                capital_next = False
            if english_char == " ":
                number_next = False
            if number_next:
                english_char = letters_to_num[english_char]
            result.append(english_char)

    return ''.join(result)


def text_to_braille(text_string):
    result = []
    num = False
    for char in text_string:
        if char.isupper():
            result.append('.....O')  # Capital follows
            result.append(english_to_braille[char.lower()])
        elif char.isnumeric():
            if not num:
                num = True
                result.append('.O.OOO')     # Num follows
            result.append(english_to_braille[num_to_letters[char]])
        else:
            if char == " ":
                num = False
            result.append(english_to_braille.get(char, '......'))  # Default to space if not found
    return ''.join(result)


def main():
    if len(sys.argv) < 2:
        print("Usage: Rerun with english or Braille")
        return
    res = ""
    for input_string in sys.argv[1:-1]:
        if is_braille(input_string):
            res = res + (braille_to_text(input_string)) + " "
        else:
            res = res + (text_to_braille(input_string)) + "......"
    if is_braille(sys.argv[-1]):
        res = res + (braille_to_text(sys.argv[-1]))
    else:
        res = res + (text_to_braille(sys.argv[-1]))
    print(res)

if __name__ == '__main__':
    main()