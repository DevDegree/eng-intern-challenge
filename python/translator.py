import sys

BRAILLE_TO_ENGLISH = {
    "......": "SPACE",
    ".....O": "CAPITALFOLLOWS",
    ".O...O": "DECIMALFOLLOWS",
    ".O.OOO": "NUMBERFOLLOWS",
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
}

BRAILLE_CHAR_TO_NUMBER = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5",
    "f": "6",
    "g": "7",
    "h": "8",
    "i": "9",
    "j": "0",
}

BRAILLE_NUMBER_TO_CHAR = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "0": "j",
}

ENGLISH_TO_BRAILLE = {
    "SPACE": "......",
    "CAPITALFOLLOWS": ".....O",
    "DECIMALFOLLOWS": ".O...O",
    "NUMBERFOLLOWS": ".O.OOO",
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

# Assumption made is that any word consisting of only O and . is Braille. Also, if length of input is not multiple of 6, must be English
def is_braille(word):
    return all([c in ".O" for c in word]) and not len(word) % 6

def braille_to_english(word):
    i = 0
    reading_number = False
    reading_capital = False
    english = ""
    while i < len(word):
        block = word[i : i + 6]

        i += 6
        if block not in BRAILLE_TO_ENGLISH:
            raise Exception("Invalid Braille Character")

        engl_char = BRAILLE_TO_ENGLISH[block]
        if engl_char == "CAPITALFOLLOWS":
            reading_capital = True
        elif engl_char == "NUMBERFOLLOWS":
            reading_number = True
        elif engl_char == "SPACE":
            english += " "
            reading_number = False
            reading_capital = False
        else:
            # the character is a-z0-9
            if reading_capital:
                english += engl_char.upper()
                reading_capital = False
            elif reading_number:
                english += BRAILLE_CHAR_TO_NUMBER[engl_char]
            elif not reading_capital:
                english += engl_char

    return english


def english_to_braille(word):
    braille = ""
    number_follows_set = False
    i = 0
    while i < len(word):
        if word[i] in "0123456789":
            while i < len(word) and word[i] in "0123456789":
                if not number_follows_set:
                    braille += ENGLISH_TO_BRAILLE["NUMBERFOLLOWS"]
                    number_follows_set = True
                braille += ENGLISH_TO_BRAILLE[BRAILLE_NUMBER_TO_CHAR[word[i]]]
                i += 1
        
        elif word[i].isalpha()  or word[i] == ' ':
            if word[i] == ' ':
                braille += ENGLISH_TO_BRAILLE["SPACE"]
                number_follows_set = False
            else:
                if word[i] == word[i].upper():
                    # Already uppercase letter
                    braille += ENGLISH_TO_BRAILLE["CAPITALFOLLOWS"]
                    braille += ENGLISH_TO_BRAILLE[word[i].lower()]
                else:
                    braille += ENGLISH_TO_BRAILLE[word[i]]
            i += 1
        
        else:
            raise Exception(f"Invalid character {word[i]} not supported in translation")
    return braille

if __name__ == "__main__":
    input = ' '.join(sys.argv[1:])
    if is_braille(input):
        print(braille_to_english(input))
    else:
        print(english_to_braille(input))
        