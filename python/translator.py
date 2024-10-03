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
def translate_to_english(braille):
    result = []
    is_capital = False
    is_number_mode = False # Flag to indicate if we are in number mode
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]
        if braille_char == '.....0': # Capital letter indicator
            is_capital = True
        elif braille_char == '.O.OOO': # Number indicator
            is_number_mode = True 
        elif braille_char == '......': # Space
            result.append(' ') # Add a space to the result
            is_number_mode = False
        else:
            translated_char = braille_to_english.get(braille_char, '')
            if is_capital:
                translated_char = translated_char.upper()
                is_capital = False #Only capitalize the next letter
            if is_number_mode and translated_char.isdigit():
                translated_char = str(int(translated_char)) #Ensure it's a number
            result.append(translated_char)
    return ''.join(result) #Join the list of English characters into a single string    
        