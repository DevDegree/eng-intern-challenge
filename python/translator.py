# Translator
#   - Given arguments passed into the program at runtime, determine if the given string should be translated to English or Braille.
#   - For Braille, each character is stored as a series of O (the letter O) or . (a period).
#   - Store Braille symbols as a 6 character string reading left to right, line by line, starting at the top left.
#   - When a Braille capital follows symbol is read, assume only the next symbol should be capitalized.
#   - When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.
# Braille Alphabet
#   Letters a through z (The ability to capitalize letters)
#   Numbers 0 through 9
#   The ability to include spaces ie: multiple words

# Example:
# Input: Hello world
# Output: .....O O.OO.. O..O.. O.O.O. O.O.O. O..OO. ...... .OOO.O O..OO. O.OOO. O.O.O. OO.O..
#         cap    h      e      l      l      o      space   w     o      r      l      d
#
# Input: 42
# Output: .O.OOO OO.O.. O.O...
#         num    4      2


import sys

BRAILLE_DICT_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

BRAILLE_DICT_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_DICT_PUNCTUATION = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

# Combined for convenience in lookup but kept distinct to avoid overlaps
BRAILLE_DICT = {**BRAILLE_DICT_LETTERS, **BRAILLE_DICT_NUMBERS, **BRAILLE_DICT_PUNCTUATION,
                'CAPITAL': '.....O', 'NUMBER': '.O.OOO', 'DECIMAL': '.O...O'}

# Reverse lookup dictionaries
LETTER_DICT_REV = {v: k for k, v in BRAILLE_DICT_LETTERS.items()}
NUMBER_DICT_REV = {v: k for k, v in BRAILLE_DICT_NUMBERS.items()}
PUNCTUATION_DICT_REV = {v: k for k, v in BRAILLE_DICT_PUNCTUATION.items()}


def detect_input_type(input_string: str) -> bool:
    if all(c in 'O.' for c in input_string):
        return 'braille'
    else:
        return 'english'


def english_to_braille(english_text: str) -> str:
    braille_text = ''
    in_number_mode = False  # Tracks if we're in number mode

    for char in english_text:
        if char.isdigit():  # Enter number mode if a digit is encountered
            if not in_number_mode:
                braille_text += BRAILLE_DICT['NUMBER']
                in_number_mode = True
            braille_text += BRAILLE_DICT_NUMBERS[char]
        
        else:  # Exit number mode if a non-digit is encountered
            if in_number_mode:
                in_number_mode = False
            if char.isupper():  # Handle capitalization
                braille_text += BRAILLE_DICT['CAPITAL'] + BRAILLE_DICT_LETTERS[char.lower()]
            
            elif char in BRAILLE_DICT_PUNCTUATION:  # Translate punctuation
                braille_text += BRAILLE_DICT_PUNCTUATION[char]
            
            elif char in BRAILLE_DICT_LETTERS:  # Translate letters
                braille_text += BRAILLE_DICT_LETTERS[char]
            
            else:  # Raise error for unrecognized characters
                raise ValueError(f"Unrecognized character in English text: '{char}'")
    
    return braille_text


def braille_to_english(braille_text: str) -> str:
    english_text = ''
    i = 0
    in_number_mode = False  # Tracks if we're in number mode

    while i < len(braille_text):
        current_char = braille_text[i:i+6]  # Read one Braille character (6 dots)

        if current_char == BRAILLE_DICT['NUMBER']:
            in_number_mode = True  # Enter number mode
            i += 6
            continue
        
        elif current_char == BRAILLE_DICT['CAPITAL']:  # Handle capitalization
            i += 6
            next_char = braille_text[i:i+6]
            if next_char in LETTER_DICT_REV:
                english_text += LETTER_DICT_REV[next_char].upper()
            else:
                raise ValueError(f"Unrecognized Braille character: '{next_char}'")
        
        elif current_char == BRAILLE_DICT['DECIMAL']:
            english_text += '.'
        
        elif in_number_mode:  # Translate numbers
            if current_char in NUMBER_DICT_REV:
                english_text += NUMBER_DICT_REV[current_char]
            else:
                raise ValueError(f"Unrecognized Braille character in number mode: '{current_char}'")

            if braille_text[i+6:i+12] == BRAILLE_DICT[' ']:  # Exit number mode at a space
                in_number_mode = False
        
        elif current_char in LETTER_DICT_REV:  # Translate letters
            english_text += LETTER_DICT_REV[current_char]

        elif current_char in PUNCTUATION_DICT_REV:  # Translate punctuation
            english_text += PUNCTUATION_DICT_REV[current_char]
        
        else:  # Raise error for unrecognized Braille characters
            raise ValueError(f"Unrecognized Braille character: '{current_char}'")

        i += 6  # Move to the next Braille character
    return english_text


def main():
    input_string = ' '.join(sys.argv[1:])  # Join all arguments into a single string
    input_type = detect_input_type(input_string)

    if input_type == 'english':
        output_string = english_to_braille(input_string)
    else:
        output_string = braille_to_english(input_string)
    
    print(output_string)

if __name__ == "__main__":
    main()