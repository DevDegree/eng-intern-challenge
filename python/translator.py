import sys

# Mapping of English letters to Braille symbols
ENGLISH_TO_BRAILLE_LETTERS = {
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

# Mapping of English digits to Braille symbols
ENGLISH_TO_BRAILLE_NUMBERS = {
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

# Reverse mapping for Braille to English conversion
BRAILLE_TO_ENGLISH_NUMBERS = {v: k for k, v in ENGLISH_TO_BRAILLE_NUMBERS.items()}
BRAILLE_TO_ENGLISH_LETTERS = {v: k for k, v in ENGLISH_TO_BRAILLE_LETTERS.items()}

# Special Braille symbols
BRAILLE_SPACE = '......'
BRAILLE_CAPITAL_INDICATOR = '.....O'
BRAILLE_NUMBER_INDICATOR = '.O.OOO'

# Set of all valid Braille symbols (letters, numbers, special symbols)
VALID_BRAILLE_SYMBOLS = set(BRAILLE_TO_ENGLISH_LETTERS) | set(BRAILLE_TO_ENGLISH_NUMBERS) | {BRAILLE_SPACE, BRAILLE_CAPITAL_INDICATOR, BRAILLE_NUMBER_INDICATOR}

def is_braille(input_text) -> bool:
    """
    Check if the input text is in Braille format.
    Braille strings must be a multiple of 6 characters and consist only of valid Braille symbols.
    """
    if len(input_text) % 6 != 0:
        return False
    for i in range(0, len(input_text), 6):
        chunk = input_text[i:i+6]
        if chunk not in VALID_BRAILLE_SYMBOLS:
            return False
    return True

def convert_braille_to_english(braille_text: str) -> str:
    """
    Convert a Braille string to its corresponding English translation.
    Handles capitalization and numbers based on special Braille indicators.
    """
    translated_text = ''
    number_mode = False
    capital_mode = False

    for i in range(0, len(braille_text), 6):
        symbol = braille_text[i:i+6]
        
        if symbol == BRAILLE_SPACE:
            translated_text += ' '
            number_mode = False
        elif symbol == BRAILLE_NUMBER_INDICATOR:
            number_mode = True
        elif symbol == BRAILLE_CAPITAL_INDICATOR:
            capital_mode = True
        elif number_mode:
            translated_text += BRAILLE_TO_ENGLISH_NUMBERS[symbol]
        elif capital_mode:
            translated_text += BRAILLE_TO_ENGLISH_LETTERS[symbol].upper()
            capital_mode = False
        else:
            translated_text += BRAILLE_TO_ENGLISH_LETTERS.get(symbol, '')

    return translated_text

def convert_english_to_braille(english_text: str) -> str:
    """
    Convert an English string to its Braille equivalent.
    Handles digits and capitalization with appropriate Braille indicators.
    """
    braille_translation = ''
    number_mode = False

    for char in english_text:
        if char.isdigit():
            if not number_mode:
                braille_translation += BRAILLE_NUMBER_INDICATOR
                number_mode = True
            braille_translation += ENGLISH_TO_BRAILLE_NUMBERS[char]
        elif char == ' ':
            braille_translation += BRAILLE_SPACE
            number_mode = False
        elif char.isupper():
            braille_translation += BRAILLE_CAPITAL_INDICATOR
            braille_translation += ENGLISH_TO_BRAILLE_LETTERS[char.lower()]
        else:
            braille_translation += ENGLISH_TO_BRAILLE_LETTERS.get(char, '')
    
    return braille_translation

def main(arguments: list) -> None:
    """
    Entry point of the application.
    It checks if the input is in Braille or English and calls the respective translation function.
    """
    if len(arguments) < 2:
        print("Usage: python translator.py <text_to_translate>")
        return

    input_text = ' '.join(arguments[1:])
    
    if is_braille(input_text):
        print(convert_braille_to_english(input_text))
    else:
        print(convert_english_to_braille(input_text))

if __name__ == '__main__':
    main(sys.argv)