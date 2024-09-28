import sys

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '.O....': '1', '.O.O..': '2', '..OO..': '3', '..OOO.': '4', '.OOO..': '5', '..OO.O': '6',
    '..OOOO': '7', '.OOOO.': '8', '.OO.O.': '9', '.OO.OO': '0', '......': ' '
}

CAPITAL_PREFIX = '.....O'
NUMBER_PREFIX = '.O.OOO'

english_to_braille = {v: k for k, v in braille_to_english.items()}
english_to_braille.update({
    ' ': '......'
})

def convertToBraille(englishString):
    brailleOutput = []
    number_mode = False
    for char in englishString:
        if char.isupper():
            brailleOutput.append(CAPITAL_PREFIX)
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                brailleOutput.append(NUMBER_PREFIX)
                number_mode = True
        else:
            number_mode = False
        brailleChar = english_to_braille.get(char, '......')
        brailleOutput.append(brailleChar)
    braille = ''.join(brailleOutput)
    return braille  # Return braille instead of printing

def convertToEnglish(brailleString):
    englishOutput = []
    brailleChars = []
    isNumber = False
    isCapital = False

    for i in range(0, len(brailleString), 6):
        brailleChars.append(brailleString[i:i+6])
    
    for brailleChar in brailleChars:
        if brailleChar == CAPITAL_PREFIX:
            isCapital = True
            continue
        if brailleChar == NUMBER_PREFIX:
            isNumber = True
            continue
        
        char = braille_to_english.get(brailleChar, '?')
        
        if char != '?':
            if isNumber:
                if char in 'abcdefghijklmnopqrstuvwxyz':
                    englishOutput.append(char)
                    isNumber = False
                else:
                    englishOutput.append(char)
            else:
                if isCapital:
                    char = char.upper()
                    isCapital = False
                englishOutput.append(char)
        else:
            englishOutput.append('?')

    english = ''.join(englishOutput).replace('?', '')
    return english  # Return English instead of printing

# Main input handling
if __name__ == "__main__":
    # Check if any arguments were provided
    if len(sys.argv) > 1:
        userInput = ' '.join(sys.argv[1:])  # Join arguments for spaces
    else:
        userInput = input("Enter text: ")

    # Check if input is Braille
    isBraille = all(char in 'O.' for char in userInput)

    if isBraille:
        output = convertToEnglish(userInput)
        print(output)
    else:
        output = convertToBraille(userInput)
        print(output)
