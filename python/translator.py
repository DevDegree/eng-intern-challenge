import sys

letter_to_braille = {
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
}

# because the values for digits overlap with the first ten English letters,
# we must create another dictionary to keep track
braille_to_english = {}
braille_to_digit = {}
for _, (key, val) in enumerate(letter_to_braille.items()):
    if key.isdigit():
        braille_to_digit[val] = key
    else:
        braille_to_english[val] = key

text = " ".join(sys.argv[1:])

result = ""
# only braille has the letter '.'
if "." in text:
    # we must convert the braille to English
    digit = False  # are we on "number" mode?
    capital = False  # is the current letter capital?
    for i in range(0, len(text), 6):  # go through the text, 6 letters at a time
        symbol = text[i : i + 6]
        if symbol == ".....O":  # capital follows
            capital = True
        elif symbol == ".O.OOO":  # number follows
            digit = True
        elif symbol == "......":  # space
            result += " "
            digit = False
        elif digit:
            result += braille_to_digit[symbol]
        elif capital:
            result += braille_to_english[symbol].upper()
            capital = False
        else:
            result += braille_to_english[symbol]
else:  # English to braille
    digit = False  # are we on "number" mode?
    for c in text:
        if c.isdigit():
            if not digit:
                result += ".O.OOO"
                digit = True
            result += letter_to_braille[c]
        elif c == " ":
            digit = False
            result += letter_to_braille[c]
        elif c.isupper():
            result += ".....O"
            result += letter_to_braille[c.lower()]
        else:
            result += letter_to_braille[c]

print(result)
