# Python submission of shopify OA
# Assuming all inputs valid -> not including error handling

import sys

class BrailleTranslator:
    # since the numbers are equal to the first 10 letters of the alphabet, automatically convert
    # using ascii values rather than hardcoding as well
    braille_map = {
        "a": "O.....",
        "b": "O.O...",
        "c": "OO....",
        "d": "OO.O..",
        "e": "O..O..",
        "f": "OOO...",
        "g": "OOOO..",
        "h": "O.OO..",
        "i": ".OO...",
        "j": ".OOO..",
        "k": "O...O.",
        "l": "O.O.O.",
        "m": "OO..O.",
        "n": "OO.OO.",
        "o": "O..OO.",
        "p": "OOO.O.",
        "q": "OOOOO.",
        "r": "O.OOO.",
        "s": ".OO.O.",
        "t": ".OOOO.",
        "u": "O...OO",
        "v": "O.O.OO",
        "w": ".OOO.O",
        "x": "OO..OO",
        "y": "OO.OOO",
        "z": "O..OOO",
        "cap": ".....O",
        "num": ".O.OOO",
        " ": "......",
    }

    # populated as the inverse of braille_map in __init__
    character_map = {}

    def __init__(self):
        # make the inverse of the braille_map for decoding
        for key in self.braille_map:
            self.character_map[self.braille_map[key]] = key

        # add characters 1~9 using a~i and hardcode 0 using 10
        for i in range(1, 10):
            self.braille_map[str(i)] = self.braille_map[chr(ord('a') + i-1)]
        self.braille_map["0"] = self.braille_map[chr(ord('a') + 10)]

    # according to the challenge guidelines, the encoder is incapable of encoding number->character strings without spaces
    # IE 123abc
    # not accounting for that edge case here since it's implied to be impossible
    # encodes from plaintext to braille string
    def encode_braille(self, input):
        output = ""
        is_number = False # only add the number modifier on the first digit
        for c in input:
            if c.isupper():
                output += self.braille_map['cap']
                c=c.lower()
            elif c.isnumeric():
                if not is_number:
                    is_number = True
                    output += self.braille_map['num']

            if c == " ":
                is_number = False # reset number modifier on space

            output += self.braille_map[c]
        return output

    #decodes braille string to plaintext
    def decode_braille(self, input):
        output = ""
        is_cap = False
        is_num = False
        for i in range(0, len(input), 6):
            braille_char = input[i:i+6]
            char = self.character_map[braille_char]

            
            if char == "cap": # apply modifiers if needed
                is_cap = True
            elif char == "num":
                is_num = True
            else:
                if is_cap: # modify output using modifiers if needed
                    output += char.upper()
                    is_cap = False # capitalization modifier resets after each character
                elif is_num:
                    output += self._char_to_num(char)
                else:
                    output += char # add directly to output if no modifiers

            if (char == " "): # reset number modifier on space
                is_num = False
        return output

    # converts the a~j to 1~0 since they share the same braille encoding
    def _char_to_num(self, char):
        if char == 'j':
            return '0'
        return str(ord(char) - ord('a') + 1)



if __name__ == "__main__":
    input = " ".join(sys.argv[1:]) # parse input from args

    # join the arguments without spaces to see if it's plaintext (alphanumeric) or encoded braille
    is_plaintext = "".join(sys.argv[1:]).isalnum()

    translator = BrailleTranslator()

    if is_plaintext:
        print(translator.encode_braille(input))
    else:
        print(translator.decode_braille(input))
