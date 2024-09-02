'''
Author: Emily Peng 
Created: Aug 31, 2024

Description:
- Program determines if input string passed as CLI argument should be translated to english or brialle.
- If input string is in english and matches the regex patten of [a-zA-Z0-9 ], the string is translated to Braille and the result is outputed to the terminal.
- If input string is valid Brialle text, the string is translated to english and the result is outputed to the terminal.
- Program behaviour for all other input strings are not defined and will result in undefined program behaviour.

'''

from sys import argv
from sys import stdout

# global constants
RAISED_DOT: str = 'O'
UNRAISED_DOT: str = '.'
BRAILLE_CAP_FOLLOWS: str = '.....O'
BRAILLE_NUM_FOLLOWS: str = '.O.OOO'
BRAILLE_SPACE: str = '......'
BRAILLE_NON_ALPHANUM_SYMBOLS: list[str] = {BRAILLE_CAP_FOLLOWS, BRAILLE_NUM_FOLLOWS, BRAILLE_SPACE}
BRAILLE_SYMBOL_LEN: int  = 6
ENGLISH_SPACE: str = ' '

BRAILLE_ENGLISH_DICT : dict[str,str]=  { # maps braille symbols to english lowercase letters
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
    'O..OOO': 'z'
}

ENGLISH_BRAILLE_DICT : dict[str,str] = { # reverse map of BRAILLE_ENGLISH_DICT
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO'
}

DIGIT_LETTER_DICT : dict[str, str] = { # maps the numeric digits to the english letter sharing the same braille symbol 
    '1' : 'a',
    '2' : 'b',
    '3' : 'c',
    '4' : 'd',
    '5' : 'e',
    '6' : 'f',
    '7' : 'g',
    '8' : 'h',
    '9' : 'i',
    '0' : 'j',
}

LETTER_DIGIT_DICT : dict[str, str] = { # the reverse map of DIGIT_LETTER_DICT
    'a' : '1',
    'b' : '2',
    'c' : '3',
    'd' : '4',
    'e' : '5',
    'f' : '6',
    'g' : '7',
    'h' : '8',
    'i' : '9',
    'j' : '0'
}

CAPITAL_LETTERS: list[str]=  { # list of uppercase letters 
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
}

class translator :
    def __init__(self) -> None:
        pass;
           
    # returns string containing the english translation to brailleText
    def __braille2English__(self, brailleText: str) -> str:
        englishResult: str = "" 
        brailleSymbol: str = ""
        nextCharCapital: bool = False
        nextCharNumeric: bool = False

        for i in range(0, len(brailleText), BRAILLE_SYMBOL_LEN):
            brailleSymbol = brailleText[i: (i + BRAILLE_SYMBOL_LEN)]

            if brailleSymbol == BRAILLE_CAP_FOLLOWS:
                nextCharCapital = True
                continue;
            
            elif brailleSymbol == BRAILLE_NUM_FOLLOWS:
                nextCharNumeric = True
                continue;
            
            elif brailleSymbol == BRAILLE_SPACE:
                # reset number follows since it affects all symbols until a new space is reached 
                nextCharNumeric = False 
                englishResult = englishResult + ENGLISH_SPACE

            else: # appending result str with the appropriate english char

                if nextCharCapital:
                   englishResult = englishResult + BRAILLE_ENGLISH_DICT[brailleSymbol].upper()
                   nextCharCapital = False # capital follows only affects the symbol directly subsequent to it
                
                elif nextCharNumeric:
                    # uses the relation that braille symbols a-j are repurposed to represent 0-9
                    englishResult = englishResult + LETTER_DIGIT_DICT[BRAILLE_ENGLISH_DICT[brailleSymbol]]

                else:
                    englishResult = englishResult + BRAILLE_ENGLISH_DICT[brailleSymbol]
        
        return englishResult;

    # returns string containing the braille translation of EnglishText
    def __english2Braille__(self, EnglishText: list[str]) -> str:
        brailleResult: str = ""
        curWord: str = ""
        char: str = ""
        
        for i in range(len(EnglishText)):
            curWord = EnglishText[i]

            for j in range(len(curWord)):
                char = curWord[j: j + 1]
                if char in CAPITAL_LETTERS:
                    brailleResult = brailleResult + BRAILLE_CAP_FOLLOWS + ENGLISH_BRAILLE_DICT[char.lower()]

                elif char in DIGIT_LETTER_DICT and j == 0:
                    brailleResult = brailleResult + BRAILLE_NUM_FOLLOWS + ENGLISH_BRAILLE_DICT[DIGIT_LETTER_DICT[char]]
                
                elif char in DIGIT_LETTER_DICT:
                    brailleResult = brailleResult + ENGLISH_BRAILLE_DICT[DIGIT_LETTER_DICT[char]]
                
                else:
                    brailleResult = brailleResult + ENGLISH_BRAILLE_DICT[char]

            if (i < len(EnglishText) - 1):
                brailleResult = brailleResult + BRAILLE_SPACE
        
        return brailleResult
    
    # if inputArr contains valid braille input, returns true. Other wise False 
    def isBraille(self, inputArr: list[str]) -> bool:
        # opted not to  simplying checking for if input contain UNRAISED_DOT
        # as would allow translator to be expanded to the full braille alphabet

        # because braille is not delimited by spaces, there will only be 1 argv element for braille input 
        if len(inputArr) > 1:
            return False; 
    
        inputText : str = inputArr[0]; #

        # determine if the len of input is a multiple of braille symbol length
        if len(inputText) % BRAILLE_SYMBOL_LEN != 0:
            return False;
        
        # chunk input into substring 6-char and verify if substring is a known braille symbol
        for i in range(0, len(inputText), BRAILLE_SYMBOL_LEN):

            substring: str = inputText[ i: (i + BRAILLE_SYMBOL_LEN)]

            if not(substring in BRAILLE_NON_ALPHANUM_SYMBOLS) and not(substring in BRAILLE_ENGLISH_DICT):
                return False

        # input passed all braille checks
        return True
    
    # determines if the inputArr should be translated to english or braille and returns the result of the translation 
    def translate(self, inputArr: list[str]) -> str:
        translatedText : str = ""

        if self.isBraille(inputArr): 
            translatedText = self.__braille2English__(inputArr[0])

        else:
            translatedText = self.__english2Braille__(inputArr)
        
        return translatedText

# main function
translator = translator();
print(translator.translate(argv[1:]));

