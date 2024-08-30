import sys

alphabet_map = {
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
    "z": "O..OOO"
}

numerics_map = {
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

follows_map = {
    ".....O": "capital",
    ".O.OOO": "number"
}

def main():
    for input in sys.stdin.read().splitlines():
        if "." in input:
            translate_to_english(input)
        else:
            translate_to_braille(input)
   

# translate from english to braille
def translate_to_braille(s):
    isNumeric = False
    res = ""
    for i in range(len(s)):
        c = s[i]
        if c.isalpha():
            # check if isNumeric cap is on. If true, add space to indicate numeric follows is off. ie) 9a
            if isNumeric:
                res += "......"
                isNumeric = False
            # check if upper case
            if c.isupper():
                res += ".....O"
            
            res += alphabet_map[c.lower()]
        elif c.isdigit():
            if not isNumeric:
                res += ".O.OOO"
                isNumeric = True
            
            res += numerics_map[c]
        else:
            # space char
            res += "......"
            isNumeric = False
    print(res)

# translate from braille to english
def translate_to_english(s):
    res = ""
    i = 0
    indicator = ""
    while i < len(s):
        braille_char = s[i:i+6]
        if braille_char in follows_map:
            indicator = follows_map[braille_char]
        elif braille_char == "......":
            res += " "
            indicator = ""
        else:
            for key,value in (numerics_map if indicator == "number" else alphabet_map).items():
                if value == braille_char:
                    if indicator == "capital":
                        res += key.upper()
                        indicator = ""
                    else:
                        res += key
                    break
            
        i += 6

    print(res)

if __name__ == "__main__":
    main()