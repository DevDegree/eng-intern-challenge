import sys

# ==========================
# Constants
# ==========================

BRAILLE_ALPHABET = {
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
    'z': 'O..OOO',
}

BRAILLE_NUMBERS = {
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

SPECIAL_CHARACTERS = {
    '.': '..OO.O',
    ',': '..O...',
    ';': '..OO..',
    '!': '..O.O.',
    '?': '..OO.O',
    '-': '....O.',
    "'": '....OO',
    '(': '...O..',
    ')': '...OO.',
    ' ': '......',
}

CAPITAL_PFX = '.....O'
NUMBER_PFX = '.O.OOO'

# Reverse mappings for Braille to English
BRAILLE_TO_LETTER = {v: k for k, v in BRAILLE_ALPHABET.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in BRAILLE_NUMBERS.items()}
BRAILLE_TO_SPECIAL = {v: k for k, v in SPECIAL_CHARACTERS.items()}


# ==========================
# Functions
# ==========================

def english_or_braille(text):
    # Check if input is in Braille or English
    if all(char in 'O.' for char in text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)


def braille_to_english(braille):
    english = ''
    i = 0
    is_capital = False
    is_number = False

    while i < len(braille):
        char_braille = braille[i:i + 6]

        # Check for special characters
        if char_braille == CAPITAL_PFX:
            is_capital = True
            i += 6
            continue
        # Check for number prefix
        elif char_braille == NUMBER_PFX:
            is_number = True
            i += 6
            continue
        # Check for special characters
        elif char_braille == '......':
            english += ' '
        # Check for letters
        elif char_braille in BRAILLE_TO_LETTER and not is_number:
            letter = BRAILLE_TO_LETTER[char_braille]
            if is_capital:
                letter = letter.upper()
                is_capital = False
            english += letter
        # Check for numbers
        elif char_braille in BRAILLE_TO_NUMBER and is_number:
            english += BRAILLE_TO_NUMBER[char_braille]
        # Check for special characters
        elif char_braille in BRAILLE_TO_SPECIAL:
            english += BRAILLE_TO_SPECIAL[char_braille]

        i += 6

        # Reset number flag if space is found
        if char_braille == '......':
            is_number = False

    return english


def english_to_braille(english):
    output = ''
    is_number = False

    for char in english:
        # Check if character is a letter
        if char.isalpha():
            if char.isupper():
                output += CAPITAL_PFX
                char = char.lower()
            output += BRAILLE_ALPHABET[char]
        # Check if character is a number
        elif char.isdigit():
            if not is_number:
                output += NUMBER_PFX
                is_number = True
            output += BRAILLE_NUMBERS[char]
        # Check if character is a special character
        elif char in SPECIAL_CHARACTERS:
            output += SPECIAL_CHARACTERS[char]
        # If character is a space
        else:
            output += SPECIAL_CHARACTERS['.']
            is_number = False

    return output


def main():
    if len(sys.argv) < 2:
        print("ERROR: invalid number of arguments")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    print(english_or_braille(input_text))


if __name__ == '__main__':
    main()