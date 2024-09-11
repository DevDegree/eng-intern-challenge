import sys

# Dictionary for English to Braille translation (letters and space)
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
}

# Dictionary for Braille to English translation (numbers)
braille_to_number = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}
# Dictionary for English to Braille translation (numbers)
number_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Dictionary for Braille to English translation (letters)
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
}

# Special Braille symbols for capitalization and numbers
capital_braille = '.....O'
number_braille = '.O.OOO'

# Fuction to translate from English to Braille
def to_braille(text):
    braille_output = []
    number_mode = False

    for char in text:
        # Check if the character is a digit
        if char.isdigit():
            if not number_mode:
                braille_output.append(number_braille)  # Activate number mode
                number_mode = True

            # Append the Braille representation of the digit directly
            braille_output.append(number_to_braille[char])
        else:
            if number_mode:
                number_mode = False  # Deactivate number mode

            if char.isupper():
                braille_output.append(capital_braille)  # Add capitalization symbol
                char = char.lower()  # Convert to lowercase

            braille_output.append(english_to_braille.get(char, '......'))

    return ''.join(braille_output)

# Function to translate from Braille to English
def to_english(braille):
    english_output = []
    i = 0
    capital_mode = False
    number_mode = False

    while i < len(braille):
        braille_char = braille[i:i+6]

        if braille_char == capital_braille:
            capital_mode = True
        elif braille_char == number_braille:
            number_mode = True
        elif braille_char == '......':
            english_output.append(' ')  # Add space to the output
            number_mode = False
        else:
            if number_mode:
                char = braille_to_number.get(braille_char, ' ')
            else:
                char = braille_to_english.get(braille_char, ' ')
                if capital_mode:
                    char = char.upper()
                    capital_mode = False

            english_output.append(char)

        i += 6 # Go to the next character

    return ''.join(english_output)

def main():
    if len(sys.argv) < 2:
        print("Please provide input text!")
        return

    input_text = ' '.join(sys.argv[1:])
    
    # Check if input is Braille or English
    if set(input_text).issubset({'O', '.'}):
        # Translate Braille to English
        output = to_english(input_text)
    else:
        # Translate English to Braille
        output = to_braille(input_text)

    print(output)

if __name__ == "__main__":
    main()