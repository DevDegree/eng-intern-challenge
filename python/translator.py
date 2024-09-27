import sys
# brailletochar searches the braille dictionary and returns the correct character
#   based on if it is a number, capital, or lowercase.
def brailletochar(b6, cap, num):
    bdict = {
        "O.....": ("a", "A", "1"),
        "O.O...": ("b", "B", "2"),
        "OO....": ("c", "C", "3"),
        "OO.O..": ("d", "D", "4"),
        "O..O..": ("e", "E", "5"),
        "OOO...": ("f", "F", "6"),
        "OOOO..": ("g", "G", "7"),
        "O.OO..": ("h", "H", "8"),
        ".OO...": ("i", "I", "9"),
        ".OOO..": ("j", "J", "O"),
        "O...O.": ("k", "K"),
        "O.O.O.": ("l", "L"),
        "OO..O.": ("m", "M"),
        "OO.OO.": ("n", "N"),
        "O..OO.": ("o", "O"),
        "OOO.O.": ("p", "P"),
        "OOOOO.": ("q", "Q"),
        "O.OOO.": ("r", "R"),
        ".OO.O.": ("s", "S"),
        ".OOOO.": ("t", "T"),
        "O...OO": ("u", "U"),
        "O.O.OO": ("v", "V"),
        ".OOO.O": ("w", "W"),
        "OO..OO": ("x", "X"),
        "OO.OOO": ("y", "Y"),
        "O..OOO": ("z", "Z"),
        "......": (" ", " "," "),
        "..OO.O": (".", ".", "."),
        "..O...": (",", ",", ","),
        "..O.OO": ("?", "?", "?"),
        "..OOO.": ("!", "!", "!"),
        "..OO..": (":", ":", ":"),
        "..O.O.": (";", ";", ";"),
        "....OO": ("-", "-", "-"),
        ".O..O.": ("/", "/", "/"),
        "O.O..O": ("(", "(", "("),
        ".O.OO.": (")", ")", ")"),        
        
    } 
    if num:
        return bdict[b6][2] 
    if cap:
        return bdict[b6][1]
    else:
        return bdict[b6][0]
# chartobraille returns the correct braille equivalent for the single character param
def chartobraille(char):
    cdict = {
        "a": "O.....",
        "A": ".....OO.....",
        "1": "O.....",
        "b": "O.O...",
        "B": ".....OO.O...",
        "2": "O.O...",
        "c": "OO....",
        "C": ".....OOO....",
        "3": "OO....",
        "d": "OO.O..",
        "D": ".....OOO.O..",
        "4": "OO.O..",
        "e": "O..O..",
        "E": ".....OO..O..",
        "5": "O..O..",
        "f": "OOO...",
        "F": ".....OOOO...",
        "6": "OOO...",
        "g": "OOOO..",
        "G": ".....OOOOO..",
        "7": "OOOO..",
        "h": "O.OO..",
        "H": ".....OO.OO..",
        "8": "O.OO..",
        "i": ".OO...",
        "I": ".....O.OO...",
        "9": ".OO...",
        "j": ".OOO..",
        "J": ".....O.OOO..",
        "O": ".OOO..",
        "k": "O...O.",
        "K": ".....OO...O.",
        "l": "O.O.O.",
        "L": ".....OO.O.O.",
        "m": "OO..O.",
        "M": ".....OOO..O.",
        "n": "OO.OO.",
        "N": ".....OOO.OO.",
        "o": "O..OO.",
        "O": ".....OO..OO.",
        "p": "OOO.O.",
        "P": ".....OOOO.O.",
        "q": "OOOOO.",
        "Q": ".....OOOOOO.",
        "r": "O.OOO.",
        "R": ".....OO.OOO.",
        "s": ".OO.O.",
        "S": ".....O.OO.O.",
        "t": ".OOOO.",
        "T": ".....O.OOOO.",
        "u": "O...OO",
        "U": ".....OO...OO",
        "v": "O.O.OO",
        "V": ".....OO.O.OO",
        "w": ".OOO.O",
        "W": ".....O.OOO.O",
        "x": "OO..OO",
        "X": ".....OOO..OO",
        "y": "OO.OOO",
        "Y": ".....OOO.OOO",
        "z": "O..OOO",
        "Z": ".....OO..OOO",
        " ": "......",
        ".": "..OO.O",
        ",": "..O...",
        "?": "..O.OO",
        "!": "..OOO.",
        ":": "..OO..",
        ";": "..O.O.",
        "-": "....OO",
        "/": ".O..O.",
        "<": ".OO..O",
        ">": "O..OO.",
        "(": "O.O..O",
        ")": ".O.OO."
    } 
    return cdict[char]
# brailletostring takes a braille string and translates it to a word string using
#   brailletochar
def brailletostring(braille):
    
    length = len(braille)
    chari = 0
    string = ""
    cap = False #Captial follows variable
    num = False #Number follows variable
    while(chari * 6 < length):
        if braille[chari*6: chari*6 + 6] == ".O.OOO":
            num = True
        elif braille[chari*6: chari*6 + 6] == ".....O":
            cap = True
        elif braille[chari*6: chari*6 + 6] == "......":
            string += brailletochar(braille[chari*6: chari*6 + 6], cap, num)
            num = False
        else:
            string += brailletochar(braille[chari*6: chari*6 + 6], cap, num)
            cap = False
        chari += 1
    return string

# stringtobraille takes a english string and translates it to a braille string
# character by character using chartobraille
def stringtobraille(str):
    length= len(str)
    index = 0
    braille_string = ""
    num = False
    while(index < length):
        if(str[index].isdigit() and not(num)):
            braille_string += ".O.OOO"
            num = True
        if(str[index] == " "):
            num = False
        braille_string+= chartobraille(str[index])
        index += 1
    
    
    return braille_string

argnum = len(sys.argv)
index = 1
fulloutput =""
while(index < argnum):
    if(len(sys.argv[index]) < 6):
        fulloutput += stringtobraille(sys.argv[index])
        if(index < argnum - 1):
                fulloutput += "......" 
    else:

        braillecheck = sys.argv[index][0:6]
        braillecount = 0
        for char in braillecheck:
            if(char == "O" or char == "."):
                braillecount += 1
        if(braillecount == 6):
            fulloutput += brailletostring(sys.argv[index])
        else:
            fulloutput += stringtobraille(sys.argv[index])
            if(index < argnum - 1):
                fulloutput += "......" 
    index += 1

print(fulloutput)
