import sys

class BrailleTranslator:

    to_braille_dict = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
        '0': '.OOO..',
        
        # punctuation
        '.': '..OO.O', ',': '.O....', '?': '.O.O.O', '!': '..OOO.', ':': '..OO..',
        ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '(': 'O.O..O', 
        ')': '.O.OO.',

        # special symbols
        'capital_follows': '.....O',
        'decimal_follows': '....O.', # not considered
        'number_follows': '.O.OOO',
        'space': '......'
    }

    to_number_dict = {
        'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
        'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
    }

    to_english_dict = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z',

        # punctuation
        '..OO.O': '.', '.O....': ',', '.O.O.O': '?', '..OOO.': '!', '..OO..': ':', 
        '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O.O..O': '(', 
        '.O.OO.': ')',

        # special symbols
        '.....O': 'capital_follows',
        '....O.': 'decimal_follows', # not considered
        '.O.OOO': 'number_follows',
        '......': 'space'
    }


    # initialize the BrailleTranslator with the input string 
    # input_str: the string to be translated, can be either english or braille
    def __init__(self, input):
        self.input_string = input
    
    # is_braille(): returns true if the string is braille
    def is_braille(self):
        # note: it is possible to input ambiguous strings, (e.g. 'O.....')
        #   which we cannot distingush between braille or english, for these
        #   assume braille, as it is not a "syntactically correct" english word

        # criteria - length should be a multiple of 6 and be composed of 0's of .'s only
        return len(self.input_string) % 6 == 0 and all(c in 'O.' for c in self.input_string)

    # translate_to_braille(): returns a string of the braille translation of input_str
    def translate_to_braille(self):
        digit_flag = False
        result = []

        for char in self.input_string:
            if char == ' ':
                result.append(self.to_braille_dict['space'])
                digit_flag = False
            elif char.isdigit():
                if digit_flag == False:
                    result.append(self.to_braille_dict['number_follows'])
                    digit_flag = True
                result.append(self.to_braille_dict[char])
            elif char.isupper():
                result.append(self.to_braille_dict['capital_follows'])
                result.append(self.to_braille_dict[char.lower()])
            else:
                result.append(self.to_braille_dict[char])
                
        return ''.join(result)
    
    # translate_to_english(): returns a string of the english translation of input_str
    def translate_to_english(self):
        result = []
        digit_flag = False
        capital_flag = False

        i = 0
        while i < len(self.input_string):
            symbol = self.input_string[i:i+6]

            if symbol == self.to_braille_dict['capital_follows']:
                capital_flag = True
                i+=6
            elif symbol == self.to_braille_dict['number_follows']:
                digit_flag = True
                i+=6
            elif symbol == self.to_braille_dict['space']:
                digit_flag = False
                result.append(' ')
                i+=6
            else:
                if digit_flag:
                    result.append(self.to_number_dict[symbol])
                else:
                    letter = self.to_english_dict[symbol]

                    if capital_flag:
                        result.append(letter.upper())
                        capital_flag = False
                    else:
                        result.append(letter)
                i+=6
        return ''.join(result)
    
    # translate(): detects input type and returns translated string
    def translate(self):
        if self.is_braille():
            return self.translate_to_english()
        else:
            return self.translate_to_braille()

if __name__ == '__main__':
    input_string = ' '.join(sys.argv[1:])
    translator = BrailleTranslator(input_string)
    print(translator.translate())
