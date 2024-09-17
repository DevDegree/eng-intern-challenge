import sys

class BrailleTranslator:
    def __init__(self):
        self.letters_to_braille = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
            'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
            'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
            'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
            'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
            'y': 'OO.OOO', 'z': 'O..OOO',
        }

        self.numbers_to_braille = {
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
            '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
            '9': '.OO...', '0': '.OOO..',
        }

        self.punctuation_to_braille = {
            '.': '.O..OO', ',': '.O....', '?': '.O.OO.', '!': '.OO.O.', 
            ':': 'OO....', ';': 'O.O...', '-': '......', '/': 'O.O...', 
            '<': 'O..OO.', '>': '.OOO.O', '(': 'OO.OO.', ')': '.OO.OO',
        }

        self.special_symbols = {
            'cap_follows': '.....O', 'num_follows': '.O.OOO', 'dec_follows': '.O...O', ' ': '......',
        }

        # Inverse mappings for braille to english
        self.braille_to_letters = {braille: letter for letter, braille in self.letters_to_braille.items()}
        self.braille_to_numbers = {braille: letter for letter, braille in self.numbers_to_braille.items()}
        self.braille_to_punctuation = {braille: letter for letter, braille in self.punctuation_to_braille.items()}

    def is_braille(self, input: str) -> bool:
        return all(char in 'O.' for char in input) and len(input) % 6 == 0

    def translate_to_braille(self, input: str) -> str:
        result = []
        next_is_num = False
        
        for char in input:
            # Number is found, add braille for number follows
            if char.isdigit() and not next_is_num:
                result.append(self.special_symbols['num_follows'])
                next_is_num = True
            # Space is found, add space
            if char == ' ':
                result.append(self.special_symbols[' '])
                next_is_num = False
            # Uppercase letter
            elif char.isupper():
                result.append(self.special_symbols['cap_follows'])
                result.append(self.letters_to_braille[char.lower()])
            # Number
            elif char.isdigit():
                result.append(self.numbers_to_braille[char])
            # Lowercase letter
            elif char in self.letters_to_braille:
                result.append(self.letters_to_braille[char])
            # Punctuation
            elif char in self.punctuation_to_braille:
                result.append(self.punctuation_to_braille[char])
            # Raising error for unrecognized characters
            else:
                raise ValueError(f"Unrecognized character '{char}' in input.")
                
        return ''.join(result)

    def translate_to_english(self, input: str) -> str:
        result = []
        i = 0
        next_is_cap = False
        next_is_num = False
        
        while i < len(input):
            symbol = input[i:i+6]
            
            if symbol == self.special_symbols['cap_follows']:
                # Next character is a capital
                next_is_cap = True
                i += 6
                continue
            
            if symbol == self.special_symbols['num_follows']:
                # Next character is a number
                next_is_num = True
                i += 6
                continue
            
            if symbol == self.special_symbols[' ']:
                # Character is a space
                result.append(' ')
                next_is_num = False
                next_is_cap = False
                i += 6
                continue
            
            if next_is_num and symbol in self.braille_to_numbers:
                result.append(self.braille_to_numbers[symbol])
            elif symbol in self.braille_to_letters:
                letter = self.braille_to_letters[symbol]
                if next_is_cap:
                    letter = letter.upper()
                    next_is_cap = False
                result.append(letter)
            elif symbol in self.braille_to_punctuation:
                result.append(self.braille_to_punctuation[symbol])
            else:
                raise ValueError(f"Unrecognized Braille symbol '{symbol}' in input.")
            
            i += 6
        
        return ''.join(result)

    def translate(self, input):
        if self.is_braille(input):
            return self.translate_to_english(input)
        else:
            return self.translate_to_braille(input)

def main():
    input = ' '.join(sys.argv[1:])
    braille_translator = BrailleTranslator()
    try:
        output = braille_translator.translate(input)
        print(output)
    except ValueError as e:
        print(f"An error occured: {e}")

if __name__ == '__main__':
    main()