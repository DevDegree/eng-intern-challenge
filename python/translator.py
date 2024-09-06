
import sys


BRAILLE_TO_ENG = {
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

ENG_TO_BRAILLE = {letter: braille for braille, letter in BRAILLE_TO_ENG.items()}

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
    ".OOO..": "0"
}

NUM_TO_BRAILLE = {number: braille for braille, number in BRAILLE_TO_NUM.items()}

BRAILLE_SPACE = "......"
BRAILLE_NEXT_UPPER = ".....O"
BRAILLE_NUM_SEQUENCE = ".O.OOO"

def is_braille(input: str):
    if(len(input)%6 != 0):
        return False
    for i in range(0, len(input), 6):
        char = input[i:i+6]
        braille_char = char in BRAILLE_TO_ENG or char in BRAILLE_TO_NUM
        braille_symbol = char == BRAILLE_SPACE or char == BRAILLE_NEXT_UPPER or char == BRAILLE_NUM_SEQUENCE
        if(not braille_char and not braille_symbol):
            return False
    return True
        
def braille_to_english(input: str):
    words = ""
    uppercase_follows = False
    number_follows = False
    count = 0
    for i in range(0, len(input), 6):
        char = input[i:i+6]
        if(number_follows):
            if(char == BRAILLE_SPACE):
                number_follows = False
                words += " "
            else:
                words += BRAILLE_TO_NUM[char]
        elif(char == BRAILLE_SPACE):
            words += " "
        elif(char == BRAILLE_NEXT_UPPER):
            uppercase_follows = True
        elif(char == BRAILLE_NUM_SEQUENCE):
            number_follows = True
        elif(uppercase_follows):
            words += BRAILLE_TO_ENG[char].upper()
            uppercase_follows = False
        else:
            words += BRAILLE_TO_ENG[char]
        print(number_follows)
    return words

def english_to_braille(input: str):
    output = ""
    prevWasNum = False
    for char in input:
        if char in NUM_TO_BRAILLE.keys():
            if(not prevWasNum):
                output += BRAILLE_NUM_SEQUENCE
                prevWasNum = True
            output += NUM_TO_BRAILLE[char]
        elif char.lower() in ENG_TO_BRAILLE.keys():
            if(prevWasNum):
                prevWasNum = False
                output += BRAILLE_SPACE
            if(char.isupper()):
                output += BRAILLE_NEXT_UPPER
            output += ENG_TO_BRAILLE[char.lower()]
            prevWasNum = False
        else:
            output += BRAILLE_SPACE
            prevWasNum = False
    return output

def main():
    if len(sys.argv) < 2:
        print("ERROR: Missing arguments")
        return

    input = " ".join(sys.argv[1:]).strip()

    if(is_braille(input)):
        print(braille_to_english(input))
    else:
        print(english_to_braille(input))
    
if __name__ == "__main__":
    main()



