import sys
from typing import List

ENG_TO_BRAILLE = {
    "a": "O.....", 
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..", 
    "f": "OOO...",
    "g": "OOOO..", 
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.", 
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.", 
    "P": "OOO.O.", 
    "q": "OOOOO.", 
    "r": "O.OOO.", 
    "s": ".OO.O.", 
    "t": ".OOOO.", 
    "u": "O...OO", 
    "v": "O.O.OO", 
    "w": ".OOO.O", 
    "x": "OO..OO", 
    "y": "OO.OOO", 
    "z": "O..OOO", 
    ".": "..OO.O", 
    ",": "..O...", 
    "?": "..OOO.", 
    "!": "..OOO.", 
    ":": "..O.O.", 
    ";": "..O.O.", 
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O", 
    ">": "O..OO.", 
    "(": "O.O..O",
    ")": ".O.OO.", 
    " ": "......",
    "CAP": ".....O", 
    "NUM": ".O.OOO"
}

NUM_TO_BRAILLE = {
    "1": "O.....", 
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..", 
    "6": "OOO...",
    "7": "OOOO..", 
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

BRAILLE_TO_ENG = {br: ch for ch, br in ENG_TO_BRAILLE.items()}
BRAILLE_TO_NUM = {br: ch for ch, br in NUM_TO_BRAILLE.items()}

def isBraille(arg: List[str]):
    """
    Checks if a given list of strings is a Braille sequence or English sequence.
    Braille sequences must:
        - have only one element (whereas English strings can include spaces, which are parsed as multiple arg elements)
        - have a length divisible by 6, as every Braille character is 6 characters long
        - only contain characters O and .
    """
    return len(arg) == 1 and len(arg[0]) % 6 == 0 and all(ch in {'O', '.'} for ch in arg[0])


class BrailleTranslator:
    """
    Iterator that emits the translated English character for every parsed Braille character
    """
    def __init__(self, braille: str):
        self.braille = braille
        self.idx = -6
        self.cap = False
        self.num = False

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx < len(self.braille) - 6:
            self.idx += 6

            brailleChar = self.braille[self.idx:self.idx + 6]
            englishChar = BRAILLE_TO_ENG[brailleChar]

            if englishChar == 'CAP':
                self.cap = True
                return ''
            elif englishChar == 'NUM':
                self.num = True
                return ''
            elif englishChar == ' ':
                self.num = False  # spaces turn off the num flag
                return englishChar
            else:
                if self.cap:
                    self.cap = False  # only emit one capital after the cap flag
                    return englishChar.upper()
                elif self.num:
                    return BRAILLE_TO_NUM[brailleChar]
                else:
                    return englishChar
        raise StopIteration


class EnglishTranslator:
    """
    Iterator that emits the translated Braille character for every parsed English character
    """
    def __init__(self, english: str):
        self.english = english
        self.idx = -1
        self.num = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.english) - 1:
            self.idx += 1

            englishChar = self.english[self.idx]

            if englishChar == " ":
                self.num = False
                return ENG_TO_BRAILLE[' ']
            elif englishChar.isnumeric():
                output = ""
                if not self.num:
                    output = ENG_TO_BRAILLE['NUM']
                    self.num = True
                return output + NUM_TO_BRAILLE[englishChar]
            else:
                output = ""
                if englishChar.isupper():
                    output = ENG_TO_BRAILLE["CAP"]
                return output + ENG_TO_BRAILLE[englishChar.lower()]
        
        raise StopIteration

if __name__ == "__main__":
    args = sys.argv[1:] # 0 index is the program name

    if isBraille(args):
        braille = args[0]
        engTranslation = "".join(ch for ch in BrailleTranslator(braille))
        print(engTranslation)
    else:
        english = " ".join(args)
        brailleTranslation = "".join(ch for ch in EnglishTranslator(english))
        print(brailleTranslation)
