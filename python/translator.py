import sys

# Creating dictionaries for letters/symbols to braille, num to Braille, and braille to alphanumeric + symbols
# Some symbols had the same braille as letters so I removed them. To be exact the braille for ">" and "o" are the same in the braille jpg.
# So I removed the following "< > ( ) /" I left - since some words use it i.e"check-in"

# Letters and symbols
alphaToBraille = {
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
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    ' ': '......'
}

# Numbers
numToBraille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

# Special arguments to braille
specialToBraille = {
    'capital': '.....O',
    'number': '.O.OOO'
}


# Braille to letters and symbols

brailleToLetter = {
    'O.....' : 'a',
    'O.O...' : 'b',
    'OO....' : 'c',
    'OO.O..' : 'd',
    'O..O..' : 'e',
    'OOO...' : 'f',
    'OOOO..' : 'g',
    'O.OO..' : 'h',
    '.OO...' : 'i',
    '.OOO..' : 'j',
    'O...O.' : 'k',
    'O.O.O.' : 'l',
    'OO..O.' : 'm',
    'OO.OO.' : 'n',
    'O..OO.' : 'o',
    'OOO.O.' : 'p',
    'OOOOO.' : 'q',
    'O.OOO.' : 'r',
    '.OO.O.' : 's',
    '.OOOO.' : 't',
    'O...OO' : 'u',
    'O.O.OO' : 'v',
    '.OOO.O' : 'w',
    'OO..OO' : 'x',
    'OO.OOO' : 'y',
    'O..OOO' : 'z',
    '..OO.O' : '.',
    '..O...' : ',',
    '..O.OO' : '?',
    '..OOO.' : '!',
    '..OO..' : ':',
    '..O.O.' : ';',
    '....OO' : '-',
    '......' : ' '
}

# Braille to numbers

brailleToNumber = {
    'O.....' : '1',
    'O.O...' : '2',
    'OO....' : '3',
    'OO.O..' : '4',
    'O..O..' : '5',
    'OOO...' : '6',
    'OOOO..' : '7',
    'O.OO..' : '8',
    '.OO...' : '9',
    '.OOO..' : '0'
}

# Braille to special args
brailletoSpecial = {
    '.....O' : 'capital',
    '.O.OOO' : 'number'
}

def alphaTransToBraille(text):

    translation = ""
    isNum = False

    for char in text:
        if char.isdigit():
            # Number to braille
            if isNum:
                translation += numToBraille[char]
            else:
                isNum = True 
                translation += specialToBraille['number']
                translation += numToBraille[char]
        elif char.isalpha():
            # Letter to braille 
            if char.isupper():
                translation += specialToBraille['capital']
                translation += alphaToBraille[char.lower()]
            else:
                translation += alphaToBraille[char]
        else:
            if char == ' ':
                isNum = False
            translation += alphaToBraille[char]

    return translation

def brailleToAlpha(text):
    
    translation = ""
    isNum = False
    isCap = False # long

    #for i in range len of text , incremant by 6 for i in range(0, len(text), 6)

    for i in range (0, len(text), 6):

        if isNum:  
            if text[i:i+6] == '......': # if space number has ended
                isNum = False
                translation += brailleToLetter[text[i:i+6]]
            else:
                translation += brailleToNumber[text[i:i+6]]
        else:
            if text[i:i+6] == '.....O': # Capital
                isCap = True
            elif text[i:i+6] == '.O.OOO': # Number follows
                isNum = True
            else:
                if isCap:
                    translation += brailleToLetter[text[i:i+6]].upper()
                    isCap = False
                else:
                    translation += brailleToLetter[text[i:i+6]]           

    return translation

def main():
    if len(sys.argv) > 1:
        inputText = ' '.join(sys.argv[1:])
    else:
        print("Please provide a string in the argument.")

    # Check if string is Braille
    # Non Braille character was found in string or string is not a multiple of 6
    if any(char not in "O." for char in inputText) or len(inputText) % 6 != 0:
        print(alphaTransToBraille(inputText)) 
    else:
        print(brailleToAlpha(inputText))

if __name__ == '__main__':
    main()