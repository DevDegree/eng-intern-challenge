import sys

# braille alphabet
brailleAlpha = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
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
    " ": "......",
    ".": ".O..OO",
    ",": ".O....",
    ":": ".OO...",
    ";": ".OO.O.",
    "?": ".O..O.",
    "!": ".OOO..",
    "-": "....OO",
    "(": "....OO",
    ")": "....OO",
    "/": ".O..O.",
    "<": ".O..O",
    ">": "O..OO.",
    "cap": ".....O",
    "dec": ".O...O",
    "num": ".O.OOO"

}

# braille numbers
brailleDigit= {
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
}

# get key from value for braille alphabet
def get_key(val):
    for key, value in brailleAlpha.items():
        if val == value:
            return key

# get key from value for braillee digit alphabet
def get_key_num(val):
    for key, value in brailleDigit.items():
        if val == value:
            return key

# check if input is braillele
def isbraille(userIn):
    alpha = False
    for letter in userIn:
        if letter != "O" and letter != ".":
            alpha = True
    if alpha == True:
        return False
    else:
        return True

#translate from alphanumeric to braille
def translate_to_braille(userIn):
    str = ""
    dig = False
    for letter in userIn:
        if letter.isupper():
            str += ".....O"
            lower = letter.lower()
            str += brailleAlpha[lower]
        elif letter.isdigit():
            #only put in front of first num
            if dig == False:
                str += ".O.OOO"
                dig = True
            str += brailleAlpha[letter]
        elif letter == ".":
            str += ".O...O"
            str += brailleAlpha[letter]
        else:
            if letter == " ":
                dig = False
            str += brailleAlpha[letter]
    return str

# translate from braille to alphanumeric
def translate_from_braille(userIn):
    str = ""
    i = 0
    temp = ""
    next = ""
    for letter in userIn:
        i += 1
        temp += letter
        if i==6:
            #check if special condition before char
            if get_key(temp) == "cap":
                next = "cap"
            elif get_key(temp) == "num":
                next = "num"
            elif get_key(temp) == "dec":
                next = "dec"
            else:
                #append to str depending on set condition
                if next == "cap":
                    str += get_key(temp).upper()
                    next = ""
                elif next == "num":
                    str += get_key_num(temp)
                else:
                    str += get_key(temp)
                    next = ""
            temp = ""
            i = 0
    return str

def main():
    if len(sys.argv) > 1:
        userIn = " ".join(sys.argv[1:]).strip()
    else:
        userIn = input("Enter text or Braille: ").strip()

    if isbraille(userIn):
        print(translate_from_braille(userIn))
    else:
        print(translate_to_braille(userIn))

if __name__ == "__main__":
    main()