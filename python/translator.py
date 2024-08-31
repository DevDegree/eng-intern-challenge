import sys

BrailleToAlphabet = {
    "O.....": 'a',
    "O.O...": 'b',
    "OO....": 'c',
    "OO.O..": 'd',
    "O..O..": 'e',
    "OOO...": 'f',
    "OOOO..": 'g',
    "O.OO..": 'h',
    ".OO...": 'i',
    ".OOO..": 'j',
    "O...O.": 'k',
    "O.O.O.": 'l',
    "OO..O.": 'm',
    "OO.OO.": 'n',
    "O..OO.": 'o',
    "OOO.O.": 'p',
    "OOOOO.": 'q',
    "O.OOO.": 'r',
    ".OO.O.": 's',
    ".OOOO.": 't',
    "O...OO": 'u',
    "O.O.OO": 'v',
    ".OOO.O": 'w',
    "OO..OO": 'x',
    "OO.OOO": 'y',
    "O..OOO": 'z',
}

BrailleToNumber = {
    "O.....": '1',
    "O.O...": '2',
    "OO....": '3',
    "OO.O..": '4',
    "O..O..": '5',
    "OOO...": '6',
    "OOOO..": '7',
    "O.OO..": '8',
    ".OO...": '9',
    ".OOO..": '0',
}

BrailleToSymbol = {
    "..OO.O": '.',
    "..O...": ',',
    "..O.OO": '?',
    "..OOO.": '!',
    "..OO..": ':',
    "..O.O.": ';',
    "....OO": '-',
    ".O..O.": '/',
    ".OO..O": '<',
    "O..OO.": '>',
    "O.O..O": '(',
    ".O.OO.": ')',
    "......": ' ',
}

BrailleToAction = {
    ".....O": "CF",
    ".O...O": "DF",
    ".O.OOO": "NF"
}

CharacterToBraille = {value: key for key, value in BrailleToAlphabet.items()}
NumberToBraille = {value: key for key, value in BrailleToNumber.items()}
SymbolToBraille = {value: key for key, value in BrailleToSymbol.items()}
ActionToBraille = {value: key for key, value in BrailleToAction.items()}

def isEnglish(message: str) -> bool:
    for char in message:
        if (char != 'O' and char != '.'):
            return True
    
    return False

def EnglishToBraille(message: str) -> str:
    output = ""
    readingNumber = False
    
    for char in message:
        if char.isalpha():
            if char.isupper():
                output += ActionToBraille["CF"]
                char = char.lower()
                
            output += CharacterToBraille[char]
            
        elif isNumber(char):
            if readingNumber == False:
                readingNumber = True
                output += ActionToBraille["NF"]
                
            output += NumberToBraille[char]
            
        elif isPunctuation(char):
            if char == "." and readingNumber:
                output += ActionToBraille["DF"]
            elif char == " ":
                readingNumber = False
                
            output += SymbolToBraille[char]
    
    return output

def isNumber(char: chr) -> bool:
    return char in NumberToBraille.keys()

def isPunctuation(char: chr) -> bool:
    return char in SymbolToBraille.keys()

def BrailleToEnglish(message: str) -> str:
    count = 0
    buffer = ""
    output = ""
    
    numberNext = False
    upperNext = False
    
    for char in message:
        buffer += char
        count += 1
        
        if count == 6:
            if buffer in BrailleToAction.keys():
                if BrailleToAction[buffer] == "CF":
                    upperNext = True
                elif BrailleToAction[buffer] == "NF":
                    numberNext = True
                    
            elif buffer in BrailleToAlphabet.keys() and numberNext == False:
                if upperNext:
                    output += BrailleToAlphabet[buffer].upper()
                    upperNext = False
                else:
                    output += BrailleToAlphabet[buffer]
                    
            elif buffer in BrailleToNumber.keys():
                output += BrailleToNumber[buffer]
                
            else:
                if buffer == "......":
                    numberNext = False
                    
                output += BrailleToSymbol[buffer]
            
            count = 0
            buffer = ""
    
    return output
    
if __name__ == "__main__":
    message = ' '.join(sys.argv[1:])
    
    if isEnglish(message):
        output = EnglishToBraille(message)
    else:
        output = BrailleToEnglish(message)
    
    print(output)
    