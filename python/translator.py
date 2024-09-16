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

BRAILLE_TO_ENGLISH = { ("N" + ENGLISH_TO_BRAILLE[key] if key.isnumeric() else ENGLISH_TO_BRAILLE[key]): key for key in ENGLISH_TO_BRAILLE }

def translate_english(english):
    """Translates an English string to Braille."""
    braille = []
    nf = False # Numeric Flag

    for char in english:
        if char == " ":
            braille.append(ENGLISH_TO_BRAILLE[" "])
            nf = False  
        elif char.isnumeric():
            if not nf:  
                braille.append(ENGLISH_TO_BRAILLE["NF"])
                nf = True  
            braille.append(ENGLISH_TO_BRAILLE[char])
        elif char.isupper():
            braille.append(ENGLISH_TO_BRAILLE["CF"])  
            braille.append(ENGLISH_TO_BRAILLE[char.lower()])  
            nf = False 
        else:
            braille.append(ENGLISH_TO_BRAILLE[char]) 
            nf = False  

    return "".join(braille)



def translate_braille(braille):
    """Translates a Braille string to English."""
    english = []
    i = 0
    nf = False  # Numeric Flag
    cf = False  # Capital Flag

    while i < len(braille):
        char = braille[i:i+6]
        
        # Handle space
        if char == ENGLISH_TO_BRAILLE[" "]:
            english.append(" ")
            nf = False
            cf = False
            i += 6
            continue

        # Handle numeric flag
        if char == ENGLISH_TO_BRAILLE["NF"]:
            nf = True
            i += 6
            continue

        # Handle capital flag
        if char == ENGLISH_TO_BRAILLE["CF"]:
            cf = True
            i += 6
            continue

        
        if nf:
            english.append(BRAILLE_TO_ENGLISH["N" + char])  # Interpret as number
        elif cf:
            english.append(BRAILLE_TO_ENGLISH[char].upper())
            cf = False 
        else:
            english.append(BRAILLE_TO_ENGLISH[char])
        
        i += 6

    return "".join(english)
 

 
if __name__ == "__main__":
    string = " ".join(sys.argv[1:])
    if "." in string:  # If the input contains braille dots, assume it's Braille
        print(translate_braille(string))
    else:
        print(translate_english(string))