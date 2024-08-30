import sys
from typing import Dict, List, Literal

"""
Assumptions
1. Input arguments are in either English or Braille, not both.
2. English inputs have only characters, numbers and spaces.
3. Only numbers are present until the next space occurs.
4. All Braille inputs are valid
Correction
input : .....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..
output: Abc 234
"""

class BrailleTranslator:
    # Constants for special indicators
    CAPITAL = 'capital'
    NUMBER = 'number'
    DECIMAL = 'decimal'
    SPACE = 'space'
    DOT = '.'
    RAISED_DOT = 'O'

    # English characters
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
        CAPITAL: '.....O', DECIMAL: '.O...O', NUMBER: '.O.OOO',
        # Special Characters
        '.': '..OO.O', ',':'..O...', '?': '..O.OO', '!': '..OOO.', 
        ':' : '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
        SPACE: '......',
        # these characters are not required in this challenge, ref: https://github.com/DevDegree/eng-intern-challenge/issues/3#issuecomment-2320788869
        # '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    }

    # English to braille alphabet
    BRAILLE_TO_ALPHA: Dict[str, str] = {}
    BRAILLE_TO_NUM: Dict[str, str] = {}
    BRAILLE_TO_SPECIAL: Dict[str, str] = {}
    

    def translate(self, input: str) -> str:
        if self._is_braille(input): return self.braille_to_english(input)
        else: return self.english_to_braille(input)

    def _is_braille(self, input: str) -> bool:
        return len(input) % 6 == 0 and set(input).issubset({self.RAISED_DOT, self.DOT})
    
    def _build_braille_to_english_table(self):
        self.BRAILLE_TO_ALPHA = { v: k for k, v in self.ALPHA_TO_BRALLIE.items() }
        self.BRAILLE_TO_NUM = { v: k for k, v in self.NUM_TO_BRALLIE.items() }
        self.BRAILLE_TO_SPECIAL = { v: k for k, v in self.SPECIAL_TO_BRALLIE.items() }
    
    def generate_from(self, tokens: List[str], target: Literal['english', 'braille']) -> str:
        output = ''
        if target == 'english':
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
        else:
            # target is braille
            for token in tokens:
                if token in self.ALPHA_TO_BRALLIE: output += self.ALPHA_TO_BRALLIE[token]
                elif token in self.NUM_TO_BRALLIE: output += self.NUM_TO_BRALLIE[token]
                else: output += self.SPECIAL_TO_BRALLIE[token]
        
        return output

    
    def braille_to_english(self, input: str) -> str:
        # Initialize braille to english table if needed
        if not self.BRAILLE_TO_ALPHA:
            self._build_braille_to_english_table()

        def parse(input: str) -> List[str]:
            tokens = []
            is_number = False
            brailles = [ input[i : i+6] for i in range(0, len(input), 6) ]

            for braille in brailles:
                if braille in self.BRAILLE_TO_SPECIAL:
                    token = self.BRAILLE_TO_SPECIAL[braille]
                    tokens.append(token)
                    if token == self.NUMBER: is_number = True
                    if token == self.SPACE: is_number = False
                else:
                    if is_number: tokens.append(self.BRAILLE_TO_NUM[braille])
                    else: tokens.append(self.BRAILLE_TO_ALPHA[braille])
            return tokens            
        
        # parse braille to tokens
        tokens = parse(input)

        # generate english from tokens
        output = self.generate_from(tokens, target='english')
        return output
    
    def english_to_braille(self, input: str) -> str:
        def parse(input: str) -> List[str]:
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
                elif char == ' ':
                    tokens.append(self.SPACE)
                    is_number = False

                # alphabet
                elif char.isalpha():
                    if char.isupper(): tokens.append(self.CAPITAL)
                    tokens.append(char.lower())
                
                # other special character
                else: tokens.append(char)
            
            return tokens
        
        # parse english to tokens
        tokens = parse(input)

        # generate braille from tokens
        output = self.generate_from(tokens, target='braille')
        return output
    


def main():
    # read input
    input = " ".join(sys.argv[1:])
    translator = BrailleTranslator()
    try:
        output = translator.translate(input)
        print(output)
    except Exception as e:
        print("An error occured during the translation, please ensure the input is valid")
        print(e)

    # # test cases
    # # test case1: number
    # assert(translator.translate(translator.translate("2213123")) == "2213123")
    # # test case2: alphabets
    # assert(translator.translate(translator.translate("adsFasdf")) == "adsFasdf")
    # # test case3: alphabets with numbers
    # assert(translator.translate(translator.translate("a1 b")) == "a1 b")
    # # test case4: alphabets with numbers complex
    # assert(translator.translate(translator.translate("dfkladfasdS1234567890 cpkldfsaj")) == "dfkladfasdS1234567890 cpkldfsaj")
    # # test case5: alphabets with numbers
    # assert(translator.translate("Abc 123 xYz") == ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")
    # # test case6: alphabets and numbers with other characters
    # assert(translator.translate(translator.translate("dfkladfasd1234567890 cpkldfsJj;")) == "dfkladfasd1234567890 cpkldfsJj;")
    # # test case7: english input but looks like braille
    # assert(translator.translate(translator.translate("O......")) == "O......")

if __name__ == "__main__":
    main()

