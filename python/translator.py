class brailleTranslator:
    # map
    braille_map = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', ' ': '......', '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
        '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
        '9': '.OO...', '0': '.OOO..'}
    
    # number only
    number_map = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', 
                  '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
                  '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
                  '0': '.OOO..'}
    
    # letter only
    letter_map = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', ' ': '......'}
    
    # reverse of number_map
    inverted_number_map = {b: e for e, b in number_map.items()}

    # reverse of letter_map
    inverted_letter_map = {b: e for e, b in letter_map.items()}
    
    cap = '.....O'
    num = '.O.OOO'

    def __init__(self, input_string):
        self.input_string = input_string
    
    def check_type(self):
        return all(c in ['O','.'] for c in self.input_string)
    
    def english_to_braille(self):
        result = []
        number_mode = False

        for c in self.input_string:
            if c.isupper():
                result.append(self.cap)
                result.append(self.braille_map[c.lower()])
            elif c.isdigit():
                if not number_mode:
                    result.append(self.num)
                    number_mode = True
                result.append(self.braille_map[c])
            elif c == ' ':
                number_mode = False
                result.append(self.braille_map[c])
            else:
                result.append(self.braille_map[c])
        return ''.join(result)
    
    def braille_to_english(self):
        result = []
        number_mode = False
        capital_mode = False
        i = 0

        while i < len(self.input_string):
            symbol = self.input_string[i:i+6]

            if symbol == self.cap:
                capital_mode = True
                i+=6
            elif symbol == self.num:
                number_mode = True
                i+=6
            elif symbol == '......':
                number_mode = False
                result.append(self.inverted_letter_map.get(symbol, ''))
                i+=6
            else:
                if number_mode:
                    result.append(self.inverted_number_map.get(symbol, ''))
                else:
                    letter = self.inverted_letter_map.get(symbol, '')
                    
                    if capital_mode:
                        result.append(letter.upper())
                        capital_mode = False
                    else:
                        result.append(letter)
                i+=6
        return ''.join(result)
                
    def translate(self):
        if self.check_type():
            return self.braille_to_english()
        return self.english_to_braille()
    

if __name__ == '__main__':
    import sys
    input_string = ' '.join(sys.argv[1:])
    translator = brailleTranslator(input_string)
    print(translator.translate())