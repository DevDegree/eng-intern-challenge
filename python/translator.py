import sys

# Mapping from English letters and symbols to Braille
english_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', ',': '.O....', ';': '.OO...', ':': '.O.O..',
    '.': '.O.OO.', '!': '.OO.O.', '?': '.OO..O', '-': '..O.O.', '/': '.O.O..',
    '(': '.O.O.O', ')': 'O..O.O', '<': 'OO...O', '>': '..OO.O',
    'capital_follows': '.....O', 'number_follows': '.O.OOO'
}

# Mapping for numbers in Braille
braille_number_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings from Braille to English characters and numbers
braille_to_english_map = {v: k for k, v in english_to_braille_map.items()}
braille_to_number_map = {v: k for k, v in braille_number_map.items()}

def braille_to_english(braille_text):
    """
    Converts a Braille string into the corresponding English text.
    """
    result = []
    index = 0
    capitalize_next = False
    number_mode = False

    while index < len(braille_text):
        symbol = braille_text[index:index+6]
        if symbol == english_to_braille_map['capital_follows']:
            capitalize_next = True
        elif symbol == english_to_braille_map['number_follows']:
            number_mode = True
        elif symbol in braille_to_english_map:
            character = braille_to_english_map[symbol]
            if number_mode and symbol in braille_to_number_map:
                result.append(braille_to_number_map[symbol])
            else:
                if capitalize_next:
                    character = character.upper()
                    capitalize_next = False
                result.append(character)
            if character == ' ':
                number_mode = False
        index += 6

    return ''.join(result)

def english_to_braille(english_text):
    """
    Converts an English text string into the corresponding Braille representation.
    """
    result = []
    number_mode = False

    for char in english_text:
        if char.isupper():
            result.append(english_to_braille_map['capital_follows'])
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille_map['number_follows'])
                number_mode = True
            result.append(braille_number_map[char])
        else:
            result.append(english_to_braille_map[char])
            if char == ' ':
                number_mode = False

    return ''.join(result)

def is_braille_format(text):
    """
    Checks whether the input string is in Braille format.
    """
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def translate_text(text):
    """
    Detects the format of the input (Braille or English) and translates it to the other format.
    """
    if is_braille_format(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(translate_text(input_text), end='')
    else:
        print("Please provide a string to translate.")
