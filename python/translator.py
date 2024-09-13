import sys

"""
    For the purposes of this challenge Braille must be displayed as O and . where O represents a raised dot. 
    You must include the entire English alphabet, the ability to capitalize letters, add spaces, and the numbers 0 through 9 as well.
    ==> Hence, no need to handle special characters like '.', '?', '>', '<', etc and no need to handle numbers with decimal points.

    Accepted characters in the input English text for this challenge:
    - English alphabets [a-z] or [A-Z]
    - Numbers [0-9]
    - Space ' '
"""

class BrailleTranslator:
    def __init__(self):    
        # mapping of braille to english letters
        self.brailleToEnglishLetter = {
            'O.....': 'a',
            'O.O...': 'b',
            'OO....': 'c',
            'OO.O..': 'd',
            'O..O..': 'e',
            'OOO...': 'f',
            'OOOO..': 'g',
            'O.OO..': 'h',
            '.OO...': 'i',
            '.OOO..': 'j',
            'O...O.': 'k',
            'O.O.O.': 'l',
            'OO..O.': 'm',
            'OO.OO.': 'n',
            'O..OO.': 'o',
            'OOO.O.': 'p',
            'OOOOO.': 'q',
            'O.OOO.': 'r',
            '.OO.O.': 's',
            '.OOOO.': 't',
            'O...OO': 'u',
            'O.O.OO': 'v',
            '.OOO.O': 'w',
            'OO..OO': 'x',
            'OO.OOO': 'y',
            'O..OOO': 'z',
        }

        # mapping of english letters to braille
        self.englishLetterToBraille = {char: brailleRep for brailleRep, char in self.brailleToEnglishLetter.items()}

        # mapping of braille to numbers
        self.brailleToNumber = {
            'O.....': '1',
            'O.O...': '2',
            'OO....': '3',
            'OO.O..': '4',
            'O..O..': '5',
            'OOO...': '6',
            'OOOO..': '7',
            'O.OO..': '8',
            '.OO...': '9',
            '.OOO..': '0',
        }
        
        # mapping of numbers to braille
        self.numberToBraille = {num: brailleRep for brailleRep, num in self.brailleToNumber.items()}

        # special cases
        self.CAPITAL = '.....O'
        self.NUMBER = '.O.OOO'
        self.SPACE = '......'


    def isBraille(self, text):
        """
            Check if the input text is in braille format or not.

            Parameters: 
                text (str): input text to check

            Returns:
                bool: True if the input text is in braille format, False otherwise.
        """

        if len(text) % 6 != 0:
            # braille text length should be multiple of 6
            return False
        
        # Assumption: OOOOOO (and similar) can be considered an English word since it does not exist in the braille alphabet
        for i in range(0, len(text), 6):
            if (text[i:i+6] not in self.brailleToEnglishLetter and 
                text[i:i+6] not in self.brailleToNumber and 
                text[i:i+6] != self.CAPITAL and text[i:i+6] != self.NUMBER and text[i:i+6] != self.SPACE):
                return False
        
        return True
    
    
    def translate(self, text):
        """
            Translate the input text to either braille or english based on the input.

            Parameters:
                text (str): input text to translate

            Returns:
                str: translated text
        """

        if self.isBraille(text):
            return self.translateToEnglish(text)
        else:
            return self.translateToBraille(text)
        
    
    def translateToEnglish(self, text):
        """
            Translate the braille text to english.

            Parameters:
                text (str): braille text to translate

            Returns:
                str: english text
        """

        englishText = []
        capital = False
        number = False

        for i in range(0, len(text), 6):
            braille = text[i:i+6]

            # check if it is any of the special cases
            if braille == self.CAPITAL:
                capital = True
                continue
            elif braille == self.NUMBER:
                number = True
                continue
            elif braille == self.SPACE:
                englishText.append(' ')
                # Assumption: when number = True, all following symbols are numbers until the next space symbol.
                number = False
                continue

            
            if not number:    # [a-z] or [A-Z]
                if braille in self.brailleToEnglishLetter:
                    if capital:
                        englishText.append(self.brailleToEnglishLetter[braille].upper())
                        capital = False
                    else:
                        englishText.append(self.brailleToEnglishLetter[braille])
                else:
                    # raise exception if the braille character is not found in the English letters mapping
                    raise ValueError("Invalid braille character: " + braille)
                    
            
            else:   # [0-9]
                if braille in self.brailleToNumber:
                    englishText.append(self.brailleToNumber[braille])
                else:
                    # raise exception if the braille character is not found in the numbers mapping
                    raise ValueError("Invalid braille character: " + braille)

        return ''.join(englishText)
    

    def translateToBraille(self, text):
        """
            Translate the english text to braille.

            Parameters:
                text (str): english text to translate

            Returns:
                str: braille text
        """

        brailleText = []
        digitSequenceStarted = False

        for char in text:
            if char.isalpha():  # [a-z] or [A-Z]
                if char.isupper():
                    brailleText.append(self.CAPITAL)

                brailleText.append(self.englishLetterToBraille[char.lower()])

            elif char.isdigit():    # [0-9]
                if not digitSequenceStarted:
                    brailleText.append(self.NUMBER)
                    digitSequenceStarted = True

                brailleText.append(self.numberToBraille[char])

            elif char.isspace():    # space
                brailleText.append(self.SPACE)
                digitSequenceStarted  = False

            else:
                # raise exception as character is not in the scope of the challenge
                raise ValueError("Invalid English character: " + char)
                
        return ''.join(brailleText)
    

if __name__ == '__main__':
    
    if len(sys.argv) >= 2:
        inputText = ' '.join(sys.argv[1:])
        translator = BrailleTranslator()
        print(translator.translate(inputText))

    else:
        sys.exit(1)