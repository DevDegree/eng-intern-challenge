class Translator:

    def __init__(self, input_string):
        self.alphabet = {
            'a' : 'O.....',
            'b' : 'O.O...',
            'c' : 'OO....',
            'd' : 'OO.O..',
            'e' : 'O..O..',
            'f' : 'OOO...',
            'g' : 'OOOO..',
            'h' : 'O.OO..',
            'i' : '.OO...',
            'j' : '.OOO..',
            'k' : 'O...O.',
            'l' : 'O.O.O.',
            'm' : 'OO..O.',
            'n' : 'OO.OO.',
            'o' : 'O..OO.',
            'p' : 'OOO.O.',
            'q' : 'OOOOO.',
            'r' : 'O.OOO.',
            's' : '.OO.O.',
            't' : '.OOOO.',
            'u' : 'O...OO',
            'v' : 'O.O.OO',
            'w': '.OOO.O',
            'x' : 'OO..OO',
            'y' : 'OO.OOO',
            'z' : 'O..OOO', 
            ' ' : '......',
        }
        self.numbers = {
            '1' : 'O.....',
            '2' : 'O.O...',
            '3' : 'OO....',
            '4' : 'O..O..',
            '5' : 'O..O..',
            '6' : 'OOO...',
            '7' : 'OOOO..',
            '8' : 'O.OO..',
            '9' : '.OO...',
            '0' : '.OOO..',
        }
        self.decimals = {
            '.' : '..OO.O',
            ',' : '..O...',
            '?' : '..O.OO',
            '!' : '..OOO.',
            ':' : '..OO..',
            ';' : '..O.O.',
            '-' : '....OO',
            '/' : '.O..O.',
            '<' : '.OO..O',
            '>' : 'O..OO.',
            '(' : 'O.O..O',
            ')' : '.O.OO.',
        }
        self.alpha = list(self.alphabet.keys())
        self.alpha_braille = list(self.alphabet.values())
        self.nums = list(self.numbers.keys())
        self.nums_braille = list(self.numbers.values())
        self.deci = list(self.decimals.keys())
        self.deci_braille = list(self.decimals.values())
        self.decode = "alpha" #alpha, nums or deci
        self.position = 0
        self.result = ""
        self.translate(input_string)

    def translate(self, string):
        if self.isBraille(string):
            self.translate_to_english(string)
        else:
            self.translate_to_braille(string)


    def isBraille(self, string):
        characters = set(string)
        contains_period = '.' in characters
        contains_O = 'O' in characters
        return (len(characters) == 2 and contains_period and contains_O)

    def translate_to_braille(self, string):
        for c in string:
            if c == " ":
                self.decode = "alpha"
                self.result += self.alphabet.get(c)
            elif c.isalpha():
                if c.isupper():
                    self.result += '.....O'
                    c = c.lower()
                self.result += self.alphabet.get(c)
            elif c.isnumeric():
                if self.decode=="nums":
                    self.result += self.numbers.get(c)
                else:
                    self.result += ".O.OOO"
                    self.decode = "nums"
                    self.result += self.numbers.get(c)
            else:
                if self.decode=="deci":
                    self.result += self.decimals.get(c)
                else:
                    self.result += ".O...O"
                    self.decode = "deci"
                    self.result += self.decimals.get(c)
                    
    def translate_to_english(self, string):
        if len(string) % 6 != 0:
            raise Exception("Invalid length")
        else:
            while self.position <= len(string) - 6:
                braille = string[self.position:self.position+6]
                if braille==".O.OOO":
                    self.decode = "nums"
                elif braille == ".O...O":
                    self.decode = "deci"
                elif braille == '......':
                    self.decode = "alpha"
                    index = self.alpha_braille.index(braille)
                    self.result += self.alpha[index]
                else:
                    self.handle_decode(braille, string)
                self.position += 6

    def handle_decode(self, braille, string):
        if self.decode == "alpha":
            if braille == ".....O":
                self.position+=6
                if self.position > len(string) - 6:
                    return ''
                index = self.alpha_braille.index(string[self.position:self.position+6])
                self.result += self.alpha[index].upper()
            else:
                index = self.alpha_braille.index(braille)
                self.result += self.alpha[index]
        elif self.decode == "nums":
            index = self.nums_braille.index(braille)
            self.result += self.nums[index]
        else:
            index = self.deci_braille.index(braille)
            self.result += self.deci[index]
            

if __name__ == "__main__":
    import sys
    input_string = ' '.join(sys.argv[1:])
    translator = Translator(input_string)
    print(translator.result)