english_to_braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.O.O..',
    'j': '.OO...',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.O.OO.',
    't': '.OO.O.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    'capital': '.....O',
}

number_to_braille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.O.O..',
    '0': '.OO...',
    'number': '.O.OOO'
}

braille_to_english = {v: k for k, v in english_to_braille.items()} # Inverting the dictionary
braille_to_number = {v: k for k, v in number_to_braille.items()} # Inverting the dictionary

# Function to detect the input type
def detect_input_type(input_string):
    return 'braille' if set(input_string).issubset({'O', '.'}) else 'english'

# Function to convert English to Braille
def english_to_braille_convert(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(english_to_braille['capital'])
                char = char.lower()
            result.append(english_to_braille[char])
        elif char.isdigit(): 
            if not number_mode:
                result.append(number_to_braille['number'])
                number_mode = True
            result.append(number_to_braille[char])
        elif char == ' ':
            result.append(english_to_braille[' '])
            number_mode = False
    
    return ''.join(result)

# Function to convert Braille to English
def braille_to_english_convert(braille):
    result = []
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capitalize_next = False
    number_mode = False
    
    for char in braille_chars:
        print(char)
        if char == english_to_braille['capital']:
            capitalize_next = True
        elif char == number_to_braille['number']:
            number_mode = True
        else:
            if number_mode and char in braille_to_number:
                result.append(braille_to_number[char])
            else:
                if char in braille_to_english:
                    letter = braille_to_english[char]
                    if capitalize_next:
                        letter = letter.upper()
                        result.append(letter)
                        capitalize_next = False
                    else: # space
                        result.append(letter)
                        number_mode = False
    
    return ''.join(result)

import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        exit(1)

    input_string = ' '.join(sys.argv[1:])
    input_type = detect_input_type(input_string)

    if input_type == 'braille':
        result = braille_to_english_convert(input_string)
    else:
        result = english_to_braille_convert(input_string)

    print(result)

if __name__ == "__main__":
    main()
