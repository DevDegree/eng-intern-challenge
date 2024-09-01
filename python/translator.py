import sys

encodings = {
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
    " ": "......",
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
    "cap": ".....O",
    "dec": ".O...O",
    "num": ".O.OOO",
}

def eng_to_braille(text):
    braille = ""
    digit = False
    for char in text:
        if char.isupper():
            braille += encodings["cap"]
            braille += encodings[char.lower()]
        elif char.isdigit() and not digit:
            digit = True
            braille += encodings["num"]
            braille += encodings[char]
        elif char.isdigit() and digit:
            braille += encodings[char]
        elif char.islower():
            braille += encodings[char]
        elif char == " ":
            digit = False
            braille += encodings[char]
        else:
            braille += encodings[char]
    return braille

def braille_to_eng(braille):
    text = ""
    digit = False
    cap = False
    for i in range(0, len(braille), 6):
        for key, value in encodings.items():
            if braille[i:i+6] == value:
                if key == "cap":
                    cap = True
                elif key == "num":
                    digit = True
                elif key == " ":
                    digit = False
                    text += key
                else:
                    if cap:
                        text += key.upper()
                        cap = False
                    elif digit and key.isdigit():
                        text += key
                    elif not digit and key.isalpha():
                        text += key
                    elif not key.isalnum():
                        text += key
    return text

def main():
    text = " ".join(sys.argv[1::])
    dot_count = text.count(".")
    o_count = text.count("O")
    if dot_count + o_count == len(text):
        print(braille_to_eng(text))
    else:
        print(eng_to_braille(text))
if __name__ == "__main__":
    main()
