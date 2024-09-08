import sys

# Braille Alphabet and Numbers (key: writen characters, value: Braille alphabets)
braille_characters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',  
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.0.00.', '>': 'O..OO.', '<': '.OO..O'
}

# dictionary for english characters
english_alphabet = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', 
    '......': ' ',
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':',
    '....OO': '-', '.O..O.': '/', 'O.O..O': '(', '.0.00.': ')', 'O..OO.': '>', '.OO..O': '<'
}

#dictionary for numbers
braille_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# Special characters
braille_capital = '.....O'
braille_number = '.O.OOO'
braille_space = "......"



def is_braille(input_str):
    """Check if the input is likely in Braille."""
    
    return all(c in 'O.' for c in input_str)

def translate_to_braille(english_text):
    """Translate English text to Braille"""
    
    result = []
    number_mode = False  

    for char in english_text:
        
        if char.isupper():
            # Add capital indicator
            result.append(braille_capital)  
            result.append(braille_characters[char.lower()])
            
        elif char.isdigit():
            # Add number indicator
            if not number_mode:
                result.append(braille_number)  
                number_mode = True
            result.append(braille_characters[char])
            
        elif char == ' ':
            # Exit number mode after space
            result.append(braille_characters[' '])  
            number_mode = False  
        
        else:
            result.append(braille_characters.get(char, '......'))  
            number_mode = False  
            
    return ''.join(result)

def translate_to_english(braille_text):
    """Translate Braille text to English"""
    
    result = [] 
    i = 0  
    capitalize_next = False  
    number_mode = False 

    while i < len(braille_text):
        symbol = braille_text[i:i+6]  
        
        # Check if the symbol is the Braille capital indicator.
        if symbol == braille_capital:
            capitalize_next = True 
            i += 6  
        
        # Check if the symbol is the Braille number indicator.
        elif symbol == braille_number:
            number_mode = True  
            i += 6  
        
        # Handle spaces (reset number mode after a space).
        elif symbol == braille_space:
            result.append(' ')  
            number_mode = False 
            i += 6  
        
        # Handle regular letters, digits, and punctuation.
        else:
            if number_mode:
                letter = braille_numbers.get(symbol, '?')  # Get the digit
            else:
                letter = english_alphabet.get(symbol, '?')  # Get the letter

            # If the capitalize flag is set and we're not in number mode
            if capitalize_next and not number_mode:
                letter = letter.upper()  
                capitalize_next = False  
            
            # Append the translated letter or digit to the result
            result.append(letter)
            i += 6  

    return ''.join(result)  

# Main function to handle input
def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    # Join all input arguments into a single string
    input_str = ' '.join(sys.argv[1:]) 

    if is_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    main()

