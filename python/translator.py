import sys

BRAILLE_TO_NUM = {
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

BRAILLE_TO_ALPHA = {
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
    "O..OOO": "z",
}

BRAILLE_TO_SPLCHAR = {
    "..OO.O":".",
    "..O...":",",
    "..O.OO":"?",
    "..OOO.":"!",
    "..OO..":":",
    "..O.O.":";",
    "....OO":"-",
    ".O..O.":"/",
    ".OO..O":"<",
    "O..OO.":">",
    "O.O..O":"(",
    ".O.OO.":")"}

WHITE_SPACE = "......"
CAP_FOLLOWS = ".....O"
NUM_FOLLOWS = ".O.OOO"
DEC_FOLLOWS = ".O...O"

# Reversing the maps
NUM_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_NUM.items()}
SPLCHAR_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_SPLCHAR.items()}
ALPHA_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_ALPHA.items()}

def braille_to_eng(braille : str):
    english = []
    num_mode = False # Flag to check if the successive characters are numbers
    cap_mode = False # Flag to check if the next character is in uppercase
    i = 0
    while (i < len(braille)):
        chunk = braille[i:i+6]
        if (chunk == WHITE_SPACE):
            english.append(" ")
            num_mode = False
        elif (chunk == "O..OO."): # Special Case: o and > have same braille representations
            if(num_mode): # > is chosen for a number context
                english.append(">")
            elif (
                (len(english) > 0 and english[-1].isalpha()) or
                 (i < len(braille) - 1 and BRAILLE_TO_ALPHA.get(braille[i+ 6: i + 12], None) is not None)):
                if (cap_mode): # o/O is chosen for an alphabet context
                        english.append("O")
                        cap_mode = False
                else:
                    english.append("o")
            else:
                english.append(">")
        elif (chunk == DEC_FOLLOWS):
            english.append(".")
        elif (chunk in BRAILLE_TO_SPLCHAR):
            english.append(BRAILLE_TO_SPLCHAR[chunk])
        elif (chunk == NUM_FOLLOWS):
            num_mode = True
        elif (not num_mode):
            if (chunk == CAP_FOLLOWS):
                cap_mode = True
            elif (cap_mode):
                character = BRAILLE_TO_ALPHA[chunk]
                english.append(character.upper())
                cap_mode = False
            else:
                character = BRAILLE_TO_ALPHA[chunk]
                english.append(character)
        else:
            english.append(BRAILLE_TO_NUM[chunk])
        i += 6
    return "".join(english)

def eng_to_braille(english: str):
    braille = []
    num_mode = False # Flag to check if the successive characters are numbers
    for ind, i in enumerate(english):
        if (i == " "):
            braille.append(WHITE_SPACE)
            num_mode = False
        elif (i.isdigit()):
            if (not num_mode):
                num_mode = True
                braille.append(NUM_FOLLOWS)
            braille.append(NUM_TO_BRAILLE[i])
        elif (i.isalpha()):
            if (i.isupper()):
                braille.append(CAP_FOLLOWS)
            braille.append(ALPHA_TO_BRAILLE[i.lower()])
            num_mode = False
        elif (i == "."): # Special case: If numerical context then add braille for decimal
            if (num_mode and ind != len(english) - 1 and english[ind + 1].isdigit()):
                braille.append(DEC_FOLLOWS)
            else: # If alphabetical context then add braille for period
                braille.append(SPLCHAR_TO_BRAILLE[i])
        else:
            braille.append(SPLCHAR_TO_BRAILLE[i])
    return "".join(braille)


def check_braille(text):
    length = len(text)
    if (length % 6 != 0):
        return False
    for i in text:
        if (i != "O" and i != "."):
            return False
    return True

def main():
    text = ' '.join(sys.argv[1:])
    result = ""
    if (check_braille(text)):
        result = braille_to_eng(text)
    else:
        result = eng_to_braille(text)
    print(result)
    
if (__name__ == "__main__"):
    main()
