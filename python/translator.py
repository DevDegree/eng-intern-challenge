import sys

letterToBraile = {
    "caps": ".....O",
    "number": ".O.OOO",
    " ": "......",
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
}
braileToLetter = {}
for k, v in letterToBraile.items():
    braileToLetter[v] = k

numberToBraile = {
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
}

braileToNumber = {}
for k, v in numberToBraile.items():
    braileToNumber[v] = k


def translateToBraile(input):
    output = ""
    number = False
    for i in range(len(input)):
        c = input[i]
        if input[i].isupper():
            output += letterToBraile["caps"]
            c = c.lower()
        if input[i].isdigit() and not number:
            output += letterToBraile["number"]
            number = True
        if c == " ":
            output += letterToBraile[" "]
            number = False
        elif c in letterToBraile:
            output += letterToBraile[c]
        elif c in numberToBraile:
            output += numberToBraile[c]

    return output


def translateToEnglish(input):
    output = ""
    number = False
    i = 0
    while i < len(input):
        c = input[i : i + 6]
        if c == "......":
            output += " "
            number = False
        elif c == ".....O":
            output += braileToLetter[input[i + 6 : i + 12]].upper()
            i += 6
        elif braileToLetter[c] == "number":
            number = True
        else:
            if number:
                output += braileToNumber[c]
            else:
                output += braileToLetter[c]
        i += 6
    return output


def main():
    if len(sys.argv) < 2:
        return
    input = " ".join(sys.argv[1:])

    english = False
    for i in range(len(input)):
        if input[i] not in [".", "O", " "]:
            english = True
            break
    if english:
        print(translateToBraile(input))
    else:
        print(translateToEnglish(input))


if __name__ == "__main__":
    main()


