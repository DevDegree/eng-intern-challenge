import sys

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS  = ".O.OOO"
SPACE           = "......"

BRAILLE_TO_LETTER_MAP = {
    # Lowercase letters a to z
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

BRAILLE_TO_NUMBER_MAP = {  
    # Numbers 1 to 0
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

NUMBER_TO_BRAILLE_MAP = {number: braille for (braille, number) in BRAILLE_TO_NUMBER_MAP.items()}

BRAILLE_TO_CHAR_MAP = {
    # Lowercase letters a to z
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

    # Capital indicator
    ".....O": "#",

    # Number indicator
    ".O.OOO": ".",

    # Space
    "......": " "
}

CHAR_TO_BRAILLE_MAP = {char: braille for (braille, char) in BRAILLE_TO_CHAR_MAP.items()}
for number, braille in NUMBER_TO_BRAILLE_MAP.items():
   CHAR_TO_BRAILLE_MAP[number] = braille

def getStringToTranslate():
    if len(sys.argv) != 1:
        return ' '.join(sys.argv[1:])
    else:
        return None

if __name__ == "__main__":
    stringToTranslate = getStringToTranslate()

    if stringToTranslate == None:
        exit()

    isBraille = True
    brailleString = ''
    englishString = ''
    letterRequired = False
    numberRequired = False
    numberCurrent = False

    if len(stringToTranslate) % 6 != 0:
        isBraille = False

    for idx in range(0, len(stringToTranslate), 6):
        charChunk = stringToTranslate[idx:idx + 6] if idx + 6 <= len(stringToTranslate) else stringToTranslate[idx:]
        
        for char in charChunk:
            if char.isnumeric() and not numberCurrent:
                brailleString += NUMBER_FOLLOWS
                numberCurrent = True
            if char.isupper():
                brailleString += CAPITAL_FOLLOWS
            if brailleString == SPACE:
                numberCurrent = False
            brailleString += CHAR_TO_BRAILLE_MAP[char.lower()]

        if isBraille:
            if charChunk in BRAILLE_TO_CHAR_MAP:
                if charChunk == NUMBER_FOLLOWS:
                    numberRequired = True
                    continue
                elif charChunk == CAPITAL_FOLLOWS:
                    letterRequired = True
                    continue

                if letterRequired:
                    if charChunk not in BRAILLE_TO_LETTER_MAP:
                        isBraille = False
                        continue
                    else:
                        englishString += BRAILLE_TO_LETTER_MAP[charChunk].upper()
                        letterRequired = False

                elif numberRequired:
                    if charChunk == SPACE:
                        englishString += " "
                        numberRequired = False

                    elif charChunk not in BRAILLE_TO_NUMBER_MAP:
                        isBraille = False
                        continue

                    else:
                        englishString += BRAILLE_TO_NUMBER_MAP[charChunk]
                else:
                    englishString += BRAILLE_TO_CHAR_MAP[charChunk]

            else:
                isBraille = False
                

    print(englishString if isBraille else brailleString)