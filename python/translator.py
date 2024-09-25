import sys
from enum import Enum


class BrailleState(Enum):
    """Represents the state of the Braille translation."""
    LOWERCASE = 1
    UPPERCASE = 2
    NUMBER = 3


eng_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital follows': '.....O', 'number follows': '.O.OOO', ' ': '......'
}

# Create a reverse mapping
braille_to_eng_map = {v: k for k, v in eng_to_braille_map.items() if k not in '1234567890'}

# A separate mapping for numbers is used because the same sequence of Braille characters can
# map to different characters (e.g. 'O.....' can be '1' or 'a')
braille_to_num_map = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6',
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def translate_to_braille(english: str) -> str:
    """Translates English text to Braille."""
    braille = ''
    number_mode = False # Flag to indicate if the current character is a number

    for c in english:
        if c.isupper():
            braille += eng_to_braille_map['capital follows']
        if c.isdigit() and not number_mode:
            braille += eng_to_braille_map['number follows']
            number_mode = True
        if c == ' ':
            number_mode = False
        
        braille += eng_to_braille_map[c.lower()]

    return braille


def translate_to_eng(braille: str) -> str:
    """Translates Braille text to English."""
    english = ''
    state = BrailleState.LOWERCASE

    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6] # Each Braille character is represented by 6 dots/zeros

        # Check if we need to change the state
        if braille_char == eng_to_braille_map['capital follows']:
            state = BrailleState.UPPERCASE
            continue
        elif braille_char == eng_to_braille_map['number follows']:
            state = BrailleState.NUMBER
            continue
        elif braille_char == eng_to_braille_map[' ']:
            state = BrailleState.LOWERCASE

        # Use the appropriate mapping dict based on the current state
        if state == BrailleState.NUMBER:
            english += braille_to_num_map[braille_char]
        else:
            eng_char = braille_to_eng_map[braille_char]
            if state == BrailleState.UPPERCASE:
                eng_char = eng_char.upper()
                # The uppercase state only applies to the next character,
                # so we reset it after using it once
                state = BrailleState.LOWERCASE
            english += eng_char
        
    return english


def is_braille(text: str) -> bool:
    """Returns True if text is in Braille, False otherwise."""
    return all(c in 'O.' for c in text)


if __name__ == '__main__':
    # Read command line arguments
    text = ' '.join(sys.argv[1:])

    # Convert the input to the appropriate format
    if is_braille(text):
        print(translate_to_eng(text))
    else:
        print(translate_to_braille(text))
