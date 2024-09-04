import sys
class BrailleTranslator:
    def __init__(self):
        self.brailleEnglish = {
            'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
            'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
            '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
            'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
            'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
            'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
            'OO.OOO': 'y', 'O..OOO': 'z',
            '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
            '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
            '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')',
            '......': ' '
        }
        self.numsToBraille = {
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
            '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
            '9': '.OO...', '0': '.OOO..'
        }
        self.englishToBraille = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
            'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
            'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
            'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
            'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
            'y': 'OO.OOO', 'z': 'O..OOO',
            '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
            ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
            '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
            ' ': '......'
        }
        self.brailleToNums = {
            'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
            'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
            '.OO...': '9', '.OOO..': '0'
        }
        self.charTypesToBraille = {
            'cap' : '.....O',
            'num' : '.O.OOO'
        }
        self.brailleToCharTypes = {
            '.....O' : 'cap',
            '.O.OOO' : 'num'
        }

    def isEnglish(self, input):
        uniqueChars = set(input)
        if len(uniqueChars) > 2:
            return True
        for char in uniqueChars:
            if char not in ['O', '.']:
                return True
        return False

    def translate(self, input):
        if self.isEnglish(input):
            return self.englishToBrailleTranslate(input)
        else:
            return self.brailleToEnglishTranslate(input)

    def brailleToEnglishTranslate(self, input):
        if len(input) % 6 != 0:
            return 'invalid'
        
        res = []
        isCap = False
        isNum = False

        l = 0
        r = 6

        while r <= len(input):
            char = input[l:r]
            if char in self.brailleToCharTypes:
                if self.brailleToCharTypes[char] == 'cap':
                    isCap = True
                else:
                    isNum = True
            elif isCap:
                res.append(chr(ord(self.brailleEnglish[char]) - 32))
                isCap = False
            elif isNum:
                if self.brailleEnglish[char] == ' ':
                    isNum = False
                else:
                    res.append(self.brailleToNums[char])
            else:
                res.append(self.brailleEnglish[char])

            l += 6
            r += 6

        return ''.join(res)

    def englishToBrailleTranslate(self, input):
        res = []
        isNum = False

        for char in input:
            if char.isdigit():
                if not isNum:
                    res.append(self.charTypesToBraille['num'])
                    isNum = True
                res.append(self.numsToBraille[char])
            else:
                isNum = False
                if char in self.englishToBraille:
                    res.append(self.englishToBraille[char])
                elif char.lower() in self.englishToBraille:
                    res.append(self.charTypesToBraille['cap'])
                    res.append(self.englishToBraille[char.lower()])

        return ''.join(res)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        inputString = ' '.join(sys.argv[1:])
        translator = BrailleTranslator()
        print(translator.translate(inputString))
    else:
        print("Invalid input.")
