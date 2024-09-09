import sys

if __name__ == "__main__":
    BRAILLE_LETTERS = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OO..OO", "OOOOO.", "O.OOO.", ".OO..O", ".OO.O.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO", "..OO.O", "..O...", "..O.OO", "..OOO.", "..OO..", "..O.O.", "....OO", ".O..O.", ".OO..O", "O..OO.", "O.O..O", ".O.OO.", "......"]
    ALPHABET_LETTERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ".", ",", "?", "!", ":", ";", "-", "/", "<", ">", "(", ")", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    CAPITAL_FOLLOWS = ".....O"
    DECIMAL_FOLLOWS = ".O...O"
    NUMBER_FOLLOWS = ".O.OOO"
    NUMBER_OF_LETTERS = 39
    NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    # Assumption is that decimal follows will follow a number follows in all cases

    inputString = input()
    outputString = ""
    english = False
    doNothing = False
    numberMode = False

    for char in ALPHABET_LETTERS:
        if char != "O" and char != ".":
            if char in inputString or char.lower() in inputString:
                english = True
    if english == True:
        for i in range(len(inputString)):
            char = inputString[i]
            # Upper case letter
            if char.isupper():
                outputString += CAPITAL_FOLLOWS
                index = ALPHABET_LETTERS.index(char)
                # char is A, B, C, D, E, F, G, H, I, or J
                if (index >= NUMBER_OF_LETTERS):
                        index -= NUMBER_OF_LETTERS
                outputString += BRAILLE_LETTERS[index]
            # Number
            elif char in NUMBERS:
                if numberMode == False:
                    outputString += NUMBER_FOLLOWS
                    numberMode = True
                index = ALPHABET_LETTERS.index(char)
                outputString += BRAILLE_LETTERS[index]
            # Lower case letter or symbol
            else:
                # Decimal case
                if char == ".":
                    if i < len(inputString)-1 and inputString[i+1] in NUMBERS:
                        index = ALPHABET_LETTERS.index(char)
                        outputString += DECIMAL_FOLLOWS
                        outputString += NUMBER_FOLLOWS
                        outputString += BRAILLE_LETTERS[index]
                else:
                    index = ALPHABET_LETTERS.index(char.capitalize())
                    # Space case
                    if index == 38:
                        if numberMode == True:
                            numberMode = False
                    # char is A, B, C, D, E, F, G, H, I, or J
                    if index >= NUMBER_OF_LETTERS:
                            index -= NUMBER_OF_LETTERS
                    outputString += BRAILLE_LETTERS[index]
    else:
        # Assumptions: inputString has length that is a multiple of 6 and if
        # capital follows, number follows, or decimal follows is read,
        # then there must be a next character
        for i in range(int(len(inputString)//6)):
            if doNothing:
                doNothing = False
                continue
            char = inputString[6*i:6*i+6]
            if char == CAPITAL_FOLLOWS:
                newChar = inputString[6*i+6:6*i+12]
                index = BRAILLE_LETTERS.index(newChar)
                if (index <= 9):
                    index += NUMBER_OF_LETTERS
                outputString += ALPHABET_LETTERS[index]
                doNothing = True
            elif char == DECIMAL_FOLLOWS:
                outputString += "."
            elif char == NUMBER_FOLLOWS:
                numberMode = True
            elif numberMode == True:
                if char == "......":
                    numberMode = False
                    outputString += " "
                else:
                    outputString += ALPHABET_LETTERS[BRAILLE_LETTERS.index(char)]
            else:
                index = BRAILLE_LETTERS.index(char)
                if (index <= 9):
                    index += NUMBER_OF_LETTERS
                outputString += ALPHABET_LETTERS[index].lower()
    print(outputString)