import sys

# Dictionary to map English characters to Braille patterns
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', 'capital_marker': '.....O', 'number_marker': '.O.OOO'
}

# Reverse the Braille to English map for decoding
braille_to_english = {v: k for k, v in english_to_braille.items()}

def check_if_braille(input_sequence):
    """Returns True if input is a valid Braille pattern."""
    return all(ch in ['O', '.'] for ch in input_sequence)

def convert_text_to_braille(input_text):
    """Converts English text to Braille notation."""
    translation = []
    num_mode = False  # Keeps track if the number mode is active
    for ch in input_text:
        if ch.isdigit():
            if not num_mode:
                translation.append(english_to_braille['number_marker'])
                num_mode = True
            translation.append(english_to_braille[ch])
        elif ch.isalpha():
            if num_mode:
                num_mode = False  # Disable number mode after digits
            if ch.isupper():
                translation.append(english_to_braille['capital_marker'])
            translation.append(english_to_braille[ch.lower()])
        elif ch == ' ':
            translation.append(english_to_braille[' '])
            num_mode = False  # Reset number mode upon encountering space
    return ''.join(translation)

def convert_braille_to_text(braille_str):
    """Converts Braille notation back to English text."""
    output = []
    num_mode = False
    index = 0
    while index < len(braille_str):
        braille_char = braille_str[index:index + 6]
        if braille_char == english_to_braille['number_marker']:
            num_mode = True
            index += 6
            continue
        if braille_char == english_to_braille['capital_marker']:
            next_braille_char = braille_str[index + 6:index + 12]
            output.append(braille_to_english[next_braille_char].upper())
            index += 12
        else:
            output.append(braille_to_english[braille_char])
            num_mode = False  # Reset after handling the Braille character
            index += 6
    return ''.join(output)

def main():
    """Main entry point for the program."""
    input_data = ' '.join(sys.argv[1:])

    if check_if_braille(input_data):
        print(convert_braille_to_text(input_data))
    else:
        print(convert_text_to_braille(input_data))

if __name__ == "__main__":
    main()