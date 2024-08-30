# Owen Zhang, owen.z.0523@gmail.com

import sys

class Translator:
    # Map from BRAILLE to ENGLISH
    BRAILLE_TO_ENGLISH = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' '
    }

    # Map from ENGLISH to BRAILLE
    ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

    # Map from BRAILLE numbers to letters
    LETTER_TO_NUMBER_MAP = {
        'j': '0', 'a': '1', 'b': '2', 'c': '3', 'd': '4',
        'e': '5','f': '6', 'g': '7', 'h': '8', 'i': '9'
    }

    def translate(self, inputStr):
        '''
        Main function to translate from BRAILLE to ENGLISH or ENGLISH to BRAILLE depending on the inputStr
        '''
        # If input is in Braille, translate to English, else translate English to Braille
        if self.isBraille(inputStr):
            return self.translateBrailleToEnglish(inputStr)
        else:
            return self.translateEnglishToBraille(inputStr)

    def isBraille(self, inputStr):
        '''
        Function to check if inputStr is in Braille
        '''
        # Length of the Braille input should be a multiple of 6 and only have the characters '0' and '.'
        return (len(inputStr) % 6 == 0 and all(c in 'O.' for c in inputStr))

    def translateBrailleToEnglish(self, inputStr):
        '''
        Function to translate Braille to English
        '''
        # Split the input into 6-character chunks
        chars = [inputStr[i:i+6] for i in range(0, len(inputStr), 6)]
        result = ""

        # Flags to check if next letter should be capitalized or a number
        capitalize_flag = False
        number_flag = False

        # Loop through each Braille character and translate to English
        for c in chars:
            if c == '.....O': # Capital symbol
                capitalize_flag = True
            elif c == '.O.OOO': # Number symbol
                number_flag = True
            elif c in self.BRAILLE_TO_ENGLISH: 
                # Get English character from the BRAILLE_TO_ENGLISH map
                letter = self.BRAILLE_TO_ENGLISH[c]
                if letter == ' ': # If space, add to result and reset number flag
                    result += ' '
                    number_flag = False
                elif number_flag: # If number flag is True, convert from letter to number with LETTER_TO_NUMBER_MAP
                    result += self.LETTER_TO_NUMBER_MAP[letter]
                elif capitalize_flag: # If capitalize flag is True, convert letter to uppercase and reset capitalize flag
                    result += letter.upper()
                    capitalize_flag = False
                else: # Else, just add letter normally
                    result += letter

        return result

    def translateEnglishToBraille(self, inputStr):
        '''
        Function to translate English to Braille
        '''
        result = ""

        # Flag to check if previous letter was a number
        number_flag = False

        # Loop through each English character and translate to Braille
        for c in inputStr:
            if c.isalpha(): # If character is a letter, if needed reset number flag and convert to lowercase, then convert to Braille
                if number_flag: # If previous character was a number, add space in Braille to end the number sequence
                    result += self.ENGLISH_TO_BRAILLE[' ']
                    number_flag = False
                
                if c.isupper(): # If letter is capitalized, add capital symbol in Braille
                    result += self.ENGLISH_TO_BRAILLE['capital']
                    c = c.lower()

                result += self.ENGLISH_TO_BRAILLE[c]

            elif c.isdigit(): # If character is a number, set number_flag and convert to Braille
                if not number_flag:
                    number_flag = True
                    result += self.ENGLISH_TO_BRAILLE['number']
                
                # Convert digit to corresponding letter
                letter = list(self.LETTER_TO_NUMBER_MAP.keys())[int(c)]
                result += self.ENGLISH_TO_BRAILLE[letter]
            
            elif c == ' ': # If character is a space, reset number flag and add space in Braille
                result += self.ENGLISH_TO_BRAILLE[' ']
                number_flag = False
        
        return result
    
if __name__ == "__main__":
    # Get input string from command line
    inputStr = ' '.join(sys.argv[1:])
    translator = Translator()

    # Translate input string
    print(translator.translate(inputStr), end='')