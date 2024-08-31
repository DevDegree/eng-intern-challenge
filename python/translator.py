import sys

class BrailleConversion:
    '''
    This module provides a BrailleConversion class that allows conversion from Braille to English and vice versa.

    It supports translation of the english alphabet, numbers from 0 - 9, and certain special characters such as 
    commas, periods, exclamation marks, question marks, hyphens, colons, and more.
    '''
    def __init__(self):
        '''
        Initializes the Braille Conversion class with dictionaries 
        that map values from English to Braille and vice versa.
        '''

        self.englishConversion = {
            #Letter Mappings
            'a': 'O.....',
            'b': 'O.O...',
            'c': 'OO....',
            'd': 'OO.O..',
            'e': 'O..O..',
            'f': 'OOO...',
            'g': 'OOOO..',
            'h': 'O.OO..',
            'i': '.OO...',
            'j': '.OOO..',
            'k': 'O...O.',
            'l': 'O.O.O.',
            'm': 'OO..O.',
            'n': 'OO.OO.',
            'o': 'O..OO.',
            'p': 'OOO.O.',
            'q': 'OOOOO.',
            'r': 'O.OOO.',
            's': '.OO.O.',
            't': '.OOOO.',
            'u': 'O...OO',
            'v': 'O.O.OO',
            'w': '.OOO.O',
            'x': 'OO..OO',
            'y': 'OO.OOO',
            'z': 'O..OOO',

            #Space mapping
            ' ': '......'
        }

        self.englishNumConversion = {
            #Number mapping
            '1': 'O.....',
            '2': 'O.O...',
            '3': 'OO....',
            '4': 'OO.O..',
            '5': 'O..O..',
            '6': 'OOO...',
            '7': 'OOOO..',
            '8': 'O.OO..',
            '9': '.OO...',
            '0': '.OOO..',

            #Special character mapping
            '.': '..OO.O',
            ',': '..O...',
            '!': '..OOO.',
            '?': '..O.OO',
            ':': '..OO..',
            ';': '..O.O.',
            '-': '....OO',
            '/': '.O..O.',
            '<': '.OO..O',
            '>': 'O..OO.',
            '(': 'O.O..O',
            ')': '.O.OO.',

        }

        self.brailleConversion = {
            #Letter mapping
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

            #Space mapping
            '......':' '
        }

        self.brailleNumConversion = {
            #Number mapping
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

            #Special character mapping
            '..OO.O': '.',
            '..O...': ',',
            '..OOO.': '!',
            '..O.OO': '?',
            '..OO..': ':',
            '..O.O.': ';',
            '....OO': '-',
            '.O..O.': '/',
            '.OO..O': '<',
            'O..OO.': '>',
            'O.O..O': '(',
            '.O.OO.': ')'
        }
        
    def brailleToEnglish(self, input):
        '''
        Converts a Braille string to English text.

        Parameters:
        input (str) - a string of braille characters in the expected (O and .) format.
        
        Returns:
        text (str) - the translated text in English.
        '''
        numChar = len(input)/6 #Represents the number of Braille characters (must be divisible by 6)
        text = ""
        upper, number = False, False #Booleans for Upper case and numbers respectively
        comparison = False #Since O and > share the same Braille character, the comparison bool makes sure that if there was previously a < sign, > is opted for. 

        for i in range(int(numChar)):
            brailleChar = input[i*6:((i+1)*6)] #Represents the characters being translated

            if brailleChar=='.....O': #Checks if next character is captalized
                upper = True
            elif brailleChar=='.O...O': #Checks if there is a decimal place
                text+="."
            elif brailleChar=='.O.OOO': #Checks if there is a number that follows, and sets number boolean to true if yes
                number = True
            elif brailleChar=="......": #Checks if character is a space
                text += " "
                number=False
            elif number and (brailleChar in self.brailleNumConversion): #
                englishChar = self.brailleNumConversion[brailleChar]
                text+=englishChar
            elif brailleChar in self.brailleConversion and not comparison:
                englishChar = self.brailleConversion[brailleChar]
                if upper:
                    englishChar = englishChar.upper()
                    upper = False
                text+=englishChar
            else:
                if brailleChar=='.OO..O': #Sets comparison gate to make sure any following > will be recognized
                    comparison = True
                elif brailleChar=='O..OO.': #Turns off comparison gate after > is indentified
                    comparison = False
                englishChar = self.brailleNumConversion[brailleChar]
                text+=englishChar

        return text

    
    def englishToBraille(self, input):
        '''
        Converts English text to Braille.
        
        Parameters:
        input (str): The English text that is translated to Braille.

        Returns: 
        braille (str): The translated Braille String
        '''
        braille = ""
        number = False

        for char in input:
            if char==' ': #Checks for space
                braille+='......'
                number=False
            elif char.isupper(): #checks if letter is upper case
                braille+='.....O'
                braille+=self.englishConversion[char.lower()]
            elif char.isnumeric(): #checks if character is number
                if not number:
                    braille+='.O.OOO'
                    number = True
                braille+=self.englishNumConversion[char]
            else: #checks if there is a space 
                if number:
                    braille+='......'
                    number = False
                if char in self.englishConversion:
                    braille += self.englishConversion[char]
                elif char in self.englishNumConversion:
                    braille += self.englishNumConversion[char]

        return braille
        
    def isBraille(self, input):
        '''
        Determines if the input is written in Braille or English text.

        Parameters:
        input (str) - the input string

        Returns:
        Boolean - If input is in Braille, True is returned. If not, False.
        '''
        brailleSet = {'.', 'O'}
        for char in input: 
            if char not in brailleSet: #Checks if each character is a braille character or not
                return False
        return True
        
    def main(self):
        '''
        Main function that handles verifying whether the input is in Braille or English.
        After which, it runs the translation function.
        '''
        if len(sys.argv) < 2: #Checks for input in command
            print("Provide Valid Input.")
            return None

        inp = " ".join(sys.argv[1:])

        braille = self.isBraille(inp) #Checks if input is braille or english

        if braille:
            print(self.brailleToEnglish(inp)) #prints english text
        else:
            print(self.englishToBraille(inp)) #prints braille text

if __name__ == '__main__':
    bc = BrailleConversion()
    bc.main()
    
