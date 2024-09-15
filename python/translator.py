import sys

# mapping of English characters to braille
CHARS_TO_BRAILLE_MAPPING = {
    'A': '.....OO.....',
    'B': '.....OO.O...',
    'C': '.....OOO....',
    'D': '.....OOO.O..',
    'E': '.....OO..O..',
    'F': '.....OOOO...',
    'G': '.....OOOOO..',
    'H': '.....OO.OO..',
    'I': '.....O.OO...',
    'J': '.....O.OOO..',
    'K': '.....OO...O.',
    'L': '.....OO.O.O.',
    'M': '.....OOO..O.',
    'N': '.....OOO.OO.',
    'O': '.....OO..OO.',
    'P': '.....OOOO.O.',
    'Q': '.....OOOOOO.',
    'R': '.....OO.OOO.',
    'S': '.....O.OO.O.',
    'T': '.....O.OOOO.',
    'U': '.....OO...OO',
    'V': '.....OO.O.OO',
    'W': '.....O.OOO.O',
    'X': '.....OOO..OO',
    'Y': '.....OOO.OOO',
    'Z': '.....OO..OOO',
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

# mapping of numerals to braille
CHARS_TO_BRAILLE_MAPPING_NUMS = {
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
}

# functions to quickly reverse English to braille mappings
def reverse_mapping(mapping):
    reversed = {}
    for key, value in mapping.items():
        reversed[value] = key
    return reversed

# braille to english characters mapping
BRAILLE_TO_CHARS_MAPPING = reverse_mapping(CHARS_TO_BRAILLE_MAPPING)

# braille to numbers mapping
BRAILLE_TO_CHARS_MAPPING_NUMS = reverse_mapping(CHARS_TO_BRAILLE_MAPPING_NUMS)

# identify if text is braille (True) or English (False)
def braille(text):
    for i in text:
        # if input does not consist of solely . or O, it must be English
        if i != '.' and i != 'O':
            return False
    return True

# translate between braille and English
def translate(text):
    out = ''
    num_mode = False
    # given text is braille
    if braille(text):
        caps = False
        # as braille characters are in groups of 6, we must iterate over the input in jumps of 6
        for i in range(0, len(text), 6):
            s = text[i: i+6]
            # check if the following character is a capital
            if s == ".....O":
                caps = True
            # check if the following character is a number
            elif s == ".O.OOO":
                num_mode = True
            elif num_mode:
                # if we were reading numbers and encounter a space, we are no longer going to be working with numbers
                if s == "......":
                    num_mode = False
                    out += ' '
                else:
                    # translate the brail into a number
                    out += BRAILLE_TO_CHARS_MAPPING_NUMS[s]
            else:
                if caps:
                    # output the character as a capital and then return to lower case
                    out += BRAILLE_TO_CHARS_MAPPING[s].upper()
                    caps = False
                else:
                    # output the character
                    out += BRAILLE_TO_CHARS_MAPPING[s]
    # given text is English
    else:
        # iterate over ever character
        for i in text:
            # if the character is a number we must beging translating accordingly and indicate that the following braile characters are to be interpreted as numbers
            if i.isdigit() and not num_mode:
                num_mode = True
                out += ".O.OOO"
            if num_mode:
                # if we encounter a non-digit, we are no longer going to be dealing with numbers, output the next character
                if not i.isdigit():
                    num_mode = False
                    out += CHARS_TO_BRAILLE_MAPPING[i]
                else:
                    # give the braille translation of the number
                    out += CHARS_TO_BRAILLE_MAPPING_NUMS[i]
            else:
                # give the braille translation of the non-numeric character
                out += CHARS_TO_BRAILLE_MAPPING[i]
    return out

# read args, feed them into translate function and print output
print(translate(' '.join(sys.argv[1:])))
