
import sys
from typing import List
import dataclasses

@dataclasses.dataclass
class Braille:
    a: str = "O....."
    b: str = "O.O..."
    c: str = "OO...."
    d: str = "OO.O.."
    e: str = "O..O.."
    f: str = "OOO..."
    g: str = "OOOO.."
    h: str = "O.OO.."
    i: str = ".OO..."
    j: str = ".OOO.."
    k: str = "O...O."
    l: str = "O.O.O."
    m: str = "OO..O."
    n: str = "OO.OO."
    o: str = "O..OO."
    p: str = "OOO.O."
    q: str = "OOOOO."
    r: str = "O.OOO."
    s: str = ".OO.O."
    t: str = ".OOOO."
    u: str = "O..OO"
    v: str = "O.O.OO"
    w: str = ".OOO.O"
    x: str = "OO..OO"
    y: str = "OO.OOO"
    z: str = "O..OOO"
    one: str = "O....."
    two: str = "O.O..."
    three: str = "OO...."
    four: str = "OO.O.."
    five: str = "O..O.."
    six: str = "OOO..."
    seven: str = "OOOO.."
    eight: str = "O.OO.."
    nine: str = ".OO..."
    zero: str = ".OOO.."
    capitalFollows: str = ".....O"
    decimalFollows: str = ".O...O"
    numberFollows: str = ".O.OOO"
    period: str = "..OO.O"
    comma: str = "..O..."
    quesionMark: str = "..O.OO"
    bang: str = "..OOO."
    colon: str = "..OO.."
    semicolon: str = "..O.O."
    dash: str = "....OO"
    slash: str = ".O..O."
    lt: str = ".OO..O"
    gt: str = "O..OO."
    openParen: str = "O.O..O"
    closeParen: str = ".O.OO."
    space: str = "......"

    def getBrailleToAlpha(self) -> dict:
        dict_brailleToAlpha = {}

        # add single letters
        for field in dataclasses.fields(Braille):
            if len(field.name) == 1:
                dict_brailleToAlpha[field.default] = field.name

        return dict_brailleToAlpha
    
    def getBrailleToNumPunc(self) -> dict:
        dict_brailleToAlpha = {}

        dict_brailleToAlpha[self.one] = "1"
        dict_brailleToAlpha[self.two] = "2"
        dict_brailleToAlpha[self.three] = "3"
        dict_brailleToAlpha[self.four] = "4"
        dict_brailleToAlpha[self.five] = "5"
        dict_brailleToAlpha[self.six] = "6"
        dict_brailleToAlpha[self.seven] = "7"
        dict_brailleToAlpha[self.eight] = "8"
        dict_brailleToAlpha[self.nine] = "9"
        dict_brailleToAlpha[self.zero] = "0"

        dict_brailleToAlpha[self.capitalFollows] = ""
        dict_brailleToAlpha[self.numberFollows] = ""
        dict_brailleToAlpha[self.period] = "."
        dict_brailleToAlpha[self.comma] = ","
        dict_brailleToAlpha[self.quesionMark] = "?"
        dict_brailleToAlpha[self.bang] = "!"
        dict_brailleToAlpha[self.colon] = ":"
        dict_brailleToAlpha[self.semicolon] = ";"
        dict_brailleToAlpha[self.dash] = "-"
        dict_brailleToAlpha[self.slash] = "/"
        dict_brailleToAlpha[self.lt] = "<"
        dict_brailleToAlpha[self.gt] = ">"
        dict_brailleToAlpha[self.openParen] = "("
        dict_brailleToAlpha[self.closeParen] = ")"
        dict_brailleToAlpha[self.space] = " "
        
        return dict_brailleToAlpha
        
    def getAlphaToBraille(self) -> dict:
        dict_alphaToBraille = {}

        # add single letters
        for field in dataclasses.fields(Braille):
            if len(field.name) == 1:
                dict_alphaToBraille[field.name] = field.default

        # add numbers and punctuation
        dict_alphaToBraille["1"] = self.one
        dict_alphaToBraille["2"] = self.two
        dict_alphaToBraille["3"] = self.three
        dict_alphaToBraille["4"] = self.four
        dict_alphaToBraille["5"] = self.five
        dict_alphaToBraille["6"] = self.six
        dict_alphaToBraille["7"] = self.seven
        dict_alphaToBraille["8"] = self.eight
        dict_alphaToBraille["9"] = self.nine
        dict_alphaToBraille["0"] = self.zero
        dict_alphaToBraille["."] = self.period
        dict_alphaToBraille[","] = self.comma
        dict_alphaToBraille["?"] = self.quesionMark
        dict_alphaToBraille["!"] = self.bang
        dict_alphaToBraille[":"] = self.colon
        dict_alphaToBraille[";"] = self.semicolon
        dict_alphaToBraille["-"] = self.dash
        dict_alphaToBraille["/"] = self.slash
        dict_alphaToBraille["<"] = self.lt
        dict_alphaToBraille[">"] = self.gt
        dict_alphaToBraille["("] = self.openParen
        dict_alphaToBraille[")"] = self.closeParen
        dict_alphaToBraille[" "] = self.space

        return dict_alphaToBraille

class Translator:
    braille = Braille()
    dict_alphaToBraille = braille.getAlphaToBraille()
    dict_brailleToAlpha = braille.getBrailleToAlpha()
    dict_brailleToNumPunc = braille.getBrailleToNumPunc()

    def __init__(self) -> None:
        return

    def translate(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""
        
        original = " ".join(words)

        # check if the first six characters are valid braille strings
        if len(original) >= 6 and original[0:6] in self.dict_brailleToAlpha or original[0:6] in self.dict_brailleToNumPunc:
            return self.brailleToAlpha(original)
        # check if the first character is alphabetical
        elif original.lower()[0] in self.dict_alphaToBraille:
            return self.alphaToBraille(original)
        
        return ""

    def brailleToAlpha(self, word: str) -> str:
        if len(word) % 6 != 0:
            return ""
        
        translation = ""
        isCap = False
        isNum = False

        for i in range(0, len(word), 6):
            brailleString = word[i: i + 6]

            if brailleString == self.braille.capitalFollows:
                isCap = True
            elif brailleString == self.braille.numberFollows:
                isNum = True
            elif isCap:
                translation += self.dict_brailleToAlpha[brailleString].upper()
                isCap = False
            elif isNum:
                if brailleString == self.braille.space:
                    isNum = False
                else:
                    translation += self.dict_brailleToNumPunc[brailleString]
            else:
                if brailleString in self.dict_brailleToAlpha:
                    translation += self.dict_brailleToAlpha[brailleString]
                elif brailleString in self.dict_brailleToNumPunc:
                    translation += self.dict_brailleToNumPunc[brailleString]
        
        return translation

    def alphaToBraille(self, word: str) -> str:
        translation = ""
        isNum = False

        for char in word:
            if char.isdigit():
                if not isNum:
                    translation += self.braille.numberFollows
                    isNum = True
                translation += self.dict_alphaToBraille[char]
            else:
                # assume that the input string will contain a space to separate numbers and letters
                if isNum:
                    isNum = False
                    
                if char.isupper():
                    translation += self.braille.capitalFollows
                    translation += self.dict_alphaToBraille[char.lower()]
                else:
                    translation += self.dict_alphaToBraille[char]

        return translation

def main():
    # get the words to be translated
    words = sys.argv[1:]
    translator = Translator()
    translation = translator.translate(words)
    print(translation)

if __name__ == "__main__":
    main()
