# Shopify Eng Intern W25 Challenge
# Braille Translator

# Dictionary for English - Braille
english_braille_alph = {
    # Lower-case letters
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", 
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "00.00.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",

    # Numbers
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO",
    "9": ".OO...", "0": ".OOO..",

    # ___ follows
    "capital follows": ".....O",
    "decimal follows": ".O...O",
    "number follows": ".O.OOO",

    # symbols
    ".": "..OO.O", ",": "..0...", "?": "..O.OO", "!": "..OOO.",
    ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",
    " ": "......",
}

#  read six chars at a time
#  append to temp string

input_word = input()

#  check if input is braille or english
if "." in input_word[:6] or "O" in input_word[:6]:
    english_brail_translate(input_word)
else:
    brail_english_translate(input_word)


# English to Braille
def english_brail_translate(word):
    print(word)


# Braille to English
def brail_english_translate(word):
    print(word)