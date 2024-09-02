import sys

# Braille to English dictionary
braille_to_letter = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.....O': 'capital', '.O.OOO': 'number','.O...O': '.'
}

# Numbers dictionary
braille_to_number = {
    '.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.O...O': '.'
}

# English to Braille dictionary
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'number': '.O.OOO','.O...O': '.'
}

# Numbers to Braille dictionary
number_to_braille = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
    ,'.O...O': '.'
}


def translate_to_braille(text):
    """
    translate_to_braille(text): Convert English text to Braille.
    """
    braille = ""
    number_mode = False  # Flag to track if we are in number mode

    for char in text:
        if char == ' ':
            braille += '......'
            number_mode = False  # Reset number mode when a space is encountered
        elif char == '.':
            braille += '.O...O'
        elif char.isupper():
            braille += english_to_braille['capital']
            braille += english_to_braille[char.lower()]
            number_mode = False  # Reset number mode when a letter is encountered
        elif char.isalpha():
            braille += english_to_braille[char]
            number_mode = False  # Reset number mode when a letter is encountered
        elif char.isdigit():
            if not number_mode:  # Add "number mode" braille only if not already in number mode
                braille += english_to_braille['number']
                number_mode = True  # Set the flag to indicate we are now in number mode
            braille += number_to_braille[char]

    return braille



def translate_to_english(braille):
    """
    translate_to_english(braille): Converts the Braille text to English.
    """
    english = ""
    i = 0
    capitalize_next = False
    number_mode = False
    while i < len(braille):
        braille_char = braille[i:i+6]

        if braille_char == '.....O':
            capitalize_next = True
            i += 6
            braille_char = braille[i:i+6]
            continue
        elif braille_char == '.O.OOO':
            number_mode = True
            i += 6
            braille_char = braille[i:i+6]
            continue
        elif braille_char == '......':
            english += " "
            number_mode = False
            i += 6
            continue

        # Handle numbers mode
        if number_mode:
            char = braille_to_number.get(braille_char, '')
            english += char

        else:
            char = braille_to_letter.get(braille_char, '')
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            english += char

        i += 6

    return english


def is_braille(text):
    """
    is_braille(text): Checks whether a text is in braille or not
    """
    return all(c in ['O', '.'] for c in text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))
