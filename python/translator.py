import argparse
import sys
codeTable = {
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
    ' ': '......',
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
    ')': '.O.OO.'}

codeTableNum={
    '.': '..OO.O',
    ',': '..O...',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    ' ': '......'} 


reverseCodeTable = {v: k for k, v in codeTable.items()}
reverseCodeTableNum = {v: k for k, v in codeTableNum.items()}

def brailleToText (brailleInput:str)->str:
    translatedText:str = ''
    isDecimal:bool = False
    isCapital:bool = False
    for i in range(0, len(brailleInput), 6):
        braille_chunk = brailleInput[i:i+6]
        if(braille_chunk == '.O...O' or braille_chunk == '.O.OOO'):
            isDecimal = True
            isCapital = False
            continue
        if (braille_chunk == '.....O'):
            isCapital = True
            isDecimal = False
            continue
               
        if (isDecimal):
            translatedText += reverseCodeTableNum.get(braille_chunk, '?')
        else:
            if (isCapital):
                translatedText += (reverseCodeTable.get(braille_chunk, '?')).upper()
                isCapital = False
            else:
                translatedText += reverseCodeTable.get(braille_chunk, '?')
        if(braille_chunk == ' '):
            translatedText += '......'
    
    return translatedText  
    
def textToBraille(textInput:str)->str:
    translatedText = ''
    isDecimal:bool = True
    for char in (textInput):
        if (char.isupper()):
            translatedText += '.....O'
            isDecimal = True
            translatedText += codeTable.get(char.lower(),'?')
        elif (char.isdigit()):
            if (isDecimal):
                translatedText += '.O.OOO'
                isDecimal = False
            translatedText += codeTableNum.get(char,'?')
        else:
             translatedText += codeTable.get(char.lower(),'?')
        if (char == '......'):
            isDecimal = True     
    return translatedText
    
def isBraille(input:str)->bool:
    if((len(input) % 6) ==0):
        if not all(char in 'O.' for char in input):
            return False
        return True
    return False
    
def main():
    parser = argparse.ArgumentParser(description='Translate between Braille and English.')
    parser.add_argument('input', type=str, help='Input string to translate')
    # args = parser.parse_args()
    input = str(sys.argv[1])
    
    result = brailleToText(input.upper()) if isBraille(input.upper()) else textToBraille(input) 
    print(result)
    
    
if __name__ == '__main__':
    main()