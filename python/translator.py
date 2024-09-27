
"""
Hello, I'm Aryan Patel, a CS/BBA student at the University of Waterloo & Wilfrid Laurier University.  
I've always loved Shopify, especially since I created my own e-commerce website during the pandemic.

Here is my Braille translator, which translates both Braille and English.  
I also included functionality for decimal points.


"""

import sys

# Braille dictionary for alphabets, numbers, capitalization, and space
english_to_braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
    'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',  
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', 
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......', 
}

# English dictionary to translate Braille text (Note it will not translate '>' due to an overlap of braille symbols)
braille_to_english_dict = {
    '.....O': 'capital', '.O.OOO': 'number', '.O...O': 'decimal',
    'O.....': 'a1', 'O.O...': 'b2', 'OO....': 'c3', 'OO.O..': 'd4', 'O..O..': 'e5',
    'OOO...': 'f6', 'OOOO..': 'g7', 'O.OO..': 'h8', '.OO...': 'i9', '.OOO..': 'j0',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v',
    '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '..O.O.': ';',
    '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O.O..O': '(', '.O.OO.': ')',
    '......': ' '
}

# O.....O.OOO.OO.OOOO.....OO.OO.......OOO.O.


# Function 1: Translating from English --> Braille
def english_to_braille(english_text):
    # Sets up basic variables
    braille_text = []
    is_number = False

    # Iterates through string
    for char in english_text:
        
        # Checks if char is a number
        if char.isdigit():
            # If not already in a number sequence, initializes the number sequence
            if not is_number:
                braille_text.append(english_to_braille_dict['number'])
                is_number = True
            # Adds the char to the braille_text array
            braille_text.append(english_to_braille_dict[char])

        # Checks if char is an alphabetic char
        elif char.isalpha():
            # If char is an uppercase, stores that information in braille
            if char.isupper():
                braille_text.append(english_to_braille_dict['capital'])
            # Appends the lowercase version of char
            braille_text.append(english_to_braille_dict[char.lower()])

        # Checks if char is a whitespace
        elif char == ' ':
            # Turns off the number sequence and appends a white space
            is_number = False
            braille_text.append(english_to_braille_dict[' '])

        # Checks if char is a .
        elif char == '.':
            # If the program is in a number sequence, appends decimal, else .
            if is_number:
                braille_text.append(english_to_braille_dict['decimal'])
            else:
                braille_text.append(english_to_braille_dict['.'])

        # Otherwise, just appends the char
        else:
            braille_text.append(english_to_braille_dict[char])
    
    # joins the array into a string and returns it
    return ''.join(braille_text)   


# Function 2: Translating from Braille --> English
def braille_to_english(braille_text):
    # sets up variables
    english_text = []
    # converts the braille text into chunks of six elements 
    braille_text = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    is_number = False
    is_next_capital = False

    # iterates through the chunked braille text
    for char in braille_text:
        # tanslates the braille char into english
        translated_char = braille_to_english_dict[char]

        # initializes a number sequence if char is 'number'
        if translated_char == 'number':
            is_number = True
            continue
        # Sets the next letter to be a capital
        elif translated_char == 'capital':
            is_next_capital = True
            continue
        # Appends a decimal and continues
        elif translated_char == 'decimal':
            english_text.append('.')
            continue

        # If char is a whitespace, deactivates the number sequence and appends whitespace
        if translated_char == ' ':
            is_number = False
            english_text.append(' ')
        # Checks if number sequence is active
        elif is_number:
            # Appends the 2nd element of the string i.e. "a1" --> "1" // "j0" --> "0"
            # All numeric charectars are stored as two element strings
            english_text.append(translated_char[1])
        # Checks if the next letter is a capital
        elif is_next_capital:
            # Appends the capitalized version of the letter
            english_text.append(translated_char[0].upper())
            is_next_capital = False
        # Appends anything else to the english_text array
        else:
            english_text.append(translated_char[0])

    # Joins all elements in the array and returns it
    return ''.join(english_text)
        

def main():
    # Checks if there is a valid number of arguements
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    text = ' '.join(sys.argv[1:])
    
    # Determines if the input is Braille or English

    # If it only contains 'O' and '.', and has length divisible by 6, treat it as Braille
    if all(c in "O." for c in text) and (len(text) % 6) == 0:       
        print(braille_to_english(text))
    # Otherwise, treat it as English
    else:   
        print(english_to_braille(text))

if __name__ == "__main__":
    main()




