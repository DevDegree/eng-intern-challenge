import sys

#Create maps for english to braille, braille to english, and number and english equivalence
ENGLISH_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", 
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", 
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", 
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", " ": "......"
}

BRAILLE_TO_ENGLISH = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h", 
    ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", 
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", 
    "OO.OOO": "y", "O..OOO": "z", "......": " "
}

LETTER_TO_NUMBER = { "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "0" }

#Declare capital and number braille separately for easier access when comparing
CAPITAL_BRAILLE = ".....O"
NUMBER_BRAILLE = ".O.OOO"

def isBraille(input):
    for char in input:
        if not (char == "." or char == "O"):
            return False
    return True

def brailleToEnglish(input):
    res = ""
    capitalizeNext = False
    numberNext = False
    
    #Iterate every 6 to get the braille representation of a symbol
    for i in range(0, len(input), 6):
        brailleSymbol = input[i:i+6]

        #Check if next needs to be capitalized or if the following will be a number
        if brailleSymbol == CAPITAL_BRAILLE:
            capitalizeNext = True
        elif brailleSymbol == NUMBER_BRAILLE:
            numberNext = True
        elif brailleSymbol in BRAILLE_TO_ENGLISH:
            #Get the english representation of the braille
            symbol = BRAILLE_TO_ENGLISH[brailleSymbol]

            #If is a space, number is over and add the space
            #If numberNext, get the number instead of the letter
            #If capitalizeNext, capitalize the letter
            if symbol == " ":
                numberNext = False
            elif numberNext:
                symbol = LETTER_TO_NUMBER[symbol]
            elif capitalizeNext:
                symbol = symbol.upper()
                capitalizeNext = False

            res += symbol
        else:
            return "Invalid input provided"

    return res

def englishToBraille(input):
    res = ""
    capitalizeNext = False
    numberNext = False

    for char in input:
        #If is a space, number is over and add the space braille
        #If is a number, put in the number next braille and the number braille
        #If is a capital, put in the capital next braille and the lower case letter braille
        #If isn't a number or capital, add regularly
        if char == " ":
            numberNext = False
            res += ENGLISH_TO_BRAILLE[" "]
        elif char.isdigit():
            if not numberNext:
                res += NUMBER_BRAILLE
                numberNext = True

            res += ENGLISH_TO_BRAILLE[char]
        elif char.lower() in ENGLISH_TO_BRAILLE:
            if char.isupper():
                res += CAPITAL_BRAILLE

            res += ENGLISH_TO_BRAILLE[char.lower()]
        else:
            return "Invalid input provided"

    return res

def main():
    #Check for no input
    if len(sys.argv) == 1:  
        print("No input provided")
        return

    input = " ".join(sys.argv[1:])

    #Check whether the string is braille or english
    if isBraille(input):
        #If string is braille, check for validity on length
        if len(input) % 6 != 0:
            print("Invalid input provided")
            return

        #Translate and output
        print(brailleToEnglish(input))
    else:
        print(englishToBraille(input))

if __name__ == "__main__":
    main()