# Author: Adam Stolnits
# Purpose: To create a translator script that can translate English to Braille & Braille to English.
# Date: September 26th, 2024
class BrailleTranslator:

    # The following is a hash map that translates each english character and symbol to Braille.
    BRAILLE_HASH_MAP = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
        'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
        ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', 
        '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......', 'capital': '.....O',
        'number': '.O.OOO'
    }

    # The following is a hash map that translates each english number to Braille.
    BRAILLE_NUMBER_HASH_MAP = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }

    REVERSE_BRAILLE_MAP = {v: k for k, v in BRAILLE_HASH_MAP.items()} # Braille Hash Map but key values are swapped.
    REVERSE_BRAILLE_NUMBER_MAP = {v: k for k, v in BRAILLE_NUMBER_HASH_MAP.items()} # Braille Number Hash Map but key values are swapped.

    # English to Braille.
    def translate_english_to_braille(self, input_str): 
        result = []
        number = False
        for char in input_str:

            # If capital
            if char.isupper():
                result.append(self.BRAILLE_HASH_MAP['capital'])
                char = char.lower()

            # If digit
            if char.isdigit() and number == False:
                result.append(self.BRAILLE_HASH_MAP['number'])
                number = True
            
            # Adds chunk if character is in map
            if char in self.BRAILLE_HASH_MAP:
                result.append(self.BRAILLE_HASH_MAP[char])
            elif char in self.BRAILLE_NUMBER_HASH_MAP:
                result.append(self.BRAILLE_NUMBER_HASH_MAP[char])

        return ''.join(result)

    # Braille to English.
    def translate_braille_to_english(self, braille_str):
        result = []
        capital = False
        number = False
        i = 0
        while i < len(braille_str):

            chunk = braille_str[i:i+6] # Counts string in chunks of 6s

            # If capital follows is found
            if chunk == self.BRAILLE_HASH_MAP['capital']: 
                capital = True
                i += 6
                continue

            # If number follows is found
            elif chunk == self.BRAILLE_HASH_MAP['number']:
                number = True
                i += 6
                continue

            # Appends translation
            elif chunk in self.REVERSE_BRAILLE_MAP:
                char = self.REVERSE_BRAILLE_MAP[chunk]
                if capital:
                    char = char.upper()
                    capital = False
                elif number:
                    char = self.REVERSE_BRAILLE_NUMBER_MAP[chunk]
                result.append(char)
            i += 6

        return ''.join(result)

    # Check if input is Braille or English.
    def is_braille(self, input_str):
        return all(char in "O." for char in input_str)

    # Determines which translation method to use based on input type.
    def translate(self, input_str):
        if self.is_braille(input_str):
            return self.translate_braille_to_english(input_str)
        else:
            return self.translate_english_to_braille(input_str)


if __name__ == "__main__":

    import sys
    translator = BrailleTranslator()
    input_str = ' '.join(sys.argv[1:]) # Takes all words in input when calling script
    print(translator.translate(input_str))
