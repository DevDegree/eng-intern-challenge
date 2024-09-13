import sys

brailleToEnglish = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '..O..O': '-',
    '..O..O': '/',
    '..O.O.': '<',
    '..OO.O': '>',
    '..OO..': '(',
    '..OO..': ')',
    '......': ' '
}

brailleToNumber = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
    '......': ' '
}



class Translator:

    def searchByValue(value, english:bool):
        if(english):
            return(list(brailleToEnglish.keys())[list(brailleToEnglish.values()).index(value)])
        else:
            return(list(brailleToEnglish.keys())[list(brailleToNumber.values()).index(value)])
    
    def isBraille(inputString):

        if len(inputString) % 6 != 0:
            return False

        for item in inputString:
            if item != "." or item != "O":
                return False
            
        return True
    
    def translateBraille(inputString):

        capital = False
        number = False
        outputString = []
        splitStrings = inputString
        size = 6

        splitStrings = [splitStrings[i:i+size] for i in range(0,len(splitStrings),size)]

        for item in splitStrings:
            
            if(item == '.....O'):
                capital = True
                continue

            if(item == '.O.OOO'):
                number = True
                continue

            if(item == '.O...O'):
                outputString.append(".")
            
            if(capital):
                outputString.append(brailleToEnglish[item].upper())
            elif(number):
                outputString.append(brailleToNumber[item])
            else:
                outputString.append(brailleToEnglish[item])

            capital = False
            if(item == '......'):
                number = False

        return outputString
    
    def translateEnglish(inputString:str):

        outputString = []
        number = False


        for item in inputString:
            
            if(item.isupper()):
                outputString.append(".....O")
                
            if(item.isnumeric() and number is False):
                number = True
                outputString.append(".O.OOO")

            if(item == '.'):
                outputString.append(".O...O")
                continue

            if(item == ' '):
                number = False
            
            outputString.append(Translator.searchByValue(value=item.lower(), english=not(number)))


        return "".join(outputString)

def main():
    
    if len(sys.argv) < 2:
        sys.exit(1)
    
    input = ""

    if(len(sys.argv) > 1):
        input = (' '.join(item for item in sys.argv[1:]))

    if(Translator.isBraille(input)):
        output = Translator.translateBraille(input)
    else:
        output = Translator.translateEnglish(input)

    print(output)

        
if __name__ == '__main__':
    main()

