import sys

if len(sys.argv) < 2:
    sys.exit()

input_args = sys.argv[1:]
input_str = ' '.join(input_args)

#[1,4]
#[2,5]
#[3,6]
letters_dot_positions = {
    'a': [1],
    'b': [1,2],
    'c': [1,4],
    'd': [1,4,5],
    'e': [1,5],
    'f': [1,2,4],
    'g': [1,2,4,5],
    'h': [1,2,5],
    'i': [2,4],
    'j': [2,4,5],
    'k': [1,3],
    'l': [1,2,3],
    'm': [1,3,4],
    'n': [1,3,4,5],
    'o': [1,3,5],
    'p': [1,2,3,4],
    'q': [1,2,3,4,5],
    'r': [1,2,3,5],
    's': [2,3,4],
    't': [2,3,4,5],
    'u': [1,3,6],
    'v': [1,2,3,6],
    'w': [2,4,5,6],
    'x': [1,3,4,6],
    'y': [1,3,4,5,6],
    'z': [1,3,5,6],
    # Punctuation
    ',': [2],
    ';': [2,3],
    ':': [2,5],
    '.': [2,5,6],
    '!': [2,3,5],
    '?': [2,3,6],
    '-': [3,6],
    '/': [3,4],
    '(': [1,2,6],
    ')': [4,5,3],
    '<': [4,2,6],
    '>': [1,5,3],
    ' ': []
}

def get_braille_code(dot_positions):
    positions_order = [1, 4, 2, 5, 3, 6]
    code = ''
    for pos in positions_order:
        if pos in dot_positions:
            code += 'O'
        else:
            code += '.'
    return code

# Build letter to braille and braille to letter mappings
letter_to_braille = {}
braille_to_letter = {}

for letter, dots in letters_dot_positions.items():
    code = get_braille_code(dots)
    letter_to_braille[letter] = code
    braille_to_letter[code] = letter

# Numbers mapping
numbers_to_letters = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '0': 'j'
}

number_to_braille = {}
braille_to_number = {}

for number, letter in numbers_to_letters.items():
    code = letter_to_braille[letter]
    number_to_braille[number] = code
    braille_to_number[code] = number

# Define capital sign and number sign
capital_sign_code = '.....O'  # dot 6
number_sign_code = '.O.OOO'   # dots 3,4,5,6

def is_braille(text):
    text_no_space = text.replace(' ', '')
    if all(c in ('O', '.') for c in text_no_space):
        if len(text_no_space) % 6 == 0:
            return True
    return False

def english_to_braille(text):
    output = ''
    number_mode = False

    for char in text:
        if char.isupper():
            output += capital_sign_code
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                output += number_sign_code
                number_mode = True
            code = number_to_braille[char]
            output += code
        else:
            number_mode = False
            if char in letter_to_braille:
                code = letter_to_braille[char]
                output += code
            else:
                pass  # Ignore unsupported characters
    return output

def braille_to_english(text):
    output = ''
    index = 0
    number_mode = False
    while index < len(text):
        if text[index] == ' ':
            index += 1
            continue
        code = text[index:index+6]
        if code == capital_sign_code:
            index +=6
            if index >= len(text):
                break
            code = text[index:index+6]
            letter = braille_to_letter.get(code, '')
            output += letter.upper()
        elif code == number_sign_code:
            number_mode = True
            index +=6
            continue
        else:
            if number_mode:
                digit = braille_to_number.get(code, '')
                output += digit
            else:
                if code in braille_to_letter:
                    letter = braille_to_letter[code]
                    output += letter
                else:
                    pass  # Ignore unsupported codes
        index += 6
    return output

if is_braille(input_str):
    result = braille_to_english(input_str)
else:
    result = english_to_braille(input_str)

print(result)