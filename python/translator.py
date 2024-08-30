import sys

class BrailleTranslator:

    ENGLISH_TO_BRAILLE = {
        'a': 'O.....', 
        'b': 'O.O...', 
        'c': 'OO....',
        'd': 'OO.O..', 
        'e': 'O..O..', 
        'f': 'OOO...',
        'g': 'OOOO..', 
        'h': 'O.OO..', 
        'i': '.OO...',
        'j': '.OOO..', 
        'k': 'O...O.', 
        'l': 'O.O.O.',
        'm': 'OO..O.', 
        'n': 'OO.OO.', 
        'o': 'O..OO.',
        'p': 'OOO.O.', 
        'q': 'OOOOO.', 
        'r': 'O.OOO.',
        's': '.OO.O.', 
        't': '.OOOO.', 
        'u': 'O...OO',
        'v': 'O.O.OO', 
        'w': '.OOO.O', 
        'x': 'OO..OO',
        'y': 'OO.OOO', 
        'z': 'O..OOO', 
        '.': '..OO.O',
        ',': '..O...', 
        '?': '..O.OO', 
        '!': '..OOO.',
        ':': '..OO..', 
        ';': '..O.O.', 
        '-': '....OO',
        '/': '.O..O.', 
        '<': '.OO..O', 
        '>': 'O..OO.',
        '(': 'O.O..O', 
        ')': '.O.OO.', 
        ' ': '......',
        'capital': '.....O', 
        'decimal': '.O...O', 
        'number': '.O.OOO',
    }

    BRAILLE_TO_ENGLISH = {braille_char: english_char for english_char, braille_char in ENGLISH_TO_BRAILLE.items()}

    def __init__(self, string):
        self.input_string = string
        self.is_braille = False

    def language_identifier(self):

        if all(char in 'O.' for char in self.input_string):
            self.is_braille = True
            return [self.input_string[i: i + 6] for i in range(0, len(self.input_string), 6)]
        
        else:
            return [char for char in self.input_string]
    
    def translate(self):

        identified_string = self.language_identifier()

        if self.is_braille:
            return self.braille_to_english(identified_string)
        
        else:
            return self.english_to_braille(identified_string)

    def english_to_braille(self, english_text):
        s = ''
        for char in english_text:

            if char.isupper():
                s += self.ENGLISH_TO_BRAILLE['capital']

            s += self.ENGLISH_TO_BRAILLE[char.lower()]
            
        return s

    def braille_to_english(self, braille_text):
        s = ''
        is_capital = False
        for braille_cell in braille_text:

            if braille_cell == '.....O':
                is_capital = True
                continue
            
            if is_capital:
                s += self.BRAILLE_TO_ENGLISH[braille_cell].upper()
                is_capital = False

            else:
                s += self.BRAILLE_TO_ENGLISH[braille_cell]

        return s
            
def main():
    string = ' '.join(sys.argv[1:])
    translator = BrailleTranslator(string)
    result = translator.translate()
    print(result)

if __name__ == '__main__':
    main()

# Translator
# When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.

# Braille Alphabet
# The ability to capitalize letters
