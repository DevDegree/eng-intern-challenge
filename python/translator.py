import sys


eng_to_braile = {
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
}

num_to_braile = {
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

cap = ".....O"
num = ".O.OOO"
space = "......"

braile_to_eng = {value: key for key, value in eng_to_braile.items()}
braile_to_num = {value: key for key, value in num_to_braile.items()}


def translate_eng(english):
    is_num = False
    braile = ""

    for c in english:
        if c in "0123456789":
            if not is_num:
                braile += num
                is_num = True

            braile += num_to_braile[c]

        elif c == " ":
            braile += space
            is_num = False
            continue

        elif c.isupper():
            braile += cap
            braile += eng_to_braile[c.lower()]
        else:
            braile += eng_to_braile[c]
    return braile

def translate_braile(braile):
    is_num = False
    is_cap = False
    english = ""

    for i in range(0, len(braile), 6):
        c = braile[i : i+6]

        if c == num:
            is_num = True
        
        elif c == space:
            english += " "
            is_num = False

        elif c == cap:
            is_cap = True

        elif is_num:
            english += braile_to_num[c]

        elif is_cap:
            english += braile_to_eng[c].upper()
            is_cap = False

        else:
            english += braile_to_eng[c]

    return english

def main():
    args = sys.argv[1:]
    params = " ".join(args)
    if all(c in 'O.' for c in params):
        print(translate_braile(params))
    else:
        print(translate_eng(params))


if __name__ == "__main__":
    main()
