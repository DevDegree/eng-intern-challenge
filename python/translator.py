import sys

class BrailleTranslator:
    def __init__(self):
        self.braille_dict = {
            "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
            "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
            "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
            "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
            "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
            "z": "O..OOO", 
            "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
            "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
            " ": "......",  # Space
            "capital": ".....O", # Capitalization symbol
            "number": ".O.OOO", # Number symbol
        }
        self.eng_dict = {v: k for k, v in self.braille_dict.items() if k not in ["capital", "number"]}

    def english_to_braille(self, text):
        result = []
        is_number = False

        for char in text:
            # Handle spaces
            if char == ' ':
                result.append(self.braille_dict[" "])
                is_number = False  # Reset number mode after space
                continue

            # Handle digits
            if char.isdigit():
                if not is_number:
                    result.append(self.braille_dict["number"])  # Number symbol
                    is_number = True  # Enter number mode
                result.append(self.braille_dict[char])
                continue

            # Handle uppercase letters
            if char.isupper():
                result.append(self.braille_dict["capital"])  # Capital letter symbol
                char = char.lower()

            # Handle lowercase letters
            if char in self.braille_dict:
                result.append(self.braille_dict[char])
                is_number = False  # Exit number mode when switching to letters
            else:
                print(f"Warning: '{char}' is not a valid character and will be skipped.")

        return ''.join(result)

    def braille_to_english(self, braille):
        result = []
        i = 0
        is_capital = False
        is_number = False
        while i < len(braille):
            # Read 6-character braille symbols
            symbol = braille[i:i+6]
            i += 6
            
            if symbol == self.braille_dict["capital"]:
                is_capital = True
                continue
            elif symbol == self.braille_dict["number"]:
                is_number = True
                continue
            elif symbol == self.braille_dict[" "]:  # Reset number mode after space
                is_number = False
                result.append(' ')
                continue

            # Handle numbers and letters differently
            if is_number:
                if symbol in self.eng_dict:
                    char = self.eng_dict[symbol]
                    if char.isdigit():  # Ensure the character is a valid number
                        result.append(char)
            else:
                if symbol in self.eng_dict:
                    char = self.eng_dict[symbol]
                    if is_capital:
                        char = char.upper()
                        is_capital = False
                    result.append(char)
                else:
                    print(f"Warning: '{symbol}' is not a valid Braille symbol and will be skipped.")
        
        return ''.join(result)

    def translate(self, input_string):
        # Determine if the input is Braille or English
        if all(c in "O." for c in input_string):
            return self.braille_to_english(input_string)
        else:
            return self.english_to_braille(input_string)

    @staticmethod
    def main():
        if len(sys.argv) < 2:
            print("Usage: python translator.py <string_to_translate>")
            return
        
        # Join all the arguments after the script name into one string
        input_string = ' '.join(sys.argv[1:])
        translator = BrailleTranslator()
        print(translator.translate(input_string))

if __name__ == "__main__":
    BrailleTranslator.main()