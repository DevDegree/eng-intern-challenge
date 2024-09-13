import sys

ALPHA_TO_BRAILLE = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......",
}

BRAILLE_TO_ALPHA = {v: k for k, v in ALPHA_TO_BRAILLE.items()}

NUMBER_TO_BRAILLE = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

SPECIAL_CHARS = {
    "capital": ".....O",
    "number": ".O.OOO"
}


def braille_to_english(braille_text):
    '''
    Takes in braille_text and returns English/alphabetal text. 
    If the given input is invalid braille text, return False.

    print(braille_to_english(".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."))
        -> Expected output: Abc 123

    print(braille_to_english(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."))
        -> Expected output: Hello world

    print(braille_to_english("...OO.OOOOOO"))
        -> Expected output: False
    '''
    if len(braille_text) % 6 or (not all(chr in ".O" for chr in braille_text)):
        return False
    
    english_text = ""
    number_mode = False
    capital_mode = False

    # Each braille character is 6 chars, so iterate over braille_text in chunks of 6 characters
    for braille_char in [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]:
        if (not braille_char in ALPHA_TO_BRAILLE.values()) and (not braille_char in SPECIAL_CHARS.values()):
            return False
        
        if braille_char == ALPHA_TO_BRAILLE[' ']:
            english_text += ' '
            number_mode = False
        elif capital_mode:
            english_text += BRAILLE_TO_ALPHA[braille_char].upper()
            capital_mode = False
        elif number_mode:
            english_text += BRAILLE_TO_NUMBER[braille_char]
        elif braille_char == SPECIAL_CHARS["capital"]:
            capital_mode = True
        elif braille_char == SPECIAL_CHARS["number"]:
            number_mode = True
        else:
            english_text += BRAILLE_TO_ALPHA[braille_char]
    
    return english_text


def english_to_braille(english_text):
    '''
    Takes in english_text and returns the corresponding braille text.

    print(english_to_braille("Hello world"))
        -> Expected output: .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..

    print(english_to_braille("42"))
        -> Expected output: .O.OOOOO.O..O.O...
    '''
    braille_text = ""
    number_mode = False
    for c in english_text:
        if c == ' ': 
            braille_text += ALPHA_TO_BRAILLE[c]
            number_mode = False
        elif c.isupper():
            braille_text += SPECIAL_CHARS["capital"]
            braille_text += ALPHA_TO_BRAILLE[c.lower()]
        elif number_mode:
            braille_text += NUMBER_TO_BRAILLE[c]
        elif c.isdigit():
            number_mode = True
            braille_text += SPECIAL_CHARS["number"]
            braille_text += NUMBER_TO_BRAILLE[c]
        else:
            braille_text += ALPHA_TO_BRAILLE[c]

    return braille_text

input_string = ' '.join(sys.argv[1:])

if braille_to_english(input_string):
    print(braille_to_english(input_string))
else:
    print(english_to_braille(input_string))
