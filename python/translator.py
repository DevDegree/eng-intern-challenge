import sys

ALPHA_TO_BRAILLE = {
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
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OO.O',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

NUMBERS_TO_BRAILLE = {
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
    '.': '..OO.O'
}

BRAILLE_TO_ALPHA = {value: key for key, value in ALPHA_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {value: key for key, value in NUMBERS_TO_BRAILLE.items()}

CAPITAL_FOLLOWS = '.....O'
DECIMAL_FOLLOWS = '.O...O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE = '......'

def isBraille(input):
    if (set(input).issubset({'O', '.'}) and (len(input) % 6 == 0)):
        return True
    return False

def convert_to_braille(input):
    res = ""
    i = 0

    while i < len(input):
        if input[i].isdigit():
            isDecimal = False
            converted_num = ""

            while i < len(input) and (input[i] != ' '):
                if input[i] == ".":
                    isDecimal = True
                converted_num += NUMBERS_TO_BRAILLE[input[i]]
                i += 1
            if isDecimal:
                res += DECIMAL_FOLLOWS
            else:
                res += NUMBER_FOLLOWS
            res += converted_num
        else:
            if input[i].isupper():
                res += CAPITAL_FOLLOWS
            res += ALPHA_TO_BRAILLE[input[i].lower()]
            i += 1
    return res

def convert_to_english(input):
    res = ""
    parsing_number = False
    next_capital = False

    for i in range(0, len(input), 6):
        code = input[i:i+6]
        
        if parsing_number:
            if code == SPACE:
                parsing_number = False
                res += " "
            else:
                res += BRAILLE_TO_NUMBERS[code]
        elif next_capital:
            next_capital = False

            if code == 'O..OO.':
                res += 'O' # To distinguish between 'o' and '>'. In this case 'o' prevails since this isnt a number
            else:
                res += BRAILLE_TO_ALPHA[code].upper()
        elif code == CAPITAL_FOLLOWS:
            next_capital = True
        elif (code == NUMBER_FOLLOWS or code == DECIMAL_FOLLOWS):
            parsing_number = True
        else:
            if code == 'O..OO.':
                res += 'o' # To distinguish between 'o' and '>'. In this case 'o' prevails since this isnt a number
            else:
                res += BRAILLE_TO_ALPHA[code]
                
    return res

def main():
    if len(sys.argv) >= 2:

        input = ' '.join(sys.argv[1:])
        
        if isBraille(input):
            print(convert_to_english(input))
        else:
            print(convert_to_braille(input))

    else:
        print("No input")

if __name__ == '__main__':
    main()
    

#Hello World
#.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..

#42
#.O.OOOOO.O..O.O...

#Abc 123
#.....OO.....O.O...OO...........O.OOOO.....O.O...OO....