import sys

# map eng alphabet to braille
alphaToBraille = {
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
    # space and punctuation
    " ": "......",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..OOO.",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "(": "O.O..O",
    ")": ".O.OO.",
}

# map digits to braille
numsToBraille = {
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

# additional braille symbols
CapitalFollows = ".....O"
DecimalFollows = ".O...O"
NumberFollows = ".O.OOO"
BrailleSpace = "......"

# map braille to eng alphabet + decimal digits
brailleToAlpha = {v: k for k, v in alphaToBraille.items()}
brailleToNums = {v: k for k, v in numsToBraille.items()}


def translateEnglishToBraille(input):
    englishText = " ".join(input)
    isNumber = False
    translatedText = ""

    for char in englishText:
        if char.isdigit():
            # add number follows symbol if beginning to add nums
            if not isNumber:
                translatedText += NumberFollows
                isNumber = True
            translatedText += numsToBraille.get(char, "")
        elif char.isalpha():
            # reset back to chars if char is anything except space
            isNumber = False
            if char.isupper():
                # add capital follows symbol
                translatedText += CapitalFollows
            translatedText += alphaToBraille.get(char.lower(), "")
        else:
            # handle spaces and punctuation
            translatedText += alphaToBraille.get(char, "")

    return translatedText


def translateBrailleToEnglish(input):
    brailleText = input[0]
    # separate braille text into array of braille chars(every 6 chars)
    brailleChars = [brailleText[i : i + 6] for i in range(0, len(brailleText), 6)]
    translatedText = ""
    capFollows = False
    numFollows = False

    for char in brailleChars:
        if char == CapitalFollows:
            capFollows = True
        elif char == NumberFollows:
            numFollows = True
        elif char == BrailleSpace:
            # add space and reset back to alphabet chars
            numFollows = False
            translatedText += " "
        elif capFollows:
            translatedText += brailleToAlpha.get(char, "").upper()
            capFollows = False
        elif numFollows:
            translatedText += brailleToNums.get(char, "")
        else:
            # add translated char and add "_" in case char doesnt exist
            translatedText += brailleToAlpha.get(char, "")

    return translatedText


def main():
    # validate input
    if len(sys.argv) < 2:
        print("")
        return

    input = sys.argv[1:]
    isBraille = input[0][0] in ["O", "."]

    if isBraille:
        print(translateBrailleToEnglish(input))
    else:
        print(translateEnglishToBraille(input))


if __name__ == "__main__":
    main()
