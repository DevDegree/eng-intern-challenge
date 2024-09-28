import sys

# Braille and corresponding English letters and numbers
biAlphArr = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO", "..OO.O", "..O...", "..O.OO", "..OOO.", "..OO..", "..O.O.", "....OO", ".O..O.", ".OO..O", "O..OO.", "O.O..O", ".O.OO.", "......"]
biNumArr = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO.."]
biSpecArr = [".....O", ".O...O", ".O.OOO"]
nomAlphArr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z",".",",","?","!",":",";","-","/","<",">","(",")"," "]
nomNumArr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


# Function to convert Braille to English
def braille_to_english(userInput):
    output = ""
    i = 0
    while i < len(userInput):
        if i + 5 < len(userInput):
            letter = userInput[i:i + 6]

            if letter in biSpecArr:
                if letter == biSpecArr[0]:  # Capital letter
                    i += 6
                    letter2 = userInput[i:i + 6]
                    if letter2 in biAlphArr:
                        output += nomAlphArr[biAlphArr.index(letter2)]
                    else:
                        output += "[Unknown Pattern]"
                elif letter == biSpecArr[1]:  # Period
                    output += "."
                    i += 6
                elif letter == biSpecArr[2]:  # Number
                    i += 6
                    letter2 = userInput[i:i + 6]
                    if letter2 in biNumArr:
                        output += nomNumArr[biNumArr.index(letter2)]
                    else:
                        output += "[Unknown Number]"
            else:
                if letter in biAlphArr:
                    output += nomAlphArr[biAlphArr.index(letter)].lower()
                else:
                    output += "[Unknown Pattern]"
        i += 6
    return output


# Function to convert English to Braille
def english_to_braille(userInput):
    output = ""
    for i in range(len(userInput)):
        if (userInput[i] in nomAlphArr) and (nomAlphArr.index(userInput[i])<26):
            output += ".....O"+biAlphArr[nomAlphArr.index(userInput[i].upper())]
        elif userInput[i].upper() in nomAlphArr:
            output += biAlphArr[nomAlphArr.index(userInput[i].upper())]
        elif userInput[i] in nomNumArr:
            if i==0:
                output += ".O.OOO" + biNumArr[nomNumArr.index(userInput[i])]
            elif userInput[i-1] not in nomNumArr:
                output += ".O.OOO" + biNumArr[nomNumArr.index(userInput[i])]

            else:
                output += biNumArr[nomNumArr.index(userInput[i])]

        elif userInput[i] == ".":
            output += ".O...O"
    return output


# Main logic to determine input type and translate
def main():
    input_text = ' '.join(sys.argv[1:]).strip()

    if set(input_text).issubset({'O', '.'}):
        translated_text = braille_to_english(input_text)
    else:
        translated_text = english_to_braille(input_text)

    print(translated_text)


if __name__ == "__main__":
    main()
