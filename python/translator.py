import sys
from collections import Counter


# PLEASE NOTE THAT THE LOGIC IS BASED ON THE IMAGE PROVIDED braille.jpg.

ALPHABET_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......"
}

DIGITS_TO_BRAILLE = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}


CAPITAL = ".....O"
NUMBER = ".O.OOO"
SPACE = "......"

BRAILLE_TO_ALPHABET = {v: k for k, v in ALPHABET_TO_BRAILLE.items()}
BRAILLE_TO_DIGITS = {v: k for k, v in DIGITS_TO_BRAILLE.items()}


def check_if_braille(text):
    counts = Counter(text)
    return len(text) % 6 == 0 and len(counts) == 2 and "O" in counts and "." in counts


def braille_to_english(braille_input):
    braille_chars = [braille_input[i:i + 6] for i in range(0, len(braille_input), 6)]
    result = []
    number_mode = False
    capitalize_next = False

    for char in braille_chars:
        if char == NUMBER:
            number_mode = True
        elif char == CAPITAL:
            capitalize_next = True
        elif char == SPACE:
            number_mode = False
            result.append(' ')
        else:
            if number_mode:
                result.append(BRAILLE_TO_DIGITS.get(char, ''))
            elif capitalize_next:
                result.append(BRAILLE_TO_ALPHABET.get(char, '').upper())
                capitalize_next = False
            else:
                result.append(BRAILLE_TO_ALPHABET.get(char, ''))

    return ''.join(result)


def english_to_braille(english_input):
    braille_result = []
    number_mode = False

    for char in english_input:
        if char.isupper():
            braille_result.append(CAPITAL)
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                number_mode = True
                braille_result.append(NUMBER)
            braille_result.append(DIGITS_TO_BRAILLE.get(char, ''))

        elif char.isalpha():
            if number_mode:
                number_mode = False
                braille_result.append(SPACE)
            braille_result.append(ALPHABET_TO_BRAILLE.get(char, ''))

        elif char == ' ':
            braille_result.append(SPACE)
            number_mode = False

    return ''.join(braille_result)


def run_translation():
    input_text = ' '.join(sys.argv[1:])
    if check_if_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))


if __name__ == "__main__":
    run_translation()
