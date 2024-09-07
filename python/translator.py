import sys

# Braille alphabet
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO', ' ': '......'
}

# Reverse dictionary for Braille to English
braille_to_english = {v: k for k, v in braille_alphabet.items()}

# Check whether the input is Braille or English
def is_braille(input_string):
    return all(char in 'O. ' for char in input_string)

# Translate English to Braille
def translate_to_braille(text):
    braille_output = ""
    number_mode = False
    
    for char in text:
        if char.isdigit() and not number_mode:
            braille_output += braille_alphabet['number']
            number_mode = True

        if char.isalpha() and number_mode:
            number_mode = False

        if char.isupper():
            braille_output += braille_alphabet['capital']
            braille_output += braille_alphabet[char.lower()]
        elif char.isdigit() or char in braille_alphabet:
            braille_output += braille_alphabet[char.lower()]
        else:
            braille_output += braille_alphabet[' ']

    return braille_output

# Translate Braille to English
def translate_to_english(braille):
    english_output = ""
    result = []
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]

    capital_mode = False
    number_mode = False

    
    for char in braille_chars:
        if char == braille_alphabet['capital']:
            capital_mode = True
            continue
        if char == braille_alphabet['number']:
            number_mode = True
            continue

        if char in braille_to_english:
            english_char = braille_to_english[char]
            if number_mode and english_char.isdigit():
                result.append(english_char)
            elif number_mode and english_char.isalpha():
                number_mode = False
                result.append(english_char)
            elif capital_mode:
                result.append(english_char.upper())
                capital_mode = False
            else:
                result.append(english_char)
            

    english_output = ''.join(result)
    
    return english_output

# Function to handle input and output
if __name__ == "__main__":

    # Get input
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        # If input is Braille, translate to English
        print(translate_to_english(input_text))
    else:
        # If input is English, translate to Braille
        print(translate_to_braille(input_text))



