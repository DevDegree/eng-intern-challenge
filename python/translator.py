import sys

# Hardcoded braille letter pairs 
BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.O.O', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

# Hardcoded braille number pairs 
BRAILLE_NUMBERS = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Hardcoded braille miscellaneous pairs 
BRAILLE_MISC = {
    'capital': '.....O', 'number': '.O.OOO'
}

# Translate english into braille 
def translate_english_to_braille(string): 
    braille_string = [] 
    number_mode = False 

    for char in string:
        if char.isdigit() and not number_mode: # If we need to activate number_mode 
            braille_string.append(BRAILLE_MISC['number'])
            number_mode = True 
        elif char == ' ' and number_mode: # Else if we need to deactivate number_mode
            number_mode = False 
        
        if number_mode: # If number_mode, pull from numbers dictionary 
            braille_string.append(BRAILLE_NUMBERS[char])
        elif char.isupper(): # If capital, captialize letter
            braille_string += [BRAILLE_MISC['capital'], BRAILLE_LETTERS[char.lower()]]
        else:
            braille_string.append(BRAILLE_LETTERS[char])
    
    return ''.join(braille_string)

def translate_braille_to_english(string):
    english_string = [] 
    mode_tracker = 'normal'

    if len(string) % 6 != 0: # Braille strings are a multiple of 6 in length 
        return 'ERROR: Invalid braille string'

    for start_index in range(0, len(string), 6):
        braille_character = string[start_index:start_index + 6] # Substring to find each 6 characters 
    
        if braille_character in BRAILLE_MISC: # If we need to update the mode 
           mode_tracker = BRAILLE_MISC[braille_character]
        elif braille_character == '......': # If the character is a space 
            english_string.append(' ')
            mode_tracker = 'normal'
        elif mode_tracker == 'capital': # If we need a capital letter 
            english_string.append(BRAILLE_LETTERS[braille_character].upper())
            mode_tracker = 'normal'
        elif mode_tracker == 'number': # If we need numbers 
            english_string.append(BRAILLE_NUMBERS[braille_character])
        else:
            english_string.append(BRAILLE_LETTERS[braille_character])
            
    return ''.join(english_string)

def is_braille(string): 
    for char in string: 
        if char == '.': # All braille inputs contain . (OOOOOO is not a valid braille but a valid english input) 
            return True 
    return False 

def main(): 
    input_string = ' '.join(sys.argv[1:])

    # Reverses the dictionaries to contain both braille -> english and english -> braille
    BRAILLE_LETTERS.update({value: key for key, value in BRAILLE_LETTERS.items()})
    BRAILLE_NUMBERS.update({value: key for key, value in BRAILLE_NUMBERS.items()})
    BRAILLE_MISC.update({value: key for key, value in BRAILLE_MISC.items()})

    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))

if __name__ == '__main__':
    main()
