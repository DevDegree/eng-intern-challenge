import sys

# Braille to English dictionary
CONST_BRAILLE_TO_ENG = {
    # Braille to Enlgish letters:
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z',

    '......': ' ', # Space
    # Unique symbols:
    '.....O': 'capitalize', # Capital follows
    '.O.OOO': 'number mode' # Number follows
}

# Braille to Numbers dictionary
CONST_BRAILLE_TO_NUM = {
    # Numbers 1-9:
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
    '.OO...': '9', '.OOO..': '0',
}

# English to Braille dictionary
CONST_ENG_TO_BRAILLE = {v: k for k, v in CONST_BRAILLE_TO_ENG.items()}
# English to numbers dictionary
CONST_NUM_TO_BRAILLE = {v: k for k, v in CONST_BRAILLE_TO_NUM.items()}

# A function which takes a Braille input str and prints the translated verion in English.
def translateToEnglish(input):
    translatedEnglish = []
    capitalizeMode = False
    numberMode = False

    brailleSymbols = []
    for idx in range(0, len(input), 6):
        brailleSymbols.append(input[idx : idx + 6])
    
    for symbol in brailleSymbols:
        if symbol == '.....O':
            capitalizeMode = True
        elif symbol == '.O.OOO':
            numberMode = True
        elif symbol == '......':
            translatedEnglish.append(' ')
            numberMode = False
        else:
            try:
                if numberMode:
                    translatedEnglish.append(CONST_BRAILLE_TO_NUM[symbol])
                elif capitalizeMode:
                    translatedEnglish.append(CONST_BRAILLE_TO_ENG[symbol].upper())
                    capitalizeMode = False
                else:
                    translatedEnglish.append(CONST_BRAILLE_TO_ENG[symbol])
            except KeyError:
                print("Invalid Braille phrase given!")
                return

    print(''.join(translatedEnglish))

# A function which takes an English input str and prints the translated verion in Braille.
def translateToBraille(input):
    translatedBraille = []
    numberMode = False
    for char in input:
        try:
            if char.isupper():
                translatedBraille.append(CONST_ENG_TO_BRAILLE['capitalize'])
                char = char.lower()
                translatedBraille.append(CONST_ENG_TO_BRAILLE[char])
            elif char.isdigit():
                if not numberMode:
                    numberMode = True
                    translatedBraille.append(CONST_ENG_TO_BRAILLE['number mode'])
                translatedBraille.append(CONST_NUM_TO_BRAILLE[char])
            elif char == ' ':
                numberMode = False
                translatedBraille.append(CONST_ENG_TO_BRAILLE[' '])
            else:
                translatedBraille.append(CONST_ENG_TO_BRAILLE[char])
                numberMode = False
        except KeyError:
            print("Invalid English phrase given!")
            return
    print(''.join(translatedBraille))

# A function which determines if the input string is in valid Braille format.
def checkBraille(input):
    if (set(input).issubset({'O', '.'})) and (len(input) % 6 == 0):
        return True
    else:
        return False

def main():
    input = " ".join(sys.argv[1:])
    if checkBraille(input):
        translateToEnglish(input)
    else:
        translateToBraille(input)

if __name__ == "__main__":
    main()
