# QUESTIONS:
    # If the input str is '123 abc' and we translate this to braille, should the output have 2 space characters next to each other
    # 1 to symbolize that numbers finish, and then the actual space character? Or just 1 space that represents both

    # DECIMAL FOLLOWS???? (only for decimals or also for other symbols)

    # test
    # when to read braille and enghlish (finish function)
            # braille when str only has "." and "O" and divisible by 6
    # number follows and spaces


# English to Braille mappings
e_to_b_alpha = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

e_to_b_num = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

e_to_b_sym = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}

# Braille to English mappings
b_to_e_alpha = {v: k for k, v in e_to_b_alpha.items()}
b_to_e_num = {v: k for k, v in e_to_b_num.items()}
b_to_e_sym = {v: k for k, v in e_to_b_sym.items()}

# Special characters for capitalization and numbers
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
DECIMAL_FOLLOWS = '.O...O'
SPACE = '......'


def braille_to_english(braille_str):
    english_str = ''
    capital_follows = False
    number_follows = False
    decimal_follows = False

    for x in range(0, len(braille_str), 6):
        character = braille_str[x:x+6]

        if character == CAPITAL_FOLLOWS:
            capital_follows = True
        elif character == NUMBER_FOLLOWS:
            number_follows = True
        elif character == DECIMAL_FOLLOWS:
            decimal_follows = True
        elif character == SPACE:
            english_str += ' '
            number_follows = False
        elif number_follows:
            num_char = b_to_e_num[character]
            english_str += num_char
        elif decimal_follows:
            sym_char = b_to_e_sym[character]
            english_str += sym_char
        else:
            english_char = b_to_e_alpha[character]

            if (capital_follows):
                english_char = english_char.upper()
                capital_follows = False
            
            english_str += english_char

    print(english_str)
    return english_str

def english_to_braille(english_str):
    braille_str = ''
    number_follows = False

    for x in range(0, len(english_str)):
        character = english_str[x]

        if character.isnumeric():
            if not number_follows:
                braille_str += NUMBER_FOLLOWS
                number_follows = True
            braille_str += e_to_b_num[character]
        elif character.isspace():
            braille_str += SPACE
            number_follows = False
        elif character.isupper():
            braille_str += CAPITAL_FOLLOWS
            braille_str += e_to_b_alpha[character.lower()]
            number_follows = False
        elif character in e_to_b_alpha:
            braille_str += e_to_b_alpha[character]
            number_follows = False
        elif character in e_to_b_num:
            braille_str += e_to_b_num[character]
            number_follows = False

    print(braille_str)
    return braille_str


if __name__ == "__main__":
    import sys
    # Combine all arguments into a single input string
    input_str = ''.join(sys.argv[1:])

    # input_str = 'O.OO..O..O..O.O.O.'
    # braille_to_english(input_str)

    if all(c in 'O.' for c in input_str):
        braille_to_english(input_str)
    else:
        english_to_braille(input_str)
