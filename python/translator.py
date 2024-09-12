import sys

class Translator:
    # Braille Patterns
    english_chars_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
    ':': '..OO..', ';': '..O.O.', '-': '..O..O', '/': '..O..O', '<': '..O.O.',
    '>': '..OO.O', '(': '..OO..', ')': '..OO..', ' ': '......',
        'capital': '.....O', 'number': '.O.OOO', 'decimal': '.O...O'
    }

    # Braille Patterns
    english_numbers_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '...O.O', ' ': '......'
}


    # Decode Braille
    braille_to_english_chars     = {braille_char: english_char for english_char, braille_char in english_chars_to_braille.items()}
    braille_to_english_numbers  = {braille_char: number_char for number_char, braille_char in english_numbers_to_braille.items()}


    def translate_braille_to_english(self,input_string):
        english_char_list = []
        braille_chars = [input_string[i:i+6] for i in range(0, len(input_string), 6)]
        capitalize_next = False
        number_mode = False
        decimal_mode = False

        
        for char in braille_chars:
            if char == self.english_chars_to_braille['capital']:
                capitalize_next = True
            elif char == self.english_chars_to_braille['number']:
                number_mode = True
            elif char == self.english_chars_to_braille['decimal']:
                decimal_mode = True
                english_char_list.append('.')
            else:
                if number_mode or decimal_mode:
                    char = self.braille_to_english_numbers.get(char, '')
                    if char in '0123456789':
                        english_char_list.append(char)
                    elif char == ' ':
                        number_mode = decimal_mode = False
                        english_char_list.append(' ')
                else:
                    char = self.braille_to_english_chars.get(char, '')
                    if char:
                        if capitalize_next:
                            char = char.upper()
                            capitalize_next = False
                        english_char_list.append(char)

        return ''.join(english_char_list)


    def translate_english_to_braille(self,input_string):
        braille_char_list = []
        number_mode = False
        decimal_mode = False

        for char in input_string:
            if char.isalpha():
                if number_mode or decimal_mode:
                    number_mode = decimal_mode = False
                if char.isupper():
                    braille_char_list.append(self.english_chars_to_braille['capital'])
                braille_char_list.append(self.english_chars_to_braille[char.lower()])
            elif char.isdigit():
                if not number_mode and not decimal_mode:
                    braille_char_list.append(self.english_chars_to_braille['number'])
                    number_mode = True
                braille_char_list.append(self.english_numbers_to_braille[char])
            elif char == '.':
                if number_mode:
                    braille_char_list.append(self.english_chars_to_braille['decimal'])
                    decimal_mode = True
                    number_mode = False
                else:
                    braille_char_list.append(self.english_chars_to_braille['.'])
            else:
                number_mode = decimal_mode = False
                braille_char_list.append(self.english_chars_to_braille.get(char, '......'))

        return ''.join(braille_char_list)
        


    def check_is_braille(self,input_string):
        for char in input_string:
            if char not in 'O.':
                return False
        return True



def main():
    translator = Translator()
    if len(sys.argv) < 2:
        sys.exit(1)

    input_str = ""
    ans = ""
    if(len(sys.argv) > 1):
        input_str = ' '.join(c for c in sys.argv[1:])

    if(translator.check_is_braille(input_str)):
        if(len(input_str) % 6 != 0):
            print("Invalid input")
            sys.exit(1)
        ans = translator.translate_braille_to_english(input_str)
    else:
        ans = translator.translate_english_to_braille(input_str)

    print(ans)

if __name__ == "__main__":
    main()