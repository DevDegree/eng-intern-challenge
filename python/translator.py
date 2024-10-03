# Darsh Shah, darsh.shah@uwaterloo.ca

import sys

class T:
    B2E = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' '
    }

    E2B = {v: k for k, v in B2E.items()}

    L2N = {
        'j': '0', 'a': '1', 'b': '2', 'c': '3', 'd': '4',
        'e': '5','f': '6', 'g': '7', 'h': '8', 'i': '9'
    }

    def translate(self, inputStr):
        if self.isBraille(inputStr):
            return self.BrailleToEnglish(inputStr)
        else:
            return self.EnglishToBraille(inputStr)

    def isBraille(self, inputStr):
        return (len(inputStr) % 6 == 0 and all(c in 'O.' for c in inputStr))

    def BrailleToEnglish(self, inputStr):
        chars = [inputStr[i:i+6] for i in range(0, len(inputStr), 6)]
        result = ""

        capitalize_flag = False
        number_flag = False

        for c in chars:
            if c == '.....O':
                capitalize_flag = True
            elif c in self.B2E: 
                letter = self.B2E[c]
                if letter == ' ': 
                    result += ' '
                    number_flag = False
                elif capitalize_flag:
                    result += letter.upper()
                    capitalize_flag = False
                elif number_flag:
                    result += self.L2N[letter]
                else: 
                    result += letter
            elif c == '.O.OOO': 
                number_flag = True

        return result

    def EnglishToBraille(self, inputStr):
        result = ""

        number_flag = False

        for c in inputStr:
            if c.isupper(): 
                result += self.E2B['capital']
                c = c.lower()
              
            if c.isalpha():
                if number_flag: 
                    result += self.E2B[' ']
                    number_flag = False

                result += self.E2B[c]

            elif c.isdigit(): 
                if not number_flag:
                    number_flag = True
                    result += self.E2B['number']
                
                letter = list(self.L2N.keys())[int(c)]
                result += self.E2B[letter]
            
            elif c == ' ': 
                result += self.E2B[' ']
                number_flag = False
        
        return result
    
if __name__ == "__main__":
    inputStr = ' '.join(sys.argv[1:])
    t = T()

    print(t.translate(inputStr), end='')
