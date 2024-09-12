dict = {
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
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
    '.': '..OO.O',
    ',': '...O..',
    '?': '..O.OO',
    '!': 'O..O..',
    '-': 'O..O..',
    '/': 'O..O..',
    '<': 'O..O..',
    '>': 'O..O..',
    '()': 'O..O..',
    ')': 'O..O..',
    ' ': '......'
}

reverse_dict_letters = {v: k for k, v in dict.items() if k.isalpha()}
reverse_dict_numbers = {v: k for k, v in dict.items() if k.isdigit()}
reverse_dict_specials = {
    v: k for k, v in dict.items() if k in ['capital', 'decimal', 'number', '.', ',', '?', '!', '-', '/', '<', '>', '()', ' ', ')']
}

def isBraille(input_str):
    parts = input_str.split()
    return all(len(part) == 6 and set(part) <= {'O', '.'} for part in parts)

def translate(input_str):
    isNum = False
    output = ""
    
    if isBraille(input_str):
        braille = []
        for i in range(0, len(input_str), 6):
            braille.append(input_str[i:i+6])
        for i in braille:
            if i in reverse_dict_letters:
                output += reverse_dict_letters[i]
            elif i in reverse_dict_numbers:
                output += reverse_dict_numbers[i]
            elif i in reverse_dict_specials:
                output += reverse_dict_specials[i]
            else:
                output += "?"
    else:
        for char in input_str:
            if char.isupper():
                output += dict['capital']
                output += dict.get(char.lower(), '......')
            elif char.isnumeric():
                if not isNum:
                    output += dict['number']
                    isNum = True
                output += dict.get(char, '......')
            elif char == ".":
                output += dict['decimal']
            elif char == " ":
                isNum = False
                output += dict[' ']
            else:
                output += dict.get(char, '......')

    return output

if __name__ == "__main__":
    import sys
    input_str = ' '.join(sys.argv[1:])
    print(translate(input_str))