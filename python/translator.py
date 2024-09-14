import sys

# Dictionaries for translation
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' ',
    '..O...': ',', '..O.O.': ';', '..OO..': ':', '..OOO.': '!', '..O.OO': '?',
    '..OO.O': '.', '....OO': '-', '.O..O.': '/', 'O.O..O': '(', '.O.OO.': ')',
    '.OO..O': '<', '.O.OO.': '>'
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}  # Reversed dictionary for English to Braille

# Numbers are like a-j but with the number symbol in front
NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

def detect_input_type(input_str):
    """Detect whether the input is Braille or English."""
    return 'braille' if any(c in input_str for c in 'O.') else 'english'

def translate_braille_to_english(braille_str):
    """Translate Braille to English."""
    english_output, capitalize_next, number_mode = [], False, False
    i = 0

    while i < len(braille_str):
        symbol = braille_str[i:i + 6]
        
        if symbol == '.....O':  # Capital symbol
            capitalize_next = True
            i += 6
            continue
        elif symbol == '.O.OOO':  # Number symbol
            number_mode = True
            i += 6
            continue

        char = BRAILLE_TO_ENGLISH.get(symbol, '?')  # Handle unknown symbols

        if number_mode:
            if char == ' ':
                number_mode = False
            else:
                char = next((k for k, v in NUMBERS.items() if v == symbol), '?')

        if capitalize_next and char != ' ':
            char = char.upper()
            capitalize_next = False

        english_output.append(char)
        i += 6

    return ''.join(english_output)

def translate_english_to_braille(english_str):
    """Translate English to Braille."""
    braille_output, number_mode = [], False

    for char in english_str:
        if char.isupper():
            braille_output.append(ENGLISH_TO_BRAILLE['capital'])
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                braille_output.append(ENGLISH_TO_BRAILLE['number'])
                number_mode = True
            braille_output.append(NUMBERS[char])
        else:
            if number_mode:
                number_mode = False
            braille_output.append(ENGLISH_TO_BRAILLE.get(char, '......'))
    return ''.join(braille_output)

if __name__ == "__main__":
    input_str = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else ''

    # Detect input type and perform the appropriate translation
    translation_function = translate_braille_to_english if detect_input_type(input_str) == 'braille' else translate_english_to_braille
    print(translation_function(input_str), end='')

