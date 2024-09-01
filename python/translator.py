
import sys

class BrailleTranslator:
    def __init__(self):
        self.BRAILLE_TO_ENGLISH_MAP = {
            # letters / numbers
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

            # commands / instructions
            ".....O": "cap", # capitalize
            ".O.OOO": "num", # num

            # special characters
            "......": " "
        }

        self.ENGLISH_TO_BRAILLE_MAP = {
            # letters
            "a": "O.....",
            "b": "O.O...",
            "c": "OO....",
            "d": "OO.O..",
            "e": "O..O..",
            "f": "OOO...",
            "g": "OOOO..",
            "h": "O.OO..",
            "i": ".OO...",
            "j": ".OOO..",
            "k": "O...O.",
            "l": "O.O.O.",
            "m": "OO..O.",
            "n": "OO.OO.",
            "o": "O..OO.",
            "p": "OOO.O.",
            "q": "OOOOO.",
            "r": "O.OOO.",
            "s": ".OO.O.",
            "t": ".OOOO.",
            "u": "O...OO",
            "v": "O.O.OO",
            "w": ".OOO.O",
            "x": "OO..OO",
            "y": "OO.OOO",
            "z": "O..OOO",

            # numbers
            "1": "O.....",
            "2": "O.O...",
            "3": "OO....",
            "4": "OO.O..",
            "5": "O..O..",
            "6": "OOO...",
            "7": "OOOO..",
            "8": "O.OO..",
            "9": ".OO...",
            "0": ".OOO..",

            # commands / instructions
            "cap": ".....O",
            "dec": ".O...O",
            "num": ".O.OOO",

            # special characters
            " ": "......"
        }
    

    def is_braille(self, string):
        if len(string) % 6 != 0:
            return False
        
        for char in string:
            if char not in ("O", "."):
                return False
        
        return True


    def translate(self, string):
        translated_string = ""
        if self.is_braille(string):
            is_cap = False
            is_num = False
            parsed_braille = [string[i:i + 6] for i in range(0, len(string), 6)]
            for br in parsed_braille:
                char = self.BRAILLE_TO_ENGLISH_MAP.get(br, None)
                if not char:
                    print("Invalid braille:", br)
                    return

                if is_cap:
                    is_cap = False
                    translated_string += char[0].upper()
                    continue
                
                elif is_num:
                    if char == " ":
                        is_num = False
                        translated_string += char
                    elif len(char) == 2:
                        translated_string += char[1]
                    else:
                        translated_string += char
                    continue

                if char == "cap":
                    is_cap = True
                elif char == "num":
                    is_num = True
                else:
                    translated_string += char[0]
            
        else:
            is_num = False
            for c in string:
                if c.lower() not in self.ENGLISH_TO_BRAILLE_MAP:
                    print("Invalid alphabet:", c)
                    return
                if 'A' <= c <= 'Z':
                    translated_string += self.ENGLISH_TO_BRAILLE_MAP["cap"]
                elif not is_num and '0' <= c <= '9':
                    is_num = True
                    translated_string += self.ENGLISH_TO_BRAILLE_MAP["num"]
                elif is_num and c == " ":
                    is_num = False
                    
                translated_string += self.ENGLISH_TO_BRAILLE_MAP[c.lower()]

        print(translated_string)

    def run(self):
        input_string = ' '.join(sys.argv[1 :])
        self.translate(input_string)

if __name__ == '__main__':
    translator = BrailleTranslator()
    translator.run()