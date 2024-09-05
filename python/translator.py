import sys
from conversion import BrailleTranslator

class BrailleProcessor:
    def __init__(self):
        self.translator = BrailleTranslator()

    def braille_to_text(self, s):
        is_numbers = False
        result = ''
        for i in range(0, len(s), 6):
            c = self.translator.braille_to_char(s[i: i + 6])
            if c == 'decimal' or c == 'number':
                is_numbers = True
            elif c == ' ':
                is_numbers = False
                result += ' '
            else:
                if is_numbers:
                    num = (ord(c) - ord('a') + 1) % 10
                    result += str(num)
                else:
                    result += c
        return result

    def text_to_braille(self, s):
        result = ''
        for c in s:
            result += self.translator.char_to_braille(c)
        return result

    def num_to_braille(self, s):
        result = ''
        for c in s:
            if c != '.':
                c = chr(int(c) + ord('a') - 1)
            result += self.translator.char_to_braille(c)
        return result

    def process_args(self, args):
        result = []
        for arg in args:
            if arg.count('.') + arg.count('O') == len(arg) and len(arg) % 6 == 0:
                result.append(self.braille_to_text(arg))
            else:
                try:
                    float(arg)
                    braille_str = ''
                    if '.' in arg:
                        braille_str += '.O...O'
                    else:
                        braille_str += '.O.OOO'
                    braille_str += self.num_to_braille(arg)
                    result.append(braille_str)
                except ValueError:
                    result.append(self.text_to_braille(arg))
        return '......'.join(result)

def main(args):
    processor = BrailleProcessor()
    print(processor.process_args(args))

if __name__ == '__main__':
    main(sys.argv[1:])
