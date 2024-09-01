# Author: Farhan Rehman

# Import libraries
import sys

# Class to translate English to Braille and Braille to English
class BrailleTranslator:
    ##### CONSTANTS #####
    # Braille dictionary for letters, capital letters, numbers, and space
    letters_to_braille = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO'
    }

    numbers_to_braille = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }

    capital_follows = '.....O'
    number_follows = '.O.OOO'
    space = '......'

    # Reverse dictionary for Braille to English translation
    braille_to_english = {v: k for k, v in letters_to_braille.items()}
    braille_to_numbers = {v: k for k, v in numbers_to_braille.items()}


    ##### METHODS #####
    def is_braille(self, text):
        """Check if text is in Braille."""
        return all(c in 'O. ' for c in text)

    def to_english(self, text):
        """Translate Braille to English."""
        number = False
        capital = False
        chars = [text[i: i + 6] for i in range(0, len(text), 6)]
        string = ""

        for char in chars:
            if char == self.space:
                number = False
                string += " "
            elif char == self.number_follows:
                number = True
            elif number:
                string += self.braille_to_numbers[char]
            elif char == self.capital_follows:
                capital = True
            elif char in self.braille_to_english:
                if capital:
                    capital = False
                    string += self.braille_to_english[char].upper()
                else:
                    string += self.braille_to_english[char]

        return string

    def to_braille(self, text):
        """Translate English to Braille."""
        number = False
        string = ""

        for char in text:
            if char == ' ':
                number = False
                string += self.space
            elif number:
                string += self.numbers_to_braille[char]
            elif char.isupper():
                string += self.capital_follows
                string += self.letters_to_braille[char.lower()]
            elif char.isdigit():
                number = True
                string += self.number_follows
                string += self.numbers_to_braille[char]
            elif char in self.letters_to_braille:
                string += self.letters_to_braille[char]

        return string

    ##### MAIN #####
    def main(self):
        if len(sys.argv) > 1:
            input_str = ' '.join(sys.argv[1:])

            if self.is_braille(input_str):
                print(self.to_english(input_str))
            else:
                print(self.to_braille(input_str))
        else:
            print("Incorrect Command Entered")

# Run the program
if __name__ == '__main__':
    translator = BrailleTranslator()
    translator.main()
