import sys

dicAlphabetToBraille = {
    'a':'O.....',
    'b':'O.O...',
    'c':'OO....',
    'd':'OO.O..',
    'e':'O..O..',
    'f':'OOO...',
    'g':'OOOO..',
    'h':'O.OO..',
    'i':'.OO...',
    'j':'.OOO..',
    'k':'O...O.',
    'l':'O.O.O.',
    'm':'OO..O.',
    'n':'OO.OO.',
    'o':'O..OO.',
    'p':'OOO.O.',
    'q':'OOOOO.',
    'r':'O.OOO.',
    's':'.OO.O.',
    't':'.OOOO.',
    'u':'O...OO',
    'v':'O.O.OO',
    'w':'.OOO.O',
    'x':'OO..OO',
    'y':'OO.OOO',
    'z':'O..OOO',
    'cf':'.....O',
    ' ':'......',
}

dicNumberToBraille = {
    '1':'O.....',
    '2':'O.O...',
    '3':'OO....',
    '4':'OO.O..',
    '5':'O..O..',
    '6':'OOO...',
    '7':'OOOO..',
    '8':'O.OO..',
    '9':'.OO...',
    '0':'.OOO..',
    'nf':'.O.OOO',
    ' ':'......',
}

dicBrailleToAlphabet = dict(zip(dicAlphabetToBraille.values(), dicAlphabetToBraille.keys()))
dicBrailleToNumber = dict(zip(dicNumberToBraille.values(), dicNumberToBraille.keys()))

class transDiver:
    def __init__(self, arg):
        joinedList = "".join(arg)
        if all( l in 'O.' for l in joinedList):
            self.ciperText = joinedList
            self.isAlphabet = False
        else:
            self.ciperText = arg
            self.isAlphabet = True

    def translate(self):
        decodedText = ""
        if self.isAlphabet:
            for word in self.ciperText:
                if word.isdigit():          # number
                    decodedText += dicNumberToBraille.get('nf')
                    for c in list(word):
                        decodedText += dicNumberToBraille.get(c)

                else:                      # alphabet
                    for c in list(word):
                        if c.isupper():
                            decodedText += dicAlphabetToBraille.get('cf')
                            c = c.lower()
                        decodedText += dicAlphabetToBraille.get(c)
                
                decodedText += dicAlphabetToBraille.get(' ')
            
            decodedText = decodedText[:-6]

        else:
            if len(self.ciperText) % 6:
                return "Wrong Braille"
            brailleTexts = [self.ciperText[i:i+6] for i in range(0, len(self.ciperText), 6)]
            numberFollows, spaceFollows, capitalFollows = '.O.OOO', '......', '.....O'
            nfRun, cfRun = False, False

            for i in range(len(brailleTexts)):
                if brailleTexts[i] == spaceFollows:
                    nfRun = False
                    decodedText += dicBrailleToNumber.get(brailleTexts[i]) if i != len(brailleTexts) - 1 else ""
                elif  nfRun or brailleTexts[i] == numberFollows:
                    nfRun = True
                    decodedText += dicBrailleToNumber.get(brailleTexts[i]) if brailleTexts[i] != numberFollows else ""
                elif cfRun:
                    cfRun = False
                    decodedText += dicBrailleToAlphabet.get(brailleTexts[i]).upper()
                else:
                    if brailleTexts[i] == capitalFollows:
                        cfRun = True
                    else:
                        decodedText += dicBrailleToAlphabet.get(brailleTexts[i])

        return decodedText


if __name__ == '__main__':
    argList = sys.argv[1:]
    driver = transDiver(argList)
    print(driver.translate())