import sys

# Dictionaries to store English to Braille and Braille to English translations

english_to_braille = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    " ": "......"
}

braille_to_english = {
    "O.....": "A",
    "O.O...": "B",
    "OO....": "C",
    "OO.O..": "D",
    "O..O..": "E",
    "OOO...": "F",
    "OOOO..": "G",
    "O.OO..": "H",
    ".OO...": "I",
    ".OOO..": "J",
    "O...O.": "K",
    "O.O.O.": "L",
    "OO..O.": "M",
    "OO.OO.": "N",
    "O..OO.": "O",
    "OOO.O.": "P",
    "OOOOO.": "Q",
    "O.OOO.": "R",
    ".OO.O.": "S",
    ".OOOO.": "T",
    "O...OO": "U",
    "O.O.OO": "V",
    ".OOO.O": "W",
    "OO..OO": "X",
    "OO.OOO": "Y",
    "O..OOO": "Z",
    "......": " "
}

# Numbers will be kept separately

num_english_to_braille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

num_braille_to_english = {
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

# Special Braille indicators
capital_follows = ".....O"
number_follows = ".O.OOO"

# Let's determine if the input string is in Braille or English
inputString = " ".join(sys.argv[1:])

isBraille = True

# Braille comes in blocks of 6 characters
if (len(inputString) % 6 != 0):
    isBraille = False

# Braille may only contain "O" and "." characters
for i in range(0, len(inputString)):
    if (inputString[i] != "O" and inputString[i] != "."):
        isBraille = False

convertedString = ""

if (isBraille):
# Conversion from Braille to English
    i = 0
    while i < len(inputString):
        # Check if capital follows
        if (inputString[i:i+6] == capital_follows):
            i += 6
            convertedString += braille_to_english[inputString[i:i+6]]
        # Check if number follows
        elif (inputString[i:i+6] == number_follows):
            i += 6
            while (i < len(inputString)):
                if (inputString[i:i+6] == "......"):
                    convertedString += " "
                    break
                # Add number conversion instead of letter conversion to string
                convertedString += num_braille_to_english[inputString[i:i+6]]
                # Skip over block
                i += 6
        else:
            convertedString += braille_to_english[inputString[i:i+6]].lower()
        i += 6
else:  
# Conversion from English to Braille
    i = 0
    while i < len(inputString):
        # Check if number follows
        if (inputString[i].isnumeric()):
            convertedString += number_follows
            while (i < len(inputString) and inputString[i] != " "):
                convertedString += num_english_to_braille[inputString[i]]
                i += 1
        # Handle uppercase letters
        elif (inputString[i].isupper()):
            convertedString += capital_follows
            convertedString += english_to_braille[inputString[i]]
            i += 1
        else:
            convertedString += english_to_braille[inputString[i].upper()]
            i += 1

print(convertedString)
