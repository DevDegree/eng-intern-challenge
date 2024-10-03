import sys

# Dictionary to map English letter & digits to Braille
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......',
    'cap': '.....O', 'num': '.O.OOO',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...''
}

# Reverse the dictionary to map Braille to English
braille_to_english = {v: k for k, v in english_to_braille}

# Function to translate English to Braille
def translate_to_braille(text):
    result =  []
    is_number_mode = False
    for char in text:
        if char.isupper():
            result.append(english_to_braille['cap'])
            char = char.lower() #Convert to lower case for Braille translation
        if char.isdigit() and not is_number_mode:
            result.append(english_to_braille['num']) #Turn on number mode
            is_number_mode = True
        elif char == ' ': #Turn off number mode
            is_number_mode = False # Reset number mode after a space
        result.append(english_to_braille[char])
    return ''.join(result) #Join the list of Braille characters into a single string
    
# Function to translate Braille to English
def    