import sys

class BrailleTranslationError(Exception):
    pass

class InvalidBrailleError(BrailleTranslationError):
    pass

class UnsupportedCharacterError(BrailleTranslationError):
    pass

class BrailleTranslator:
    ENG_TO_BRAILLE_CHARS = {
        'a': "O.....", 'b': "O.O...", 'c': "OO....",
        'd': "OO.O..", 'e': "O..O..", 'f': "OOO...",
        'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...",
        'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
        'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
        'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.",
        's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO",
        'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
        'y': "OO.OOO", 'z': "O..OOO", ' ': "......",
    }
    
    ENG_TO_BRAILLE_NUMS = {
        '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", 
        '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
        '9': ".OO...", '0': ".OOO.."
    }
    
    CAPITAL_BRAILLE = ".....O"
    NUMBER_BRAILLE = ".O.OOO"

    BRAILLE_TO_ENG_CHARS = {v: k for k, v in ENG_TO_BRAILLE_CHARS.items()}
    BRAILLE_TO_ENG_NUMS = {v: k for k, v in ENG_TO_BRAILLE_NUMS.items()}

    def __init__(self):
        self.is_next_capital = False
        self.is_number_mode = False

    def is_braille(self, value: str) -> bool:
        return all(c in "O." for c in value) and len(value) % 6 == 0

    def translate_braille_to_eng(self, value: str) -> str:
        if not self.is_braille(value):
            raise InvalidBrailleError("The provided string is not valid Braille.")
        
        translated_str = []
        num_chars = len(value)
        
        for i in range(0, num_chars, 6):
            curr_symbol = value[i:i+6]
            if curr_symbol == self.CAPITAL_BRAILLE:
                self.is_next_capital = True
            elif curr_symbol == self.NUMBER_BRAILLE:
                self.is_number_mode = True
            else:
                char = self._translate_symbol(curr_symbol)
                translated_str.append(char)
        
        return ''.join(translated_str)

    def _translate_symbol(self, symbol: str) -> str:
        if self.is_next_capital:
            char = self.BRAILLE_TO_ENG_CHARS.get(symbol, '?').upper()
            self.is_next_capital = False
        elif self.is_number_mode:
            char = self.BRAILLE_TO_ENG_NUMS.get(symbol, '?')
            if char == ' ':
                self.is_number_mode = False
        else:
            char = self.BRAILLE_TO_ENG_CHARS.get(symbol, '?')
        
        if char == '?':
            raise UnsupportedCharacterError(f"Unsupported Braille symbol: {symbol}")
        
        return char

    def translate_eng_to_braille(self, value: str) -> str:
        translated_str = []

        for char in value:
            if char.isdigit():
                if not self.is_number_mode:
                    translated_str.append(self.NUMBER_BRAILLE)
                    self.is_number_mode = True
                translated_str.append(self.ENG_TO_BRAILLE_NUMS[char])
            elif char.isalpha():
                if char.isupper():
                    translated_str.append(self.CAPITAL_BRAILLE)
                translated_str.append(self.ENG_TO_BRAILLE_CHARS[char.lower()])
                self.is_number_mode = False
            elif char == ' ':
                translated_str.append(self.ENG_TO_BRAILLE_CHARS[char])
                self.is_number_mode = False
            else:
                raise UnsupportedCharacterError(f"Unsupported character: {char}")

        return ''.join(translated_str)

def main():
    if len(sys.argv) < 2:
        sys.exit("Error: Please provide an input string to translate.")

    input_value = ' '.join(sys.argv[1:])
    translator = BrailleTranslator()

    try:
        if translator.is_braille(input_value):
            print(translator.translate_braille_to_eng(input_value))
        else:
            print(translator.translate_eng_to_braille(input_value))
    except BrailleTranslationError as e:
        sys.exit(f"Translation error: {e}")
    except Exception as e:
        sys.exit(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
