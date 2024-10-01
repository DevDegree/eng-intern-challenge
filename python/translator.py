import sys

# Braille patterns for a-z
braille_alphabet = {
    'a': 'O.....',  
    'b': 'O.O...', 
    'c': 'OO....', 
    'd': 'OO.O..', 
    'e': 'O..O..',  
    'f': 'OOO...',  
    'g': 'OOOO..', 
    'h': 'O.OO..', 
    'i': '.OO...', 
    'j': '.OOO..', 
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
}

# Mapping numbers to Braille
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
    '0': '.OOO..', 
}

# Special symbols
capital_sign = '.....O'
number_sign = '.O.OOO'
space_sign = '......' 

# Mappings for decoding
braille_to_letter = {v: k for k, v in braille_alphabet.items()}
braille_to_number = {v: k for k, v in numbers.items()}

# Check if input is in Braille format
def is_braille_input(input_string):
    s = input_string.replace(' ', '')
    if len(s) % 6 != 0:
        return False
    return all(c in ('O', '.') for c in s)

# Convert braille character to integer
def braille_char_to_int(braille_char):
    code = 0
    for i, c in enumerate(braille_char):
        if c == 'O':
            code |= 1 << i
    return code

# Convert integer to braille character
def int_to_braille_char(code):
    braille_char = ''
    for i in range(6):
        braille_char += 'O' if code & (1 << i) else '.'
    return braille_char

def english_to_braille(text):
    result = []
    braille_word = []
    number_mode = False
    for char in text:
        braille_char = ''
        # Numbers case
        if char.isdigit():
            if not number_mode:
                braille_word.append(number_sign)
                number_mode = True
            braille_char = numbers[char]
        else:
            #Spacebar
            if char.isspace():
                number_mode = False
                braille_char = space_sign
            # Capital letters
            elif char.isupper():
                braille_word.append(capital_sign)
                braille_char = braille_alphabet[char.lower()]
            # Lowercase letters
            else:
                braille_char = braille_alphabet.get(char.lower(), '')
        if braille_char:
            braille_word.append(braille_char)
    result.append(''.join(braille_word))
    return ''.join(result)

def braille_to_english(braille_text):
    result = []
    count = 0
    braille_word = ''
    number_mode = False
    capital_mode = False

    for character in braille_text: 
        # parsing every 6 char into one braille word
        if count < 6:
            braille_word += character
            count += 1
        # handling braille words 
        if count == 6: 
            count = 0
            # Special cases (number, capital, space)
            if braille_word == number_sign:
                number_mode = True
            elif braille_word == space_sign:
                number_mode = False
                result.append(' ')
            elif braille_word == capital_sign:
                capital_mode = True
            # Appending actual English char/numbers
            else: 
                if number_mode:
                    result.append(braille_to_number.get(braille_word, ''))
                elif capital_mode:
                    result.append(braille_to_letter.get(braille_word, '').upper())
                    capital_mode = False
                else:
                    result.append(braille_to_letter.get(braille_word, ''))
            braille_word = ''
    return ''.join(result)

def main():
    if len(sys.argv) == 0:
        print("")

    input_string = ' '.join(sys.argv[1:])
    if is_braille_input(input_string):
        translation = braille_to_english(input_string)
    else:
        translation = english_to_braille(input_string)
    print(translation)

if __name__ == "__main__":
    main()
