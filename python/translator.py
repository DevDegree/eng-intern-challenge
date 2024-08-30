
import sys

"""
Assumptions
1. the arguments are in either English or Braille, not both

2. English inputs have only letters and numbers

3. after an input includes a number, only numbers are present until the next space

4. all Braille inputs are valid


Correction
input : .....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..
output: Abc 234
"""

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

SYMBOL_TO_BRAILLE = {
    'capital': '.....O',
    'number' : '.O.OOO',
    'space'  : '......'
}

def invertDict(dictionary):
    # requires unique keys and values
    inverted = {}
    for key, value in dictionary.items():
        inverted[value] = key
    
    return inverted

def isBraille(text):
    for word in text:
        if '.' in word:
            return True
    return False

def toBraille(text):
    length = len(text)
    braille_output = ''
    
    # merge english to braille lookup tables
    braille_lookup = dict(ENGLISH_TO_BRAILLE.items() | NUMBER_TO_BRAILLE.items() | SYMBOL_TO_BRAILLE.items())
    
    # construct braille output
    for ind, word in enumerate(text, start=1):
        number_follows = False
        
        for _, symbol in enumerate(word):
            if (symbol.isalpha() and symbol == symbol.upper()):
                braille_output += braille_lookup['capital']
            if (symbol.isnumeric() and not number_follows):
                braille_output += braille_lookup['number']
                number_follows = True
            
            braille_output += braille_lookup[symbol.lower()]
        
        if (ind < length):
            # do not add space for last word
            braille_output += braille_lookup['space']
    
    return braille_output
    
def toEnglish(text):
    english_output = ''
    
    # create braille to english lookup
    english_lookup = invertDict(ENGLISH_TO_BRAILLE)
    number_lookup  = invertDict(NUMBER_TO_BRAILLE)
    symbol_lookup  = invertDict(SYMBOL_TO_BRAILLE)
    
    # create list of braille symbols
    braille = []
    for word in text:
        for ind in range(0, len(word), 6):
            braille.append(word[ind : ind+6])
    
    # construct english output
    capital_follows = False
    number_follows  = False
    for symbol in braille:
        if (symbol in symbol_lookup):
            if (symbol_lookup[symbol] == 'space'):
                english_output += ' '
                number_follows = False
                
            capital_follows |= symbol_lookup[symbol] == 'capital'                
            number_follows  |= symbol_lookup[symbol] == 'number'
            continue
        
        # letter or number
        if (number_follows):
            english_output += number_lookup[symbol]
        elif (capital_follows):
            english_output += english_lookup[symbol].upper()
        else:
            english_output += english_lookup[symbol]
        
        capital_follows = False
    
    return english_output

if __name__ == '__main__':
    input_words = sys.argv[1:]
    output = ''
    
    if isBraille(input_words):
        output = toEnglish(input_words)
    else:
        output = toBraille(input_words)
        
    print(output)