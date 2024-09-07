import sys

BRAILLE_TO_SPECIAL_SYMBOL = {
    '.....O': 'CAPITAL',
    '.O...O': 'DECIMAL',
    '.O.OOO': 'NUMBER',
}

SPECIAL_SYMBOL_TO_BRAILLE = {symbol: braille for braille, symbol in BRAILLE_TO_SPECIAL_SYMBOL.items()}

BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '..OO.O': '.', '......': ' ',
}

ENGLISH_TO_BRAILLE = {english: braille for braille, english in BRAILLE_TO_ENGLISH.items()}

BRAILLE_TO_NUMBER = {
    '.OOO..': 'O',
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
}

NUMBER_TO_BRAILLE = {number: braille for braille, number in BRAILLE_TO_NUMBER.items()}

def translateText(text):
    """
    Translates between braille and english text inputs.
    
    Params:
        text (str): The text input to be translated.
    
    Returns:
        str: The translated text.
    """
    if determineAlphabetType(text) == 'Braille':
        return brailleToEnglish(text)
    return englishToBraille(text)

def determineAlphabetType(text):
    """
    Determines the type of text input recieved. Either 'English' or 'Braille'.
    
    Params:
        text (str): The text input.
    
    Returns:
        str: The text input type. Either 'English' or 'Braille'.
    """
    if len(text) % 6 != 0: return 'English'
    for char in text:
        if char != '.' and char != 'O': 
            return 'English'
    return 'Braille'
    
    
def brailleToEnglish(input):
    """
    Coverts the braille text input to the english.
    
    Params:
        text (str): The braille text to be converted.
    
    Returns:
        str: The converted text.
    """
    res, i = '', 0
    while i < len(input):
        braile = input[i : i + 6]
        
        if braile in BRAILLE_TO_SPECIAL_SYMBOL:
            symbol = BRAILLE_TO_SPECIAL_SYMBOL[braile]
            
            i += 6
            braile = input[i : i + 6]
            
            if symbol == 'CAPITAL':
                res += BRAILLE_TO_ENGLISH[braile].upper()
            elif symbol == 'DECIMAL':
                res += BRAILLE_TO_ENGLISH[braile]
            elif symbol == 'NUMBER':
                while i < len(input):
                    if braile == '......':
                        res += ''
                        break
                    res += BRAILLE_TO_NUMBER[braile]
                    i += 6
                    braile = input[i : i + 6]
        else:
            res += BRAILLE_TO_ENGLISH[braile]
            
        i += 6     
    return res
    

def englishToBraille(text: str) -> str:
    """
    Coverts the english text input to the corresponding braille format.
    
    Params:
        text (str): The english text to be converted.
    
    Returns:
        str: The converted text.
    """
    res, i = '', 0
    while i < len(text):        
        if text[i].isupper():
            res += SPECIAL_SYMBOL_TO_BRAILLE['CAPITAL'] + ENGLISH_TO_BRAILLE[text[i].lower()]
        elif text[i] == '.':
            res += SPECIAL_SYMBOL_TO_BRAILLE['DECIMAL'] + ENGLISH_TO_BRAILLE['.']
        elif text[i].isdigit():
            res += SPECIAL_SYMBOL_TO_BRAILLE['NUMBER']
            while i < len(text):
                if not text[i].isdigit():
                    res += ENGLISH_TO_BRAILLE[' ']
                    break
                res += NUMBER_TO_BRAILLE[text[i]]
                i += 1
            continue
        else:
            res += ENGLISH_TO_BRAILLE[text[i]]
            
        i += 1
    return res

def main():
    if len(sys.argv) == 2:
        print(translateText(sys.argv[1]))
    elif len(sys.argv) > 2:
        res = [ translateText(arg) for arg in sys.argv[1:]]
        print('......'.join(res))

if __name__ == '__main__':
    main()