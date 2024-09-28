import sys

char_to_braille = {
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
}

num_to_braille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

instr_to_braille = {
    "cap": ".....O",
    "num": ".O.OOO",
    "spa": "......"
}

def reverse(a):
    b = dict()
    for key in a:
        b[a[key]] = key
    return b

braille_to_char = reverse(char_to_braille)

braille_to_num = reverse(num_to_braille)

braille_to_instr = reverse(instr_to_braille)

def is_braille(s):
    for i in s:
        if i != "O" and i != ".":
            return False
    if len(s) % 6 != 0:
        return False
    return True

a = sys.argv

for i in range(1, len(a)):
    s = a[i]
    if is_braille(s):
        next_num = False
        next_cap = False

        idx = 0

        while idx < len(s):
            next_char = ""
            for i in range(6):
                next_char += s[idx]
                idx += 1
            
            if next_char in braille_to_instr:
                if braille_to_instr[next_char] == "cap":
                    next_cap = True
                elif braille_to_instr[next_char] == "num":
                    next_num = True
                elif braille_to_instr[next_char] == "spa":
                    print(" ", end="")
                    next_num = False
            elif next_num:
                print(braille_to_num[next_char], end="")
            else:
                out_char = braille_to_char[next_char]
                if next_cap:
                    out_char = out_char.upper()
                    next_cap = False
                print(out_char, end="")
        
        if i != len(a) - 1:
            print(" ", end="")
            next_num = False

    else:
        next_num = False
        for c in s:
            if c == " ":
                next_num = False
                print(instr_to_braille["spa"], end="")
            elif c.isdigit():
                if not next_num:
                    print(instr_to_braille["num"], end="")
                    next_num = True
                print(num_to_braille[c], end="")
            else:
                if c.isalpha() and c.isupper():
                    print(instr_to_braille["cap"], end="")
                    c = c.lower()
                print(char_to_braille[c], end="")
        if i != len(a) - 1:
            print(instr_to_braille["spa"], end="")
            next_num = False
