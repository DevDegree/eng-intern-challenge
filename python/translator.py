# Brandon Vo

import sys

letter_to_braille = {
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
    ' ': '......'
}

number_to_braille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

braille_capital = '.....O'
braille_number = '.O.OOO'

braille_to_letter = {v: k for k, v in letter_to_braille.items()}
braille_to_number = {v: k for k, v in number_to_braille.items()}

def is_braille(input):
    return all(c == '.' or c == 'O' for c in input) # Check if all characters are either '.' or 'O'

def english_to_braille(input):
    output = ''
    is_number = False # Flag since all following symbols are numbers until the next space symbol
    
    for c in input:
        if c.isalpha() or c == ' ': # Check if the character is a letter or a space
            is_number = False
            if c.isupper():
                output += braille_capital # Add the capital indicator
                c = c.lower() # Convert to lowercase to get the braille representation in the dictionary below
            output += letter_to_braille.get(c)
        elif c.isdigit():
            if not is_number:
                is_number = True
                output += braille_number # Add the number indicator
            output += number_to_braille.get(c)

    return output

def braille_to_english(input):
    output = ''
    is_capital = False
    is_number = False

    # Split into 6 character chunks to get the braille representation of each letter
    braille_chunks = [input[i:i+6] for i in range(0, len(input), 6)]

    for chunk in braille_chunks:
        if is_capital: # Previous chunk was a capital indicator
            output += (braille_to_letter.get(chunk)).upper()
            is_capital = False
        elif is_number: # Number indicator has been set previously
            output += braille_to_number.get(chunk)
        elif chunk == braille_capital: # Capital indicator found
            is_capital = True
            is_number = False
        elif chunk == braille_number: # Number indicator
            is_number = True
        else: # No indicator found so it is a letter
            output += braille_to_letter.get(chunk)

    return output

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <input>")
        return

    input = ' '.join(sys.argv[1:])

    if is_braille(input):
        output = braille_to_english(input)
    else:
        output = english_to_braille(input)
    print(output)

# Run the main function if the script is run directly using python3 translator.py
if __name__ == "__main__":
    main()