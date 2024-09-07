import sys

# English to Braille mappings (6-dot Braille patterns)
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', '.': '..OO.O', ',': '..O...', '!': '..OOO.', '?': '..O.OO', ':': '..00..',
    ';': '..O.O.', '(': 'O.O..O', ')': '.O.OO.'
}

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', 
    '......': ' ', '..OO.O': '.', '..O...': ',', '..OOO.': '!', '..O.OO': '?', '..00..': ':',
    '..O.O.': ';', 'O.O..O': '(', '.O.OO.': ')'
}

braille_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}


# Special symbols
capital_braille = '.....O'  # Capital follows symbol
number_braille = '.O.OOO'   # Number follows symbol

def english_to_braille_converter(input):
    input_array = list(input)
    braille_translation = ''
    digit_symbol = False
    for char in input_array:
        if char.isalpha():
            if char.isupper():
                braille_translation += capital_braille
            braille_translation += english_to_braille[char.lower()]
        elif char.isdigit():
            if digit_symbol == False:
                braille_translation += number_braille
                digit_symbol = True
            braille_translation += english_to_braille[char]
            
        else:
            digit_symbol = False
            braille_translation += english_to_braille[char]
    return braille_translation

def braille_to_english_converter(input):
    divided_per_character = [input[i:i+6] for i in range(0, len(input), 6)]
    english_translation = ''
    is_capital = False
    is_number = False
    for character in divided_per_character:
        if character == capital_braille:
            # capitalize next character
            is_capital = True
        elif character == number_braille:
            # next character is a number
            is_number = True
        elif character == '......':
            # character is a space, which means that following symbols are no longer numbers
            is_number = False
            english_translation += braille_to_english[character]
        else:
            if (is_number):
                english_translation += braille_numbers[character]
            elif (is_capital):
                english_translation += braille_to_english[character].upper()
            else:
                english_translation += braille_to_english[character]
            is_capital = False
    return english_translation

def is_braille(text):
    # Check if the text contains only 'O' and '.' and is in multiples of 6 characters
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text>")
        return
    input_text = sys.argv[1:]
    input_text = ' '.join(input_text)
    if (is_braille(input_text)):
        english = braille_to_english_converter(input_text)
        print(english)
        return english
    if not is_braille(input_text):
        braille = english_to_braille_converter(input_text)
        print(braille)
        return braille
if __name__ == "__main__":
    main()
