import sys

braille_eng_map = {
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
    "upper": ".....O",
    "number": ".O.OOO",
    " ": "......"
}

keys = list(braille_eng_map.keys())
for key in keys:
    braille_eng_map[braille_eng_map[key]] = key
        
args = sys.argv
# Convert multi-word inputs into one string with spaces
string = " ".join(args[1:])

braille = False
# String is in Braille if and only if it has a .
if '.' in string:
    braille = True

res = ""

if braille:
    curr = 0
    upper = False
    number = False
    while curr < len(string):
        braille_letter = string[curr : curr + 6]
        eng_letter = braille_eng_map[braille_letter]
        if eng_letter == "upper":
            upper = True
        elif eng_letter == "number":
            number = True
        elif eng_letter == " ":
            res += " "
            number = False
        else:
            if upper:
                res += chr(ord(eng_letter) - 32)
                upper = False
            elif number:
                # 1 to 9 have the same Braille representation as a to i, respectively
                # Convert to number
                if eng_letter in "abcdefghi":
                    res += chr(ord(eng_letter) - 48)
                # 0 has the same Braille representation as j
                elif eng_letter == "j":
                    res += chr(ord(eng_letter) - 58)
            else:
                res += eng_letter
        curr += 6
else:
    curr = 0
    number = False
    while curr < len(string):
        eng_letter = string[curr]
        if ord('A') <= ord(eng_letter) <= ord('Z'):
            res += braille_eng_map["upper"]
            res += braille_eng_map[chr(ord(eng_letter) + 32)]
        elif eng_letter in "0123456789":
            if not number:
                res += braille_eng_map["number"]
                number = True
            if eng_letter in "123456789":
                res += braille_eng_map[chr(ord(eng_letter) + 48)]
            elif eng_letter == "0":
                res += braille_eng_map[chr(ord(eng_letter) + 58)]
        elif eng_letter == " ":
            number = False
            res += braille_eng_map[eng_letter]
        else:
            res += braille_eng_map[eng_letter]
        curr += 1

print(res)
