import sys

# Dicts used to decode/encode
brailleLetterDict = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    " ": "......"
}
brailleNumDict = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}
brailleModeDict = {
    "capital_follows": ".....O",
    "number_follows": ".O.OOO"
}

# Returns the letter/number decoded from the braille character
def decode( brailleChar, mode, capitalize ):
    if ( mode == "capital_follows"):
        for letter, braille in brailleLetterDict.items():
            if braille == brailleChar:
                if( capitalize ):
                    return letter
                else:
                    return letter.lower()
                
    if ( mode == "number_follows"):
        for num, braille in brailleNumDict.items():
            if braille == brailleChar:
                return num


def parse_braille( arg ):
    # mode == "capital_follows" or number_follows
    # It will keep track of which type of braille symbols
    # will be read next. 
    mode = ""
    capitalize = False

    result = ""
    for i in range(0, len(arg), 6):
        brailleChar = arg[i:i+6]

        # Verify that the braille character is not a new mode
        modeChanged = False
        for brailleMode, braille in brailleModeDict.items():
            if braille == brailleChar:
                mode = brailleMode
                capitalize = True
                modeChanged = True
                break
        
        # Only decode if the mode is set and if it has not just changed
        if (mode != "" and not modeChanged):
            result += decode(brailleChar, mode, capitalize)
            capitalize = False

    print(result)


def parse_english( args ):
    result = ""

    mode = ""
    for word in args:
        for c in word:
            if ( c.isdigit() ):
                if ( mode != "number_follows"):
                    mode = "number_follows"
                    result += brailleModeDict["number_follows"]
                
                result += brailleNumDict[c]
            else:
                if ( c.upper() == c):
                    result += brailleModeDict["capital_follows"]
                    result += brailleLetterDict[c.upper()]
                else:
                    result += brailleLetterDict[c.upper()]
        
        result += brailleLetterDict[" "]
        # Add a space after each word

    # Remove the additional last space
    print(result[:-6])
    

if __name__ == '__main__':
    # Determine if the given string is English or Braille
    # by verifying if the input only contains '.' and 'O'
    # and if the number of characters are a multiple of 6
    text = ""
    try:
        if (len(sys.argv) > 2 ):
            parse_english(sys.argv[1:])
            exit 
        else:
            text = sys.argv[1]
    except IndexError:
        exit

    test = text.replace(".", "")
    test = test.replace("O", "")
    if ( len(test) == 0 and len(text) % 6 == 0):
        parse_braille(text)
    else:
        parse_english([text])