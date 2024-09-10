
import sys

# Braille dictionary
eng_to_braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
    '9': '.OO...', '0': '.OOO..', 
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

braille_to_eng_letters_dict = {
    'O.....': 'a',  'O.O...': 'b',  'OO....': 'c',  'OO.O..': 'd',  'O..O..': 'e',  'OOO...': 'f',  'OOOO..': 'g',  'O.OO..': 'h', 
    '.OO...': 'i',  '.OOO..': 'j',  'O...O.': 'k',  'O.O.O.': 'l',  'OO..O.': 'm',  'OO.OO.': 'n',  'O..OO.': 'o',  'OOO.O.': 'p', 
    'OOOOO.': 'q',  'O.OOO.': 'r',  '.OO.O.': 's',  '.OOOO.': 't',  'O...OO': 'u',  'O.O.OO': 'v',  '.OOO.O': 'w',  'OO..OO': 'x', 
    'OO.OOO': 'y',  'O..OOO': 'z',  
    '......': ' ',  '.....O': 'capital',  '.O.OOO': 'number'
}
# prevent overlap with number that are the same as letters
braille_to_eng_numbers_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 
    'OOO...': '6','OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def is_braille(input_string):
    return all(c in 'O.' for c in input_string)

def english_to_braille(english_text):
    result = []
    num_mode = False
    
    for char in english_text:
        if char.isdigit():
            if not num_mode:
                result.append(eng_to_braille_dict['number'])
                num_mode = True
            result.append(eng_to_braille_dict[char])
        elif char.isalpha():
            if num_mode:
                num_mode = False
            if char.isupper():
                result.append(eng_to_braille_dict['capital'])
            result.append(eng_to_braille_dict[char.lower()])
        elif char == ' ':
            result.append(eng_to_braille_dict[' '])
            num_mode = False
    
    return ''.join(result)

def braille_to_english(braille_text):
    result = []
    num_mode = False
    i = 0
    
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        
        # Handle capitalization
        if braille_char == eng_to_braille_dict['capital']:
            i += 6
            braille_char = braille_text[i:i+6]
            result.append(braille_to_eng_letters_dict[braille_char].upper())
        
        # Handle numbers
        elif braille_char == eng_to_braille_dict['number']:
            num_mode = True
        
        # Handle spaces
        elif braille_char == eng_to_braille_dict[' ']:
            result.append(' ')
            num_mode = False  # Turn off number mode when a space is encountered
        
        # Handle normal letters or numbers
        else:
            # If we're in number mode, treat it as a number
            if num_mode:
                num = braille_to_eng_numbers_dict[braille_char]
                result.append(num)
            else:
                letter = braille_to_eng_letters_dict[braille_char]
                result.append(letter)
                num_mode = False  # Only turn off num_mode when processing a non-number

        i += 6
    
    return ''.join(result)

if __name__ == '__main__':
    # Get input string from the command line
    input_string = " ".join(sys.argv[1:])
    
    # Determine if it's Braille or English and translate
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))
