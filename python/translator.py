import sys

class Translator:
    def __init__(self):
        self.BRAILLE_TO_ENG = {
            "O.....": "a1",
            "O.O...": "b2", 
            "OO....": "c3", 
            "OO.O..": "d4", 
            "O..O..": "e5", 
            "OOO...": "f6", 
            "OOOO..": "g7", 
            "O.OO..": "h8", 
            ".OO...": "i9", 
            ".OOO..": "j0", 
            "O...O.": "k",
            "O.O.O.": "l",
            "OO..O.": "m",
            "OO.OO.": "n",
            "O..OO.": "o",
            "OOO.O.": "p",
            "OOOOO.": "q",
            "O.OOO.": "r",
            ".OO.O.": "s",
            ".OOOO.": "t",
            "O...OO": "u",
            "O.O.OO": "v",
            ".OOO.O": "w",
            "OO..OO": "x",
            "OO.OOO": "y",
            "O..OOO": "z",
            "......": " ",
            ".....O": "C", # CAPITALIZE
            ".O.OOO": "N"  # NUMBER
        }
        self.ENG_TO_BRAILLE = {char: k for k, v in self.BRAILLE_TO_ENG.items() for char in v}

    def translate(self, string):
        result = ""
        if self.is_braille(string):
            if not len(string) % 6 == 0:
                print("Invalid braille characters")
                return
            isNum = False
            isCap = False
            for idx in range(0, len(string), 6):
                braille_char = string[idx:idx+6]
                if braille_char not in self.BRAILLE_TO_ENG:
                    print("Invalid braille characters")
                    return
                eng_char = self.BRAILLE_TO_ENG[braille_char]
                # handle special characters
                if eng_char == "C":
                    isCap = True
                elif eng_char == "N":
                    isNum = True
                elif isNum and len(eng_char) >= 2:
                    result += eng_char[1]
                elif eng_char == " ":
                    isNum = False
                    result += " "
                elif isCap:
                    result += eng_char[0].upper()
                    isCap = False
                else:
                    result += eng_char[0]
        else:
            isNum = False
            for char in string:
                if char.isupper():
                    result += self.ENG_TO_BRAILLE["C"] + self.ENG_TO_BRAILLE[char.lower()]
                elif char.isnumeric():
                    if not isNum:
                        result += self.ENG_TO_BRAILLE["N"]
                        isNum = True
                    result += self.ENG_TO_BRAILLE[char]
                else:
                    if char == " " and isNum:
                        isNum = False
                    result += self.ENG_TO_BRAILLE[char]
        print(result)


    def is_braille(self, string):
        return len(string) >= 6 and "." in string[:6] # all valid braille characters have at least one period

if __name__ == "__main__":
    translator = Translator()
    
    string = " ".join(sys.argv[1:])
    translator.translate(string)
