class Braille:
    '''
    Unconventional use of a class but in my opinion it works well here.
    It looks neater and you can easily change the string representation of RAISED_DOT and BLANK_DOT in 
    the future if need be.
    '''
    RAISED_DOT = 'O' # 1
    BLANK_DOT = '.' # 0

    def __new__(cls, dots):
        '''
        Args: 
            dots (list): a list of integers [0, 1]
            1 represents a raised dot and 0  a blank dot.

        Returns:
            A string representation of the Braille character as specified by the requirements.
        '''
        return "".join([cls.RAISED_DOT if dot else cls.BLANK_DOT for dot in dots])


char2Braille = {
    # Alphabet
    'a': Braille( [1, 0,
                   0, 0,
                   0, 0]),
    
    'b': Braille( [1, 0,
                   1, 0,
                   0, 0]),
    
    'c': Braille( [1, 1,
                   0, 0,
                   0, 0]),
    
    'd': Braille( [1, 1,
                   0, 1,
                   0, 0]),
    
    'e': Braille( [1, 0,
                   0, 1,
                   0, 0]),
    
    'f': Braille( [1, 1,
                   1, 0,
                   0, 0]),
    
    'g': Braille( [1, 1,
                   1, 1,
                   0, 0]),
    
    'h': Braille( [1, 0,
                   1, 1,
                   0, 0]),
    
    'i': Braille( [0, 1,
                   1, 0,
                   0, 0]),
    
    'j': Braille( [0, 1,
                   1, 1,
                   0, 0]),
    
    'k': Braille( [1, 0,
                   0, 0,
                   1, 0]),
    
    'l': Braille( [1, 0,
                   1, 0,
                   1, 0]),
    
    'm': Braille( [1, 1,
                   0, 0,
                   1, 0]),
    
    'n': Braille( [1, 1,
                   0, 1,
                   1, 0]),
    
    'o': Braille( [1, 0,
                   0, 1,
                   1, 0]),
    
    'p': Braille( [1, 1,
                   1, 0,
                   1, 0]),
    
    'q': Braille( [1, 1,
                   1, 1,
                   1, 0]),
    
    'r': Braille( [1, 0,
                   1, 1,
                   1, 0]),
    
    's': Braille( [0, 1,
                   1, 0,
                   1, 0]),
    
    't': Braille( [0, 1,
                   1, 1,
                   1, 0]),
    
    'u': Braille( [1, 0,
                   0, 0,
                   1, 1]),
    
    'v': Braille( [1, 0,
                   1, 0,
                   1, 1]),
    
    'w': Braille( [0, 1,
                   1, 1,
                   0, 1]),
    
    'x': Braille( [1, 1,
                   0, 0,
                   1, 1]),
    
    'y': Braille( [1, 1,
                   0, 1,
                   1, 1]),
    
    'z': Braille( [1, 0,
                   0, 1,
                   1, 1]),

    # Numbers
    '1': Braille( [1, 0,
                   0, 0,
                   0, 0]),

    '2': Braille( [1, 0,
                   1, 0,
                   0, 0]),

    '3': Braille( [1, 1,
                   0, 0,
                   0, 0]),

    '4': Braille( [1, 1,
                   0, 1,
                   0, 0]),

    '5': Braille( [1, 0,
                   0, 1,
                   0, 0]),

    '6': Braille( [1, 1,
                   1, 0,
                   0, 0]),

    '7': Braille( [1, 1,
                   1, 1,
                   0, 0]),

    '8': Braille( [1, 0,
                   1, 1,
                   0, 0]),

    '9': Braille( [0, 1,
                   1, 0,
                   0, 0]),

    '0': Braille( [0, 1,
                   1, 1,
                   0, 0]),

    # Punctuation (not talked about in the requirements)
    '.': Braille( [0, 1,
                   0, 1,
                   1, 0]),

    ',': Braille( [0, 1,
                   0, 0,
                   0, 0]),

    '?': Braille( [0, 1,
                   0, 0,
                   1, 1]),

    '!': Braille( [0, 1,
                   1, 1,
                   0, 0]),

    ':': Braille( [0, 1,
                   0, 0,
                   1, 0]),

    ';': Braille( [0, 1,
                   1, 0,
                   1, 0]),

    '-': Braille( [0, 0,
                   1, 0,
                   1, 0]),

    '/': Braille( [0, 0,
                   1, 1,
                   0, 1]),

    '<': Braille( [0, 0,
                   1, 0,
                   0, 1]),

    '>': Braille( [0, 0,
                   1, 0,
                   1, 1]),

    '(': Braille( [0, 0,
                   1, 1,
                   1, 0]),

    ')': Braille( [0, 0,
                   1, 1,
                   1, 1]),

    # Special
    ' ': Braille( [0, 0,
                   0, 0,
                   0, 0]),

    'capital_follows': Braille( [0, 0,
                                 0, 0,
                                 0, 1]),

    # decimal_follows is not talked about in the requirements; code does not quite cater for it
    'decimal_follows': Braille( [0, 1,
                                 0, 0,
                                 0, 1]),

    'number_follows': Braille( [0, 1,
                                0, 1,
                                1, 1]),
}

braille2Char = {v : k for k, v in char2Braille.items() if k not in '1234567890'} 
# The if statement ignores the digits otherwise they will overwrite letters 'a' through 'j'



if __name__ == '__main__':
    print(char2Braille['d'])
    print(braille2Char['OO.O..'])
    