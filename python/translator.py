import sys

# Braille mappings
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital_follows', '.O.OOO': 'number_follows'
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

numbers = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

def chunk_string(string, chunk_size):
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

def braille_to_text(braille):
    chunks = chunk_string(braille, 6)
    result = []
    capitalize_next = False
    number_mode = False

    for chunk in chunks:
        if chunk == english_to_braille['capital_follows']:
            capitalize_next = True
        elif chunk == english_to_braille['number_follows']:
            number_mode = True
        else:
            char = braille_to_english.get(chunk, '')
            if number_mode and char in numbers:
                result.append(numbers[char])
            else:
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                result.append(char)
                number_mode = False

    return ''.join(result)

def text_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille['number_follows'])
                number_mode = True
            result.append(english_to_braille[list(numbers.keys())[list(numbers.values()).index(char)]])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(english_to_braille['capital_follows'])
            if char.lower() in english_to_braille:
                result.append(english_to_braille[char.lower()])
            elif char == ' ':
                result.append(english_to_braille[' '])
            # Ignore characters not in mapping

    return ''.join(result)

def translate(input_string):
    if set(input_string).issubset({'O', '.'}):
        return braille_to_text(input_string)
    else:
        return text_to_braille(input_string)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Not a valid input")
    else:
        input_string = ' '.join(sys.argv[1:])
        print(translate(input_string), end='')