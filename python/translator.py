import sys

class Translator:
    def __init__(self):
        self.char_to_braille = {
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
            " ": "......",
            "capital": ".....O",  # Braille symbol for capitalization
            "number": ".O.OOO"    # Braille symbol for numbers
        }

        # Reverse dictionary for Braille-to-text translation (excluding numbers)
        self.braille_to_english = {v: k for k, v in self.char_to_braille.items() if not k.isdigit()}
        
        # Separate dictionary for translating Braille symbol to numbers
        self.braille_to_number = {v: k for k, v in self.char_to_braille.items() if k.isdigit()}

    def is_braille(self, input_str):
        return all(char in "O." for char in input_str) and len(input_str) % 6 == 0
    
    # Main translation function to switch between text-to-Braille and Braille-to-text
    def translate(self, input_str):
        if not input_str:
            return ""
        
        if self.is_braille(input_str):
            return self.braille_to_text(input_str)
        else:
            return self.text_to_braille(input_str)
    
    def text_to_braille(self, text):
        braille_output = []

        return "".join(braille_output)
    
    def braille_to_text(self, braille):
        text_output = []

        return "".join(text_output)

if __name__ == "__main__":
    args = sys.argv[1:]
    input_str = " ".join(args)

    translator = Translator()

    print(translator.translate(input_str))