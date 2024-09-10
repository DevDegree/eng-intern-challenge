# Braille encoding
BRAILLE_ENCODING = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO'
}

# Numbers encoding
NUMBER_ENCODING = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse dictionary for faster lookups
ENGLISH_FROM_BRAILLE = {v: k for k, v in BRAILLE_ENCODING.items()}
NUMBER_FROM_BRAILLE = {v: k for k, v in NUMBER_ENCODING.items()}

def braille_to_english(braille_string):
    # Split the input string into segments of 6 characters each
    braille_list = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    english_output = []
    is_capital = False
    is_number = False

    for br in braille_list:
        if br == BRAILLE_ENCODING['cap']:
            is_capital = True
            continue
        elif br == BRAILLE_ENCODING['num']:
            is_number = True
            continue

        # Handling number decoding
        if is_number:
            if br in NUMBER_FROM_BRAILLE:
                char = NUMBER_FROM_BRAILLE[br]
            else:
                is_number = False  # Reset number mode if the pattern isn't a number
                char = ENGLISH_FROM_BRAILLE.get(br, '?')  # Check if it's a letter
        else:
            char = ENGLISH_FROM_BRAILLE.get(br, '?')

        if char == '?':
            print(f"Warning: Unrecognized Braille pattern '{br}'")
        else:
            if is_capital and char.isalpha():
                char = char.upper()
                is_capital = False  # Reset capital flag after use

        english_output.append(char)

    return ''.join(english_output)

def english_to_braille(english_string):
    braille_output = []
    last_was_number = False  # To track if the last character was a number

    for char in english_string:
        if char.isdigit():
            if not last_was_number:
                braille_output.append(BRAILLE_ENCODING['num'])  # Append num only if the last character was not a number
            braille_output.append(NUMBER_ENCODING[char])
            last_was_number = True
        else:
            if last_was_number and char != ' ':
                last_was_number = False  # Reset if next character is not a number and not a space
            if char.isupper():
                braille_output.append(BRAILLE_ENCODING['cap'])
                braille_output.append(BRAILLE_ENCODING[char.lower()])
            else:
                braille_output.append(BRAILLE_ENCODING[char])

    return ''.join(braille_output)

# Be sure to adjust the dictionaries and other variables as necessary to match your actual encoding and application structure.

def main(input_string):
    # Determine if the input is Braille or English
    if all(c in 'O.' for c in input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_string = ''.join(sys.argv[1:])  # Join without spaces
        print(main(input_string))
    else:
        print("Usage: python braille_translator.py <string>")