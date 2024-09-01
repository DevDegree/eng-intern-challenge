import sys
# Constants

BASE_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO...", "0": ".OOO..", " ": "......"
}

CAPITAL_PREFIX = "O.OOOO"
NUMBER_PREFIX = ".O.OOO"

'''
In Braille Alphabet in the technical requirements it does not state that '.' can be a vaild alphabet input in this program

Vaild Braille Alphabet are:
    1. Letters a through z(lowercase and uppercase)
    2. Numbers 0 through 9
    3. Spaces

This means if '.' is found in a string it is a braille and not a vaild braille alphabet
'''
def is_braille(text):
    for c in text:
        if c == '.':
            return True
    return False

def vaild_braille(text):
    return len(text) % 6 == 0

# Gets input from terminal
def get_system_arguments(args):
    text = ""
    for i in range(1,len(args) - 1):
        text += args[i] + " "
    text += args[len(args) - 1]

    return text

# Runs the Translator
def main():
    text = get_system_arguments(sys.argv)
    print(text)
    if is_braille(text) and vaild_braille(text):
        print(True)
    print("RAN")

if __name__ == "__main__":
    main() 