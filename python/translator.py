import sys
from typing import Dict

class BrailleTranslator:
    ALPHA_TO_BRALLIE: Dict[str, str] = {
        # English characters
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
        'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
        'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
        'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO', 
    }

    # Numbers
    NUM_TO_BRALLIE: Dict[str, str] = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
        '9': '.OO...', '0': '.OOO..',
    }

    # Special Characters
    SPECIAL_TO_BRALLIE: Dict[str, str] = {
        # Follows
        'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO',
        # Special Characters
        '.': '..OO.O', ',':'..O...', '?': '..O.OO', '!': '..OOO.', 
        ':' : '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
        '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
        'space': '......',
    }

    CAPITAL = 'capital'
    NUMBER = 'number'
    DECIMAL = 'decimal'
    SPACE = 'space'
    

    def translate(self, input: str) -> str:
        if self.is_braille(input): return self.braille_to_english(input)
        else: return self.english_to_braille(input)

    def is_braille(self, input: str) -> bool:
        return len(input) % 6 == 0 and set(input).issubset({'O', '.'})
    
    def braille_to_english(self, input: str) -> str:
        # TODO: change to build when needed
        braille_to_num = { v: k for k, v in self.NUM_TO_BRALLIE }
        braille_to_alpha = { v: k for k, v in self.ALPHA_TO_BRALLIE }
        braille_to_special = { v: k for k, v in self.SPECIAL_TO_BRALLIE }

        brailles = [ input[i : i+6] for i in range(0, len(input), 6) ]

        tokens = []

        is_number = False

        for braille in brailles:
            if braille in braille_to_special:
                token = braille_to_special[braille]
                tokens.append(token)
                if token == " ": is_number = False

            else:
                if is_number: tokens.append(braille_to_num[braille])
                else: tokens.append(braille_to_alpha[braille])
        
        return ''.join(tokens)
    
    def english_to_braille(self, input: str) -> str:
        # TODO: change to build when needed
        brallie_alphabet = self.ALPHA_TO_BRALLIE + self.NUM_TO_BRALLIE + self.SPECIAL_TO_BRALLIE
        def decode_english(input: str):
            tokens = []
            has_starting_number = False
            for char in input:
                # number
                if char.is_digit():
                    if not has_starting_number:
                        tokens.append(self.NUMBER)
                        has_starting_number = True
                    tokens.append(char)

                # space
                # TODO: check if there is any characters missed
                elif char == '':
                    tokens.append(self.SPACE)
                    has_starting_number = False

                # alphabet
                elif char.is_alpha():
                    if char.is_upper():
                        tokens.append(self.CAPITAL)
                    tokens.append(char.lower())
                
                # special character
                else:
                    tokens.appned(char)
            return tokens
                        
        tokens = decode_english(input)
        output = ''.join([brallie_alphabet[token] for token in tokens])

        return output


def main():
    input: str = " ".join(sys.argv[1:])
    
    return

if __name__ == "__main__":
    main()