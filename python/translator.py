class Translator:
    def __init__(self):
        # Dictionary for English to braille
        self.eng_to_br = {
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
            "0": ".OOO..",
            "1": "O.....",
            "2": "O.O...",
            "3": "OO....",
            "4": "OO.O..",
            "5": "O..O..",
            "6": "OOO...",
            "7": "OOOO..",
            "8": "O.OO..",
            "9": ".OO...",
            " ": "......",
            "^": ".....O"
        }   

        # Dictionary for braille to English
        self.br_to_eng ={
            "O.....": "a",
            "O.O...": "b",
            "OO....": "c",
            "OO.O..": "d",
            "O..O..": "e",
            "OOO...": "f",
            "OOOO..": "g",
            "O.OO..": "h",
            ".OO...": "i",
            ".OOO..": "j",
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
            ".OOO..": "0",
            "O.....": "1",
            "O.O...": "2",
            "OO....": "3",
            "OO.O..": "4",
            "O..O..": "5",
            "OOO...": "6",
            "OOOO..": "7",
            "O.OO..": "8",
            ".OO...": "9",
            "......": " ",
            ".....O": "^"
        }

        # Function to convert English to Braille
        def eng_to_braille(self, text):
            braille = ""
            for char in text:
                if char.isupper():
                    braille += self.eng_to_br["^"]
                    char = char.lower()
                braille += self.eng_to_br[char]
            return braille
        
        # Function to convert Braille to English
        def braille_to_eng(self, text):
            words = [text[i:i+6] for i in range(0, len(text), 6)]
            english = ""
            caps = False
            for word  in words :
                if word == ".....O":
                    caps = True
                    continue
                else:
                    if caps:
                        english += self.br_to_eng[word].upper()
                        caps = False
                    else:
                        english += self.br_to_eng[word]
            return english
        

            

   

def main():
    pass
if __name__=="__main__":
    main()
