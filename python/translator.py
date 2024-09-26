eng_braille = {
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

    'cap': '.....O', 
    'num': '.O.OOO',
    'dec': '.O...O',

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
    ')': '.O.OO.',
    ' ': '......' 
}

braille_eng = {}
for key in eng_braille:
    value = eng_braille[key]
    
    # Handle next appirance of 'value' in the dictionary (as a key), append the character to the list
    if value in braille_eng:
        braille_eng[value].append(key)
        #print(braille_eng[value][0] + "  " + braille_eng[value][1] + "  " + value + "  "+ key)
    else:
        # Handle first appirance of 'value'
        braille_eng[value] = [key]

# Function to convert English text to Braille
def eng_to_braille(text):
    result = []
    num_mode = False
    for char in text:
        # Handle uppercase characters
        if char.isupper():
            result.append(eng_braille['cap']) # Append capitalization marker
            char = char.lower() # Convert to lowercase for further processing
        # Handle numeric mode
        elif char.isdigit() and num_mode == False: 
            num_mode = True 
            result.append(eng_braille['num']) # Append numeric mode marker 
        # Translate character to Braille if it exists in the dictionary
        if char in eng_braille:
            if not char.isdigit() and num_mode == True:
                num_mode = False
            result.append(eng_braille[char]) # Append the Braille equivalent of the character
    return str().join(result) # Join the Braille symbols together into a single string

# Function to convert Braille back to English
def braille_to_eng(braille):
    result = []
    i = 0
    capital = False
    numlock = False
    while i < len(braille):
        symbol = braille[i:i+6] # Extract the next Braille symbol (6-positions)
        if symbol == eng_braille['cap']:
            capital = True # Set capital flag if capitalization marker is found
        elif symbol == eng_braille['num']:
            numlock = True # Set numeric mode flag if numeric marker is found
        elif symbol in braille_eng:
            # Get the English equivalent of the Braille symbol
            char = braille_eng[symbol][0]
            if capital:
                char = char.upper() # Convert to uppercase if capital flag is set
                capital = False
            if numlock and len(braille_eng[symbol]) > 1 and char != ' ':
                char = braille_eng[symbol][1] # Use the numeric equivalent in numeric mode
            else: 
                numlock = False
            result.append(char) # Append the character to the result list
        i += 6
    return str().join(result) # Join the characters together into a single string

import sys

# Main function to handle input and call appropriate translation function
def main():
    input_text = ' '.join(sys.argv[1:])
    
    # Check if input is Braille (only 'O' and '.' characters and valid length)
    if all(c in 'O.' for c in input_text) and len(input_text) % 6 == 0:
        print(braille_to_eng(input_text)) # Convert Braille to English
    else:
        print(eng_to_braille(input_text)) # Convert English to Braille

# Check if script is being run directly, and that an argument is provided
if __name__ == "__main__" and len(sys.argv) > 1:
    main() # Execute the main function
else:
    print("Please run code directly and with an expected argument") # Error message if no argument is provided
