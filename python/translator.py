import sys

class BrailleTranslator:
    brailleToEn = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '......': ' '
    }
    enToBraille = {}
    for key, value in brailleToEn.items():
        enToBraille[value] = key

    numSymbol = ".O.OOO"
    capSymbol = ".....O"

    def __init__(self, inpStr):
        self.input = inpStr

    def brailleToEng(self):
        result = ""
        capsNext = False
        numMode = False
        chars = [self.input[i:i+6] for i in range(0, len(self.input), 6)]

        for char in chars:
            print(f"Processing Braille: '{char}'")  

            if char == self.capSymbol:
                capsNext = True
                print(f"Found capitalization symbol")  
            elif char == self.numSymbol:
                numMode = True
                print(f"Found number symbol, switching to number mode")  
            else:
                letter = self.brailleToEn.get(char, ' ')
                if numMode:
                    if letter in 'abcdefghi':
                        letter = str('123456789'.index(letter) + 1)
                    elif letter == 'j':
                        letter = '0'
                    numMode = False
                    print(f"Translated Braille to digit: '{letter}'")  
                elif capsNext:
                    letter = letter.upper()
                    capsNext = False
                    print(f"Translated Braille to uppercase letter: '{letter}'")  
                else:
                    print(f"Translated Braille to letter: '{letter}'")  
                result += letter
                print(f"Result so far: '{result}'\n")  

        return result

    
    def engToBraille(self):
        result = ""
        numMode = False  
        for char in self.input:
            if char == ' ':
                result += self.enToBraille[' ']
                numMode = False 
            elif char.isupper():
                result += self.capSymbol
                char = char.lower()
                numMode = False 
            elif char.isdigit():
                if not numMode:
                    result += self.numSymbol
                    numMode = True
                if char == '0':
                    char = 'j'
                else:
                    char = "abcdefghi"[int(char) - 1]
            else:
                numMode = False  
            braille_char = self.enToBraille.get(char, self.enToBraille[' '])
            
            if not (char == ' ' and result.endswith('......')):
                result += braille_char
                
        return result
    


    def translate(self):
        if all(c in {'O', '.'} for c in self.input): 
            return self.brailleToEng()
        else:
            return self.engToBraille()
    
if __name__ == "__main__": 
    if len(sys.argv) < 2:
        print("Please give string to translate")
    else:
        inpStr = " ".join(sys.argv[1:])
        translator = BrailleTranslator(inpStr)
        print(translator.translate())
