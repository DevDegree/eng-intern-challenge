import sys

# python3: OOO.O.OO.OOO.OOOO.O.OO..O..OO.OO.OO..O.OOOOO....

# translator.py: .OOOO.O.OOO.O.....OO.OO..OO.O.O.O.O.O......OOOO.O..OO.O.OOO...OO.OOOO.O.OO.OOO

# Abc: .....OO.....O.O...OO....

# 123: .O.OOOO.....O.O...OO....

# xYz: OO..OO.....OOO.OOOO..OOO

# Hello world: .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
# 42: .O.OOOOO.O..O.O...
# Abc 123: .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
# Abc 123 xYz: .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    '.....O': 'capital', '.O.OOO': 'number', '......': ' ', 
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..O.O.': ';',
    '..OO..': ':', '....OO': '-', '.O..O.': '/',
    'O.O..O': '(', '.O.OO.': ')'
}

braille_to_number = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
    '.....O': 'capital', '.O.OOO': 'number', '......': ' ',  
    '.OO..O': '<', 'O..OO.': '>',
}

english_to_braille = {
    'A': '.....O' + 'O.....', 'B': '.....O' + 'O.O...', 'C': '.....O' + 'OO....',
    'D': '.....O' + 'OO.O..', 'E': '.....O' + 'O..O..', 'F': '.....O' + 'OOO...',
    'G': '.....O' + 'OOOO..', 'H': '.....O' + 'O.OO..', 'I': '.....O' + '.OO...',
    'J': '.....O' + '.OOO..', 'K': '.....O' + 'O...O.', 'L': '.....O' + 'O.O.O.',
    'M': '.....O' + 'OO..O.', 'N': '.....O' + 'OO.OO.', 'O': '.....O' + 'O..OO.',
    'P': '.....O' + 'OOO.O.', 'Q': '.....O' + 'OOOOO.', 'R': '.....O' + 'O.OOO.',
    'S': '.....O' + '.OO.O.', 'T': '.....O' + '.OOOO.', 'U': '.....O' + 'O...OO',
    'V': '.....O' + 'O.O.OO', 'W': '.....O' + '.OOO.O', 'X': '.....O' + 'OO..OO',
    'Y': '.....O' + 'OO.OOO', 'Z': '.....O' + 'O..OOO', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO', ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ';': '..O.O.',
    ':': '..OO..', '-': '....OO', '/': '.O..O.',
    '(': 'O.O..O',  ')': '.O.OO.', '<': '.OO..O', '>': 'O..OO.'

}

number_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO', ' ': '......',
}

def is_braille(text):
    for c in text:
        if c not in 'O.':
            return False
    return True

def translate_to_english(braille):
    result = ''
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        chunk = braille[i:i+6]

        if chunk == '.....O':  # Capital letter follows
            capitalize_next = True
            i += 6
            continue

        if chunk == '.O.OOO':  # Number follows
            number_mode = True
            i += 6
            continue

        char = braille_to_english.get(chunk, '')
        if capitalize_next:
            char = char.upper()
            capitalize_next = False
        
        if number_mode:
            char = braille_to_number.get(chunk, '')

        result += char
        i += 6

        if char == ' ':  # Reset number mode after space
            number_mode = False

    return result

def translate_to_braille(english):
    result = ''
    number_mode = False
    i = 0

    while i < len(english):

        if english[i].isalpha() and english[i].isupper(): # capital case
            result += english_to_braille[english[i]]
            i += 1

        elif english[i].isalpha() and not english[i].isupper(): # lower case
            result += english_to_braille[english[i].upper()][6:]
            i += 1

        elif english[i] in ".,?!;:-/()<>": # special chars
            result += english_to_braille[english[i]]
            i += 1

        elif english[i] == ' ': # spaces
            result += english_to_braille[' ']
            i += 1

        elif english[i].isnumeric(): # numeric
            if not number_mode:
                number_mode = True
                result += number_to_braille['number']
            result += number_to_braille[english[i]]
            i += 1

    return result


def main():
    input_text = " ".join(sys.argv[1:])

    if is_braille(input_text):
        output = translate_to_english(input_text)
    else:
        output = translate_to_braille(input_text)
    
    print(output)

if __name__ == '__main__':
    main()