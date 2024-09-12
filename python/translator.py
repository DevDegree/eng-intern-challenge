import sys

# Mapping Braille patterns to English letters
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

# Mapping English letters back to Braille
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Special Braille symbols for numbers and capital letters
number_prefix = '.O.OOO'
capital_prefix = '.....O'

# Number mappings
numbers = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

# Splits a string into chunks of a given size
def chunk_string(string, chunk_size):
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

# Checks if the input text is Braille
def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

# This Braille into English text
def braille_to_text(braille):
    result = []
    chunks = chunk_string(braille, 6)
    capitalize_next = False
    number_mode = False

    for chunk in chunks:
        if chunk == capital_prefix:
            capitalize_next = True
        elif chunk == number_prefix:
            number_mode = True
        else:
            char = braille_to_english.get(chunk, '')
            if number_mode:
                char = numbers.get(char, char)
            elif capitalize_next:
                char = char.upper()
                capitalize_next = False
            
            result.append(char)
            
            if char == ' ':
                number_mode = False

    return ''.join(result)

# This func Converts English text into Braille
def text_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(number_prefix)
                number_mode = True
            result.append(english_to_braille[list(numbers.keys())[list(numbers.values()).index(char)]])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(capital_prefix)
            result.append(english_to_braille[char.lower()])
        elif char == ' ':
            number_mode = False
            result.append(english_to_braille[char])
        else:
            number_mode = False

    return ''.join(result)

# This function whether to translate Braille to English or English to Braille
def translate(input_string):
    if is_braille(input_string):
        return braille_to_text(input_string)
    else:
        return text_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string> [<input_string2> ...]")
        sys.exit(1)
    
    input_string = ' '.join(sys.argv[1:])
    print(translate(input_string), end='')