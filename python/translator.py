# Braille to English translator by Massimo Scanga
import sys

# Library of each English letter corresponding to Braille
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', 'cap': '.....O', 'num': '.O.OOO'
}
# Reverse translation Braille to English
english_alphabet = {v: k for k, v in braille_alphabet.items()}

# Function for Eng to Braille
def english_to_braille(text):
    """Translate English to Braille."""
    braille = []
    number_mode = False

    for char in text:
        if char.isupper():  # Handle uppercase letters
            braille.extend([braille_alphabet['cap'], braille_alphabet[char.lower()]])
        elif char.isdigit():  # Handle numbers with number indicator
            braille.append(braille_alphabet['num'] if not number_mode else braille_alphabet[char])
            number_mode = True
        else:  # Handle letters and spaces
            braille.append(braille_alphabet.get(char, '......'))
            number_mode = False

    return ''.join(braille)

# Function for Braille to Eng

# Detect Language input and choose correct translation function
def main():

# Run main function
if __name__ == "__main__":
    main() 