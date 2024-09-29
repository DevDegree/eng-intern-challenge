import sys

class Mapper:

    CAPITAL_FOLLOWS = '.....O'
    NUMBER_FOLLOWS = '.O.OOO'
    SPACE = '......'

    def __init__(self) -> None:
            self.en_to_br = {
                # a - z
                'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
                'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
                'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
                'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
            }

            self.br_to_en = {v: k for k,v in self.en_to_br.items()}
            self.en_to_num = {
                'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 
                'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
            }
            self.num_to_en = {v: k for k,v in self.en_to_num.items()}
    
    def to_english(self, br_char, capitalize=False):
        return self.br_to_en.get(br_char, "").upper() if capitalize else self.br_to_en.get(br_char, "")

    def to_braille(self, char):
        return self.en_to_br.get(char, "")
    
    def numberify(self, letter):
        return self.en_to_num.get(letter, "")
    
    def englify(self, num):
        return self.num_to_en.get(num, "")


class Translator:
    def __init__(self) -> None:
          self.mapper = Mapper()

    def is_braille(self, s):
        return len(s) % 6 == 0 and all(c in ['O', '.'] for c in s)
    
    def translate_english_to_braille(self, sentence):
        temp = []
        is_first_digit = True
        englify = False
        x = 0
        while x < len(sentence):
            char = sentence[x]
            if char.isupper():
                temp.append(Mapper.CAPITAL_FOLLOWS)
                temp.append(self.mapper.to_braille(char.lower()))
            elif char.isdigit():
                if is_first_digit:
                    englify = True
                    is_first_digit = False
                    temp.append(Mapper.NUMBER_FOLLOWS)
            elif char.isspace():
                if not is_first_digit: is_first_digit = True
                if englify: englify = False
            if englify:
                lett = self.mapper.englify(char)
                temp.append(self.mapper.to_braille(lett))
            else:
                temp.append(self.mapper.to_braille(char))
            x += 1
        return temp
                 
                 
    
    def translate_braille_to_english(self, sentence):
        temp = []
        x = 0
        capitalize = False
        numberify = False
        while x < len(sentence) - 5:
            braille_text = sentence[x:x+6]
            if braille_text == Mapper.CAPITAL_FOLLOWS:
                capitalize = True
                x += 6
                continue
            if braille_text == Mapper.NUMBER_FOLLOWS:
                numberify = True
                x += 6
                continue
            if braille_text == Mapper.SPACE:
                if numberify: numberify = False

            if capitalize:
                capitalize = False
                temp.append(self.mapper.to_english(braille_text, capitalize=True))
            elif numberify:
                letter = self.mapper.to_english(braille_text)
                temp.append(self.mapper.numberify(letter))
            else:
                temp.append(self.mapper.to_english(braille_text))
                 
            x += 6
        
        return temp



def main():
    if len(sys.argv) == 1:
        print("Usage: python3 translator.py text")
        sys.exit(0)

    inputs = []
    translator = Translator()
    output = []
    for arg in sys.argv[1:]:
        inputs.append(arg)
        inputs.append(' ')
    inputs = ''.join(inputs[:-1])


    if translator.is_braille(inputs):
        output = translator.translate_braille_to_english(inputs)
    else:
        output = translator.translate_english_to_braille(inputs)
    
    sys.stdout.write(''.join(output))
        

if __name__ == "__main__":
    main()