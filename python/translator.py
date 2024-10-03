import sys

class BrailleTranslator:
    def __init__(self):
        self.english_to_braille = {
            'a': 'O.....',  'b': 'O.O...',  'c': 'OO....',  'd': 'OO.O..',
            'e': 'O..O..',  'f': 'OOO...',  'g': 'OOOO..',  'h': 'O.OO..',
            'i': '.OO...',  'j': '.OOO..',  'k': 'O...O.',  'l': 'O.O.O.',
            'm': 'OO..O.',  'n': 'OO.OO.',  'o': 'O..OO.',  'p': 'OOO.O.',
            'q': 'OOOOO.',  'r': 'O.OOO.',  's': '.OO.O.',  't': '.OOOO.',
            'u': 'O...OO',  'v': 'O.O.OO',  'w': '.OOO.O',  'x': 'OO..OO',
            'y': 'OO.OOO',  'z': 'O..OOO',  ' ': '......',
        }

        self.capital_follows = '.....O'
        self.number_follows = '.O.OOO'

        self.braille_to_english = {s: t for t, s in self.english_to_braille.items()}

        self.number_mapping = {
            'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
            'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
        }
    

    def is_braille(self, text):
        return len(text) % 6 == 0 and all(char in 'O.' for char in text) 
    

    def convert_english_to_braille(self, text):
        result = []
        number_mode = False
        
        for char in text:
            if char.isdigit():
                if not number_mode:
                    result.append(self.number_follows)
                    number_mode = True
                # Find the letter that corresponds to this number
                letter = [k for k, v in self.number_mapping.items() if v == char][0]
                result.append(self.english_to_braille[letter])
            else:
                if number_mode and char == ' ':
                    number_mode = False
                elif number_mode and not char.isdigit():
                    number_mode = False
                
                if char.isupper():
                    result.append(self.capital_follows)
                    result.append(self.english_to_braille[char.lower()])
                else:
                    result.append(self.english_to_braille[char.lower()])
        
        return ''.join(result)
    

    def convert_braille_to_english(self, text):
        result = []
        chunks = [text[i:i+6] for i in range(0, len(text), 6)]
        i = 0
        number_mode = False
        
        while i < len(chunks):
            chunk = chunks[i]
            
            if chunk == self.number_follows:
                number_mode = True
                i += 1
                continue
            
            if chunk == self.capital_follows:
                next_char = self.braille_to_english[chunks[i+1]]
                if number_mode:
                    result.append(self.number_mapping[next_char])
                else:
                    result.append(next_char.upper())
                i += 2
                continue
            
            char = self.braille_to_english[chunk]
            if number_mode and char != ' ':
                result.append(self.number_mapping[char])
            else:
                if char == ' ':
                    number_mode = False
                result.append(char)
            i += 1
        
        return ''.join(result)
    

    def translate(self, text):
        if self.is_braille(text):
            return self.convert_braille_to_english(text)
        else:
            return self.convert_english_to_braille(text)
        
    
def main():
    input_text = ' '.join(sys.argv[1:])
    translator = BrailleTranslator()
    result = translator.translate(input_text)
    print(result)


if __name__ == "__main__":
    main()
    
