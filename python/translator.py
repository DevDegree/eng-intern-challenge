import sys

TO_LETTERS = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z"
}

FROM_LETTERS = {v: k for k, v in TO_LETTERS.items()}

TO_NUMBERS = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

FROM_NUMBERS = {v: k for k, v in TO_NUMBERS.items()}

CAPITAL = ".....O"
NUMBER  = ".O.OOO"
SPACE   = "......"


def english_to_brail(inputs):
    braille = ""
    isNumber = False

    for word in inputs:
        for char in word:
            if char.isupper():
                braille += CAPITAL
                char = char.lower()
            if char in FROM_NUMBERS:
                if not isNumber:
                    braille += NUMBER
                    isNumber = True
                braille += FROM_NUMBERS[char]
            elif char in FROM_LETTERS:
                braille += FROM_LETTERS[char]
            elif char == " ":
                isNumber = False
                braille += SPACE
            else:
                print("incorrect input")
        braille += SPACE
    return braille[:-6]


def brail_to_english(inputs):
    english = ""
    isNumber = False
    isCapital = False

    for i in range(0, len(inputs), 6):
        char = inputs[i:i+6]
        if char == NUMBER:
            isNumber = True
        elif char == CAPITAL:
            isCapital = True
        elif char == SPACE:
            english += " "
            isNumber = False
        elif isNumber and char in TO_NUMBERS:
            english += TO_NUMBERS[char]
        elif char in TO_LETTERS:
            letter = TO_LETTERS[char]
            if isCapital:
                letter = letter.upper()
                isCapital = False
            english += letter
        else:
            print("incorrect input")
    return english


def is_brail(inputs):
    for i in inputs:
        if len(i) % 6 != 0:
            return False
        for char in i:
            if char not in ["O", "."]:
                return False
    return True


if __name__ == "__main__":
    inputs = sys.argv[1:]
    if is_brail(inputs):
        result = brail_to_english(inputs)
    else:
        result = english_to_brail(inputs)

    print(result)
