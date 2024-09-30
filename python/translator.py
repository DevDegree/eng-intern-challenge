import argparse
import sys

brailleMap = {
    "a":"O.....", "b":"O.O...", "c":"OO....", "d":"OO.O..", 
    "e":"O..O..", "f":"OOO...", "g":"OOOO..", "h":"O.OO..",
    "i":".OO...", "j":".OOO..", "k":"O...O.", "l":"O.O.O.",
    "m":"OO..O.", "n":"OO.OO.", "o":"O..OO.", "p":"OOO.O.",
    "q":"OOOOO.", "r":"O.OOO.", "s":".OO.O.", "t":".OOOO.",
    "u":"O...OO", "v":"O.O.OO", "w":".OOO.O", "x":"OO..OO", 
    "y":"OO.OOO", "z":"O..OOO", "1":"O.....", "2":"O.O...",
    "3":"OO....", "4":"OO.O..", "5":"O..O..", "6":"OOO...",
    "7":"OOOO..", "8":"O.OO..", "9":".OO...", "O":".OOO..", 
    "capitalFollows":".....O", "decimalFollows":".O...O", "numberFollows":".O.OOO", " ":"......"
}

alphaMap = {} # takes in alphabet characters and special condition characters as keys and br equivalents as values
numberMap = {} # takes in numbers and space as keys and br equivalents as values

for k, v in brailleMap.items(): #reversing dictionary 
    if k.isnumeric() or k == " ": 
        numberMap[v] = k 
    else: 
        alphaMap[v] = k

def alphaToBr(inputString):
    """With an input string of alphabet characters, 
    this function converts the input into its Braille equivalent as a string 

    Parameters
    ----------
    inputString : str
        A given input of English string with alphanumeric values and decimals 

    """
    res = ""
    numberFollows = True
    for c in inputString: 
        if c.isalpha(): # if c is a letter 
            if c.isupper():
                res += brailleMap["capitalFollows"]
            res += brailleMap[c.lower()]
        elif c.isnumeric(): #if c is a number
            if numberFollows:
                res += brailleMap["numberFollows"]
                numberFollows = False 
            res += brailleMap[c]
        else: # if c is a special character 
            if c == ".":
                res += brailleMap["decimalFollows"] # checking if its a decimal value 
            res += brailleMap[c]
            if c == " ": 
                if not numberFollows:
                    numberFollows = True
    return res

def brToAlpha(inputString): 
    """With an input string of . or O characters, 
    this function converts the input into its alphabet equivalent as a string.

    Parameters
    ----------
    inputString : str
        A given input of brallie values with . or O characters 

    Raises
    ------
    Exception
        If the length of argument mod 6 != 0 
    """
    if len(inputString) % 6 != 0: 
        raise Exception("invalid string")

    asList = [] 
    for i in range(0, len(inputString)-1, 6): #setting up as list 
        asList.append(inputString[i: i+6])
    res = ""

    isCapital = False # flags to keep track of 
    isDecimal = False 
    isNumber = False 

    for br in asList:
        print(res)
        if br == ".....0": # capitalFollows
            isCapital = True   
        elif br == ".0...0": # decimalFollows 
            isDecimal = True
        elif br == ".0.000": # numberFollows 
            isNumber = True 
        else: # none of the above 
            if isCapital: 
                res += alphaMap[br].upper()
                isCapital = False 
            elif isDecimal: 
                res += "."
                isDecimal = False
            elif isNumber:
                if br == "......": # checking for space 
                    isNumber = False 
                res += numberMap[br]
            elif br == "......":
                res += " "
            else: 
                res += alphaMap[br]
    return res

def main():
    if len(sys.argv) > 1:
        input_strings = sys.argv[1:]
        combined_input = " ".join(input_strings)
        isAlphaToBr = False 

        if len(combined_input) % 6 != 0: # Determining what type of input it is 
            isAlphaToBr = True
        else: 
            for c in combined_input: 
                if c != "O" and c != ".": 
                    isAlphaToBr = True
                    break

        if isAlphaToBr:
            print(alphaToBr(combined_input))
            return alphaToBr(combined_input)
        else:
            print(brToAlpha(combined_input))
            return brToAlpha(combined_input)

if __name__ == '__main__':
    main()
