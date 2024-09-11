import sys

# Dictionary to translate English letters to Braille
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......'
}

# Reverse dictionary to translate Braille to English
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}

# Special Braille symbols
BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'

def is_braille(text):
    """Check if the input text is in Braille format."""
    # logic applied: text should contain only 'O' and '.' and should be a multiple of 6
    return set(text).issubset({'O', '.'}) and len(text) % 6 == 0

def english_to_braille(text):
    """Convert English text to Braille."""

    # logic applied: iterate through each character in the text and convert it to Braille
    # by lookin up the dictionary

    result = []
    number_mode = False

    for char in text:
        if char == ' ':
            result.append(ENGLISH_TO_BRAILLE[' '])
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                result.append(BRAILLE_NUMBER)
                number_mode = True
            result.append(ENGLISH_TO_BRAILLE[char])
        else:
            if char.isupper():
                result.append(BRAILLE_CAPITAL)
            result.append(ENGLISH_TO_BRAILLE[char.lower()])

    return ''.join(result)

def braille_to_english(text):
    """Convert Braille text to English."""

    #  logic applied: iterate through each symbol in the text and convert it to English 
    #  by looking up the reverse dictionary

    result = []
    capital_mode = False
    number_mode = False

    for i in range(0, len(text), 6):
        symbol = text[i:i+6]
        if symbol == BRAILLE_CAPITAL:
            capital_mode = True
        elif symbol == BRAILLE_NUMBER:
            number_mode = True
        elif symbol == '......':
            result.append(' ')
            number_mode = False
        elif number_mode:
            result.append(BRAILLE_TO_ENGLISH[symbol])
        else:
            char = BRAILLE_TO_ENGLISH[symbol]
            if capital_mode:
                char = char.upper()
                capital_mode = False
            result.append(char)

    return ''.join(result)

def main():
    # print(f"Received arguments: {sys.argv[1:]}")
    if len(sys.argv) < 2:
        sys.exit("Usage: python translator.py <text>")

    input_text = ' '.join(sys.argv[1:])
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == '__main__':
    main()
