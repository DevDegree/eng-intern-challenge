import sys
import random

CAPITAL = -32
CAPITAL_BRAILLE = ".....O"
NUMBER_BRAILLE = ".O.OOO"
DECIMAL_BRAILLE = ".O...O"
SPACE_BRAILLE = "......"
TO_NUMBER = ord("a") - ord("1")
ZERO = ".OOO.."

braille_letters = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", 
                   "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO","O..OOO"]
braille_special = [CAPITAL_BRAILLE, NUMBER_BRAILLE, DECIMAL_BRAILLE, SPACE_BRAILLE, ZERO]
#braille_to_ascii converts the braille string to the ASCII code of the character
#For letters, the lowercase ASCII value is stored
#special characters are pre-stored
braille_to_ascii = {
    "..OO.O": ord("."), #decimal
    "..O...": ord(","), #comma
    "...OOO": ord("?"), #question mark
    "..OOO.": ord("!"), #exclamation mark
    "..OO..": ord(":"), #colon
    "..O.O.": ord(";"), #semi-colon
    "....OO": ord("-"), #hyphen
    ".O..O.": ord("/"), #slash
    ".OO..O": ord("<"), #less than
    "O..OO.": ord(">"), #greater than
    "O.O..O": ord("("), #open bracket
    ".O.OO.": ord(")"), #close bracket
    "......": ord(" ") #space
}


#store braille and their corresponding ASCII value for lowercase English letters
for i in range(len(braille_letters)):
    braille_to_ascii[braille_letters[i]] = ord("a") + i


english_to_braille = {}

for braille in braille_to_ascii:
    character = chr(braille_to_ascii[braille])
    english_to_braille[character] = braille

#Returns True if the string is English, else False
def isEnglish(string: str) -> bool:
    #If string length is not a multiple of 6, it can't be Braille, thus it is English
    if len(string) % 6 != 0:
        return True
    
    #Check if the string is constructed of Braille characters
    for idx in range(0, len(string), 6):
        substring = string[idx: idx+6]
        if substring not in braille_to_ascii and substring not in braille_special:
            print(substring)
            return True
        
    return False

def main(string):
    res = ""

    if isEnglish(string):
        start_number = False
        for char in string:
            if char == " ":
                start_number = False

            if ord("0") <= ord(char) <= ord("9"):
                if not start_number:
                    res += NUMBER_BRAILLE
                    start_number = True

            if start_number and char == ".":
                res += DECIMAL_BRAILLE

            elif ord("A") <= ord(char) <= ord("Z"):
                res += CAPITAL_BRAILLE
                res += english_to_braille[chr(ord(char) - CAPITAL)]
            elif char == "0":
                res += ZERO
            elif ord("1") <= ord(char) <= ord("9"):
                res += english_to_braille[chr(ord(char) + TO_NUMBER)]
            else:
                res += english_to_braille[char]

    else:
        capital = False
        number = False

        for idx in range(0, len(string), 6):
            substring = string[idx: idx+6]
            if substring == CAPITAL_BRAILLE:
                capital = True
            elif substring == NUMBER_BRAILLE:
                number = True
            elif substring == DECIMAL_BRAILLE:
                res += "."
            elif substring == SPACE_BRAILLE:
                res += " "
                number = False
            elif number:
                if substring == ZERO:
                    res += "0"
                else:
                    print(braille_to_ascii[substring] - TO_NUMBER)
                    print(chr(braille_to_ascii[substring] - TO_NUMBER))
                    res += chr(braille_to_ascii[substring] - TO_NUMBER)
            elif capital:
                res += chr(braille_to_ascii[substring] + CAPITAL)
                capital = False
            else:
                res += chr(braille_to_ascii[substring])
    
    print(res, end="")
    return res

if __name__ == "__main__":
    user_input = sys.argv
    for i in range(1, len(user_input)):
        arg = user_input[i]
        main(arg)
        if i != len(user_input) - 1:
            print(english_to_braille[" "], end="")
