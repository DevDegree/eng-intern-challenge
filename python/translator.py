import sys
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'decimal': '.O.OOO', 'number': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', 
    ' ': '......'
}
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z',
    '.....O': 'capital', '.O.OOO': 'number', '......': ' '
    }
braille_to_english_number = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0', 
}


def check_braille(string):
    for char in string:
        if char not in 'O.':
            return False # English string
    return True # braille

def translate_english(english):
    result = []
    is_number = False
    for char in english:
        if char.isdigit(): #numbers O-9
            if not is_number:
                result.append(english_to_braille['number'])
                is_number = True
            result.append(english_to_braille[char])
        elif char.isalpha(): # letters a-z
            if is_number:
                is_number = False
            if char.isupper():
                result.append(english_to_braille['capital'])
                char = char.lower()
            result.append(english_to_braille[char])
        else:   # space, no other possible chars here
            result.append(english_to_braille[' '])

    return ''.join(result)

def translate_braille(braille):
    result = []
    is_number = False
    i = 0
    while i < len(braille):
        char = braille[i:i+6]
        if char == english_to_braille['capital']:
            # check if next char is capitalized
            i = i+6
            char = braille[i:i+6]
            result.append(braille_to_english[char].upper()) # add capitalized letter
        elif char == english_to_braille['number']:
            is_number = True
        elif char == english_to_braille[' ']:
            is_number = False
            result.append(' ')
        else:
            if is_number:
                result.append(braille_to_english_number[char])
            else:
                result.append(braille_to_english[char])
        i = i+6

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Please add the string that you want to translate when running this program")
        sys.exit(1)
    input = ' '.join(sys.argv[1:])  # get the input string

    if check_braille(input):
        print(translate_braille(input))
    else:
        print(translate_english(input))



if __name__ == '__main__':
    main()

