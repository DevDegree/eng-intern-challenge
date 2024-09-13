import sys

class Translator:
    def __init__(self):
        self.braille_to_english_letters = {
            'O.....': 'a', 
            'O.O...': 'b',
            'OO....': 'c',
            'OO.O..': 'd',
            'O..O..': 'e',
            'OOO...': 'f',
            'OOOO..': 'g',
            'O.OO..': 'h',
            '.OO...': 'i', 
            '.OOO..': 'j',
            'O...O.': 'k', 
            'O.O.O.': 'l', 
            'OO..O.': 'm', 
            'OO.OO.': 'n', 
            'O..OO.': 'o',
            'OOO.O.': 'p', 
            'OOOOO.': 'q', 
            'O.OOO.': 'r', 
            '.OO.O.': 's', 
            '.OOOO.': 't',
            'O...OO': 'u', 
            'O.O.OO': 'v', 
            '.OOO.O': 'w', 
            'OO..OO': 'x', 
            'OO.OOO': 'y', 
            'O..OOO': 'z',
        }

        self.braille_special_characters = {
            '.....O': 'capital_follows',
            '.O...O': 'decimal_follows',
            '.O.OOO': 'number_follows',
            '......': 'space',
            '..O...': ',', 
            '..OO.O': '.', 
            '..O.OO': '?', 
            '..OOO..': '!', 
            '..OO..': ':', 
            '..O.O.': ';', 
            'O.O..O': '(', 
            '.O.OO.': ')', 
            '....OO': '-', 
            '.O..O.': '/',
            '.OO..O': '<', 
            'O..OO.': '>', 
        }

        self.braille_to_english_digits = {
            'O.....': '1', 
            'O.O...': '2', 
            'OO....': '3', 
            'OO.O..': '4', 
            'O..O..': '5',
            'OOO...': '6', 
            'OOOO..': '7', 
            'O.OO..': '8', 
            '.OO...': '9', 
            '.OOO..': '0',
        }
        
        self.english_to_braille_letters = {v: k for k, v in self.braille_to_english_letters.items()}
        self.english_special_characters = {v: k for k, v in self.braille_special_characters.items()}
        self.english_to_braille_digits = {v: k for k, v in self.braille_to_english_digits.items()}
        
    def is_braille(self, s):
        if len(s) < 6:
            return False

        return set(s) == set(['O', '.'])

    def braille_to_english(self, s):
        is_number = False
        is_capital = False
        result = []
        for i in range(0, len(s), 6):
            char = s[i:i+6]
            if char in self.braille_special_characters:
                if self.braille_special_characters[char] == 'capital_follows':
                    is_capital = True
                elif self.braille_special_characters[char] == 'number_follows':
                    is_number = True
                elif self.braille_special_characters[char] == 'decimal_follows':
                    result.append('.')
                elif self.braille_special_characters[char] == 'space':
                    result.append(' ')
                    is_number = False

            elif is_number: 
                result.append(self.braille_to_english_digits.get(char, ''))
            
            elif is_capital:
                result.append(self.braille_to_english_letters.get(char, '').upper())
                is_capital = False
            
            else:
                result.append(self.braille_to_english_letters.get(char, ''))

        return ''.join(result)

    def english_to_braille(self, s):
        result = ''
        previous_digit = False

        for char in s:
            #lower case
            if 'a' <= char <= 'z':
                braille = self.english_to_braille_letters[char]
                result += braille
                previous_digit = False

            # upper case
            elif 'A' <= char <= 'Z':
                result += self.english_special_characters['capital_follows']
                braille = self.english_to_braille_letters[char.lower()]
                result += braille
                previous_digit = False

            # digits
            elif char.isdigit():
                if not previous_digit:
                    result += self.english_special_characters['number_follows']
                    previous_digit = True

                braille = self.english_to_braille_digits[char]
                result += braille
                previous_digit = True
                
            # space
            elif char == ' ':
                result += self.english_special_characters['space']
                previous_digit = False
                
            elif previous_digit and char == '.':
                result += self.english_special_characters['decimal_follows']
                previous_digit = False
                
            # special characters
            else:
                result += self.english_special_characters[char]
                previous_digit = False

        return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text>")
        sys.exit(1)

    translator = Translator()
    text = ' '.join(sys.argv[1:])
    if translator.is_braille(text):
        print(translator.braille_to_english(text))
    else:
        print(translator.english_to_braille(text))

if __name__ == '__main__':
    main()