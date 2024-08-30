import sys

class EnglishBrailleTranslator:
    def __init__(self) -> None:
        self.letter_to_braille = {
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
            'z': 'O..OOO'
        }
        self.braille_to_letter = {v: k for k, v in self.letter_to_braille.items()}

        self.digit_to_braille = {
            '1': 'O.....',
            '2': 'O.O...',
            '3': 'OO....',
            '4': 'OO.O..',
            '5': 'O..O..',
            '6': 'OOO...',
            '7': 'OOOO..',
            '8': 'O.OO..',
            '9': '.OO...',
            '0': '.OOO..'
        }
        self.braille_to_digit = {v: k for k, v in self.digit_to_braille.items()}

        self.space_braille = '......'
        self.capital_follows_braille = '.....O'
        self.number_follows_braille = '.O.OOO'
    
    def translate(self, text):
        if all(c in {'O', '.', ' '} for c in text):
            return self.braille_to_english(text)
        return self.english_to_braille(text)

    def english_to_braille(self, english_text):
        braille_text = ''
        is_number = False
        
        for c in english_text:
            if c.isalpha():
                if c.isupper():
                    braille_text += self.capital_follows_braille + self.letter_to_braille[c.lower()]
                else:
                    braille_text += self.letter_to_braille[c]
            elif c.isdigit():
                if not is_number:
                    braille_text += self.number_follows_braille 
                    is_number = True
                braille_text += self.digit_to_braille[c]
            elif c == ' ':
                braille_text += self.space_braille
                is_number = False  

        return braille_text

    def braille_to_english(self, braille_text):
        english_text = ''
        i = 0
        is_number = False

        while i < len(braille_text):
            braille_code = braille_text[i: i + 6]

            if braille_code == self.number_follows_braille:
                is_number = True 
                i += 6
                continue
            elif braille_code == self.capital_follows_braille:
                i += 6
                braille_code = braille_text[i: i + 6]
                english_text += self.braille_to_letter[braille_code].upper()
            elif braille_code == self.space_braille:
                english_text += ' '
                is_number = False 
            else:
                if is_number:
                    english_text += self.braille_to_digit[braille_code]
                else:
                    english_text += self.braille_to_letter[braille_code]
            i += 6

        return english_text

def main() -> None:
    translator = EnglishBrailleTranslator()
    input_text = " ".join(sys.argv[1:])  
    print(translator.translate(input_text))

if __name__ == "__main__":
   main()
