# in order to input arguments 
import sys

englishCharToBraile = {
    # lowercase alpha
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", 
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", 
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", 
    "y": "OO.OOO", "z": "O..OOO", 

    # numbers
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", 
    "9": ".OO...", "0": ".OOO..",

    # symbols
    " ": "......", ".": ".O..OO", ",": "..O...", "?": "O..O.O", "!": "..OOO.", "'": ".....O", "-": "....OO", ":": "O...OO", ";": "O.O..O", 
    "/": ".O.O.O", "(": ".OO.OO", ")": ".OO.OO",

    # capitalization, decimal, and number follows symbols
    "capital follows": ".....O", "decimal follows": ".O...O", "number follows": ".O.OOO"
}


brailleCharToEnglish = {
    # lowercase alpha
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
    ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", 
    "OO.OOO": "y", "O..OOO": "z",

    # symbols
     "......":" ", ".O..OO": ".", "..O...": ",", "O..O.O": "?", "..OOO.": "!", ".....O": "'", "....OO": "-", "O...OO": ":", "O.O..O": ";", 
    ".O.O.O": "/", ".OO.OO": "(", ".OO.OO": ")",

    # Capitalization and numbers follow symbols
    ".....O": "capital follows", ".O...O": ".", ".O.OOO": "number follows"
}

# call if they come after number follows
brailleNumToEnglish = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", 
    ".OO...": "9", ".OOO..": "0", ".O...O": "."
}


def main(): 
    # check if any english characters
    userInput = sys.argv[1]
    isEnglish = False
    for c in userInput: 
            if (c != 'O') and (c != '.'):
                isEnglish = True
                break

    # combine all args into one string
    fullString = ' '.join(sys.argv[1:])   
    if(isEnglish):
        printEnglishToBraile(fullString)
    else:
        printBraileToEnglish(fullString)

#english to braile mapping
def printEnglishToBraile(english: str): 
    braile: str = ''
    isNum = False
    for c in english:
        # if uppercase
        if c.isupper():
            braile += englishCharToBraile["capital follows"]
            c = c.lower()

        # space to break the is a num
        if c == ' ':
            isNum = False

       
        if c.isdigit():
            # if num first number in sequence
            if(not isNum): 
                isNum = True
                braile += englishCharToBraile["number follows"]
        
        # decimal follows rather than period during a number
        if isNum and c == '.': 
            braile += englishCharToBraile["decimal follows"]
            continue

        braileChar = englishCharToBraile[c]
        braile += braileChar

    print(braile)


def printBraileToEnglish(braile: str):
    english : str = ''
    isNum = False
    isCapital = False

    # skip 6 characters at a time
    for c in range(0, len(braile), 6):
        chars = braile[c: c+6]
        englishTranslation = brailleCharToEnglish[chars]

        if englishTranslation == "number follows": 
            isNum = True
            continue
        if englishTranslation == "capital follows":
            isCapital = True
            continue

        if isCapital:
            english += englishTranslation.upper()
            isCapital = False
        elif isNum:
            english += brailleNumToEnglish[chars]    
        else:
            english += englishTranslation
            if englishTranslation == " ":
                isNum = False 
    print(english)

if __name__ == "__main__":
    main()


