import sys

# Map for converting braille to characters
BRAILLE_TO_CHAR = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' ',
    '.....O': 'capital_follows',
    '.O.OOO': 'number_follows',
}

# Map for converting braille to numbers
BRAILLE_TO_NUM = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
    '......': ' ',
    '.....O': 'capital_follows',
    '.O.OOO': 'number_follows',
}

# Reversed maps
CHAR_TO_BRAILLE = {char: braille for braille, char in BRAILLE_TO_CHAR.items()}
NUM_TO_BRAILLE = {num: braille for braille, num in BRAILLE_TO_NUM.items()}

# Constant for length of braille symbols
BRAILLE_SYMBOL_LENGTH = 6

# Return True if text is in braille, False otherwise
def is_braille(text: str) -> bool:
    return len(text) % BRAILLE_SYMBOL_LENGTH == 0 and all(char in "O." for char in text)

# Split a braille message into a list of braille symbols
def split_braille_message(message: str) -> list[str]:
    return [str(message[i:i+BRAILLE_SYMBOL_LENGTH]) for i in range(0, len(message), BRAILLE_SYMBOL_LENGTH)]

# Output conversion of braille message in english
def braille_to_english(message: str):

    output = ''

    capitalize = False
    numbered = False

    braille_symbols = split_braille_message(message)

    for symbol in braille_symbols:

        if numbered:
            text = BRAILLE_TO_NUM[symbol]
        else:
            text = BRAILLE_TO_CHAR[symbol]    

        if text == 'capital_follows':
            capitalize = True

        elif text == 'number_follows':
            numbered = True

        elif text == ' ':
            if numbered:
                numbered = False
            output += text        
        else:
            if capitalize:
                text = text.upper()
                capitalize = False
            output += text

    return output

# Output conversion of English to braille
def english_to_braille(message: str):
    output = ''

    numbered = False

    for char in message:
        if char.isdigit():

            if not numbered:
                output += NUM_TO_BRAILLE['number_follows']
                numbered = True

            symbol = NUM_TO_BRAILLE[char]
        else:

            if numbered:
                numbered = False

            if char != ' ' and char.isupper():
                output += CHAR_TO_BRAILLE['capital_follows']

            symbol = CHAR_TO_BRAILLE[char.lower()]
            
        output += symbol
    
    return output

message = ' '.join(sys.argv[1:])
output = braille_to_english(message) if is_braille(message) else english_to_braille(message)

sys.stdout.write(output)

