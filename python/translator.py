import sys

def brailleToEnglish(brailleText):
    # Braille to English dictionary
    brailleDict = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '.....O': 'capital', '.0...0': 'decimal', '.O.OOO': 'number',
        '..OO.O': '.', 
        '..O...': ',', 
        '..O.OO': '?', 
        '..OOO.': '!', 
        '..OO..' : ':',
        '..O.O.' : ';',
        '....OO' : '-',
        '.O..O.' : '/',
        '.OO..O' : '<',
        # duplicate key for '>' and 'o'
        # 'O..OO.' : '>',
        'O.O..O' : '(',
        '.O.OO.' : ')',
        '......' : ' ',
    }
    # mapping for numbers
    brailleNumDict = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
        'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
    }



    english = ''
    # flags to check if the next character is capital, number or decimal
    cap = False
    num = False
    dec = False

    # loop through every 6 characters
    for i in range(0, len(brailleText), 6):
        char = brailleDict[brailleText[i:i+6]]
        # check if the character is capital, number or decimal and set the flags
        if char == 'capital':
            cap = True
        elif char == 'number':
            num = True
        elif char == 'decimal':
            dec = True
        # check if the character is space and reset the number flag
        elif char == ' ':
            num = False
            english = english + char
        else:
            # capitalize the character if the flag is set
            if cap:
                char = char.upper()
                cap = False
            if num:
            # if number flag is set, convert to number
                char = brailleNumDict[char]
            if dec:
                char = char + '.'
                dec = False
            # append the character to the english string
            english = english + char
    return english

def englishToBraille(englishText):
    # English to Braille dictionary
    brailleDict = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
     'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
     'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
     'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
     'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
     'z': 'O..OOO', 'capital': '.....O', 'decimal': '.0...0', 'number': '.O.OOO', 
     '.': '..OO.O', 
     ',': '..O...', 
     '?': '..O.OO', 
     '!': '..OOO.', 
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
    # mapping for numbers
    brailleNumDict = { '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
        '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
    }
    
    braille = ''
    # number flag
    num = False
    for char in englishText:
        # check for capital, number, decimal, space and append the corresponding braille character
        if char.isupper():
            braille = braille + brailleDict['capital'] + brailleDict[char.lower()]
        elif char.isdigit():
            if not num:
                braille = braille + brailleDict['number']
                num = True
            braille = braille + brailleDict[brailleNumDict[char]]
        elif char == '.':
            braille = braille + brailleDict['decimal']
        elif char == ' ':
            print("space", brailleDict[char], char)
            braille = braille + brailleDict[char]
            num = False
        # else append the corresponding braille character
        else:
            braille = braille + brailleDict[char]
    return braille

def main():
    input = sys.argv[1]
    # input is braille if it contains only O and . and the length is a multiple of 6
    if all(char in 'O.' for char in input) and len(input) % 6 == 0:
        print(brailleToEnglish(input))
    else:
        print(englishToBraille(input))

if __name__ == '__main__':
    main()