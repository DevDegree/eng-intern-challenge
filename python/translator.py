class BrailleTranslator:
    """
    Detected issues:
    - the character "<" is repeated to the letter "o" and the number "0". There should be a way to differentiate between the two.
    - it will continue printing numbers until a space is detected, what about numbers and letters in the same word? "123abc"
    """

    # # unflatten matrix
    # print("=== unflatten matrix ===")
    # import numpy as np
    # t = np.array(list(t))
    # t = t.reshape((len(t)//6, 3,2))
    # print(t)
    def __init__(self):
        self.braille_dict = {
            # Capital follows
            'capital': '.....O',
            # number follows
            'number': '.O.OOO',
            # Space
            ' ': '......',
            #characters
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
            # Numbers
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
            # punctuation
            '.': '..OO.O',
            ',': '..O...',
            '?': '..O.OO',
            '!': '..OOO.',
            ':': '..OO..',
            ';': '..O.O.',
            '-': '....OO',
            '/':'.O..O.',
            '<':'.OO..O',
            # '>':'O..OO.', # This value is repeated to O, there should be a way to differentiate between the two
            '(': 'O..OO.',
            ')': '.OO.O.',

        }

        # Due to some errors on duplicated elements, reversing the dictionary is not possible
        self.braille_follows={
            # Capital follows
             '.....O':'capital',
            # number follows
            '.O.OOO':'number'
        }
        self.braille_chars={
            'O.....':'a',
            'O.O...':'b',
            'OO....':'c',
            'OO.O..':'d',
            'O..O..':'e',
            'OOO...':'f',
            'OOOO..':'g',
            'O.OO..':'h',
            '.OO...':'i',
            '.OOO..':'j',
            'O...O.':'k',
            'O.O.O.':'l',
            'OO..O.':'m',
            'OO.OO.':'n',
            'O..OO.':'o',
            'OOO.O.':'p',
            'OOOOO.':'q',
            'O.OOO.':'r',
            '.OO.O.':'s',
            '.OOOO.':'t',
            'O...OO':'u',
            'O.O.OO':'v',
            '.OOO.O':'w',
            'OO..OO':'x',
            'OO.OOO':'y',
            'O..OOO':'z',
            #punctuation
            '..OO.O':'.',
            '..O...':',',
            '..O.OO':'?',
            '..OOO.':'!',
            '..OO..':':',
            '..O.O.':';',
            '....OO':'-',
            '.O..O.':'/',
            '.OO..O':'<',
            # 'O..OO.':'>', # This value is repeated to O, there should be a way to differentiate between the two
            'O.O..O': '(',
            '.O.OO.': ')',
            # Space
            '......':' '
        }
        self.braille_numbers={
            'O.....':'1',
            'O.O...':'2',
            'OO....':'3',
            'OO.O..':'4',
            'O..O..':'5',
            'OOO...':'6',
            'OOOO..':'7',
            'O.OO..':'8',
            '.OO...':'9',
            '.OOO..':'0',
            'O..OO.':'>', # This value is repeated to O, there should be a way to differentiate between the two

        }


    def is_braille(self, text):
        """is_braile checks if the string is a valid braille string or plain text"""
        return len(text) % 6 == 0 and "O" in text and "." in text


    def parse_string(self, _str):
        """parse_string converts a string to braille or vice versa"""
        if self.is_braille(_str):
            # convert braille to text
            text=""
            special=""
            for cell_index in range(0, len(_str), 6):
                if _str[cell_index:cell_index + 6] in self.braille_dict.values():
                    if _str[cell_index:cell_index + 6] in self.braille_follows.keys():
                        special = self.braille_follows[_str[cell_index:cell_index + 6]]
                    else:
                        if self.braille_chars[_str[cell_index:cell_index + 6]] == ' ':
                            text+=self.braille_chars[_str[cell_index:cell_index + 6]]
                            special=""
                        elif special == 'capital':
                            text+=self.braille_chars[_str[cell_index:cell_index + 6]].upper()
                            special=""
                        elif special == 'number':
                            # assume all following symbols are numbers until the next space symbol.
                            text+=self.braille_numbers[_str[cell_index:cell_index + 6]]
                        else:
                            text+=self.braille_chars[_str[cell_index:cell_index + 6]]
            return text
        else:
            # convert text to braille
            braille=""
            number_follows=False
            for c in _str:
                if c.isupper():
                    braille+=self.braille_dict['capital']
                    braille+=self.braille_dict[c.lower()]
                    number_follows = False

                elif c.isdigit():
                    if not number_follows:
                        # only add the number follows if the number is not following another number
                        braille+=self.braille_dict['number']
                    braille+=self.braille_dict[c]
                    number_follows = True

                else:
                    number_follows = False
                    braille+=self.braille_dict[c]
            return braille


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text>")
        sys.exit(1)
    text = " ".join(sys.argv[1:])
    translator = BrailleTranslator()
    print(translator.parse_string(text))


