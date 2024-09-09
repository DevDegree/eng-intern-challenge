import sys
input = sys.argv[1:]
input = " ".join(input)  #Concat the input arguments into a single string

#Mapping Braille patterns to numbers
bnum = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}
#Mapping Braille patterns to letters and control codes
b = {
    "O.....": "A",
    "O.O...": "B",
    "OO....": "C",
    "OO.O..": "D",
    "O..O..": "E",
    "OOO...": "F",
    "OOOO..": "G",
    "O.OO..": "H",
    ".OO...": "I",
    ".OOO..": "J",
    "O...O.": "K",
    "O.O.O.": "L",
    "OO..O.": "M",
    "OO.OO.": "N",
    "O..OO.": "O",
    "OOO.O.": "P",
    "OOOOO.": "Q",
    "O.OOO.": "R",
    ".OO.O.": "S",
    ".OOOO.": "T",
    "O...OO": "U",
    "O.O.OO": "V",
    ".OOO.O": "W",
    "OO..OO": "X",
    "OO.OOO": "Y",
    "O..OOO": "Z",
    ".....O": "capital follows",  #Code for capital letters
    ".O.OOO": "number follows",  #Code for numbers
    "......": "space"  #Space character
}
#Reverse dictionary mapping letters and numbers to Braille patterns
engval = {
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
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    "capital follows": ".....O",
    "number follows": ".O.OOO",
    "space": "......"
}

#Check that the input is braille
def is_braille(text):
    if(len(text) % 6 != 0):  #Braille code must be a multiple of 6 characters
        return False

    for i in range(0, len(text), 6):
        cur = text[i:i+6]
        if(cur not in b and cur not in bnum):  #Check validity of segments
            return False

    return True

#If the input is not Braille, convert text to Braille
if(is_braille(input) == False):
    out = ""
    num = False  #Number mode flag

    for i in range(0, len(input)):
        if(input[i].isupper()):  #Handle capitals
            out += engval["capital follows"]
            out += engval[input[i]]
        elif(input[i].isdigit() and num == False):  #Handle numbers
            out += engval["number follows"]
            out += engval[input[i]]
            num = True  #Activate number mode
        elif(input[i].isspace()):  #Handle spaces
            out += engval["space"]
            num = False  #Deactivate number mode
        else:  #Handle lowercase letters
            out += engval[input[i].upper()]
    print(out)

#If input is Braille, convert Braille to text
else: 
    out = ""
    num = False  #Create flag to track if the number mode is active
    cap = False  #Capital mode flag

    for i in range(0, len(input), 6):
        cur = input[i:i+6]

        if(b[cur] == "number follows"):  #Handle number mode
            num = True
        elif(b[cur] == "capital follows"):  #Handle capital mode
            cap = True
        elif(b[cur] == "space"):  #Handle spaces
            out += " "
            num = False  #Deactivate number mode
        elif(num == True):  #Handle numbers
            out += bnum[cur]
        elif(cap == True):  #Handle capital letters
            out += b[cur]
            cap = False  #Deactivate capital mode
        else:  #Handle lowercase letters
            out += b[cur].lower()
    print(out)