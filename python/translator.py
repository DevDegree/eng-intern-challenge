# Braille alphabet mapping

braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'A': '.....O' + 'O.....', 'B': '.....O' + 'O.O...', 'C': '.....O' + 'OO....', 'D': '.....O' + 'OO.O..',
    'E': '.....O' + 'O..O..', 'F': '.....O' + 'OOO...', 'G': '.....O' + 'OOOO..', 'H': '.....O' + 'O.OO..',
    'I': '.....O' + '.OO...', 'J': '.....O' + '.OOO..',
    'K': '.....O' + 'O...O.', 'L': '.....O' + 'O.O.O.', 'M': '.....O' + 'OO..O.', 'N': '.....O' + 'OO.OO.',
    'O': '.....O' + 'O..OO.', 'P': '.....O' + 'OOO.O.', 'Q': '.....O' + 'OOOOO.', 'R': '.....O' + 'O.OOO.',
    'S': '.....O' + '.OO.O.', 'T': '.....O' + '.OOOO.', 'U': '.....O' + 'O...OO', 'V': '.....O' + 'O.O.OO',
    'W': '.....O' + '.OOO.O', 'X': '.....O' + 'OO..OO', 'Y': '.....O' + 'OO.OOO', 'Z': '.....O' + 'O..OOO',
    '0': '.OOO.O', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
}

# Invert the braille_map to got from braille to English
english_map = {v: k for k, v in braille_map.items()}

# function to check if the input is braille or English
def is_braille(input_str):
    return all(c in 'O.' for c in input_str)

# function to translate English to Braile
def english_to_braille(english_str):
    braille_translation = []
    for char in english_str:
        braille_translation.append(braille_map.get(char, ''))
    return ''.join(braille_translation)

# function to translae braille to english
def braille_to_english(braille_str):
    english_translation = []
    i = 0
    while i < len(braille_str):
        if braille_str[i:i+6] == '.....O': # capital letter
            english_translation.append(english_map.get(braille_str[i:i+12], ''))
            i += 12
        else:
            english_translation.append(english_map.get(braille_str[i:i+6], ''))
            i += 6
    return ''.join(english_translation)