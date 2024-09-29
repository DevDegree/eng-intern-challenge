# Mapping Braille symbols for letters, numbers, and spaces
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', ' ': '......'  # Space is represented by empty Braille cells
}

# Special Braille symbols for capital letters and numbers
braille_special = {
    'capital': '.....O',  # Indicates the next letter is capitalized
    'number': '.O.OOO'    # Indicates numbers follow
}

# Reverse mappings to convert Braille back to English
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_special = {v: k for v, k in braille_special.items()}

def is_braille(input_string):
    """
    Determines whether the input string is written in Braille.
    Braille strings only contain 'O', '.', and spaces.
    """
    return all(c in 'O. ' for c in input_string)

def translate_to_braille(text):
    """
    Translates a given English string into Braille.
    Handles capitalization and numbers by using special Braille indicators.
    """
    braille_translation = []
    number_mode = False  # To track if we are in number mode

    for char in text:
        if char.isupper():
            # Capitalization indicator before upper case letters
            braille_translation.append(braille_special['capital'])
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                # Insert number mode symbol before first number
                braille_translation.append(braille_special['number'])
                number_mode = True
            braille_translation.append(braille_alphabet[char])
        elif char.isalpha():
            # Any non-digit character stops number mode
            number_mode = False
            braille_translation.append(braille_alphabet.get(char, '......'))
        else:
            # Spaces or unsupported symbols default to empty Braille cells
            braille_translation.append(braille_alphabet.get(char, '......'))

    return ''.join(braille_translation)

def translate_to_english(braille_text):
    """
    Translates a given Braille string into English.
    Handles special cases like capitalization and numbers.
    """
    english_translation = []
    i = 0
    number_mode = False  # To track if we are in number mode
    capitalize_next = False  # To track if the next letter should be capitalized

    while i < len(braille_text):
        braille_char = braille_text[i:i+6]

        # Check for special Braille characters (capital or number mode)
        if braille_char == braille_special['capital']:
            capitalize_next = True
            i += 6
            continue

        if braille_char == braille_special['number']:
            number_mode = True
            i += 6
            continue

        # Normal character lookup
        letter = reverse_braille_alphabet.get(braille_char, ' ')

        # Apply capitalization if needed
        if capitalize_next:
            letter = letter.upper()
            capitalize_next = False  # Reset after using the capital marker

        # Apply number mode (if active)
        if number_mode and letter.isdigit():
            english_translation.append(letter)
        else:
            english_translation.append(letter)

        i += 6  # Move to the next Braille character (6 dots long)
        number_mode = False  # Reset number mode after a letter

    return ''.join(english_translation)

def main(input_string):
    """
    Main function to determine whether the input string is in English or Braille,
    and translate it accordingly.
    """
    if is_braille(input_string):
        # Translate from Braille to English
        print(translate_to_english(input_string))
    else:
        # Translate from English to Braille
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    import sys

    # Take the command line input as the text to translate
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])  # Join all arguments as a single input string
        main(input_string)
    else:
        print("Please provide a string to translate.")
