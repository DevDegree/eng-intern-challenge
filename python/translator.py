import sys

# Mapping of English characters to Braille
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.O..OO', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': '..O...O.....', '2': '..O...O.O...', '3': '..O...OO....', '4': '..O...OO.O..', '5': '..O...O..O..',
    '6': '..O...OOO...', '7': '..O...OOOO..', '8': '..O...O.OO..', '9': '..O....OO...', '0': '..O...O.O.OO'
}

# Reverse mapping from Braille to English
braille_to_english = {v: k for k, v in english_to_braille.items()}

def is_braille(input_string):
    """Determine if the input string is in Braille format."""
    return all(char in 'O.' for char in input_string)

def translate_to_braille(input_string):
    """Translate English text to Braille."""
    braille = []
    for char in input_string:
        if char.isupper():
            braille.append('.....O')  # Capitalization indicator
            char = char.lower()
        braille.append(english_to_braille.get(char, '......'))  # Default to space for unknown chars
    return ''.join(braille)

def translate_to_english(input_string):
    """Translate Braille text to English."""
    english = []
    is_capital = False
    for i in range(0, len(input_string), 6):
        braille_char = input_string[i:i+6]
        if braille_char == '.....O':
            is_capital = True
        else:
            char = braille_to_english.get(braille_char, ' ')
            if is_capital:
                char = char.upper()
                is_capital = False
            english.append(char)
    return ''.join(english)

def main():
    # Join all arguments into a single string
    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()
