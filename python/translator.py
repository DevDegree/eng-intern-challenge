import sys

brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

alphabetDict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ', '.....O': 'capital'
}

numDict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
} # I had to create 2 dictionaries as the program kept confusing the braille symbol for 'a' with the braille symbol for '1'

def isBraille(str):
    return all(c in "O." for c in str) #checks if each char in the str is either O or .

def engToBraille(engStr):
    brailleStr = []
    numFlag = False

    for char in engStr:

        if char.isdigit() and not numFlag:
            numFlag = True
            brailleStr.append(brailleDict['number']) # if a digit is found and a number flag isn't raised already, add the number symbol to the output string
        elif char.isalpha() and numFlag:
            numFlag = False
            brailleStr.append('......') # if a number is ending and a alphabet is found, add a space symbol to the output string
        
        if char.isupper():
            brailleStr.append(brailleDict['capital']) # if a capital letter is found add the capital symbol to the output string
            char = char.lower()

        brailleStr.append(brailleDict.get(char, '......')) # translate the character using the braille dictionary, adds a space symbol if the character is not recognized in the dictionary
    
    return ''.join(brailleStr)

def brailleToEng(brailleStr):
    engStr = []
    numFlag = False
    capFlag = False

    for i in range(0, len(brailleStr), 6):
        brailleSym = brailleStr[i:i+6]

        # translating the special characters
        if brailleSym == brailleDict['capital']: # raise the capital flag if capital braille found
            capFlag = True
        elif brailleSym == brailleDict['number']: # raise the number flag if number braille found
            numFlag = True
        elif brailleSym == '......': # add a space character in the output string if space braille found
            engStr.append(' ')
            numFlag = False
        else: # translating regular characters
            if numFlag:
                char = numDict.get(brailleSym, '?') # translate from the number dictionary if the number flag is raised
            else:
                char = alphabetDict.get(brailleSym, '?') # translate from the alphabet dictionary if the number flag is not raised
                if capFlag:
                    char = char.upper() # convert the output character to upper if capital flag is raised
                    capFlag = False
            engStr.append(char)

    return ''.join(engStr)


def main():

    # precautionary code
    if len(sys.argv) < 2:
        print("Please provide an input string to translate. Usage: 'python3 translator.py <input string>'")
        return

    inputStr = ' '.join(sys.argv[1:]) # getting the input string from the command line

    if isBraille(inputStr):
        print(brailleToEng(inputStr))
    else:
        print(engToBraille(inputStr))

if __name__ == "__main__":
    main()