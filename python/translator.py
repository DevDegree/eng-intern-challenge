import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 'capital': '..O...',
    'number': '.O.OOO',  '.': 'O.O.OO', ',': 'O.....', '?': 'O.O.O.', '!': 'O.OOO.', ':': 'OO..OO',
    ';': 'O.O...', '-': '..OOO.', '/': 'O..O.O', '(': 'O.OOOO', ')': 'O.OOOO',
    '<': 'OO..OO', '>': '.OO.OO', ' ': '......'
}

english_dict = {v: k for k, v in braille_dict.items()}

def translate(input_text):
    if input_text[0] in ['O', '.']:
        # Braille to English
        translated = []
        for i in range(0, len(input_text), 6):
            braille_char = input_text[i:i+6]
            if braille_char in english_dict:
                translated.append(english_dict[braille_char])
            else:
                translated.append('?')  # Indicate an unknown Braille character
        return ''.join(translated)
    else:
        # English to Braille
        return ''.join([braille_dict.get(char.lower(), '?') for char in input_text])



if __name__ == "__main__":
    input_text = sys.argv[1]
    print(translate(input_text))

