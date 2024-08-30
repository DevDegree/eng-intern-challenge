import sys

brailAlpha = {
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

brailDigit= {
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

def get_key(val):
    for key, value in brailAlpha.items():
        if val == value:
            return key

def get_key_num(val):
    for key, value in brailDigit.items():
        if val == value:
            return key

    return "key doesn't exist"

def isbrail(userIn):
    alpha = False
    for letter in userIn:
        if letter != "O" and letter != ".":
            alpha = True
    if alpha == True:
        return False
    else:
        return True

def translate_to_brail(userIn):
    str = ""
    dig = False
    for letter in userIn:
        if letter.isupper():
            str += ".....O"
            lower = letter.lower()
            str += brailAlpha[lower]
        elif letter.isdigit():
            if dig == False:
                str += ".O.OOO"
                dig = True
            str += brailAlpha[letter]
        elif letter == ".":
            str += ".O...O"
            str += brailAlpha[letter]
        else:
            if letter == " ":
                dig = False
            str += brailAlpha[letter]
    return str
def translate_from_brail(userIn):
    str = ""
    i = 0
    temp = ""
    next = ""
    for letter in userIn:
        i += 1
        temp += letter
        if i==6:
            if get_key(temp) == "cap":
                next = "cap"
            elif get_key(temp) == "num":
                next = "num"
            elif get_key(temp) == "dec":
                next = "dec"
            else:
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

    if isbrail(userIn):
        print(translate_from_brail(userIn))
    else:
        print(translate_to_brail(userIn))

if __name__ == "__main__":
    main()



