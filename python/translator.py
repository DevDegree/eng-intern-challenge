import sys

class BrailleConverter:
    # English to Braille mappings
    ENGLISH_TO_BRAILLE = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
        "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
        "z": "O..OOO", " ": "......", "cap": ".....O", "num": ".O.OOO"
    }

    # Braille to English mappings
    BRAILLE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_BRAILLE.items()}
    
    NUM_TO_BRAILLE = {
        "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
        "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
    }
    
    BRAILLE_TO_NUM = {value: key for key, value in NUM_TO_BRAILLE.items()}
    
    def __init__(self):
        self.number_mode = False
        self.capitalize_next = False
    
    def to_braille(self, text):
        braille_output = []
        for char in text:
            if char.isupper():
                braille_output.append(self.ENGLISH_TO_BRAILLE['cap'])
                char = char.lower()
            if char.isdigit():
                if not self.number_mode:
                    braille_output.append(self.ENGLISH_TO_BRAILLE['num'])
                    self.number_mode = True
                braille_output.append(self.NUM_TO_BRAILLE[char])
            elif char == ' ':
                self.number_mode = False
                braille_output.append(self.ENGLISH_TO_BRAILLE[char])
            else:
                self.number_mode = False
                braille_output.append(self.ENGLISH_TO_BRAILLE.get(char, ''))
        return ''.join(braille_output)

    def from_braille(self, braille_text):
        braille_groups = [braille_text[i:i + 6] for i in range(0, len(braille_text), 6)]
        english_output = []
        for symbol in braille_groups:
            if symbol == self.ENGLISH_TO_BRAILLE['cap']:
                self.capitalize_next = True
            elif symbol == self.ENGLISH_TO_BRAILLE['num']:
                self.number_mode = True
            else:
                if self.number_mode:
                    english_output.append(self.BRAILLE_TO_NUM.get(symbol, ''))
                    self.number_mode = False
                else:
                    letter = self.BRAILLE_TO_ENGLISH.get(symbol, '')
                    if self.capitalize_next:
                        letter = letter.upper()
                        self.capitalize_next = False
                    english_output.append(letter)
        return ''.join(english_output)

def detect_input_type(input_string):
    converter = BrailleConverter()
    if all(c in 'O.' for c in input_string):
        return converter.from_braille(input_string)
    else:
        return converter.to_braille(input_string)

def main():
    input_string = ' '.join(sys.argv[1:])
    print(detect_input_type(input_string))

if __name__ == "__main__":
    main()
