import re
import sys

english_to_braille = {
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
    " ": "......"
}

braille_to_english = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " "
    
}

braille_to_numbers = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
    "O..OO.": ">"
}

def englishToBraille(toTranslate):
    message = ""
    for i in range(len(toTranslate)):
        character = toTranslate[i]
        if character.isalpha() and character.isupper(): 
            message += ".....O"
            message += english_to_braille.get(character.lower())
        elif character.isnumeric():
            prev = toTranslate[i-1]
            if not prev.isnumeric() or i == 0:
                message += ".O.OOO" 
            message += english_to_braille.get(character)

        else:
            message += english_to_braille.get(character)
    return message



def brailleToEnglish(toTranslate):
    message = ""
    num = False
    capital = False
    for i in range(0, len(toTranslate),6):
        character = toTranslate[i:i+6]
        if character == ".....O":
            capital = True
        elif character == ".O.OOO":
            num = True
        elif character == ".O...O":
            continue
        elif character == "......":
            message += " "
            num = False
        elif capital:
            message += braille_to_english.get(character).upper()
            capital = False
        elif num:
            message += braille_to_numbers.get(character)
        else:
            message += braille_to_english.get(character)
    return message



toTranslate = ""
for i in range(1, len(sys.argv)):
    toTranslate += sys.argv[i] + " "

toTranslate = toTranslate[:-1]

if(bool(re.match('[O.]', toTranslate)) and len(toTranslate) >= 6):
    print(brailleToEnglish(toTranslate))
else:
    print(englishToBraille(toTranslate))
