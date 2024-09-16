import sys

# Dictionaries to map Braille to English and vice versa
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',  # Space mapping
    '.....O': 'CAP', '.O.OOO': 'NUM'  # Capital and number indicators
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

NUMBER_MAP = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

# Function to convert Braille to English text
def braille_to_english(braille_string):
    index = 0
    translated_text = []
    capitalize = False
    number_mode = False

    while index < len(braille_string):
        symbol = braille_string[index:index+6]

        if symbol == ENGLISH_TO_BRAILLE['CAP']:
            capitalize = True
        elif symbol == ENGLISH_TO_BRAILLE['NUM']:
            number_mode = True
        elif symbol in BRAILLE_TO_ENGLISH:
            char = BRAILLE_TO_ENGLISH[symbol]
            if number_mode and char in NUMBER_MAP:
                translated_text.append(NUMBER_MAP[char])
            else:
                if capitalize:
                    char = char.upper()
                    capitalize = False
                translated_text.append(char)
            if char == ' ':
                number_mode = False

        index += 6

    return ''.join(translated_text)

# Function to convert English text to Braille
def english_to_braille(text):
    braille_output = []
    number_mode_active = False

    for character in text:
        if character.isupper():
            braille_output.append(ENGLISH_TO_BRAILLE['CAP'])
            character = character.lower()

        if character.isdigit():
            if not number_mode_active:
                braille_output.append(ENGLISH_TO_BRAILLE['NUM'])
                number_mode_active = True
            character = [k for k, v in NUMBER_MAP.items() if v == character][0]
        elif number_mode_active:
            number_mode_active = False

        braille_output.append(ENGLISH_TO_BRAILLE[character])

    return ''.join(braille_output)

# Main translation function that decides the conversion direction
def translate(input_text):
    if set(input_text).issubset({'O', '.'}):
        return braille_to_english(input_text)
    else:
        return english_to_braille(input_text)

# Main script execution
if __name__ == "__main__":
    input_data = ' '.join(sys.argv[1:])
    translation = translate(input_data)
    sys.stdout.write(translation)
    sys.stdout.flush()
