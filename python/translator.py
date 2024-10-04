import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'capital': '.....O',  
    'number': '.O.OOO', 
    '0': '.OOOOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
}

braille_to_english = {}
for key, value in braille_alphabet.items():
    braille_to_english[value] = key

def is_braille(input_text):
    return all(c in 'O.' for c in input_text)

def to_braille(text):
    result = []
    is_number_mode = False  
    
    for char in text:
        if char.isdigit():
            if not is_number_mode:
                result.append(braille_alphabet['number'])  
                is_number_mode = True
            result.append(braille_alphabet[char])
        elif char == ' ':
            result.append(braille_alphabet[' '])
            is_number_mode = False  
        elif char.isupper():
            result.append(braille_alphabet['capital'])  
            result.append(braille_alphabet[char.lower()])
            is_number_mode = False 
        else:
            result.append(braille_alphabet[char])
            is_number_mode = False  

    return ''.join(result)

def to_english(braille):
    result=[]
    i = 0
    is_capital = False
    is_number = False

    while i < len(braille):
        symbol = braille[i:i+6]

        if symbol == braille_alphabet['capital']:
            is_capital = True
            i += 6
            continue
        elif symbol == braille_alphabet['number']:
            is_number = True
            i += 6
            continue
        elif symbol == braille_alphabet[' ']:
            result.append(' ')
            is_number = False
            i += 6
            continue

        char = braille_to_english.get(symbol, '')

        if is_number:
            result.append(char)
        elif is_capital:
            result.append(char.upper())
            is_capital = False
        else:
            result.append(char)

        i += 6

    return ''.join(result)

def main():
    input = ' '.join(sys.argv[1:])  

    if is_braille(input):
        print(to_english(input))
    else:
        print(to_braille(input))

if __name__ == "__main__":
    main()