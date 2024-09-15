# sys.argv reads args from whatever you type in the console
import sys
# re.findall is used for checking for valid Braille strings
import re

# Note: I removed the characters < and > from the Braille alphabet (the image seen from Wikipedia) because > has the
# same code as the letter "O". Additionally, the requirements for this task only state letters a-z, numbers 0-9, and
# space are strictly required.

# English to Braille dicts
en_br_alpha = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e":  "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h":  "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l":  "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o":  "O..OO.",
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
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}
en_br_num = {
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
en_br_merged = {**en_br_alpha, **en_br_num}

# Braille to English dicts (The same as above, but reversed. Behold the reason I separated them: Braille reuses codes
# (i.e., abcde is the same as 12345). So I decided to just have one be the alphabet & special chars and the other be
# numbers)
br_en_alpha = {val: key for key, val in en_br_alpha.items()}
br_en_num = {val: key for key, val in en_br_num.items()}

# Reconstruct the arguments passed through the command line
_msg = ""
for arg in range(1, len(sys.argv)):
    # If it's not the last argument, then add a space in between
    _msg += sys.argv[arg] + (" " if arg < len(sys.argv) - 1 else "")

# Verification of the string (if it's just sets of 6 .'s or O's then it's Braille, otherwise treat as English)
# 0 is English, 1 is Braille
_mode = 0
if re.fullmatch("^([Oo.]{6})+$", _msg) is not None:
    _mode = 1


def translate(msg, mode):
    o = ""
    isNumber = False
    # English to Braille
    if mode == 0:
        # Iter over characters
        for c in msg:
            # Capital follows
            if c != c.lower():
                o += ".....O"
            # Number follows
            elif c in "1234567890" and isNumber is not True:
                o += ".O.OOO"
                isNumber = True
            # Cancel the number thing
            elif c == " ":
                isNumber = False
            # Add the braille of the character
            o += en_br_merged.get(c.lower(), "")
    # Braille to English
    else:
        isCapital = False
        for i in range(0, len(msg) // 6):
            word = msg[6*i:(6*i)+6]
            # Space resets the number mode (and gets added)
            if word == "......":
                isNumber = False
                o += " "
                continue
            # Number follows switches to numerical mode
            elif word == ".O.OOO":
                isNumber = True
                continue
            # Capital follows turns on capitalization
            elif word == ".....O":
                isCapital = True
                continue
            # Add a number to the string
            elif isNumber:
                o += br_en_num.get(word, "(NUM)")
            # Add text to the string (capitalized when necessary)
            else:
                toAdd = br_en_alpha.get(word, "(ALP)")
                if isCapital:
                    toAdd = toAdd.upper()
                    isCapital = False
                o += toAdd
    return o


print(translate(_msg, _mode))
