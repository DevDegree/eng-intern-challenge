# braille_translator.py
import sys

# Braille mapping for letters, numbers, and special instructions
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 'cap': '.....O',
    'num': '...OOO'
}

# Number mapping in Braille
number_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
}

# Helper function to determine if input is English or Braille
def is_braille(input_string):
    return all(c in 'O.' for c in input_string)

# Function to translate English to Braille
def english_to_braille(input_string):
    result = []
    i = 0
    while i < len(input_string):
        char = input_string[i]
        if char.isupper():
            result.append(braille_dict['cap'])
            char = char.lower()
        if char.isdigit():
            result.append(braille_dict['num'])
            result.append(number_dict[char])
        else:
            result.append(braille_dict.get(char, '......'))
        i += 1
    return ''.join(result)

# Function to translate Braille to English
def braille_to_english(input_string):
    result = []
    i = 0
    is_capital = False
    is_number = False
    while i < len(input_string):
        slice = input_string[i:i+6]
        if slice == braille_dict['cap']:
            is_capital = True
        elif slice == braille_dict['num']:
            is_number = True
        else:
            for key, value in (number_dict if is_number else braille_dict).items():
                if value == slice:
                    char = key.upper() if is_capital else key
                    result.append(char)
                    is_capital = False
                    is_number = False if char == ' ' else is_number
        i += 6
    return ''.join(result)

# Main execution logic
if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

