import sys

alphabet = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OO...',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    'cap': '.....O',
    'dec': '.O...O',
    'num': '.O.OOO',
    ' ': '......'
}

decimals = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.'
}

numbers = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

def is_braille(input):
    return set(input) <= {'O', '.'}

def braille_string_to_array(input):
    return [input[i:i+6] for i in range(0, len(input), 6)]

def braille_to_english(input):
    result = ""
    is_capitalized = False
    is_decimal = False
    is_number = False

    sentence = braille_string_to_array(input)

    for char in sentence:
        if (is_decimal):
            english_char = decimals[char]
            is_decimal = False
        elif(is_number):
            english_char = numbers[char]
            is_number = False
        else:
            english_char = alphabet[char]

        if english_char is None:
            return "Provided string is invalid"
        elif english_char == 'cap':
            is_capitalized = True
        elif english_char == 'dec':
            is_decimal = True
        elif english_char == 'num':
            is_number = True
        else:
            result += english_char

        if is_capitalized:
            english_char = english_char.upper()
            is_capitalized = False  

    return result

def english_to_braille(input):
    result = ""
    
    for char in input:
        if char.isupper():
            result += alphabet['cap']
            char = char.lower()

        if char in alphabet:
            result += alphabet[char]
        elif char in decimals:
            result += decimals[char]
        elif char in numbers:
            result += numbers[char]
        else:
            return "Provided string is invalid"
        
    return result

def translate(input_string):
    if is_braille(input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Number of arguments incorrect")
        sys.exit(1)
    
    print(translate(sys.argv[1]))