import argparse, re

class translator:
    def __init__(self) -> None:

        parser = argparse.ArgumentParser(description='Translate a string into braille or braille to text.')

        parser.add_argument('BrailleOrText', nargs='+', type=str)

        givenArgument = parser.parse_args()

        combinedArgument = ' '.join(givenArgument.BrailleOrText)

        # alphabets to braille map
        self.alphaToBrailleMap = {
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
            'z': 'O..OOO'
        }
        # numbers to braille map
        self.numToBrailleMap = {
            '1': 'O.....',
            '2': 'O.O...',
            '3': 'OO....',
            '4': 'OO.O..',
            '5': 'O..O..',
            '6': 'OOO...',
            '7': 'OOOO..',
            '8': 'O.OO..',
            '9': '.OO...',
            '0': '.OOO..'
        }
        # symbol to braille map
        self.symbolToBrailleMap = {
            ',': '..O...',
            '?': '..O.OO',
            '!': '..OOO.',
            ':': '..OO..',
            ';': '..O.O.',
            '-': '....OO',
            '/': '.O..O.',
            '<': '.OO..O',
            '>': 'O..OO.',
            '(': 'O.O..O',
            ')': '.O.OO.'
        }

        # reverse the maps for braille to anything else
        self.brailleToAlphaMap = {value: key for key, value in self.alphaToBrailleMap.items()}
        self.brailleToNumMap = {value: key for key, value in self.numToBrailleMap.items()}
        self.brailleToSymbolMap = {value: key for key, value in self.symbolToBrailleMap.items()}

        # we will not use string comparisons but instead do hash maps for capital follows, decimal follows, and number follows because comparing strings is a O(n) operation
        self.capitalFollows = {'cap': '.....O', '.....O': '.....O'}
        self.numberFollows = {'num': '.O.OOO', '.O.OOO': '.O.OOO'}
        self.decimalFollows = {'.': '.', 'dec': '.O...O', '.O...O': '.O...O'}
        self.actualDecimal = '..OO.O'
        self.space = {' ': '......', '......': '......'}


        # set up regex
        pattern = r'^(?=.*[O.])[O.]{2,}$' # whole idea for this is to make sure we tree a single O or . as english and not braille because logically that doesn't make sense if we treat it as braille
        compiledPattern = re.compile(pattern)
        if re.match(compiledPattern, combinedArgument):
            print(self.handle_Braille(combinedArgument))
        else:
            print(self.handle_English(combinedArgument))


    def handle_Braille(self, braille) -> str:
        """
        Function description:
        This function takes a string of braille characters and converts it to the corresponding text. It processes the braille string in chunks of 6 characters, handling special markers for capital letters, numbers, and decimals.

        Input:
        - braille (str): A string of braille characters to be converted to text.

        Output:
        - str: The text representation of the input braille string.
        """

        returnString = ''

        isCapital = False
        isNumber = False
        isDecimal = False

        prev = 0
        for idx in range(6, len(braille) + 6, 6):
            currBraille = braille[prev: idx]

            # Check for capital, number, decimal, or space markers
            if currBraille in self.capitalFollows:
                isCapital = True
            
            elif currBraille in self.numberFollows:
                isNumber = True

            elif currBraille in self.decimalFollows:
                isDecimal = True

            elif currBraille in self.space:
                isNumber = False
                returnString += ' '

            elif currBraille in self.brailleToAlphaMap and not isNumber and not isDecimal:
                if isCapital:
                    returnString += self.brailleToAlphaMap[currBraille].upper()
                    isCapital = False
                else:
                    returnString += self.brailleToAlphaMap[currBraille]
            
            elif currBraille in self.brailleToNumMap and isNumber:
                returnString += self.brailleToNumMap[currBraille]
            
            elif currBraille in self.brailleToSymbolMap:
                returnString += self.brailleToSymbolMap[currBraille]
            
            elif isDecimal:
                returnString += '.'
                isDecimal = False

            # Move to the next chunk of braille characters
            prev = idx

        return returnString

    def handle_English(self, text) -> str:
        """
        Function description:
        This function takes a string of English text and converts it to its braille representation. It handles alphabetic characters, digits, symbols, spaces, and decimal points by using predefined mappings and markers.

        Input:
        - text (str): A string of English text to be converted to braille.

        Output:
        - str: The braille representation of the input text.
        """


        returnString = ''
        alreadyNum = False

        # Process each character in the input text
        for char in text:

            # Handle alphabet characters
            if char.isalpha():
                if char.isupper():
                    returnString += self.capitalFollows['cap']
                returnString += self.alphaToBrailleMap[char.lower()]
            
            # Handle digit characters
            elif char.isdigit():
                if not alreadyNum:
                    returnString += self.numberFollows['num']
                    alreadyNum = True
                returnString += self.numToBrailleMap[char]

            # Handle symbols
            elif char in self.symbolToBrailleMap:
                returnString += self.symbolToBrailleMap[char]

            # Handle spaces
            elif char in self.space:
                returnString += self.space[' ']
                alreadyNum = False
            
            # Handle decimal points
            elif char in self.decimalFollows:
                returnString += self.decimalFollows['dec']
                returnString += self.actualDecimal

        return returnString

if __name__ == "__main__":
    translatorObject = translator()


