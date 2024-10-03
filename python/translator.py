import sys

# Define constants for special Braille characters
CAPITAL_FOLLOWS = '.....0'
NUMBER_FOLLOWS = '.0.000'
DECIMAL_FOLLOWS = '.0...0'
SPACE = '......'

# Define Braille to English mappings for Braille letters, numbers, and symbols 
BRAILLE_ALPH_MAP = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
}

BRAILLE_NUM_MAP = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}

BRAILLE_SYMBOL_MAP = {
    "..OO.O": ".", "..O...": ",", "..O.OO": "?",
    "..OOO.": "!", "..OO..": ":", "..O.O.": ";",
    "....OO": "-", ".O..O.": "/", ".OO..O": "<",
    "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")",
}

# Define reverse mappings for English to Braille
REVERSE_BRAILLE_ALPH_MAP = {v: k for k, v in BRAILLE_ALPH_MAP.items()}
REVERSE_BRAILLE_NUM_MAP = {v: k for k, v in BRAILLE_NUM_MAP.items()}
REVERSE_BRAILLE_SYMBOL_MAP = {v: k for k, v in BRAILLE_SYMBOL_MAP.items()}


def translate_to_braille(text):
    translated_text = ''
    is_number = False  # Flag to check if character is a number
    
    # Iterate through each character in the input text
    for char in text:
        if char.isdigit():
            # Show a number follows in Braille if it wasn't already a number
            if not is_number:
                translated_text += NUMBER_FOLLOWS
                is_number = True 
            translated_text += REVERSE_BRAILLE_NUM_MAP[char]
        elif char.isalpha():
            # Handle capital letters
            if char.isupper():
                translated_text += CAPITAL_FOLLOWS
            translated_text += REVERSE_BRAILLE_ALPH_MAP[char.lower()]
            is_number = False  
        elif char == ' ':
            translated_text += SPACE
            is_number = False  
        elif char in REVERSE_BRAILLE_SYMBOL_MAP:
            translated_text += REVERSE_BRAILLE_SYMBOL_MAP[char]
            is_number = False 
        else:
            # Raise an error if the character is not supported
            raise ValueError(f"Character not supported: {char}")

    # Ensure the length of the Braille translation is a valid multiple of 6
    if len(translated_text) % 6 != 0:
        raise AssertionError("Invalid Braille result length: must be a multiple of 6 dots")

    return translated_text


def translate_to_english(braille):
    assert len(braille) % 6 == 0, "Invalid Braille input length"
    next_is = None
    result = ""

    # Process the input Braille text in chunks of 6 characters
    for i in range(0, len(braille), 6):
        current_text = braille[i:i+6]

        # Check for control characters (capital, number, decimal)
        if current_text == CAPITAL_FOLLOWS:
            next_is = 'CAP'
        elif current_text == NUMBER_FOLLOWS:
            next_is = 'NUM'
        elif current_text == DECIMAL_FOLLOWS:
            next_is = 'DECIMAL'
        elif current_text == SPACE:
            result += ' '
            next_is = None
        else:
            # Handle regular Braille letters, numbers, or symbols
            if next_is == 'CAP':
                result += BRAILLE_ALPH_MAP[current_text].upper()
                next_is = None
            elif next_is == 'NUM':
                result += BRAILLE_NUM_MAP[current_text]
                next_is = None
            elif next_is == 'DECIMAL':
                if current_text in BRAILLE_SYMBOL_MAP:
                    result += BRAILLE_SYMBOL_MAP[current_text]
                next_is = None
            else:
                if current_text in BRAILLE_ALPH_MAP:
                    result += BRAILLE_ALPH_MAP[current_text]
                elif current_text in BRAILLE_NUM_MAP:
                    result += BRAILLE_NUM_MAP[current_text]
                elif current_text in BRAILLE_SYMBOL_MAP:
                    result += BRAILLE_SYMBOL_MAP[current_text]
                else:
                    raise ValueError(f"Unsupported Braille text: {current_text}")

    return result


def main():
    input_text = " ".join(sys.argv[1:])
    braille_input = True

    # Determine if the input is Braille or English
    for char in input_text:
        if char not in 'O.':  # If any character is not 'O' or '.', it's English
            translated_text = translate_to_braille(input_text)
            braille_input = False
            break

    # If it wasn't marked as English, assume it's Braille
    if braille_input and len(input_text) % 6 == 0:
        translated_text = translate_to_english(input_text)
    elif braille_input and len(input_text) % 6 != 0:
        raise AssertionError("Invalid Braille input length: must be a multiple of 6 dots")

    print(translated_text)

if __name__ == "__main__":
    main()

