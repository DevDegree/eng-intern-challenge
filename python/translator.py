import sys

# English to Braille mapping
english_to_braille = {
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

# Numbers map
number_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# reverse mappings
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_number = {v: k for k, v in number_map.items()}

def translate_braille_to_english(braille):
    """
    Translates a Braille string to its corresponding English text
    """
    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        char = braille[i:i+6]
        if char == english_to_braille['capital_follows']:
            capitalize_next = True
        elif char == english_to_braille['number_follows']:
            number_mode = True
        elif char in braille_to_english:
            letter = braille_to_english[char]
            if number_mode and char in braille_to_number:
                result.append(braille_to_number[char])
            else:
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                result.append(letter)
            if letter == ' ':
                number_mode = False
        i += 6

    return ''.join(result)

def translate_english_to_braille(text):
    """
    Translates an English text string to its corresponding Braille representation
    """
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(english_to_braille['capital_follows'])
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille['number_follows'])
                number_mode = True
            result.append(number_map[char])
        else:
            result.append(english_to_braille[char])
            if char == ' ':
                number_mode = False

    return ''.join(result)

def detect_braille(text):
    """
    Determines if a given string is in Braille format
    """
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def translate(text):
    """
    Detects the input format (Braille or English) and translates it to the opposite format
    """
    if detect_braille(text):
        return translate_braille_to_english(text)
    else:
        return translate_english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(translate(input_text), end='')
    else:
        print("Enter a string please")
