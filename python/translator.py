# Dictionary converting english alphabet characters to braille
character_to_braille = {
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
    'z': 'O..OOO'
}

# Dictionary converting digits to braille
digit_to_braille = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
}

# Dictionary converting english punctuation to braille
punctuation_to_braille = {
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
}

# Braille symbols for capitalization, decimal, and number follows
uppercase_follows = '.....O'
decimal_follows = '.O...O'
number_follows = '.O.OOO'


# Dictionaries containing braille to character, digit, punctuation
# Obtained by swapping key: values from the original dictionaries
braille_to_character = dict((reversed(item) for item in character_to_braille.items()))
braille_to_digit = dict((reversed(item) for item in digit_to_braille.items()))
braille_to_punctuation = dict((reversed(item) for item in punctuation_to_braille.items()))


"""
    Convert an English text to Braille
        param text: English text to convert
        returns: Braille representation of the text
"""
def english_to_braille(text):

    braille_text = ''

    for char in text:

        if char.isalpha():
            if char.isupper():
                braille_text += uppercase_follows
            braille_text += character_to_braille[char.lower()]

        elif char in digit_to_braille:
            braille_text += number_follows
            braille_text += digit_to_braille[char]

        elif char in punctuation_to_braille:
            braille_text += punctuation_to_braille[char]

    return braille_text



if __name__ == '__main__':
    import sys
    args = sys.argv
    args.pop(0)

    # Get the input text as a string
    text = ' '.join(args)
    # Get the unique characters in the input
    characters = set(text)

    


