import sys

CAPITAL_NEXT = '.....O'
NUMBER_NEXT = '.O.OOO'
SPACE = '......'

# mapping from english characters and numbers to braille
english_to_braille = {
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
}

number_to_braille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

braille_to_english = {}
braille_to_number = {}

# exception for when we try to translate a braille string that is not valid
class InvalidBrailleException(Exception):
    pass

# takes in eng (an english string) and translates it to braille
def translate_english_to_braille(eng: str) -> str:
    braille = ''

    # when this flag is true, any braille sequences added will be assumed to be numbers
    number_flag = False

    # loop through the eng string and translate it to braille character by character
    for ch in eng:
        if ch.isalpha():
            if ch.isupper():
                braille += CAPITAL_NEXT
            braille += english_to_braille[ch.lower()]
        elif ch.isnumeric():
            if not number_flag:
                number_flag = True
                braille += NUMBER_NEXT
            braille += number_to_braille[ch]
        elif ch == ' ':
            braille += SPACE

    return braille

# takes in braille (a braille string) and translates it to english
def translate_braille_to_english(braille: str) -> str:
    if len(braille) % 6 != 0:
        raise InvalidBrailleException("Length of braille message must be divisible by 6")

    eng = ''

    capital_flag = False
    number_flag = False

    # loop through all sized 6 blocks in msg and translate it to english characters
    block_count = len(braille) // 6
    for i in range(block_count):
        block = braille[i * 6 : (i + 1) * 6]
        if block == CAPITAL_NEXT:
            capital_flag = True
        elif block == NUMBER_NEXT:
            number_flag = True
            capital_flag = False
        elif block == SPACE:
            eng += ' '
            number_flag = False
            capital_flag = False
        elif number_flag:
            if block not in braille_to_number:
                raise InvalidBrailleException(f"Tried to translate invalid braille sequence to number: {block}")
            eng += braille_to_number[block]
        else:
            if block not in braille_to_english:
                raise InvalidBrailleException(f"Tried to translate invalid braille sequence to english: {block}")
            if capital_flag:
                eng += braille_to_english[block].upper()
            else:
                eng += braille_to_english[block]
            capital_flag = False

    return eng

# returns true if s is a braille string and false otherwise
def is_braille(s: str) -> bool:
    return all(ch in 'O.' for ch in s)

def main():
    # create mapping from braille to english using mapping from english to braille
    for k, v in english_to_braille.items():
        braille_to_english[v] = k

    # create mapping from number to english using mapping from number to braille
    for k, v in number_to_braille.items():
        braille_to_number[v] = k

    # parse the input string, preserving spaces
    inp = sys.argv[1]
    for s in sys.argv[2:]:
        inp += ' ' + s

    if not is_braille(inp):
        print(translate_english_to_braille(inp))
    else:
        print(translate_braille_to_english(inp))

if __name__ == "__main__":
    main()