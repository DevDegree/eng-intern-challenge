import sys
# Dictionaries for translating between text and Braille
TEXT_CHAR_DICT = {'a': "O.....", 'b': "O.O...", 'c': "OO....",
                  'd': "OO.O..", 'e': "O..O..", 'f': "OOO...",
                  'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...",
                  'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
                  'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
                  'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.",
                  's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO",
                  'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
                  'y': "OO.OOO", 'z': "O..OOO", '.': "..OO.O",
                  ',': "..O...", '?': "..O.OO", '!': "..OOO.",
                  ':': "..OO..", ';': "..O.O.", '_': "....OO",
                  '/': ".O..O.", '(': "O.O..O", ')': ".O.OO."}
TEXT_NUM_DICT = {'1': "O.....", '2': "O.O...",

                 '3': "OO....", '4': "OO.O..",
                 '5': "O..O..", '6': "OOO...",
                 '7': "OOOO..", '8': "O.OO..",
                 '9': ".OO...", '0': ".OOO..",
                 '<': ".OO..O", '>': "O..OO."}

# Reverse dictionaries for Braille to text translation
BRAILLE_CHAR_DICT = {v: k for k, v in TEXT_CHAR_DICT.items()}
BRAILLE_NUM_DICT = {v: k for k, v in TEXT_NUM_DICT.items()}

# Special Braille symbols
CAPNEXT = ".....O"
NUMNEXT = ".O.OOO"
SPACE = "......"


def toBraille(text: str) -> str:
    numberMode = False
    brailleString = ""

    for c in text:

        # Check if c is a letter, capitalise if need be
        if c.lower() in TEXT_CHAR_DICT:
            if c.isupper():
                brailleString += CAPNEXT
            brailleString += TEXT_CHAR_DICT[c.lower()]

        # Check if c is a number, if first number add NUMNEXT and go into number mode
        elif c in TEXT_NUM_DICT:
            if not numberMode:
                brailleString += NUMNEXT
                numberMode = True
            brailleString += TEXT_NUM_DICT[c]

        # Check if c is a space
        elif c == ' ':
            brailleString += SPACE
            numberMode = False

    return brailleString


def toText(braille: str) -> str:
    numNext, capNext = False, False
    textString = ""

    # Iterate through the string 6 symbols at a time, analyse each group of 6
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]

        if symbol == CAPNEXT:
            capNext = True
        elif symbol == NUMNEXT:
            numNext = True
        elif symbol == SPACE:
            numNext = False
            textString += ' '
        elif numNext:
            textString += BRAILLE_NUM_DICT[symbol]
        else:
            c = BRAILLE_CHAR_DICT[symbol]
            if capNext:
                textString += c.upper()
                capNext = False
            else:
                textString += c
    return textString


def translate(input: str) -> str:
    inputSet = set(input)  # Input without any duplicates

    # Check if input is braille
    if (len(input) % 6 == 0) and inputSet <= {'O', '.'}:
        return toText(input)
    else:
        return toBraille(input)


if __name__ == "__main__":
    print(translate(' '.join(sys.argv[1:])))  # Join args in a single string
