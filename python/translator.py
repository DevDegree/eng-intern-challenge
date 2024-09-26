class Translator:
    def __init__(self, string):
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
            'O' : '.OOO..',
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
        self.x = 0
        self.result = ""
        self.translate(string)

    def translate(self, string):
        if (any(c.isalpha() for c in string)):
            self.translate_to_braille(string)
        else:
            self.translate_to_english(string)


    def translate_to_braille(self, string):
        for c in string:
            if (c == " "):
                self.decode = "alpha"
                self.result += self.alphabet.get(c)
            elif (c.isalpha()):
                if (c.isupper()):
                    self.result += '.....O'
                    c = c.lower()
                    self.result += self.alphabet.get(c)
            elif (c.isnumeric()):
                if (decode=="nums"):
                    self.result += self.nums.get(c)
                else:
                    self.result += ".O...O"
                    self.decode = "nums"
                    self.result += self.numbers.get(c)
            else:
                if (self.decode=="deci"):
                    self.result += self.deci.get(c)
                else:
                    self.result += ".O.OOO"
                    self.decode = "deci"
                    self.result += self.decimals.get(c)
        return self.result

    def translate_to_english(self, string):
        if (len(string) % 6 != 0):
            raise Exception("Invalid length")
        else:
            while (self.x <= len(string)):
                braille = string[x:x+6]
                if (braille==".O.OOO"):
                    decode = "nums"
                elif (braille == ".O...O"):
                    braille = string[x:x+6]
                elif (braille == '......'):
                    decode = "alpha"
                    position = alpha_braille.index(braille)
                    result += alpha[position]
                else:
                    handle_decode(braille)
                x += 6
        return result

    def handle_decode(self, string):
        if (decode=="alpha"):
            if (braille == ".....O"):
                x+=6
                position = alpha_braille.index(string[x:x+6])
                result += alpha[position].upper()
            else:
                position = alpha_braille.index(braille)
                result += alpha[position]
        elif (decode=="nums"):
            position = nums_braille.index(braille)
            result += nums[position]
        else:
            position = deci_braille.index(braille)
            result += deci[position]

if __name__==" __main__":
    import sys
    string = ' '.join(sys.argv[1:])
    translator = Translator(string)
    print(translator.result)
