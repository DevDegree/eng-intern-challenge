from sys import argv

# Create a Dictionary for our conversion
ENGLISH_TO_BRAILLE = {
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
    "cap": ".....O",
    "num": ".O.OOO",
}

# Create Separate Dictionaries for Braille to Letters and Numbers 
BRAILLE_TO_LETTER = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if not k.isnumeric()}
BRAILLE_TO_NUMBER = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if k.isnumeric()}



class Translator:
    def __init__(self, input_text):
        self.input_text = input_text
        self.output_text = ""

    # Convert English to Braille
    def to_braille(self) -> str:
        for char in self.input_text: # Loop through each character in the input text
            # Manage uppercase 
            if char.isupper(): 
                self.output_text += ENGLISH_TO_BRAILLE["cap"]
                char = char.lower()
                self.output_text += ENGLISH_TO_BRAILLE[char]
            # Manage number
            elif char.isnumeric():
                self.output_text += ENGLISH_TO_BRAILLE["num"]
                self.output_text += ENGLISH_TO_BRAILLE[char]
            # Manage normal characters
            else:
                self.output_text += ENGLISH_TO_BRAILLE[char]
        return self.output_text

    # Convert Braille to English
    def to_english(self) -> str:
        # Split the input text into 6 character chunks
        braille_chars = [self.input_text[i:i + 6] for i in range(0, len(self.input_text), 6)]
        for char in braille_chars:
            if char == ENGLISH_TO_BRAILLE["cap"]:
                self.output_text += BRAILLE_TO_LETTER[char].upper()
            elif char == ENGLISH_TO_BRAILLE["num"]:
                self.output_text += BRAILLE_TO_NUMBER[braille_chars[braille_chars.index(char) + 1]]
            else:
                self.output_text += BRAILLE_TO_LETTER[char]
        return self.output_text


    