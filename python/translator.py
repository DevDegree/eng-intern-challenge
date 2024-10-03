#!/usr/bin/env python3

BrailleToEnglish={
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
".....O": "capital",
".O...O": "decimal",
".O.OOO": "number",
"..OO.O": ".",
"..O...": ",",
"..O.OO": "?",
"..OOO.": "!",
"..OO..": ":",
"..O.O.": ";",
"....OO": "-",
".O..O.": "/",
".OO..O": "<",
"OOOOOO": ">",
"O.O..O": "(",
".O.OO.": ")",
"......": " "
}

BrailleToEnglishNumbers={
"O.....": "1",
"O.O...": "2",
"OO....": "3",
"OO.O..": "4",
"O..O..": "5",
"OOO...": "6",
"OOOO..": "7",
"O.OO..": "8",
".OO...": "9",
".OOO..": "0"
}

EnglishToBraille={
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
"capital": ".....O",
"decimal": ".O...O",
"number": ".O.OOO",
".": "..OO.O",
",": "..O...",
"?": "..O.OO",
"!": "..OOO.",
":": "..OO..",
";": "..O.O.",
"-": "....OO",
"/": ".O..O.",
"<": ".OO..O",
">": "OOOOOO",
"(": "O.O..O",
")": ".O.OO.",
" ": "......"
}

EnglishToBrailleNumbers={
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

def translate_to_braille(text):
    braille = ""
    isNumeric = False

    for char in text:
        if char == " ":
            braille += EnglishToBraille[char]
            isNumeric = False
            continue
        elif char == ".":
            braille += EnglishToBraille["decimal"]
            continue
        elif char.isnumeric():
            if not isNumeric:
                isNumeric = True
                braille += EnglishToBraille["number"]
            braille += EnglishToBrailleNumbers[char]
            continue
        elif char.islower():
            braille += EnglishToBraille[char]
        elif char.isupper():
            braille += EnglishToBraille["capital"]
            braille += EnglishToBraille[char.lower()]
        else:
            braille += EnglishToBraille[char]
    return braille
  
def translate_to_english(braille):
    english = ""
    isNumeric = False
    isCapital = False
    for i in range(0,len(braille),6):
        char = braille[i:i+6]
        if char == EnglishToBraille[" "]:
            english += BrailleToEnglish[char]
            isNumeric = False
            continue
        elif char == EnglishToBraille["number"]:
            isNumeric = True
            continue
        elif char == EnglishToBraille["capital"]:
            isCapital = True
            continue
        elif isCapital:
            english += BrailleToEnglish[char].upper()
            isCapital = False
            continue
        elif isNumeric:
            english += BrailleToEnglishNumbers[char]
            continue
        else:
            english += BrailleToEnglish[char]
    return english

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: translator.py <text>")
        sys.exit(1)

    text = ""
    for i in range (1, len(sys.argv)):
        text+=sys.argv[i] + " "
    text = text.strip()
    if (all(c in ".O" for c in text)):
        english = translate_to_english(text)
        print("".join(english))
    else:
        braille = translate_to_braille(text)
        print("".join(braille))

if __name__ == "__main__":
    main()