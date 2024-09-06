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
        is_digit = False

        for char in text:
            if char.isupper():
                braille_output.append(self.char_to_braille["capital"])
                braille_output.append(self.char_to_braille[char.lower()])
            elif char.isdigit():
                if not is_digit:
                    braille_output.append(self.char_to_braille["number"])
                    is_digit = True

                braille_output.append(self.char_to_braille[char])
            else:
                if char == " ":
                    is_digit = False

                braille_output.append(self.char_to_braille[char])

        return "".join(braille_output)
    
    def braille_to_text(self, braille):
        text_output = []
        braille_chunks = [braille[i:i+6] for i in range(0, len(braille), 6)]
        capitalize_next = False
        is_number = False

        for chunk in braille_chunks:
            if chunk == self.char_to_braille["capital"]:
                capitalize_next = True
                continue
            elif chunk == self.char_to_braille["number"]:
                is_number = True
                continue
            elif chunk == self.char_to_braille[" "]:
                is_number = False

            if is_number:
                char = self.braille_to_number.get(chunk, "")
            else:
                char = self.braille_to_english.get(chunk, "")

            # Capitalize if needed
            if capitalize_next and char:
                char = char.upper()
                capitalize_next = False
            
            text_output.append(char)

        return "".join(text_output)

if __name__ == "__main__":
    args = sys.argv[1:]
    input_str = " ".join(args)

    translator = Translator()

    print(translator.translate(input_str))