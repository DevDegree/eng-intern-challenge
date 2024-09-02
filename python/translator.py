import sys

#mapping English letters to braille characters
toBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.",
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",

    #mapping capital letters, numbers, and spaces to braille characters for full translation support
    "caps": ".....O", "number": ".O.OOO", " ": "......",
}

toLetter = {}
for k, v in toBraille.items():
    toLetter[v] = k

#mapping numbers to braille characters
numBraille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}

brailleNum = {}
for k, v in numBraille.items():
    brailleNum[v] = k

#translates an English string to Braille text
#Iterates through each character of the input string, converts uppercase to lowercase
#Uses the dictionary to obtain the Braille equivalent of the character and concatenates the characters into an output string
def brailleTranslate(input):
    output = ""
    number = False
    for i in range(len(input)):
        j = input[i]
        if input[i].isupper():
            output += toBraille["caps"]
            j = j.lower()
        if input[i].isdigit() and not number:
            output += toBraille["number"]
            number = True
        if j == " ":
            output += toBraille[" "]
            number = False
        elif j in toBraille:
            output += toBraille[j]
        elif j in numBraille:
            output += numBraille[j]
    return output

#translates a Braille string to English text
#processes 6 characters at a time (length of each Braille character)
#converts the Braille characters into their corresponding English letter, number, or space
def engTranslate(input):
    output = ""
    number = False
    i = 0
    while i < len(input):
        j = input[i : i + 6]
        if j == "......":
            output += " "
            number = False
        elif j == ".....O":
            output += toLetter[input[i + 6 : i + 12]].upper()
            i += 6
        elif toLetter[j] == "number":
            number = True
        else:
            if number:
                output += brailleNum[j]
            else:
                output += toLetter[j]
        i += 6
    return output

#process inputs to determine if the text is English or Braille, then translates accordingly and outputs the translation
def main():
    if len(sys.argv) >= 2:
        input = " ".join(sys.argv[1:])
        english = any(char not in [".", "O", " "] for char in input)

        if english:
            result = brailleTranslate(input)
        else:
            result = engTranslate(input)

        print(result)


if __name__ == "__main__":
    main()