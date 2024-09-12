import sys

class Translator:
    english_to_braille_dict = {
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
        "cap": ".....O",
        "num": ".O.OOO",
        " ": "......",
    }
    
    braille_to_english_dict = {}
    
    def __init__(self):
        for key in self.english_to_braille_dict:
            self.braille_to_english_dict[self.english_to_braille_dict[key]] = key
        # Note that 1-9 has the same braille as a-i
        for i in range(1, 10):
            self.english_to_braille_dict[str(i)] = self.english_to_braille_dict[chr(ord('a') + i - 1)]
        # Note that braille '0' is the same as 'j'
        self.english_to_braille_dict["0"] = self.english_to_braille_dict["j"]
        
    def eng_to_braille(self, text):
        res = []
        nums_on = False
        for c in text:
            if c.isupper():
                res.append(self.english_to_braille_dict["cap"])
                c = c.lower()
            elif c.isnumeric():
                if not nums_on:
                    nums_on = True
                    res.append(self.english_to_braille_dict["num"])
            if c == " ":
                nums_on = False
            res.append(self.english_to_braille_dict[c])
        return "".join(res)

        
        
    def braille_to_eng(self, text):
        caps_on = False
        nums_on = False
        res = []
        n = len(text)
        # Read in 6 chars at a time
        for i in range(0, n, 6):
            braille_char = input[i : i + 6]
            english_char = self.braille_to_english_dict[braille_char]
            
            if english_char == "cap":
                caps_on = True
            elif english_char == 'num':
                nums_on = True
            else:
                if caps_on:
                    # caps resets
                    res.append(english_char.upper())
                    caps_on = False
                elif nums_on:
                    if english_char == 'j':
                        res.append('0')
                    else:
                        res.append(str(ord(english_char) - ord('a') + 1))
                else:
                    res.append(english_char)
                if english_char == " ":
                    nums_on = False
        return "".join(res)
                
    
if __name__ == "__main__":
    input = " ".join(sys.argv[1:])

    # True if input is English
    is_english = "".join(sys.argv[1:]).replace(" ", "").isalnum()

    translator = Translator()

    if is_english:
        print(translator.eng_to_braille(input))
    else:
        print(translator.braille_to_eng(input))