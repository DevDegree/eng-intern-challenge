import argparse, re

class translator:
    def __init__(self) -> None:

        parser = argparse.ArgumentParser(description='Translate a string into braille or braille to text.')

        parser.add_argument('BrailleOrText', type=str)

        givenArgument = parser.parse_args()

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
            '.': '..OO.O',
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
            ')': '.O.OO.',
            ' ': '......'
        }

        # reverse the maps for braille to anything else
        self.brailleToAlphaMap = {value: key for key, value in self.alphaToBrailleMap.items()}
        self.brailleToNumMap = {value: key for key, value in self.numToBrailleMap.items()}
        self.brailleToSymbolMap = {value: key for key, value in self.symbolToBrailleMap.items()}


        # set up regex
        pattern = r'^(?=.*[O.])[O.]{2,}$' # whole idea for this is to make sure we tree a single O or . as english and not braille because logically that doesn't make sense if we treat it as braille
        compiledPattern = re.compile(pattern)
        if re.match(compiledPattern, givenArgument.BrailleOrText):
            self.handle_Braille(givenArgument.BrailleOrText)
        else:
            self.handle_English(givenArgument.BrailleOrText)


    def handle_Braille(self, braille):
        pass

    def handle_English(self, text):
        pass




if __name__ == "__main__":
    translatorObject = translator()


