import sys

# Braille character's representations stored in a dictonary
BRL_MATRIX = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

# Braille capital and number indicators
CAPS_INDICATOR = '.....O'  # Capital letter indicator
NUM_INDICATOR = '.O.OOO'   # Number indicator

# Numbers use the same patterns as a-j
NUM_MATRIX = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......'
}

# Reverse lookup for Braille symbols
ENGLISH_BRL_LOOKUP = {v: k for k, v in BRL_MATRIX.items()}
NUMBER_BRL_LOOKUP = {v: k for k, v in NUM_MATRIX.items()}

# Function to determine if the input is Braille
def is_braille(input_string):
    return all(char in 'O.' for char in input_string) and len(input_string) % 6 == 0

# Function to translate from Braille to English
def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    is_number = False

    while i < len(braille):
        # Check for capital symbol
        if braille[i:i+6] == CAPS_INDICATOR:
            capitalize_next = True
            i += 6
            continue
        # Check for number symbol
        elif braille[i:i+6] == NUM_INDICATOR:
            is_number = True
            i += 6
            continue
        else:
            # Get the next Braille character (6 dots)
            braille_char = braille[i:i+6]
            
            # If we are in number mode, interpret as a number
            if is_number:
                letter = NUMBER_BRL_LOOKUP.get(braille_char, '?')
                result.append(letter)
                i += 6
                # Turn off number mode after a space
                if braille_char == BRL_MATRIX[' ']:
                    is_number = False
            else:
                # Interpret as a letter
                letter = ENGLISH_BRL_LOOKUP.get(braille_char, '?')
                if capitalize_next:
                    letter = letter.upper()  # Capitalize next letter
                    capitalize_next = False  # Reset capitalization flag
                result.append(letter)
                i += 6
    return ''.join(result)

# Function to translate from English to Braille
def english_to_braille(text):
    result = []
    for i, char in enumerate(text):
        # Verify if character is an alphabet
        if char.isalpha():
            if char.isupper():
                result.append(CAPS_INDICATOR)
                char = char.lower()
            result.append(BRL_MATRIX.get(char, '......'))

        # Check if its a number
        elif char.isdigit():
            # Add braille number indicator to the result if the preceeding character \
            # is not a digit or when the very first character is a digit 
            if (not text[i-1].isdigit() or i==0):
                result.append(NUM_INDICATOR)
            result.append(NUM_MATRIX.get(char, '......'))

        # Add braille for space (and other special characters)
        else:
            result.append('......')

    return ''.join(result)

# Main function that handles input and determines the translation direction
def main():
    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()

