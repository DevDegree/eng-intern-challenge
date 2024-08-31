import sys

LETTER_DICT = {
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
    "CAPITAL": ".....O",
    "NUMBER": ".O.OOO",
}

NUMBER_DICT = {
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
    " ": "......",
    "CAPITAL": ".....O",
    "NUMBER": ".O.OOO",
}

# a string is in braille if and only if the set of characters only contain '.' and 'O'
def input_is_braille(input):
    input_set = set(input)

    if len(input_set) == 2 and "." in input_set and "O" in input_set:
        return True

    return False

args = sys.argv[1:]

inp = ' '.join(args)

if input_is_braille(inp):
    isCapital = False
    isNumber = False
    isDecimal = False

    for i in range(0, len(inp), 6):

        # is currently reading as number
        if isNumber:
            braille_char = inp[i:i+6]

            # search for corresponding number
            for key, value in NUMBER_DICT.items():
                if value == braille_char:
                    # if the char is a space, we reset the number flag
                    if key == " ":
                        isNumber = False
                    # NUMBER and CAPITAL do nothing in this context
                    elif key == "NUMBER" or key == "CAPITAL":
                        continue
                    # print the number otherwise
                    else:
                        print(key, end="")
                    break

        # is currently reading as capital letter
        elif isCapital:
            braille_char = inp[i:i+6]

            # search for corresponding capital
            for key, value in LETTER_DICT.items():
                if value == braille_char:
                    # CAPITAL does nothing in this context
                    if key == "CAPITAL":
                        continue
                    elif key == "NUMBER":
                        isNumber = True
                        isCapital = False
                    # print the capital otherwise and reset the capital flag
                    else:
                        print(key.upper(), end="")
                        isCapital = False
                    break

        # is currently reading as a lowercase letter
        else:
            braille_char = inp[i:i+6]

            # search for corresponding letter
            for key, value in LETTER_DICT.items():
                if value == braille_char:
                    # if the char is a space, we print a space
                    if key == " ":
                        print(" ", end="")
                    # if the char is a capital, we set the capital flag
                    elif key == "CAPITAL":
                        isCapital = True
                    # if the char is a number, we set the number flag
                    elif key == "NUMBER":
                        isNumber = True
                    # print the letter otherwise
                    else:
                        print(key, end="")
                    break

else:
    number_follower = False
    for i in inp:
        if i.isupper():
            print(LETTER_DICT["CAPITAL"], end="")
            i = i.lower()
        if i.isdigit() and not number_follower:
            print(NUMBER_DICT["NUMBER"], end="")
            number_follower = True
        if i.isdigit() and number_follower:
            print(NUMBER_DICT[i], end="")
        if i.isalpha():
            print(LETTER_DICT[i], end="")
        if i == " ":
            print(LETTER_DICT[" "], end="")
            number_follower = False
