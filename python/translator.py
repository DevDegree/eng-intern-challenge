import sys

CAPITAL_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O"
NUMBER_FOLLOWS = ".O.OOO"
BRAILLE_SPACE = "......"

BRAILLE_TO_ENGLISH = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z"
}

ENGLISH_TO_BRAILLE = {
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
    ' ': BRAILLE_SPACE,
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '.O...O.',
    '/': '.O..O.',
    '<': '.O.O..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.'
}


BRAILLE_NUMBERS = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

# Numbers to Braille dictionary
NUMBERS_BRAILLE = {number: braille for braille, number in BRAILLE_NUMBERS.items()}

def identify_language(input_text):

    if len(input_text) % 6 != 0:
        return "ENGLISH"
    
    
    for i in range(0, len(input_text), 6):
        chunk = input_text[i:i+6]
        braille_map = chunk in BRAILLE_TO_ENGLISH or chunk  in BRAILLE_NUMBERS
        braille_char = chunk == CAPITAL_FOLLOWS or chunk == BRAILLE_SPACE or chunk == NUMBER_FOLLOWS
        if (not braille_map and not braille_char):
            return "ENGLISH"
    
    return "BRAILLE"

def braille_to_english_converter(input_text):
    final_text = ""
    caps_on = False
    next_num = False
    for i in range(0, len(input_text), 6):
        chunk = input_text[i:i+6]

        if chunk == CAPITAL_FOLLOWS:
            caps_on = True
        elif chunk == NUMBER_FOLLOWS:
            next_num = True
        elif caps_on:
            final_text += BRAILLE_TO_ENGLISH[chunk].upper()
            caps_on = False
        elif chunk == BRAILLE_SPACE:
            final_text += " "
            next_num = False
        elif next_num:
            final_text += BRAILLE_NUMBERS[chunk]
        else:
            final_text += BRAILLE_TO_ENGLISH[chunk]

    print(final_text)


def english_to_braille(input_text):
    final_text = ""
    prev_num = False
    
    for i in input_text:
        if prev_num:
            if not i.isnumeric():
                #prev_num = False
                if i.isupper():
                    final_text += CAPITAL_FOLLOWS
                    final_text += ENGLISH_TO_BRAILLE[i.lower()]
                else:
                    final_text += ENGLISH_TO_BRAILLE[i]
                prev_num = False
                final_text += BRAILLE_SPACE
            else:
                final_text += NUMBERS_BRAILLE[i]
        else:
            if i.isnumeric():
                final_text += NUMBER_FOLLOWS
                final_text += NUMBERS_BRAILLE[i]
                prev_num = True
            else:
                if i.isupper():
                    final_text += CAPITAL_FOLLOWS
                    final_text += ENGLISH_TO_BRAILLE[i.lower()]
                else:
                    final_text += ENGLISH_TO_BRAILLE[i]
    print(final_text)


def main():
    if len(sys.argv) < 2:
        print("ERROR: Missing arguments")
        return

    input_text = " ".join(sys.argv[1:]).strip()

    type = identify_language(input_text)

    if type == "BRAILLE":
        braille_to_english_converter(input_text)
    else:
        english_to_braille(input_text)

if __name__ == "__main__":
    main()


