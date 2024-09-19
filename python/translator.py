# Braille to English mapping (Braille represented as a tuple of 'O' and '.')
braille_to_english = {
    ('O.', '..', '..'): 'a', ('O.', 'O.', '..'): 'b', ('OO', '..', '..'): 'c',
    ('OO', '.O', '..'): 'd', ('O.', '.O', '..'): 'e', ('OO', 'O.', '..'): 'f',
    ('OO', 'OO', '..'): 'g', ('O.', 'OO', '..'): 'h', ('.O', 'O.', '..'): 'i',
    ('.O', 'OO', '..'): 'j', ('O.', '..', 'O.'): 'k', ('O.', 'O.', 'O.'): 'l',
    ('OO', '..', 'O.'): 'm', ('OO', '.O', 'O.'): 'n', ('O.', '.O', 'O.'): 'o',
    ('OO', 'O.', 'O.'): 'p', ('OO', 'OO', 'O.'): 'q', ('O.', 'OO', 'O.'): 'r',
    ('.O', 'O.', 'O.'): 's', ('.O', 'OO', 'O.'): 't', ('O.', '..', 'OO'): 'u',
    ('O.', 'O.', 'OO'): 'v', ('.O', 'OO', '.O'): 'w', ('OO', '..', 'OO'): 'x',
    ('OO', '.O', 'OO'): 'y', ('O.', '.O', 'OO'): 'z',
    # Capital sign
    ('..', '..', '.O'): 'CAP',  # Used to capitalize the next letter
    # Numbers (using the same pattern as letters a-j, but prefixed with the number sign)
    ('..', 'OO', 'O.'): '1', ('..', 'OO', 'OO'): '2', ('..', 'O.', 'O.'): '3',
    ('..', 'O.', 'OO'): '4', ('..', '.O', 'O.'): '5', ('..', 'O.', '.O'): '6',
}