import sys

# Define constants for special Braille symbols
CAPITAL = '.....O'
NUMBER = '.O.OOO'
SPACE = '......'

# Mappings for English to Braille
BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

NUMERIC_MAP = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings for Braille to English
REVERSE_BRAILLE_LETTER_MAP = {v: k for k, v in BRAILLE_MAP.items()}
REVERSE_BRAILLE_NUMBER_MAP = {v: k for k, v in NUMERIC_MAP.items()}

def is_braille(input_text: str) -> bool:
    # Check if input length is a multiple of 6
    if len(input_text) % 6 != 0:
        return False
    
    # Iterate over the input text in chunks of 6
    for i in range(0, len(input_text), 6):
        chunk = input_text[i:i + 6]
        # Check if the chunk is not in any of the Braille maps or special symbols
        if (
            chunk not in REVERSE_BRAILLE_LETTER_MAP and 
            chunk not in REVERSE_BRAILLE_NUMBER_MAP and 
            chunk != CAPITAL and 
            chunk != NUMBER and 
            chunk != SPACE
        ):
            return False  # If any chunk is invalid, it's not Braille
    
    return True  # All chunks are valid Braille symbols

def translate_to_braille(text):
    result = []
    number_mode = False  # Track whether we're in number mode

    for char in text:
        if char.isupper():
            # Reset number mode and add capital indicator for uppercase letters
            number_mode = False
            result.append(CAPITAL)
            result.append(BRAILLE_MAP[char.lower()])
        elif char.isdigit():
            # Set number mode and add number indicator if the first digit
            if not number_mode:
                result.append(NUMBER)
                number_mode = True
            result.append(NUMERIC_MAP[char])
        elif char == " ":
            result.append(SPACE)
        else:
            # Reset number mode when transitioning from digits to non-digits
            if number_mode and char.isalpha():
                number_mode = False
            result.append(BRAILLE_MAP[char])
    
    return ''.join(result)

def translate_to_english(braille):
    result = []
    index = 0
    number_mode = False
    capital_mode = False

    while index < len(braille):
        braille_char = braille[index:index+6]
        if braille_char == CAPITAL:
            # Set capital mode for the next letter
            capital_mode = True
            index += 6
        elif braille_char == NUMBER:
            # Set number mode for following characters
            number_mode = True
            index += 6
        elif braille_char == SPACE:
            # Append a space and end number mode
            result.append(" ")
            number_mode = False
            index += 6
        else:
            if number_mode:
                # Use number map if number mode is enabled
                char = REVERSE_BRAILLE_NUMBER_MAP.get(braille_char, '')
                result.append(char)
            else:
                # Translate letters if number mode is disabled
                char = REVERSE_BRAILLE_LETTER_MAP.get(braille_char, '')
                if capital_mode:
                    char = char.upper()
                    capital_mode = False  # Reset capital mode after use
                result.append(char)

            index += 6

    return ''.join(result)

if __name__ == '__main__':
    # Concatenate all input arguments into a single string
    concatenated_text = ' '.join(sys.argv[1:])

    # Determine if the concatenated input is Braille or English
    if is_braille(concatenated_text):
        # If the argument is Braille, translate to English
        result = translate_to_english(concatenated_text)
    else:
        # If the argument is English, translate to Braille
        result = translate_to_braille(concatenated_text)

    # Print the final output
    print(result)

