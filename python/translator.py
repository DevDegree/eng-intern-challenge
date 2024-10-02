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

# English to Braille
def english_to_braille(text):
    """Translate English to Braille."""
    braille = []
    number_mode = False

    for char in text:
        if char.isupper():  # Handle uppercase letters
            braille.extend([braille_alphabet['cap'], braille_alphabet[char.lower()]])
        elif char.isdigit():  # Handle numbers with number indicator
            if not number_mode:
                braille.append(braille_alphabet['num'])
                number_mode = True
            braille.append(braille_alphabet[char])
        else:  # Handle letters and spaces
            braille.append(braille_alphabet.get(char, '......'))
            number_mode = False  # Reset number mode after non-digit characters

    return ''.join(braille)

# Braille to English
def braille_to_english(braille):
    """Translate Braille to English."""
    english = []
    number_mode = False
    capitalize_next = False

    for i in range(0, len(braille), 6):  # Process 6-character chunks
        char = braille[i:i+6]

        if char == braille_alphabet['cap']:  # Capital letter indicator
            capitalize_next = True
        elif char == braille_alphabet['num']:  # Number indicator
            number_mode = True
        elif char == braille_alphabet[' ']:  # Space
            english.append(' ')
            number_mode = False  # Reset number mode after space
        else:
            letter = english_alphabet.get(char, '')  # Map Braille to English
            
            # Handle capitalization
            if capitalize_next:
                letter = letter.upper()
                capitalize_next = False
            
            # Handle number mode
            if number_mode:
                if letter.isdigit():
                    english.append(letter)
                else:
                    # If it's not a digit, reset number mode
                    number_mode = False
                    english.append(letter)
            else:
                english.append(letter)

            # Reset number mode after letters or spaces
            if not letter.isdigit() and letter != '':
                number_mode = False

    return ''.join(english)

# Main function for input detection and processing
def main():
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        is_braille = all(c in ['O', '.'] for c in input_text)  # Check if input is Braille
        # Translate accordingly
        print(braille_to_english(input_text) if is_braille else english_to_braille(input_text))

# Execute main function
if __name__ == "__main__":
    main()