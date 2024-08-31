import re

TRANSLATOR = {
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

REVERSE_TRANSLATOR = {v: k for k, v in TRANSLATOR.items()}
REVERSE_NUM = {v: k for k, v in NUM_MODE.items()}

def translate_to_braille(input, mode):
    result = ""
    for c in input:
        if c.isdigit():
            if mode == "alpha":
                mode = "num"
                result = result + TRANSLATOR["num"]
            result = result + TRANSLATOR[NUM_MODE[c]]
        elif c == "." and mode == "num":
            result = result + TRANSLATOR["dec"] + TRANSLATOR["."]
        else:
            mode = "alpha"
            if c.isupper():
                result = result + TRANSLATOR["cap"] + TRANSLATOR[c.lower()]
            else:
                result = result + TRANSLATOR[c]
        
    
    return result

def translate_to_eng(input, mode): 
    result = ""
    for i in range(0, len(input), 6):
        c = input[i: i+6]
        if c not in REVERSE_TRANSLATOR:
            return translate_to_braille(input, "alpha")
        
        if REVERSE_TRANSLATOR[c] in ["num", "cap", "dec"]:
            mode = REVERSE_TRANSLATOR[c]
            continue
    
        if mode == "num":
            result = result + REVERSE_NUM[REVERSE_TRANSLATOR[c]]
            if REVERSE_NUM[REVERSE_TRANSLATOR[c]] == " ":
                mode = "alpha"
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
    
while True:    
    user_input = input("please enter a word or enter q to quit:\n")
    if (user_input == "q"):
        break
    print(translate(user_input))
