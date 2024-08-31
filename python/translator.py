import sys

BrailleToAlphabet = {
    "O.....": 'A',
    "O.O...": 'B',
    "OO....": 'C',
    "OO.O..": 'D',
    "O..O..": 'E',
    "OOO...": 'F',
    "OOOO..": 'G',
    "O.OO..": 'H',
    ".OO...": 'I',
    ".OOO..": 'J',
    "O...O.": 'K',
    "O.O.O.": 'L',
    "OO..O.": 'M',
    "OO.OO.": 'N',
    "O..OO.": 'O',
    "OOO.O.": 'P',
    "OOOOO.": 'Q',
    "O.OOO.": 'R',
    ".OO.O.": 'S',
    ".OOOO.": 'T',
    "O...OO": 'U',
    "O.O.OO": 'V',
    ".OOO.O": 'W',
    "OO..OO": 'X',
    "OO.OOO": 'Y',
    "O..OOO": 'Z',
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

AlphaBetToBraille = {value: key for key, value in BrailleToAlphabet.items()}
NumberToBraille = {value: key for key, value in BrailleToNumber.items()}
SymbolToBraille = {value: key for key, value in BrailleToSymbol.items()}
ActionBetToBraille = {value: key for key, value in BrailleToAction.items()}

def isEnglish(message: str) -> bool:
    for char in message:
        if (char != 'O' or char != '.'):
            return False
    
    return True
    
if __name__ == "__main__":
    message = sys.argv[1]
    print(message)
    
