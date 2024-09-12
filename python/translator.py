# Braille representations using 'O' for raised dots and '.' for flat dots
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO'
}

# Reverse mapping from Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# function to detect if input is Braille or English and translate accordingly
def detect_and_translate(input_string):
    # Detect if input is Braille or English based on presence of 'O' and '.' or normal letters/numbers
    if all(c in 'O.' for c in input_string):
        # translate input to English
        return "English"
    else:
        # translate input to Braille
        return "Braille"

if __name__ == "__main__":
    # Take the input from the command line arguments
    input_text = input("Enter the text you want to translate (English or Braille): ")
    output_text = detect_and_translate(input_text)
    print(output_text)