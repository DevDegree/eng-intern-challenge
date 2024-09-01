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
In Braille Alphabet in the technical tequirements it does not state that '.' is a vaild braille alahabet

Vaild Braille Alphabet are:
    1. Letters a through z(lowercase and uppercase)
    2. Numbers 0 through 9
    3. Spaces

Every braille contains a '.' thus if a string(text) contains '.' it means it has to be a braille
'''
def is_braille(text):
    for c in text:
        if c == '.':
            return True
    return False

def vaild_braille(text):
    return len(text) % 6 == 0

# Created to run my own tests
def main():
    print("Hello World :) ")

if __name__ == "__main__":
    main() 