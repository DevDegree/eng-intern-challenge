# Updated Braille Translator with Fixes
import sys

# Updated Braille mappings including punctuation and special symbols
alphanumeric_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', ' ': '......',
}

braille_to_alphabet = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '  # Space
}

braille_to_numeric = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}


# Function to determine if the input is Braille or English
def is_braille(input_string):
    return all(char in 'O.' for char in input_string)


# Function to translate English to Braille
def english_to_braille(english_string):
    braille_translation = []
    number_flag = False
    for char in english_string:
        if char.isupper():
            braille_translation.append('.....O')
            char = char.lower()
        if char.isdigit() and number_flag is False:
            braille_translation.append('.O.OOO')
            number_flag = True
        if char == ' ':
            number_flag = False
        braille_translation.append(alphanumeric_to_braille.get(char, '......'))  # Default for space or unknown
    return ''.join(braille_translation)


# Function to translate Braille to English
def braille_to_english(braille_string):
    english_translation = []
    capital_flag = False
    number_flag = False

    # Parse the Braille string into chunks of 6, representing each Braille character
    braille_chars = [braille_string[i:i + 6] for i in range(0, len(braille_string), 6)]

    for braille_char in braille_chars:
        if braille_char == '.....O':  # raise capital flag
            capital_flag = True
            continue
        if braille_char == '.O.OOO':  # raise number flag
            number_flag = True
            continue
        if braille_char == '......':  # check for space
            english_translation.append(' ')
            number_flag = False  # Reset the number flag after a space
            continue

        # Get the corresponding English character in braille_to_alphabet dictionary
        english_char = braille_to_alphabet.get(braille_char, ' ')

        # Get the corresponding numeric character in braille_to_numeric dictionary
        numeric_char = braille_to_numeric.get(braille_char, ' ')

        # Handle flags: Capital, Number
        if capital_flag:
            english_translation.append(english_char.upper())
            capital_flag = False  # Reset the capital flag after affecting one character
        elif number_flag:
            english_translation.append(numeric_char)
        else:
            # Default behavior (no flag)
            english_translation.append(english_char)

    return ''.join(english_translation)


# Main function to handle input and determine translation direction
def main():
    input_string = ' '.join(sys.argv[1:]) # parses input from command line
    if is_braille(input_string):  # Check the type of input to determine translation direction
        sys.stdout.write(braille_to_english(input_string))  # used sys.stdout.write instead of print to avoid newline
    else:
        sys.stdout.write(english_to_braille(input_string))


if __name__ == "__main__":
    main()