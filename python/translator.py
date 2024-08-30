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
        # '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
        'space': '......',
    }

    # Constants for special indicators
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
        braille_to_num = { v: k for k, v in self.NUM_TO_BRALLIE.items() }
        braille_to_alpha = { v: k for k, v in self.ALPHA_TO_BRALLIE.items() }
        braille_to_special = { v: k for k, v in self.SPECIAL_TO_BRALLIE.items() }

        brailles = [ input[i : i+6] for i in range(0, len(input), 6) ]

        tokens = []

        is_number = False

        # parse
        for braille in brailles:
            if braille in braille_to_special:
                token = braille_to_special[braille]
                tokens.append(token)
                if token == self.NUMBER: is_number = True
                if token == 'space': is_number = False

            else:
                if is_number: tokens.append(braille_to_num[braille])
                else: tokens.append(braille_to_alpha[braille])
        
        # generate
        output = ''
        next_is_capital = False
        for token in tokens:
            if token == self.CAPITAL: next_is_capital = True
            elif token == self.NUMBER: continue
            elif token == self.SPACE:
                output += ' '
            elif next_is_capital:
                output += token.upper()
                next_is_capital = False
            else: output += token

        return output
    
    def english_to_braille(self, input: str) -> str:
        def decode_english(input: str):
            tokens = []
            is_number = False
            for char in input:
                # number
                if char.isdigit():
                    if not is_number:
                        tokens.append(self.NUMBER)
                        is_number = True
                    tokens.append(char)

                # space
                # TODO: check if there is any characters missed
                elif char == ' ':
                    tokens.append(self.SPACE)
                    is_number = False

                # alphabet
                elif char.isalpha():
                    if char.isupper(): tokens.append(self.CAPITAL)
                    tokens.append(char.lower())
                
                # special character
                else: tokens.append(char)
            
            return tokens
        
        # parse english to tokens
        tokens = decode_english(input)

        # translate tokens to braille
        output = self.translate_tokens(tokens, self.ALPHA_TO_BRALLIE, self.NUM_TO_BRALLIE, self.SPECIAL_TO_BRALLIE)

        return output

    def translate_tokens(self, tokens, alphabet1, alphabet2, alphabet3) -> str:
        output = ''
    
        for token in tokens:
            if token in alphabet1: output += alphabet1[token]
            elif token in alphabet2: output += alphabet2[token]
            else: output += alphabet3[token]
        
        return output

def main():
    input = " ".join(sys.argv[1:])
    translator = BrailleTranslator()
    output = translator.translate(input)
    print(output)

    # test cases
    print("test case1: number", translator.translate(translator.translate("2213123")) == "2213123")
    print("test case2: alphabets", translator.translate(translator.translate("adsFasdf")) == "adsFasdf")
    print("test case3: alphabets", translator.translate(translator.translate("a1 b")) == "a1 b")
    print("test case4: alphabets and numbers", translator.translate(translator.translate("dfkladfasd1234567890 cpkldfsaj")) == "dfkladfasd1234567890 cpkldfsaj")
    print("test case5: alphabets and numbers", translator.translate("Abc 123 xYz") == ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")

# TODO: no need to run in infinite loop
if __name__ == "__main__":
    main()

