
"""
Matthew Ackroyd
email: matt.ackroyd04@gmail.com
"""

import sys

symbolBraillePairs = {
    "A": "O.....",  "B": "O.O...",  "C": "OO....",  "D": "OO.O..",
    "E": "O..O..",  "F": "OOO...",  "G": "OOOO..",  "H": "O.OO..",
    "I": ".OO...",  "J": ".OOO..",  "K": "O...O.",  "L": "O.O.O.",
    "M": "OO..O.",  "N": "OO.OO.",  "O": "O..OO.",  "P": "OOO.O.",
    "Q": "OOOOO.",  "R": "O.OOO.",  "S": ".OO.O.",  "T": ".OOOO.",
    "U": "O...OO",  "V": "O.O.OO",  "W": ".OOO.O",  "X": "OO..OO",
    "Y": "OO.OOO",  "Z": "O..OOO",  "1": "O.....",  "2": "O.O...",
    "3": "OO....",  "4": "OO.O..",  "5": "O..O..",  "6": "OOO...",
    "7": "OOOO..",  "8": "O.OO..",  "9": ".OO...",  "0": ".OOO..",
    "Cap": ".....O","Dec": ".O...O","Num": ".O.OOO",".": "..OO.O",
    ",": "..O...",  "?": "..O.OO",  "!": "..OOO.",  ":": "..OO..",
    ";": "..O.O.",  "-": "....OO",  "/": ".O..O.",  "<": ".OO..O",
    ">": "O..OO.",  "(": "O.O..O",  ")": ".O.OO.",  " ": "......"}

brailleNumberPairs = {
    "O.....": "1",  "O.O...": "2",  "OO....": "3",  "OO.O..": "4",
    "O..O..": "5",  "OOO...": "6",  "OOOO..": "7",  "O.OO..": "8",
    ".OO...": "9",  ".OOO..": "0",  "......": " ",".O...O": "Dec"}

def BrailleToEnglish(string):
    output = ""
    count = 0
    capFollows = False
    numFollows = False

    # For loop equivalent with increments of 6
    while count < len(string):
        value = string[count:count + 6]

        # if expecting a number grab from the correct key
        if numFollows:
            currentLetter = brailleNumberPairs.get(value)
        else:
            # Use the Value of the dict to grab the key
            currentLetter = list(symbolBraillePairs.keys())[list(symbolBraillePairs.values()).index(value)]

        # If current char is a space end the number sequence
        if currentLetter == " ":
            numFollows = False

        # If a decimal follows symbol is found replace it with "."
        if currentLetter == "Dec":
            currentLetter = "."

        if currentLetter == "Num":
            numFollows = True

        elif currentLetter == "Cap":
            capFollows = True

        else:
            # If the last char was a Cap char then capitalize this letter, if not then ensure its lowercase
            if capFollows == True:
                output += currentLetter.capitalize()
                capFollows = False
            else:
                output += currentLetter.lower()

        # increment the loop by 6 to grab the next set of 6 chars
        count += 6

    return output


def EnglishToBraille(string):
    output = ""
    numberFollows = False

    # Loop through every character in the input
    for x in string:
        # Check if it's a number if so insert a num follows symbol before the number
        if x.isnumeric() and numberFollows == False:
            numberFollows = True
            output += symbolBraillePairs.get("Num")

        elif x == " ":                          # If a Space Is encountered while a number is being outputted, then stop
            numberFollows = False

        elif numberFollows == True and x == ".":  # If A "." is encountered while outputting a number replace it with a
            x = "Dec"                             # dec follows symbol

        # if the letter is capitalized then insert a Cap Follows symbol before it
        elif x.isupper():
            output += symbolBraillePairs.get("Cap")

        # add to the output
        output += symbolBraillePairs.get(x.capitalize())

    # Return the output
    return output


def main(string):
    # Loop through the characters of the string input and check to if there is any character other than "." or "O"
    # if so then the input must be a word and need to be translated to braille
    for char in string:
        if char != "O" and char != ".":
            print(EnglishToBraille(string))
            sys.exit(0)

    # if the test for the string bring a word fails, then it must be Braille in need to translation to english
    # then test if the string is divisible by 6 to make sure that it's a valid input
    if len(string) % 6 == 0:
        print(BrailleToEnglish(string))


if __name__ == "__main__":
    # Check there are args, then group everything but the first arg
    if len(sys.argv) > 1:
        args = ""
        for string in sys.argv:
            if string != sys.argv[0]:
                args += string + " "

        main(args.strip())
