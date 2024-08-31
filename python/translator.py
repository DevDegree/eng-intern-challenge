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
    ">": "O..OO.",
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
    "0": "j"
}

def translate_to_braille(input, mode):
    result = ""
    for c in input:
        if c.isdigit():
            if mode == "alpha_mode":
                mode = "num_mode"
                result = result + TRANSLATOR["num"]
            result = result + TRANSLATOR[NUM_MODE[c]]
        else:
            mode = "alpha_mode"
            if c.isupper():
                result = result + TRANSLATOR["cap"] + TRANSLATOR[c.lower()]
            elif c == ".":
                result = result + TRANSLATOR["dec"] + TRANSLATOR["."]
            else:
                result = result + TRANSLATOR[c]
        
    
    return result

def translate_to_eng(input): 
    return ""

def translate(input): 
    if (re.match(r'^[O.]+$', input) is not None and len(input) % 6 == 0):
        return translate_to_eng(input)
    else:
        return translate_to_braille(input, "alpha_mode")
    
while True:    
    user_input = input()
    print(translate(user_input))
