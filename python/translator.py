# A command-line application that translates between English and Braille and vice versa.

import sys

# Braille translation dictionaries
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
    'O..OOO': 'z', '......': ' ', '.....O': '1', '..O...': '2', '...O..': '3', 
    '...OO.': '4', '..OO..': '5', '..OOO.': '6', '..OO.O': '7', '..O.O.': '8',
    '..O.OO': '9', '...OOO': '0'
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

def translate(input_string):
    # Detect if the input is English or Braille based on characters
    if set(input_string).issubset({'O', '.'}):
        # Input is Braille
        words = input_string.split(' ')
        translated = ''.join(braille_to_english.get(word, '?') for word in words)
    else:
        # Input is English
        translated = ' '.join(english_to_braille.get(char, '......') for char in input_string.lower())
    return translated

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        sys.exit(1)
    
    input_string = sys.argv[1]
    result = translate(input_string)
    print(result)
