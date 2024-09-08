
# Libraries
import sys

class BrailleTranslator:
    
    # Constructor
    def __init__(self):
        # Lists
        stringList = [
        'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..',
        'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..', 
        'O...O.', 'O.O.O.', 'OO..O.', 'OO.OO.', 'O..OO.', 
        'OOO.O.', 'OOOOO.', 'O.OOO.', '.OO.O.', '.OOOO.', 
        'O...OO', 'O.O.OO', '.OOO.O', 'OO..OO', 'OO.OOO', 
        'O..OOO', '......', '.....O', '.O.OOO'
        ]
        charList = [
            'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y',
            'z', ' ', 0, 1
        ]
        digitList = [
            '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0',
        ]
        
        # Dictionaries
        self.stringToCharDict = {}
        self.charToStringDict = {}
        self.charToDigitDict = {}
        self.digitToCharDict = {}
        for i in range(len(stringList)):
            self.stringToCharDict[stringList[i]] = charList[i]
            self.charToStringDict[charList[i]] = stringList[i]     
        for i in range(len(digitList)):
            self.charToDigitDict[charList[i]] = digitList[i]
            self.digitToCharDict[digitList[i]] = charList[i]
    
    
    # Translate
    def translate(self, text):
        size = len(text)
        
        # Check size
        if size % 6 != 0:
            return self.convertEnglishToBraille(text, size)
    
        # Check characters
        for ch in text:
            # Contains dot symbol
            if ch == '.':
                return self.convertBrailleToEnglish(text, size)
            # Contains non O symbols
            elif ch != 'O':
                return self.convertEnglishToBraille(text, size)
        
        # Only contains O symbols
        return self.convertEnglishToBraille(text, size)
    
    
    # Convert from Braille to English
    def convertBrailleToEnglish(self, text, size):
        output = ''
        isCapital = False
        isNumber = False
        
        for i in range(0, size, 6):      
            ch = self.stringToCharDict[text[i:i+6]]
            
            # Is space
            if ch == ' ':
                isNumber = False
                output += ' '
            # Is capital        
            elif ch == 0:
                isCapital = True
            # Is number
            elif ch == 1:
                isNumber = True
            # Others
            else:
                # Uppercase letter
                if isCapital:
                    isCapital = False
                    output += ch.upper()
                # Digit
                elif isNumber:
                    output += self.charToDigitDict[ch]
                # Lowercase letter
                else:
                    output += ch
        
        return output
    
    
    # Convert from English to Braille
    def convertEnglishToBraille(self, text, size):
        output = ''
        isNumber = False
        
        for i in range(size):
            ch = text[i]
            
            # Is space
            if ch == ' ':
                isNumber = False
                output += self.charToStringDict[ch]
            # Is uppercase letter
            elif ch.isupper():
                output += self.charToStringDict[0] + self.charToStringDict[ch.lower()]
            # Is digit
            elif ch.isdigit():
                # First digit
                if not isNumber:
                    isNumber = True
                    output += self.charToStringDict[1]
                
                output += self.charToStringDict[self.digitToCharDict[ch]]
            # Is lowercase letter
            else:
                output += self.charToStringDict[ch]
        
        return output


# Executation
if __name__ == '__main__':
    size = len(sys.argv)
    
    if size > 1:
        text = ' '.join(sys.argv[1:])
        output = BrailleTranslator().translate(text)
        print(output)
        