import sys

english_to_braille_map = {
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
    "cf": ".....O",
    "nf": ".O.OOO",
    " ": "......",
}

def isArgsBraille(inputArgs: list[str]):
    brailleAlphabet = "O."

    for arg in inputArgs:
        for char in arg:
            if char not in brailleAlphabet:
                return False
    
    return True

def convertASCIIToBraille(consoleArgs: list[str]):
    print("CONVERT ASCII TO BRAILLE")
    pass

def convertBrailleToASCII(consoleArgs: list[str]):
    print("CONVERT BRAILLE TO ASCII")
    pass


def main():
    if len(sys.argv) == 1:
        # Edge case: No arguments was passed onto console
        return

    # remove the program location from args
    inputArgs = sys.argv[1:]

    if isArgsBraille(inputArgs):
        convertBrailleToASCII(inputArgs)
    else:
        convertASCIIToBraille(inputArgs)
    



if __name__ == "__main__":
    main()
    pass
