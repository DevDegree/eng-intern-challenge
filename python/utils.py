def is_valid_braille(input):
    """
    To check if an input is valid braille, we need to first make sure that it can be divided into chunks of 6, as there are 6 dots in a braille symbol. 
    Then we need to check that there are no characters other than O(letter o) and .(period)
    """

    if len(input) % 6 != 0:
        return False
    
    return all(char in ['O', '.'] for char in input)


def is_valid_english(input):
    """
    To check if an input is valid english, we need to create a list of all characters that would currently be considered valid (so excluding things such as ∈, ∑, and é),
    the simplest way to do this is probably to just scrape the english_braille_map that we already have, which is the approach I chose.
    Then we need to make sure that all of the characters in the input are one of those valid characters.
    """
    
    # Probably not a good idea to hardcode this number in, but I decided to leave it for now.
    num_eng_chars_in_dict = 52
    valid_characters = list(english_braille_map.keys())[:num_eng_chars_in_dict]
    
    return all(char in valid_characters for char in input.lower())


def is_number(char):
    return char.isdigit()


def is_capital(char):
    return char == char.upper() and char.isalpha()


def chunk_braille_input(input):
    """
    This function returns a list of all of the braille symbols in a braille input. I chose the word chunks to represent each "chunk" or more accurately each individual symbol in the total input. Hopefully it gives you a laugh.
    It works by creating a for loop the length of how many braille symbols there are in the input, and then using array slicing to capture them, stepping forward by six each time.

    loop 1:
    0 x 6 = 0: 0 x 6 + 6 = 6 ([0:6])
    loop 2:
    1 x 6 = 6: 1 x 6 + 6 = 12 ([6:12])
    etc.
    """
    braille_chunked = []

    for i in range(0, len(input) // 6):
        braille_chunked.append(input[i * 6: i * 6 + 6])
    
    return braille_chunked


# A dictionary that has both english to braille mappings as well as braille to english.
# See notes in middle of dictionary

english_braille_map = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'CAPITAL_FOLLOWS': '.....O',
    'DECIMAL_FOLLOWS': '.O...O',
    'NUMBER_FOLLOWS': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
    # NOTE: I chose to structure it like this to deal with the problem of the data from a to j being overwritten. Since all keys in a dictionary must be unique, and a-j and 1-0 are all the same keys, they get overwritten.
    'O.....': ['a', '1'],
    'O.O...': ['b', '2'],
    'OO....': ['c', '3'],
    'OO.O..': ['d', '4'],
    'O..O..': ['e', '5'],
    'OOO...': ['f', '6'],
    'OOOO..': ['g', '7'],
    'O.OO..': ['h', '8'],
    '.OO...': ['i', '9'],
    '.OOO..': ['j', '0'],
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    # NOTE: I don't really know how I would deal with this situation since there's no SPECIAL_CHARACTER_FOLLOWS braille symbol, I guess I could just make my own braille haha
    'O..OO.': ['o', '>'],
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    # NOTE: I don't actually need these next 3 symbols, but I'm deciding to leave them in just incase there are any edge cases that I haven't thought of.
    '.....O': 'CAPITAL_FOLLOWS',
    '.O...O': 'DECIMAL_FOLLOWS',
    '.O.OOO': 'NUMBER_FOLLOWS',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
}
