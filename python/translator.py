# Mappings
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..'
}

# Special Braille indicators
capital_indicator = '.....O'
number_indicator = '.O.OOO'
space = '......'


def translate_to_braille(text):
    braille_translation = []
    in_number_mode = False

    for char in text:
        if char.isdigit():
            if not in_number_mode:
                braille_translation.append(number_indicator)
                in_number_mode = True
            braille_translation.append(braille_dict[char])
        else:
            if in_number_mode:
                in_number_mode = False  # Exit number mode after numbers

            if char.isupper():
                braille_translation.append(capital_indicator)
                char = char.lower()  # Convert to lowercase for mapping

            if char == ' ':
                braille_translation.append(space)
            else:
                braille_translation.append(braille_dict.get(char, space))  # Default to space if not found

    return ''.join(braille_translation)


if __name__ == "__main__":
    import sys

    input_text = " ".join(sys.argv[1:])
    print(translate_to_braille(input_text))
