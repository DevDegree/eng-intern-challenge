import sys
from contextlib import redirect_stdout

def braile(string):
    outputString = ""
    isBraileInput = True
    isDecimal = False
    isNumber = False
    isUpper = False
    for letter in string:
        if letter == "." or letter == "O":
            isBraileInput = True
        else:
            isBraileInput = False
            break
    
    braileDict = {
        'a': 'O.....','b': 'O.O...','c': 'OO....','d': 'OO.O..',
        'e': 'O..O..','f': 'OOO...','g': 'OOOO..','h': 'O.OO..',
        'i': '.OO...','j': '.OOO..','k': 'O...O.','l': 'O.O.O.',
        'm': 'OO..O.','n': 'OO.OO.','o': 'O..OO.','p': 'OOO.O.',
        'q': 'OOOOO.','r': 'O.OOO.','s': '.OO.O.','t': '.OOOO.',
        'u': 'O...OO','v': 'O.O.OO','w': '.OOO.O','x': 'OO..OO',
        'y': 'OO.OOO','z': 'O..OOO',' ': '......','1': 'O.....',
        '2': 'O.O...','3': 'OO....','4': 'OO.O..','5': 'O..O..',
        '6': 'OOO...','7': 'OOOO..','8': 'O.OO..','9': '.OO...',
        '0': '.OOO..','.': '..OO.O',',': '..O...','?': '..O.OO',
        '!': '..OOO.',':': '..OO..',';': '..O.O.','-': '....OO',
        '/': '.O..O.','<': '.OO..O',#'>': 'O..OO.',
        '(': 'O.O..O',')': '.O.OO.','capital': '.....O',
        'decimal': '.O...O','number': '.O.OOO',
    }
    
    def textToBraile(string, outputString, isDecimal, isNumber):
        for i, letter in enumerate(string):
            if letter.isupper(): #If letter is uppercase
                outputString = outputString + braileDict['capital']
                letter = letter.lower()
                outputString = outputString + braileDict[letter]
            elif letter == "." and i > 0 and i < len(string) - 1 and string[i+1].isdigit() and string[i-1].isdigit() and not isDecimal: #If letter is decimal
                outputString = outputString + braileDict['decimal']
                isDecimal = True
            elif letter.isdigit() and not isNumber: #If letter is number
                outputString = outputString + braileDict['number']
                isNumber = True
                outputString = outputString + braileDict[letter]
            elif letter == " ": #If letter is not a number
                isDecimal = False
                isNumber = False
                outputString = outputString + braileDict[letter]
            else: #All other cases
                outputString = outputString + braileDict[letter]
        return outputString
    
    def braileToText(string, outputString, isNumber, isUpper):
        for i in range(0, len(string), 6): #Iterate through string in 6 character increments
            braileLetter = string[i:i+6] #Get 6 character substring
            for key, value in braileDict.items(): #Iterate through dictionary
                if braileLetter == '......': #If substring is a space
                    isNumber = False
                if braileLetter == '.O.OOO': #If substring is a number
                    isNumber = True
                elif braileLetter == '.....O': #If substring is uppercase
                    isUpper = True
                elif value == braileLetter and isNumber and key.isdigit(): #If substring matches dictionary value and is a number
                    outputString = outputString + key
                elif value == braileLetter and value == '.O...O' : #If substring matches dictionary value of decimal
                    outputString = outputString + "."
                elif value == braileLetter and not isNumber and not key.isdigit(): #If substring matches dictionary value in all other cases when it is not a number
                    if isUpper: #If letter is uppercase
                        outputString = outputString + key.upper()
                    else:
                        outputString = outputString + key
                    isUpper = False #Reset isUpper
        return outputString
    
    if(isBraileInput):
        return braileToText(string, outputString, isNumber, isUpper)
    elif(not isBraileInput):
        return textToBraile(string, outputString, isDecimal, isNumber)

def main():
    n = " ".join(sys.argv[1:])
    with redirect_stdout(sys.stderr):
        solution = braile(n)
    print(solution)
    
if __name__ == "__main__":
    main()