#!/usr/bin/env python3
import sys

# Braille Translator - Command line application 
# Shopify Intern Coding Challenge, applicant: Agamjot Sodhi
# September 12th, 2024


# Dictionary to map Braille symbols to English letters, digits, and special symbols
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '..O...': 'cap', '.O.OOO': 'num'
}

# Dictionary to map English letters, digits, and special symbols to Braille
# Reverses Braille to English dictionary
english_to_braille = {v: k for k, v in braille_to_english.items() if v not in ['cap', 'num', '']}

# Include mappings for numbers and special symbols
english_to_braille.update({
    ' ': '......',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    'cap': '.....',  # Capitalization indicator
    'num': '.O.OOO'  # Number indicator
})

# Add mappings for capital letters by prepending the capitalization marker
# Allows program to handle capital letters in Braille
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    lowercase_braille = english_to_braille.get(letter.lower())
    english_to_braille[letter] = '.....O' + lowercase_braille


# Function to identify if the input string is Braille
def is_braille(s):
    """ Determine if input string is in Braille format. """
    
    return all(c in "O. " for c in s) # Braille strings contain only 'O', '.', and spaces.


# Function to translate Braille to English
def translate_braille_to_english(braille_string):
    """ Translate a Braille string to English. """
    
    words = braille_string.split(' ')
    result = []
    # Handles capitalization and number indicators.
    capital_next = False
    number_mode = False
    
    for word in words:
        while word:
            symbol = word[:6]  # Each Braille character is represented by 6 symbols
            word = word[6:]  # Move to the next character
            
            if symbol == '......':  # Space between words
                result.append(' ')
                capital_next = False
                number_mode = False
            elif symbol == '.....':  # Capitalization indicator
                capital_next = True
            elif symbol == '.O.OOO':  # Number mode indicator
                number_mode = True
            else:
                char = braille_to_english.get(symbol, '')
                if capital_next:
                    char = char.upper()
                    capital_next = False
                if number_mode:
                    if 'a' <= char <= 'j':  # Convert a-j to 1-9
                        char = str(ord(char) - ord('a') + 1)
                    number_mode = False
                result.append(char)
    
    return ''.join(result)


# Function to translate English to Braille
def translate_english_to_braille(english_string):
    """ Translate an English string to Braille. """
    
    result = []
    number_mode = False
    
    for char in english_string:
        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille['num'])  # Add number indicator
                number_mode = True
            result.append(english_to_braille.get(char, ''))
        else:
            if number_mode:
                number_mode = False  # Reset number mode after processing digits
            result.append(english_to_braille.get(char, ''))
    
    return ''.join(result)

def main():
    """ Main function to handle command-line input and determine the translation direction. """
    
    if len(sys.argv) < 2:
        print("Usage: translator.py <string_to_translate>")
        sys.exit(1)
    
    input_string = ' '.join(sys.argv[1:])  # Combine arguments into a single string
    
    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))


if __name__ == "__main__":
    main()
