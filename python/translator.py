braille_dict = {
    # Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    # Numbers
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    # Indicators
    'capital': '.....O',  # Capitalization indicator
    'decimal': '.O...O',  # Decimal follows
    'number': '.O.OOO', # Number indicator

    # Special characters
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'

}

def is_braille (input):
    """
        Checks if the input string is a Braille representation.
        Args:
            input (str): The string to check.
        Returns:
            bool: True if the input string consists only of 'O' and '.'
    """
    return all(char in ['O', '.'] for char in input)

def is_english(input):
    """
        Checks if the input string is an English text.
        Args:
            input (str): The string to check.
        Returns:
            bool: True if the input string contains any alphanumeric characters or spaces
        """
    return any(char.isalnum() or char.isspace() for char in input)

