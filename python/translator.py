
import sys

## some notes 
## -- conversion from english to braille '1a' doesn't work because we are not sure of whether the a will be a letter or number. 
## My program assumes the a will be 1

## -- 'o' has the same braille translation as '>'

# Define braille to english and english to braille dictionaries
engToBraille = {
    'a':'O.....',
    'b':'O.O...',
    'c':'OO....',
    'd':'OO.O..',
    'e':'O..O..',
    'f':'OOO...',
    'g':'OOOO..',
    'h':'O.OO..',
    'i':'.OO...',
    'j':'.OOO..',
    'k':'O...O.',
    'l':'O.O.O.',
    'm':'OO..O.',
    'n':'OO.OO.',
    'o':'O..OO.',
    'p':'OOO.O.',
    'q':'OOOOO.',
    'r':'O.OOO.',
    's':'.OO.O.',
    't':'.OOOO.',
    'u':'O...OO',
    'v':'O.O.OO',
    'w':'.OOO.O',
    'x':'OO..OO',
    'y':'OO.OOO',
    'z':'O..OOO',
    ' ':'......',
    '.':'..OO.O',
    ',':'..O...',
    '?':'..O.OO',
    '!':'..OOO.',
    ':':'..OO..',
    ';':'..O.O.',
    '-':'....OO',
    '/':'.O..O.',
    '<':'.OO..O',
    '>':'O..OO.', ## duplicate of o
    '(':'O.O..O',
    ')':'.O.OO.'
}

special = {
    'capital':'.....O',
    'decimal':'.O...O',
    'number':'.O.OOO'
}

numberToAlphabet = {
    '1':'a',
    '2':'b',
    '3':'c',
    '4':'d',
    '5':'e',
    '6':'f',
    '7':'g',
    '8':'h',
    '9':'i',
    '0':'j'
}

flippedEngToBraille = {value: key for key, value in engToBraille.items() if key != '>'}
flippedSpecial = {value: key for key, value in special.items()}
flippedNumberToAlphabet = {value: key for key, value in numberToAlphabet.items()}

if __name__ == "__main__":

    # last stores whether the last translation was from English to braille or otherwise, used to remove spaces from the end of the final result
    last = None

    # answer is the variable being built
    answer = ''

    # Capture all arguments except the script name
    args = sys.argv[1:]

    # For cases with multiple arguments
    for arg in args:

        # Braille conversion
        if set(arg) == set('O.') and len(arg) % 6 == 0:  
            cur = ['']
            nextCharNum = False
            nextCharCap = False
            # Loop through the braille and convert it
            while arg:
                group = arg[:6]
                arg = arg[6:]
                if group in flippedSpecial:
                    if flippedSpecial[group] == 'capital':
                        nextCharCap = True

                    elif flippedSpecial[group] == 'decimal':
                        nextCharNum = True
                        cur[0] += '.'

                    elif flippedSpecial[group] == 'number':
                        nextCharNum = True
                elif group in flippedEngToBraille:
                    if nextCharCap:
                        nextCharCap = False
                        cur[0] += flippedEngToBraille[group].upper()
                    elif nextCharNum and flippedEngToBraille[group] in flippedNumberToAlphabet:
                        cur[0] += flippedNumberToAlphabet[flippedEngToBraille[group]]
                    else:
                        nextCharNum = False
                        cur[0] += flippedEngToBraille[group]
            answer += cur[0]
            answer += flippedEngToBraille['......']
            last = 'english'
                
        else:
            # English conversion
            cur = ['']
            prevCharNum = False
            # Loop through the English and convert it
            while arg:
                char = arg[0]
                arg = arg[1:]
                if char.isalpha():
                    if char.isupper():
                        cur[0] += (special['capital'])
                        cur[0] += (engToBraille[char.lower()])
                    else:
                        cur[0] += (engToBraille[char])
                    prevCharNum = False
                elif char.isnumeric():
                    if prevCharNum:
                        cur[0] += (engToBraille[numberToAlphabet[char]])
                    else:
                        cur[0] += (special['number'])
                        cur[0] += (engToBraille[numberToAlphabet[char]])
                    prevCharNum = True
                else:
                    if char == '.' and arg and arg[0].isnumeric():
                        cur[0] += (special['decimal'])
                        prevCharNum = True
                    elif char in engToBraille:
                        cur[0] += (engToBraille[char])
                        prevCharNum = False
            answer += cur[0]
            answer += engToBraille[' ']
            last = 'braille'

    if last == 'braille':
        print(answer[:-6])
    else:
        print(answer[:-1])
