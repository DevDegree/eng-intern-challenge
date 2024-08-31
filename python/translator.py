
# For getting command line args
import sys

from typing import Dict

# Special Characters
SPACE_CHARACTER = "......"
NUMBER_FOLLOWS = ".O.OOO"
CAPITAL_FOLLOWS = ".....O"

LETTERS_TO_BRAILLE: Dict[str, str] = {
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
    'z': 'O..OOO'
}

NUMBERS_TO_BRAILLE: Dict[str, str] = {
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
}


def reverse_dict(dict_to_reverse: Dict[str, str]) -> Dict[str, str]:
    return {value: key for key, value in dict_to_reverse.items()}


BRAILLE_TO_LETTERS = reverse_dict(LETTERS_TO_BRAILLE)
BRAILLE_TO_NUMBERS = reverse_dict(NUMBERS_TO_BRAILLE)


# Number mode is whether we are supposed to look at the numbers mapping or not
def process_braille_character(braille_segment: str, number_mode: bool, capitalize: bool) -> str:
    if braille_segment == SPACE_CHARACTER:
        return " "
    if number_mode:
        return BRAILLE_TO_NUMBERS[braille_segment]
    if capitalize:
        return BRAILLE_TO_LETTERS[braille_segment].capitalize()
    else:
        return BRAILLE_TO_LETTERS[braille_segment]


def process_english_character(english_character: str):
    if english_character.isspace():
        return SPACE_CHARACTER
    if english_character.isupper():
        return CAPITAL_FOLLOWS + LETTERS_TO_BRAILLE[english_character.lower()]
    if english_character.isnumeric():
        return NUMBERS_TO_BRAILLE[english_character]
    else:
        return LETTERS_TO_BRAILLE[english_character]


# Translates the braille string into english
def process_braille_text(full_braille_text: str) -> str:
    answer = ""
    individual_characters = []
    number_mode = False
    capitalize = False

    # Split the braille string into portions of lengths 6 (assuming this operation will work fine)
    for i in range(0, len(full_braille_text), 6):
        individual_characters.append(full_braille_text[i:i + 6])

    for letter in individual_characters:
        if letter == SPACE_CHARACTER:
            number_mode = False
        # If we see a number follows character, just set number mode to true and continue,
        # otherwise the algorithm will attempt to look up this value in the dictionary and fail
        if letter == NUMBER_FOLLOWS:
            number_mode = True
            continue
        # Continuing here for the same reason as above
        if letter == CAPITAL_FOLLOWS:
            capitalize = True
            continue
        answer += process_braille_character(letter, number_mode, capitalize)
        capitalize = False
    return answer


# Translates the english text into braille
def process_english_text(english_text: str) -> str:
    answer = ""
    number_mode = False
    for character in english_text:
        if character.isspace():
            number_mode = False
        if character.isnumeric() and not number_mode:
            number_mode = True
            answer += NUMBER_FOLLOWS
        answer += process_english_character(character)
    return answer


def main() -> None:
    # argv[0] is the name of the program, so we have to use argv[1] here
    original_input = " ".join(sys.argv[1:])
    is_braille = all(character in {".", "O"} for character in original_input)
    if is_braille:
        sys.stdout.write(process_braille_text(original_input))
    else:
        sys.stdout.write(process_english_text(original_input))


if __name__ == "__main__":
    main()
