english_to_braille_main_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O..O.O', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

# Separate dictionary because of the redundancy with letters.
english_to_braille_numbers_dict = {
    '0': '.OOO..','1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Create dicts specifically for the reverse translation. Takes a bit more memory, but keeps searches O(1).  
braille_to_english_main_dict = {v: k for k, v in english_to_braille_main_dict.items()}
braille_to_english_numbers_dict = {v: k for k, v in english_to_braille_numbers_dict.items()}

braille_alphabet = ['O','.']
