import sys

english_to_braille_conv = {
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

    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",

    " ": "......",
}

capitalNext = ".....O"
numberNext = ".O.O.."

# check whether it is braille using bool
def isBraille(input):
    for letter in input:
        if letter not in 'O.':
            return False
    return True

#translates to english
def translateBraille(string):

    return -1

#translates to braille
def translateEnglish(string):

    return -1

def main():
    inputString = sys.argv[1]
    brailleCheck = isBraille(inputString)
    translatedString = translateBraille() if brailleCheck else translateEnglish()
    print(translatedString)
    return

if __name__ == "__main__":
    main()