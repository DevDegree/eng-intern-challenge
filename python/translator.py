import sys

ENGLISH_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO..",
    " ": "......", "CF": ".....O", "NF": ".O.OOO"
}
# inverts the mapping above, but adds the char "N" to the keys of numbers to differentiate from the keys of the first 10 letters of the alphabet
BRAILLE_TO_ENGLISH = { ("N" + ENGLISH_TO_BRAILLE[key] if key.isnumeric() else ENGLISH_TO_BRAILLE[key]): key for key in ENGLISH_TO_BRAILLE }

def translateEnglish(english):
    braille = []
    nf = False
    try:
        for char in english:
            if char == " ":
                nf = False
            elif char.isnumeric() and not nf:
                nf = True
                braille.append(ENGLISH_TO_BRAILLE["NF"])
            elif char.isupper():
                braille.append(ENGLISH_TO_BRAILLE["CF"])
            braille.append(ENGLISH_TO_BRAILLE[char.lower()])
    except KeyError:
        return "invalid string"
    return "".join(braille)

def translateBraille(braille):
    english = []
    nf = False
    cf = False
    try:
        for i in range(0, len(braille), 6):
            char = braille[i:i+6]
            if BRAILLE_TO_ENGLISH[char] == " ":
                nf = False
                english.append(BRAILLE_TO_ENGLISH[char])
            elif BRAILLE_TO_ENGLISH[char] == "NF":
                nf = True
            elif BRAILLE_TO_ENGLISH[char] == "CF":
                cf = True
            elif nf:
                english.append(BRAILLE_TO_ENGLISH["N" + char])
            elif cf:
                cf = False
                english.append(BRAILLE_TO_ENGLISH[char].upper())
            else:
                english.append(BRAILLE_TO_ENGLISH[char])
    except KeyError:
        return "invalid string"
    return "".join(english)

if __name__ == "__main__":
    string = " ".join(sys.argv[1:])
    if "." in string: # "." is enough to differentiate as it is not included our legal english lexicon but is included within every legal braille char
        print(translateBraille(string))
    else:
        print(translateEnglish(string))