# author: Annabel Zecchel
# email: zecchelannabel@gmail.com
# Date: Sept. 2. 2024

import sys

# Dictionaries for translations
brDict = {
    'letters': {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO'
    },
    'numbers': {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
        '0': '.OOO..'
    },
    'special': {
        'capital': '.....O', 'number': '.O.OOO', 'space': '......', 
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
        ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
        '<': '.O.O.O', '>': 'O.O.O.', '(': 'O.O..O', ')': '.O.OO.'
    }
}

# reversing dictionaries for other direction
engDict = {
    'letters': {i: j for j, i in brDict['letters'].items()},
    'numbers': {i: j for j, i in brDict['numbers'].items()},
    'special': {i: j for j, i in brDict['special'].items()}
}

def checkBr(brStr):
    """Checks if the string is in Braille by making cells and then checking each cell to make sure they are valid Braille cells."""
    if len(brStr) % 6 != 0:
        return False
    
    for i in range(0, len(brStr), 6):
        if brStr[i:i+6] not in engDict['letters'] and brStr[i:i+6] not in engDict['numbers'] and brStr[i:i+6] not in engDict['special']:
            return False
        
    return True

def engToBr(english):
    """Translates English to Braille, handling numbers, spaces, and capital letters."""
    translated = []
    number_mode = False

    for char in english:
        if char.isdigit():
            if not number_mode:
                translated.append(brDict['special']['number'])
                number_mode = True
            translated.append(brDict['numbers'][char])

        elif char == ' ':
            translated.append(brDict['special']['space'])
            number_mode = False  # number mode after space

        elif char.isupper():
            if not number_mode:
                translated.append(brDict['special']['capital']) 
            translated.append(brDict['letters'][char.lower()]) 
            number_mode = False  # number mode after capital letter

        else:
            translated.append(brDict['letters'].get(char, '?'))  # unknown characters
            number_mode = False  # number mode after any non-digit/non-capital character

    return ''.join(translated)

def brToEng(braille):
    """Translates Braille to English, correctly interpreting numbers, capitals, and spaces."""
    translated = []
    number_mode = False
    capital_mode = False

    for i in range(0, len(braille), 6):
        braille_cell = braille[i:i+6]
        if braille_cell == brDict['special']['capital']:
            capital_mode = True

        elif braille_cell == brDict['special']['number']:
            number_mode = True
        
        elif braille_cell == brDict['special']['space']:
            number_mode = False
            capital_mode = False
            translated.append(' ')
            
        else:
            if braille_cell in (engDict['letters'] if not number_mode else engDict['numbers']):
                char = (engDict['letters'] if not number_mode else engDict['numbers'])[braille_cell]

                # capital mode if true
                if capital_mode:
                    char = char.upper()
                    capital_mode = False 
                
                translated.append(char)
            else:
                translated.append('?')
                
    return ''.join(translated)

def translate(input):
    """Determine which language it is in, and then perform translation."""
    if checkBr(input):
        return brToEng(input)
    else:
        return engToBr(input)

def main():
    """Main function. Handles command line args."""
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        return
    
    input = ' '.join(sys.argv[1:])
    translated = translate(input)
    sys.stdout.write(translated)

if __name__ == "__main__":
    main()