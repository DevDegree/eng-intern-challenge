import sys

class BrailleTranslator:
    # constants representing special braille patterns
    BRAILLE_CAPITAL_FOLLOWS = '.....O'
    BRAILLE_DECIMAL_FOLLOWS = '.0...0'
    BRAILLE_NUMBER_FOLLOWS = '.O.OOO'
    BRAILLE_SPACE = '......'

    # mapping english letters to their braille representations
    BRAILLE_LETTER_MAP = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
        'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
        'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
        'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
        'y': 'OO.OOO', 'z': 'O..OOO'
    }

    # mapping numbers to their braille representations
    BRAILLE_NUMBER_MAP = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
        '9': '.OO...', '0': '.OOO..'
    }

    # mapping braille letter representations to english letters by reversing above dictionary
    ENGLISH_LETTER_MAP = {val: key for key, val in BRAILLE_LETTER_MAP.items()}

     # mapping braille number representations to numbers by reversing above dictionary
    ENGLISH_NUMBER_MAP = {val: key for key, val in BRAILLE_NUMBER_MAP.items()}

    def __init__(self, user_input):
        # initialize with user input and determine if it is braille (else english)
        self.user_input = user_input
        self.is_braille_input = self.is_braille(user_input)

    def is_braille(self, user_input):
        # check if the input consists only of braille characters (O and .)
        braille_characters = {'O', '.'}
        return all(char in braille_characters for char in user_input)

    def translate(self):
        # choose translator based on whether input is braille or english
        if self.is_braille_input:
            return self.braille_to_english_translator()
        return self.english_to_braille_translator()

    def english_to_braille_translator(self):
        # translate english text to braille representation
        braille_translation = []
        number_follows = False  # flag to track if the previous character was a number

        for char in self.user_input:
            if char.isalpha():
                # if the character is a letter, check if we need to separate from a number
                if number_follows:
                    braille_translation.append(self.BRAILLE_SPACE)  # add space before letters if needed
                    number_follows = False 
                # if the letter is uppercase, add the capital indicator
                if char.isupper():
                    braille_translation.append(self.BRAILLE_CAPITAL_FOLLOWS)
                # add the braille representation of the lowercase letter
                braille_translation.append(self.BRAILLE_LETTER_MAP[char.lower()])
            elif char.isdigit():
                # if the character is a digit, check if we need to indicate a number context
                if not number_follows:
                    braille_translation.append(self.BRAILLE_NUMBER_FOLLOWS)  # mark the start of a number
                    number_follows = True
                # add the braille representation of the digit
                braille_translation.append(self.BRAILLE_NUMBER_MAP[char])
            elif char == ' ':
                # if the character is a space, add the braille space representation
                braille_translation.append(self.BRAILLE_SPACE)
                number_follows = False

        return ''.join(braille_translation)


    def braille_to_english_translator(self):
        # translate braille representation back to english text
        english_translation = []
        number_follows = False  # flag to track if numbers are being translated

        for i in range(0, len(self.user_input), 6):
            braille_symbol = self.user_input[i:i + 6]

            if braille_symbol == self.BRAILLE_CAPITAL_FOLLOWS:
                # process capital letters in braille
                i += 6 
                next_braille_symbol = self.user_input[i:i + 6]
                if next_braille_symbol in self.ENGLISH_LETTER_MAP:
                    english_translation.append(self.ENGLISH_LETTER_MAP[next_braille_symbol].upper())
            elif braille_symbol == self.BRAILLE_NUMBER_FOLLOWS:
                # set flag to indicate that numbers are expected next
                number_follows = True
            elif braille_symbol == self.BRAILLE_SPACE:
                # append a space for braille space
                english_translation.append(' ')
                number_follows = False
            elif number_follows and braille_symbol in self.ENGLISH_NUMBER_MAP:
                # translate braille number to number
                english_translation.append(self.ENGLISH_NUMBER_MAP[braille_symbol])
            elif not number_follows and braille_symbol in self.ENGLISH_LETTER_MAP:
                # translate braille letter to english letter
                english_translation.append(self.ENGLISH_LETTER_MAP[braille_symbol])

        return ''.join(english_translation)

def main():
    # gather user input from command line arguments
    user_input = ' '.join(sys.argv[1:])
    translator = BrailleTranslator(user_input)

    # perform translation
    result = translator.translate()
    print(result) 

if __name__ == "__main__":
    main() 

