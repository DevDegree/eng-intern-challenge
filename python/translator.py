
import sys

# English + Characters to Braille
CHARS_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......', '.': '..OO..', ',': '..O...', ';': '..OO..', 
    ':': '...O..', '!': '..OO.O', '?': '..O.O.', "'": '....O.', '-': '....OO'
}

# Numbers to Braille
NUMS_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Follow Characters to Braille
FOLLOWS_TO_BRAILLE = {
    'capital': '.....O', 
    'number': '.O.OOO'
}

def english_to_braille(english):
    braille = []

    # is number flag
    num = False

    for char in english:

        # check if character is uppercase - if so, next letter will be capital
        if char.isupper():
            braille.append(FOLLOWS_TO_BRAILLE['capital'])
            char = char.lower()
        
        # check if character is a number - if so, next char will be a number
        if char.isdigit():
            if not num:
                braille.append(FOLLOWS_TO_BRAILLE['number'])
                num = True
            braille.append(NUMS_TO_BRAILLE[char])
        # check if character is in the dictionary
        elif char in CHARS_TO_BRAILLE:
            braille.append(CHARS_TO_BRAILLE[char])
            num = False
        # default to space
        else:
            braille.append(CHARS_TO_BRAILLE[' '])
        
    return ''.join(braille)


def braille_to_english(braille):
    english = []

    # is number flag
    num = False

    # is capital flag
    capital = False

    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]

        if braille_char == FOLLOWS_TO_BRAILLE['capital']:
            capital = True
            continue
        if braille_char == FOLLOWS_TO_BRAILLE['number']:
            num = True
            continue

        if capital:
            # capital remains true until next letter is found
            english.append(list(CHARS_TO_BRAILLE.keys())[list(CHARS_TO_BRAILLE.values()).index(braille_char)].upper())
            capital = False
        elif num:
            # num remains true until a space is found
            if braille_char == CHARS_TO_BRAILLE[' ']:
                english.append(' ')
                num = False
                continue

            english.append(list(NUMS_TO_BRAILLE.keys())[list(NUMS_TO_BRAILLE.values()).index(braille_char)])

        else:
            if braille_char in CHARS_TO_BRAILLE.values():
                english.append(list(CHARS_TO_BRAILLE.keys())[list(CHARS_TO_BRAILLE.values()).index(braille_char)])

    return ''.join(english)
      

if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])

    if all(c in 'O.' for c in input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))