import sys

#mapping braille cells to english letters
brailleToEnglishLetter = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
    ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", "......": " ", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(", ".O.OO.": ")"
}

#mapping braille cells to numbers
brailleToEnglishNumber = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

#mapping english letters to braille cells
englishToBrailleLetter = {v : k for k, v in brailleToEnglishLetter.items()}

#mapping numbers to braille cells
englishToBrailleNumber = {v : k for k, v in brailleToEnglishNumber.items()}

def printEnglishTranslation(input):
    """
    A function that prints the english translation of a message written in braille
    
    Parameters:
    input (string): The message written in braille
    """

    capitalFollows, numberFollows = False, False

    for i in range(0, len(input), 6): #traversing through every braille cell
        character = input[i:i + 6]    #the braille cell

        if character == ".....O":     #if we are met with a capital follows character
            capitalFollows = True
        elif character == ".O.OOO":   #if we are met with a number follows character
            numberFollows = True
        elif capitalFollows:
            print(brailleToEnglishLetter[character].upper(), end="")
            capitalFollows = False    #only one character is capitalized
        elif numberFollows:
            if brailleToEnglishLetter[character] != " ": 
                print(brailleToEnglishNumber[character], end="")
            else:
                print(" ", end="")
                numberFollows = False #every braille cell until the next space represents a number
        else:
            print(brailleToEnglishLetter[character], end="")

def printBrailleTranslation(input):
    """
    A function that prints the braille translation of a message written in english
    
    Parameters:
    input (string): The message written in english
    """

    i = 0
    
    while i < len(input):
        character = input[i]

        if character.isupper():      # if a character is an uppercase, a capital follows character must be added
            print(".....O" + englishToBrailleLetter[character.lower()], end="")
            i += 1
        elif character.isnumeric():  # if a character is a number, a number follows character must be added
            print(".O.OOO", end="")
            while i < len(input) and character.isnumeric():
                print(englishToBrailleNumber[character], end="")
                i += 1
                character = input[i]
        else:
            print(englishToBrailleLetter[character], end="")
            i += 1

def isBraille(input):
    """
    A function that checks if a message is written in braille or not
    
    Parameters:
    input (string): The message

    Returns:
    boolean: True if the message is most likely written in braille, False otherwise
    """

    for i in range(len(input)):
        if input[i] != "O" and input[i] != ".":
            return False
        
    return True

if __name__ == "__main__":
    input = " ".join(sys.argv[1:])
    if isBraille(input):
        printEnglishTranslation(input)
    else:
        printBrailleTranslation(input)