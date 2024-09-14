import sys

eToB = {
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
    "W": ".OO.OO",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    "capital follows": ".....O",
    "number follows": ".O.OOO",
    "decimal follows": ".O...O",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}

numChars = {
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
}

def englishToBraille():
    toTranslate = sys.argv[1:]
    translated = ""
    for i in toTranslate:
        for char in i:
            if char.isalpha():
                if char.isupper():
                    translated += eToB["capital follows"]
                    translated += eToB[char]
                if char.islower():
                    translated += eToB[char.upper()]
            else:
                if char.isdigit():
                    if not (eToB["number follows"]) in translated:
                        translated += eToB["number follows"]
                    translated += numChars[char]
                else:
                    translated += eToB[char]
        translated += eToB[" "]

    print(translated[:-6])

def brailleToEnglish():
    toTranslate = sys.argv[1:]
    translated = ""
    for i in toTranslate:
        for j in range(0, len(i), 6):
            group = i[j:j+6]
            key = next(key for key, value in eToB.items() if value == group)
            if key == 'capital follows':
                translated += "\\"
            elif key == 'number follows':
                translated += "#"
            else:
                if translated.endswith("\\"):
                    translated = translated[:-1]
                    translated += key.upper()
                elif translated.endswith("#"):
                    translated = translated[:-1]
                    key = next(key for key, value in numChars.items() if value == group)
                    translated += key
                    translated += "#"
                else:
                    translated += key.lower()

    translated = translated.replace("#", "")
    translated = translated.replace("\\", "")
    print(translated)


def main():
    if (all(char in ['O', '.'] for char in sys.argv[1])):
        brailleToEnglish()
    else:
        englishToBraille()


if __name__ == "__main__":
    main()
