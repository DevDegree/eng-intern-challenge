import sys

# Braille alphabet and number mappings
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', 'cap': '.....O',  
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
    'num': 'O.OOOO', 'decimal': '.O...O',  
}

# Reverse mappings for decoding Braille to English
english_alphabet = {}
for letter, braille in braille_alphabet.items():
    english_alphabet[braille] = letter

english_numbers = {}
for number, braille in braille_numbers.items():
    english_numbers[braille] = number

def is_braille(input_string):
    return all(char in 'O.' for char in input_string)

def translate_to_braille(english_text):
    result = []
    is_number = False

    for char in english_text:
        if char.isupper():
            result.append(braille_alphabet['cap'])  
            char = char.lower()

        if char.isdigit() and not is_number:
            result.append(braille_numbers['num'])  
            is_number = True

        if char in braille_alphabet:
            result.append(braille_alphabet[char])
        elif char in braille_numbers:
            result.append(braille_numbers[char])

        if char == ' ':
            is_number = False
            result.append(braille_alphabet[char])
    
    return ''.join(result)

def translate_to_english(braille_text):
    result = []
    is_capital = False
    is_number = False

    braille_cells = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]

    for cell in braille_cells:
        if cell == braille_alphabet['cap']:
            is_capital = True
            continue

        if cell == braille_numbers['num']:
            is_number = True
            continue

        if is_number:
            result.append(english_numbers.get(cell, ''))
        else:
            letter = english_alphabet.get(cell, '')
            if is_capital:
                letter = letter.upper()
            result.append(letter)

        is_capital = False
        is_number = False

    return ''.join(result)

if __name__ == "__main__":
    print("Arguments passed:", sys.argv) 

    for i, input_text in enumerate(sys.argv[1:]):
        if i > 0:
            print(braille_alphabet[' '], end='')  
        if is_braille(input_text):
            print(translate_to_english(input_text), end='')
        else:
            print(translate_to_braille(input_text), end='')

    print() 
