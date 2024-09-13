
import sys

class Translator:

    CAPITAL_FOLLOWS = ".....O"
    NUMBER_FOLLOWS = ".O.OOO"
    SPACE = "......"

    def __init__(self) -> None:
  
  
        self.ENGLISH_TO_BRAILLE = {
            'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
            'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
            'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
            'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
            'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
            'z': "O..OOO", ' ': self.SPACE, 'CAPITAL': self.CAPITAL_FOLLOWS, 'NUMBER': self.NUMBER_FOLLOWS
        }

        self.NUMBER_TO_BRAILLE = {
            '0': ".OOO..", '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
            '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO..."
        }

    
        self.BRAILLE_TO_ENGLISH = {braille: english for english, braille in self.ENGLISH_TO_BRAILLE.items() if english not in ['CAPITAL', 'NUMBER']}
        self.BRAILLE_TO_NUMBER = {braille: number for number, braille in self.NUMBER_TO_BRAILLE.items()}

    def classify_input(self, text: str) -> str:

        if all(char in "O. " for char in text) and len(text.replace(" ", "")) % 6 == 0:
            return 'BRAILLE'
        return 'ENGLISH'

    def translate_to_braille(self, text: str) -> str:

        result = []
        is_number = False

        for char in text:
            if char == ' ':
                result.append(self.SPACE)
            elif char.isupper():
                result.append(self.CAPITAL_FOLLOWS)
                result.append(self.ENGLISH_TO_BRAILLE[char.lower()])
                is_number = False
            elif char.isdigit():
                if not is_number:
                    result.append(self.NUMBER_FOLLOWS)
                    is_number = True
                result.append(self.NUMBER_TO_BRAILLE[char])
            else:
                result.append(self.ENGLISH_TO_BRAILLE.get(char, ''))
                is_number = False

        return ''.join(result)

    def translate_to_english(self, braille: str) -> str:

        result = []
        is_capital = False
        is_number = False

       
        braille_symbol_length = 6


        for i in range(0, len(braille), braille_symbol_length):
            symbol = braille[i:i + braille_symbol_length]

            if symbol == self.CAPITAL_FOLLOWS:
                is_capital = True
            elif symbol == self.NUMBER_FOLLOWS:
                is_number = True
            elif symbol == self.SPACE:
                result.append(' ')
                is_number = False  
            else:
                if is_number:
               
                    result.append(self.BRAILLE_TO_NUMBER.get(symbol, ''))
                else:
                   
                    letter = self.BRAILLE_TO_ENGLISH.get(symbol, '')
                    if is_capital:
                        letter = letter.upper()
                        is_capital = False  
                    result.append(letter)

        return ''.join(result)


def main() -> None:

    translator = Translator()

    input_text = ' '.join(sys.argv[1:])
    input_type = translator.classify_input(input_text)

    if input_type == 'BRAILLE':
        print(translator.translate_to_english(input_text))
    else:
        print(translator.translate_to_braille(input_text))


if __name__ == "__main__":
    main()
