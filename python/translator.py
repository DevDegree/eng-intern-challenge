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

def braille_to_english(message):
    output = []
    i = 0
    numbered = False

    while i < len(message):
        symbol = message[i:i+6]

        if symbol == CHAR_TO_BRAILLE["capital_follows"]:
            output.append(BRAILLE_TO_CHAR[message[i+6:i+12]].upper())
            i += 12
        
        elif symbol == CHAR_TO_BRAILLE["number_follows"]:
            numbered = True
            i += 6
        
        else:
            char = BRAILLE_TO_CHAR[symbol]
            if numbered and char.isalpha():
                numbered = False

            output.append(char)
            i += 6
    
    return "".join(output)

def english_to_braille(message):

    output = []
    numbered = False

    for char in message:
        if char.isupper():
            output.append(CHAR_TO_BRAILLE['capital_follows'])
            char = char.lower()

        elif char.isdigit() and not numbered:
            numbered = True
            output.append(CHAR_TO_BRAILLE['number_follows'])
        
        elif not char.isdigit():
            if char.isspace():
                numbered = False
            output.append(CHAR_TO_BRAILLE[char])
    
    return ''.join(output)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
        if all(char in "O." for char in message) and len(message) % 6 == 0:
            print(braille_to_english(message))
        else:
            print(english_to_braille(message))

