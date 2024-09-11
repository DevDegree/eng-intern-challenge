import sys

# Map translating ASCII Characters and Instruction to Braille Text equivalent 
ASCII_TO_BRAILLE_MAP = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    "0": ".OOO..", "cf": ".....O", "nf": ".O.OOO", " ": "......",
}
# cf = capital follows
# nf = number follows

# Map translating Braille text to ASCII Alphabet Characters
BRAILLE_TO_ASCII_MAP = {
	"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
	"OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
	"O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
	"OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
	"O..OOO": "z", ".....O": "cf", ".O.OOO": "nf", "......": " ",
}
# cf = capital follows
# nf = number follows

# Map translating Braille text to ASCII Numeric Characters
BRAILLE_TO_ASCII_NUM_MAP = {
	"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
	"OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}


# The Braille Alphabet
BRAILLE_ALPHABET = "O."

# Determine if arguments are ASCII or Braille text
def isArgsBraille(inputArgs):
    for arg in inputArgs:
        for char in arg:
            if char not in BRAILLE_ALPHABET:
                return False
    
    return True

# Determine if the text is valid Braille text 
def isValidBraille(inputArgs):
    inputString = ''.join(inputArgs)

    if len(inputString) % 6 != 0:
        print("Invalid Brialle Text")
        return False

    return True

# converting ASCII to Braille text provided an array of strings
def convertASCIIToBraille(args):
    # print("CONVERT ASCII TO BRAILLE")
    brailleText = ""

    for text in args:
        flagNum = False

        for char in text:
            # Convert to ASCII value
            code = ord(char)
            
            # Compare ASCII value if it falls between Capital A -> Z
            if code >= 65 and code <= 90:
                code += 32
                brailleText += ASCII_TO_BRAILLE_MAP["cf"]
            
            # Compare ASCII value if it falls between 0 -> 9
            elif code >= 48 and code <= 57:
                if not flagNum:
                    brailleText += ASCII_TO_BRAILLE_MAP["nf"]
                    flagNum = True
            
            brailleText += ASCII_TO_BRAILLE_MAP[chr(code)]
        brailleText += ASCII_TO_BRAILLE_MAP[" "]
    
    return brailleText[:len(brailleText)-6]


def convertBrailleToASCII(args):
    # print("CONVERT BRAILLE TO ASCII")
    inputString = ''.join(args)

    asciiText = ""

    flagCap = False
    flagNum = False
    for x in range(0, len(inputString), 6):
        brailleCode = inputString[x:x+6]
        if brailleCode in BRAILLE_TO_ASCII_MAP:
            asciiLetter = BRAILLE_TO_ASCII_MAP[brailleCode]

            if BRAILLE_TO_ASCII_MAP[brailleCode] == "cf":
                flagCap = True
                continue
            elif BRAILLE_TO_ASCII_MAP[brailleCode] == "nf":
                flagNum = True 
                continue
            elif BRAILLE_TO_ASCII_MAP[brailleCode] == " ":
                flagNum = False
                flagCap = False

            if flagCap:
                asciiLetter = asciiLetter.upper()
                flagCap = False
            elif flagNum:
                asciiLetter = BRAILLE_TO_ASCII_NUM_MAP[brailleCode]

            asciiText += asciiLetter
                
    return asciiText


def main():
    if len(sys.argv) == 1:
        # Edge case: No arguments was passed onto console
        return

    # remove the program location from args
    inputArgs = sys.argv[1:]

    if isArgsBraille(inputArgs):
        if isValidBraille(inputArgs):
            print(convertBrailleToASCII(inputArgs))
    else:
        print(convertASCIIToBraille(inputArgs))
    


if __name__ == "__main__":
    main()
