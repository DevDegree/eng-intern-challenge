import sys

class BrailleTranslator:
    def __init__(self):
        self.brailleAlphabet = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
            'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
            'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
            'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
            'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'number': '.O.OOO',
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
            '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
        }
        self.englishAlphabet = {v: k for k, v in self.brailleAlphabet.items()}

    def isBraille(self, input_str):
        return set(input_str).issubset({'O', '.'})

    def translateToBraille(self, englishStr):
        result = []
        numberMode = False

        for char in englishStr:
            if char.isdigit():
                if not numberMode:
                    result.append(self.brailleAlphabet['number'])
                    numberMode = True
                result.append(self.brailleAlphabet[char])
            elif char.isalpha():
                if char.isupper():
                    result.append(self.brailleAlphabet['capital'])
                    char = char.lower()
                result.append(self.brailleAlphabet[char])
                numberMode = False
            elif char == ' ':
                result.append(self.brailleAlphabet[' '])
                numberMode = False
        
        return ''.join(result)


    def translateToEnglish(self, brailleStr):
        result = []
        numberMode = False
        i = 0

        while i < len(brailleStr):
            brailleChar = brailleStr[i:i+6]
            
            if brailleChar == self.brailleAlphabet['number']:
                numberMode = True
            elif brailleChar == self.brailleAlphabet['capital']:
                nextBrailleChar = brailleStr[i+6:i+12]
                result.append(self.englishAlphabet[nextBrailleChar].upper())
                i += 6
            elif brailleChar == self.brailleAlphabet[' ']:
                result.append(' ')
                numberMode = False
            else:
                if numberMode and brailleChar in self.englishAlphabet:
                    result.append(self.englishAlphabet[brailleChar])
                else:
                    result.append(self.englishAlphabet[brailleChar])
                numberMode = False
            i += 6

        return ''.join(result)


    def translate(self, inputStr):
        if self.isBraille(inputStr):
            return self.translateToEnglish(inputStr)
        else:
            return self.translateToBraille(inputStr)


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <inputString>")
        return

    inputStr = ' '.join(sys.argv[1:])
    translator = BrailleTranslator()
    result = translator.translate(inputStr)
    print(result)

if __name__ == "__main__":
    main()
