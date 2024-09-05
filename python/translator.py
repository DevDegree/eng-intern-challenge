
import sys

ENGLISH_BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O',
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ' : '......',
    'capital' : '.....O', 'number' : '.O.OOO'
}

ENGLISH_BRAILLE_NUMBERS = { 
    '0' : '.OOO..', '1' : 'O.....', '2' : 'O.O...', '3' : 'OO....', '4' : 'OO.O..',
    '5' : 'O..O..', '6' : 'OOO...', '7' : 'OOOO..', '8' : 'O.OO..', '9' : '.OO...'
}

BRAILLE_ENGLISH_LETTERS = {v: k for k, v in ENGLISH_BRAILLE_LETTERS.items()}
BRAILLE_ENGLISH_NUMBERS = {v: k for k, v in ENGLISH_BRAILLE_NUMBERS.items()}

def convert_to_braille(message):
    output = []
    isNumbers = False
    for char in message:
        if char.isdigit() and not isNumbers:
            output.append(ENGLISH_BRAILLE_LETTERS['number'])
            isNumbers = True
        
        if char.isdigit():
            output.append(ENGLISH_BRAILLE_NUMBERS[char])
        elif char.isalpha():
            if char.isupper():
                output.append(ENGLISH_BRAILLE_LETTERS['capital'])
            output.append(ENGLISH_BRAILLE_LETTERS[char.lower()])
            isNumbers = False
        else :
            output.append(ENGLISH_BRAILLE_LETTERS[char])
            isNumbers = False

    return ''.join(output)

def convert_to_english(message):
    output = []
    index = 0
    nextCapital = False
    nextNumber = False

    while index < len(message):
        braille = message[index:index+6]

        if braille == ENGLISH_BRAILLE_LETTERS['capital']:
            nextCapital = True
            index += 6
            continue
        
        if braille == ENGLISH_BRAILLE_LETTERS['number']:
            nextNumber = True
            index += 6
            continue
        
        if nextNumber:
            char = BRAILLE_ENGLISH_NUMBERS.get(braille)
        else:
            char = BRAILLE_ENGLISH_LETTERS.get(braille)

        if nextCapital:
            output.append(char.upper())
            nextCapital = False
        else:
            output.append(char)

        # Reset number mode after space
        if braille == ENGLISH_BRAILLE_LETTERS[' ']:
            nextNumber = False

        index += 6

    return ''.join(output)


def main():
    if len(sys.argv) < 2: 
        sys.exit(1)
    
    translation_input = ' '.join(sys.argv[1:])

    if all(c in {'O', '.'} for c in translation_input):
        print(convert_to_english(translation_input))
    else:
        print(convert_to_braille(translation_input))

if __name__ == '__main__':
    main()
