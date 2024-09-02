import re, sys

ENG_TO_BRAILLE = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
    "cap": ".....O",
    "dec": ".O...O",
    "num": ".O.OOO"
}

NUM_MODE = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "0": "j",
    ">": "o"
}

REVERSE_TRANSLATOR = {v: k for k, v in ENG_TO_BRAILLE.items()}
REVERSE_NUM = {v: k for k, v in NUM_MODE.items()}

def translate_to_braille(input, mode):
    result = ""
    for c in input:
        #check if the c is a number
        if c.isdigit():
            #check if we are at the first digit of the number, if we are, change mode to num 
            if mode == "alpha":
                mode = "num"
                result = result + ENG_TO_BRAILLE["num"]
            result = result + ENG_TO_BRAILLE[NUM_MODE[c]]
        #check if where we are in the string is a decimal
        elif c == "." and mode == "num":
            result = result + ENG_TO_BRAILLE["dec"] + ENG_TO_BRAILLE["."]
        else:
            #change the mode to alphabet if no longer numeric (assuming number is followed by a space)
            mode = "alpha"
            if c.isupper():
                result = result + ENG_TO_BRAILLE["cap"] + ENG_TO_BRAILLE[c.lower()]
            else:
                result = result + ENG_TO_BRAILLE[c]
        
    
    return result

def translate_to_eng(input, mode): 
    result = ""
    for i in range(0, len(input), 6):
        c = input[i: i+6]
        #check if the symbol is valid
        if c not in REVERSE_TRANSLATOR:
            return translate_to_braille(input, "alpha")
        
        #check if we are in any of the special modes 
        if REVERSE_TRANSLATOR[c] in ["num", "cap", "dec"]:
            mode = REVERSE_TRANSLATOR[c]
            continue
    
        if mode == "num":
            #check if we have encountered the end of the numeric string
            if REVERSE_TRANSLATOR[c] == " ":
                mode = "alpha"
                result = result + " "
            else: result = result + REVERSE_NUM[REVERSE_TRANSLATOR[c]]
        elif mode == "cap":
            result = result + REVERSE_TRANSLATOR[c].upper()
            mode = "alpha"
        elif mode == "dec":
            result = result + "."
            mode = "num"
        else:
            result = result + REVERSE_TRANSLATOR[c]


    return result

def translate(input): 
    if (re.match(r'^[O.]+$', input) is not None and len(input) % 6 == 0):
        return translate_to_eng(input, "alpha")
    else:
        return translate_to_braille(input, "alpha")
    
def main():  
    user_input = ' '.join(sys.argv[1:])
    print(translate(user_input))

if __name__ == '__main__':
    main()
