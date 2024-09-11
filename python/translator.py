# Richard Bai, r25bai@uwaterloo.ca

import sys

class Translator:

    # Mapping BRAILLE to ENGLISH
    BRAILLE_TO_ENGLISH = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' '
    }

    # Mapping ENGLISH to BRAILLE (reverse of BRAILLE_TO_ENGLISH)
    ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

    # Mapping of numbers to their corresponding letter representation in BRAILLE
    LETTER_TO_NUMBER = {
        'j': '0', 'a': '1', 'b': '2', 'c': '3', 'd': '4',
        'e': '5','f': '6', 'g': '7', 'h': '8', 'i': '9'
    }

    def isBraille(self, inputStr):
        '''
        Function to check if the input string is in BRAILLE
        '''

        # If BRAILLE, the length should be multiple of 6 and only contain 0 or .
        return (len(inputStr) % 6 == 0 and all(char in 'O.' for char in inputStr))
    
    def translateEnglishToBraille(self, inputStr):
        '''
        Function to translate from ENGLISH to BRAILLE
        '''
        translatedStr = ''
        is_number_mode = False

        for char in inputStr:
            # If the character is a letter
            if char.isalpha():
                if is_number_mode: # If in number mode, add space and reset flag
                    translatedStr += self.ENGLISH_TO_BRAILLE[' ']
                    is_number_mode = False
                if char.isupper(): # If uppercase, add capital symbol
                    translatedStr += self.ENGLISH_TO_BRAILLE['capital']
                translatedStr += self.ENGLISH_TO_BRAILLE[char.lower()] # Add the lowercase letter
            elif char.isdigit():
                if not is_number_mode:
                    translatedStr += self.ENGLISH_TO_BRAILLE['number']
                    is_number_mode = True
                # Use the new NUMBERS_TO_BRAILLE mapping
                letter = list(self.LETTER_TO_NUMBER.keys())[list(self.LETTER_TO_NUMBER.values()).index(char)]
                translatedStr += self.ENGLISH_TO_BRAILLE[letter]
            elif char == ' ':
                translatedStr += self.ENGLISH_TO_BRAILLE[' ']
                is_number_mode = False

        return translatedStr

    def translateBrailleToEnglish(self, inputStr):
        '''
        Function to translate from BRAILLE to ENGLISH
        '''

        # Split the input string into 6-character chunks
        braille_chars = [inputStr[i:i+6] for i in range(0, len(inputStr), 6)]
        
        # Initialize result and flags
        translatedStr = ''
        is_capital = False
        is_number = False
        
        for braille_char in braille_chars:
            if braille_char == self.ENGLISH_TO_BRAILLE['capital']:
                is_capital = True
            elif braille_char == self.ENGLISH_TO_BRAILLE['number']:
                is_number = True
            elif braille_char in self.BRAILLE_TO_ENGLISH: 
                # Get English character from the BRAILLE_TO_ENGLISH map
                letter = self.BRAILLE_TO_ENGLISH[braille_char]
                if letter == ' ': # If space, add to result and reset number flag
                    translatedStr += ' '
                    is_number = False
                elif is_number: # Convert from letter to number with LETTER_TO_NUMBER_MAP
                    translatedStr += self.LETTER_TO_NUMBER[letter]
                elif is_capital: # Convert letter to uppercase and reset flag
                    translatedStr += letter.upper()
                    is_capital = False
                else: # Else, just add letter normally
                    translatedStr += letter

        return translatedStr

    def translate(self, inputStr):
        '''
        Main translation function that determines the input type and calls the appropriate translation method
        '''
        if self.isBraille(inputStr):
            return self.translateBrailleToEnglish(inputStr)
        else:
            return self.translateEnglishToBraille(inputStr)

if __name__ == "__main__":
    inputStr = ' '.join(sys.argv[1:])
    translator = Translator()
    print(translator.translate(inputStr))
