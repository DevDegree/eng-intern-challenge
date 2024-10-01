import sys

# Dictionary to map English characters to Braille patterns.
ENG_TO_BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
}

# Dictionary to map numbers to Braille patterns.
ENG_TO_BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Dictionary to map special characters to Braille patterns.
ENG_TO_BRAILLE_SPECIALS = {
    '.': '..OO.O', ',': '..O...', ';': '..OO..', '!': '..O.O.', '?': '..OO.O',
    '-': '....O.', "'": '....OO', '(': '...O..', ')': '...OO.', ' ': '......',
}

# Prefixes used in Braille for capitalization and numbers.
BRAILLE_CAPITALS = '.....O'
BRAILLE_NUMBERS = '.O.OOO'

# Dictionary to map Braille patterns to English characters, numbers, and special characters.
BRAILLE_TO_ENG_LETTERS = {value: key for key, value in ENG_TO_BRAILLE_LETTERS.items()}
BRAILLE_TO_ENG_NUMBERS = {value: key for key, value in ENG_TO_BRAILLE_NUMBERS.items()}
BRAILLE_TO_ENG_SPECIALS = {value: key for key, value in ENG_TO_BRAILLE_SPECIALS.items()}

# Function to determine if the input text is in Braille or English.
# If it's Braille, convert it to English. Otherwise, convert it to Braille.
def convert_to_braille_or_english(input_text):
    if all(char in 'O.' for char in input_text):
        return braille_to_english(input_text)
    else:
        return english_to_braille(input_text)

# Function to convert Braille text to English.
# Handles capitalization and number prefixes.
def braille_to_english(braille_text):
    english_text = ''
    i = 0
    capital_flag = False
    number_flag = False

    while i < len(braille_text):
        braille_char = braille_text[i:i + 6]

        if braille_char == BRAILLE_CAPITALS:
            capital_flag = True
            i += 6
            continue
        elif braille_char == BRAILLE_NUMBERS:
            number_flag = True
            i += 6
            continue
        elif braille_char == '......':
            english_text += ' '
        elif braille_char in BRAILLE_TO_ENG_LETTERS and not number_flag:
            letter = BRAILLE_TO_ENG_LETTERS[braille_char]
            if capital_flag:
                letter = letter.upper()
                capital_flag = False
            english_text += letter
        elif braille_char in BRAILLE_TO_ENG_NUMBERS and number_flag:
            english_text += BRAILLE_TO_ENG_NUMBERS[braille_char]
        elif braille_char in BRAILLE_TO_ENG_SPECIALS:
            english_text += BRAILLE_TO_ENG_SPECIALS[braille_char]

        i += 6

        if braille_char == '......':
            number_flag = False

    return english_text

# Function to convert English text to Braille.
# Handles capitalization and number prefixes.
def english_to_braille(english_text):
    braille_output = ''
    number_flag = False

    for char in english_text:
        if char.isalpha():
            if char.isupper():
                braille_output += BRAILLE_CAPITALS
                char = char.lower()
            braille_output += ENG_TO_BRAILLE_LETTERS[char]
        elif char.isdigit():
            if not number_flag:
                braille_output += BRAILLE_NUMBERS
                number_flag = True
            braille_output += ENG_TO_BRAILLE_NUMBERS[char]
        elif char in ENG_TO_BRAILLE_SPECIALS:
            braille_output += ENG_TO_BRAILLE_SPECIALS[char]
        else:
            braille_output += ENG_TO_BRAILLE_SPECIALS[' ']
            number_flag = False

    return braille_output

# Main function to handle command-line input and call the conversion function.
def main():
    if len(sys.argv) < 2:
        print("ERROR: invalid number of arguments")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    output_text = convert_to_braille_or_english(input_text)
    print(output_text)

# Entry point for command-line execution.
if __name__ == '__main__':
    main()