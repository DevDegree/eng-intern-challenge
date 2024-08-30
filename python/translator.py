import sys
import re

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.O.OOO': 'NUMBER', '.....O': 'CAPITAL', '.O...O': 'DECIMAL',
    '..OO.O':'DECIMAL', '..OO..': '.', '..O...': ',', '..O.OO': '?', '..OO.O': '!',
    '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.O.O..': '>', '.O..O.': '<',
    '..OO..': '(',
}

braille_to_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9',
    '.OOO..': '0', '..OO..': '.'
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

numbers_to_braille = {v: k for k, v in braille_to_numbers.items()}


def translateToBraille(eng_input):
    output = ''
    numberMode = False
    for c in eng_input:
        #check for capital letters
        if c.isupper(): 
            output += english_to_braille['CAPITAL'] 
        
        #check for digits to activate numbermode if not active
        elif c.isdigit(): 
            if numberMode == False:
                numberMode = True
                output += english_to_braille['NUMBER']
        
        #deactivate numbermode if space is detected and numbermode is active
        elif c == ' ': 
            numberMode = False

        #check for decimal
        elif c == '.': 
            if numberMode:
                output += english_to_braille['DECIMAL']

        #if numbermode, take braille from numbers_to_braille dict, else take from english_to_braille dict
        if numberMode: 
            output += numbers_to_braille[c]
        else:
            output += english_to_braille[c.lower()]

    return output

def translateToEnglish(braille_input):
    output = ''
    numberMode = False
    capitalMode = False
    for i in range(0,len(braille_input),6):
        c = braille_input[i:i+6] #check input string in blocks of 6 (length of a braille character)
        
        #check for capitalization
        if c == english_to_braille['CAPITAL']:
            capitalMode = True
            continue

        #check for numbers to activate numbermode
        elif c == english_to_braille['NUMBER']:
            numberMode = True
            continue

        #check for decimal character to skip
        elif c == english_to_braille['DECIMAL']:
            continue
        
        #check for space to deactivate numbermode if active
        elif c == english_to_braille[' ']:
            numberMode = False

        #if numbermode, find english chars from braille_to_numbers dict else find from braille_to_english dict
        if numberMode:
            output += braille_to_numbers[c]
        else:
            if capitalMode:
                output += braille_to_english[c].upper()
                capitalMode = False
            else:
                output += braille_to_english[c]

    return output

def main():
    if len(sys.argv) < 2:
        print("Error: no input string provided")
        return
    
    pattern = r'^[O.]+$'  #regular expression for string entirely made up of only 'O' and '.'

    input_text = ' '.join(sys.argv[1:])
    #print(input_text)

    if bool(re.fullmatch(pattern, input_text)) == True:
        print(translateToEnglish(input_text))
    else:
        print(translateToBraille(input_text))

if __name__ == "__main__":
    main()
