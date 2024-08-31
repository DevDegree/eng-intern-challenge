import sys

eng_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital follows': '.....O', 'number follows': '.O.OOO', ' ': '......'
}

# Create a reverse mapping
braille_to_eng_map = {v: k for k, v in eng_to_braille_map.items() if k not in '1234567890'}

# A separate mapping for numbers is used because the same sequence of Braille characters can
# map to different characters (e.g. 'O.....' can be '1' or 'a')
braille_to_num_map = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6',
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def braille_to_eng(text: str) -> str:
    pass

def eng_to_braille(text: str) -> str:
    pass

def is_braille(text: str) -> bool:
    """
    Returns True if text is in Braille, False otherwise.

    Args:
        text (str): A string of text to check.

    Returns:
        bool: True if text is in Braille, False otherwise.
    """
    return all(c in '0.' for c in text)

if __name__ == '__main__':
    # Read command line arguments
    text = ' '.join(sys.argv[1:])

    # Convert the input to the appropriate format
    if is_braille(text):
        print(braille_to_eng(text))
    else:
        print(eng_to_braille(text))