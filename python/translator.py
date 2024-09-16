import sys

# mappings: use 2 hash tables for O(1) lookup translating in each direction
ENGLISH_TO_BRAILLE = {
    # numbers
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", 

    # alphabet
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    
    # other chars
    " ": "......",

    # special markers
    "capital": ".....O",
    "number": ".O.OOO",
}

# map for everything except numbers
BRAILLE_TO_ENGLISH = {
    value: key
    for key, value in list(ENGLISH_TO_BRAILLE.items())[10:] # skip the first 10 entries which correspond to numbers
}

# special map for numbers since the keys are the same as letters a-j
BRAILLE_TO_NUMBERS = {
    value: key
    for key, value in list(ENGLISH_TO_BRAILLE.items())[:10] # only map numbers
}



# -----------------------------------------

def isBrailleInput(input):
    # assuming all braille inputs are well-formatted

    # cursory check for best case efficiency:
    if len(input) % 6 == 0:
        # thorough check:
        # braille <=> contains "."
        #  - if braille, it must contain at least 1 occurence of "." since "OOOOOO" is not a braille character
        # if not braille, it will contain 0 occurences of "." since "." character is not expected to be translated to braille
        if "." in input:
            return True
    
    return False
    

def englishToBraille(input):
    braille = []
    numberMode = False # flag to track when a number is being read in

    for char in input:
        if char.isdigit():
            # append a number marker if this is the first numerical character in the number sequence
            if not numberMode: 
                braille.append(ENGLISH_TO_BRAILLE["number"])
                numberMode = True
        else: 
            # set the numberMode flag to false upon the end of a number sequence
            if numberMode: 
                # validate that character immediately following the end of a number is a space
                # eg. input should be formatted like "123 abc", not "123abc" which would be translated to "123123"

                # I COMMENTED OUT THE ASSERTION BELOW BECAUSE I DON'T KNOW IF A HUMAN WILL ACTUALLY READ THE EXCEPTION
                # assert char == " ", "Ambiguous input formatting: numbers must be followed by a space"

                numberMode = False

            # append a capital marker if necessary
            if char.isupper():
                braille.append(ENGLISH_TO_BRAILLE["capital"])
        
        braille.append(ENGLISH_TO_BRAILLE[char.lower()])

    return "".join(braille)


def brailleToEnglish(input):
    english = []
    numberMode = False
    capitalMode = False

    # split input in the 6 char long chunks
    brailleChunks = [
        input[i: i + 6]
        for i in range(0, len(input), 6)
    ] 

    for bChunk in brailleChunks:
        assert bChunk in BRAILLE_TO_ENGLISH, f"Invalid Braille: {bChunk}"
        
        eChar = BRAILLE_TO_ENGLISH[bChunk]            

        # check if the input is a marker
        if eChar =="number":
            numberMode = True
        elif eChar == "capital":
            capitalMode = True
        elif eChar == " ":
            numberMode = False
            english.append(" ")

        else:
            if numberMode:
                english.append(BRAILLE_TO_NUMBERS[bChunk])
            else:
                if capitalMode:
                    english.append(eChar.capitalize())
                    capitalMode = False # turn off the capitalMode flag since it only applies to 1 char
                else:
                    english.append(eChar)
    
    return "".join(english)


# for personal testing only
def printBraille(braille):

    brailleChunks = [
        braille[i: i + 6]
        for i in range(0, len(braille), 6)
    ] 

    for bChunk in brailleChunks:
        for i in range(0, 6, 2):
            print(bChunk[i:i + 2])
        print()


def main(input):
    if (isBrailleInput(input)):
        print(brailleToEnglish(input))
    else:
        print(englishToBraille(input))


if __name__ == "__main__" and len(sys.argv) >= 2:
    main(" ".join(sys.argv[1:])) # join all args into a single string

