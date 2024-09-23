import sys

class Translator:
    def __init__(self):
        self.specials = {
            "CAPS" : ".....O",
            "NUMS" : ".O.OOO",
            "SPACE" : "......"
        }
    
    def brailleKey(self):
        self.symbolsBraille = {
            "O..." : "a",
            "O.O." : "b",
            "OO.." : "c",
            "OO.O" : "d",
            "O..O" : "e",
            "OOO." : "f",
            "OOOO" : "g",
            "O.OO" : "h",
            ".OO." : "i",
            ".OOO" : "j"
        }
    
    def englishKey(self):
        self.symbolsEnglish = {
            "a" : "O...",
            "b" : "O.O.",
            "c" : "OO..",
            "d" : "OO.O",
            "e" : "O..O",
            "f" : "OOO.",
            "g" : "OOOO",
            "h" : "O.OO",
            "i" : ".OO.",
            "j" : ".OOO" 
        }
    
    def translateToEnglish(self, input):
        output = ''
        i = 0
        CAPS = False
        CAPS_ASCII_DIFF = 0
        
        NUMS = False
        
        while i < len(input):
            symbol = input[i : (i + 6)] # get the six character for Braille Symbol
            common = symbol[:4]
            
            if (symbol == self.specials['SPACE']):
                output = output + " "
                NUMS = False
                i += 6
                continue
            
            if (symbol == self.specials['CAPS']):
                CAPS = True
                i += 6
                continue

            if (symbol == self.specials['NUMS']):
                NUMS = True
                i += 6
                continue
            
            if NUMS:
                number = ord(self.symbolsBraille[common]) - ord('a') + 1
                output = output + str((number) % 10)
                i += 6
                continue
            
            if CAPS:
                CAPS_ASCII_DIFF = 32
            else:
                CAPS_ASCII_DIFF = 0
            
            if (symbol[5] == 'O'):
                if(symbol[4] == 'O'):
                    output =  output + chr(ord(self.symbolsBraille[common]) + 20 - CAPS_ASCII_DIFF)
                else:
                    output =  output + chr(ord(self.symbolsBraille[common]) + 13 - CAPS_ASCII_DIFF) # w or W
            else:
                if (symbol[4] == 'O'):
                    output =  output + chr(ord(self.symbolsBraille[common]) + 10 - CAPS_ASCII_DIFF)
                else:
                    output =  output + chr(ord(self.symbolsBraille[common]) - CAPS_ASCII_DIFF)
            
            CAPS = False
            i += 6
        
        return output

def isBraille(input):
    '''
    Check if inputs is in Braille format
    - As all characters in braille symbols are 6 character strings long, then the length of the whole input must be a multiple of 6 
    - All braille symbols are made of either '.' or 'O' and of the regex form ^[\.O]{6}
    '''
    # Check if the input length is a multiple of 6
    if (len(input) % 6 != 0):
        return False

    # Check if all symbols are either '.' or '0'
    for i in input:
        if (i not in {'.', 'O'}):
            return False
    return True

def run():
    '''
    Check and convert into input that is valid for translation
    '''
    output = ''
    # Check if an argument or input is given for translation
    if (len(sys.argv) == 1):
        return
    
    # Add spaces for english words if required (braille input will have a single input)
    inputs =  ' '.join(sys.argv[1:])
    
    translator = Translator()

    if (isBraille(inputs)):
        translator.brailleKey()
        output = translator.translateToEnglish(inputs) # translate to English
    else:
        # EnglishTranslator(inputs) # translate to Braille
        pass
    
    print(output)

if __name__ == "__main__":
    run()