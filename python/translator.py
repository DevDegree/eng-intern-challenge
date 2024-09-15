import sys

toBraille = {
    "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..", "E": "O..O..", "F": "OOO...", "G": "OOOO..", "H": "O.OO..",
    "I": ".OO...", "J": ".OOO..", "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.", "P": "OOO.O.",
    "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.", "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO",
    "Y": "OO.OOO", "Z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...",
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", " ": "......"
}

toEng = {
    "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D", "O..O..": "E", "OOO...": "F", "OOOO..": "G", "O.OO..": "H",
    ".OO...": "I", ".OOO..": "J", "O...O.": "K", "O.O.O.": "L", "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O", "OOO.O.": "P",
    "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T", "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X",
    "OO.OOO": "Y", "O..OOO": "Z", "......": " "
}

toNum = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}
code = " ".join(sys.argv[1:])
braille = "." in code 
decoded = ""
substring = ""
capital = False
num = False
if braille:
    for i in range(len(code)//6):
        substring = code[6*i:6*i+6]
        # Numbers
        if num:
            if substring == "......":
                num = False
            decoded += toNum.get(substring)
        # Capitalize
        elif substring == ".....O":
            capital = True
            continue
        # Letters
        else:
            # Number start
            if substring == ".O.OOO":
                num = True
                continue
            else:
                if capital:
                    decoded += toEng.get(substring)
                    capital = False
                else:
                    decoded += toEng.get(substring).lower()
else:
    for i in range(len(code)):
        char = code[i]
        if char == " ":
            num = False
        # Numbers
        if char >= "0" and char <= "9":
            if not num:
                num = True
                decoded += ".O.OOO" + toBraille.get(char)
            else:
                decoded += toBraille.get(char)
        # Uppercase
        elif char.isupper():
            decoded += ".....O" + toBraille.get(char)
        # Lowercase
        else:
            decoded += toBraille.get(char.upper())

print(decoded)