import sys


BRAILLE2ENGLISH = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "CAPITAL", "O.OOOO": "NUMBER", "......": " ",  
    ".O..OO": ".", ".O....": ",", ".OO..O": "!", ".O.O.O": "?"  
}

ENGLISH2BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "CAPITAL": ".....O", "NUMBER": ".O.OOO",  
    ".": ".O..OO", ",": ".O....", "!": ".OO..O", "?": ".O.O.O", " ": "......"
}
#42: .O.OOOOO.O..O.O...

NUMBERS2BRAILLE = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

def translate2braille(text):
    braille_text = ""
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_text += ENGLISH2BRAILLE["NUMBER"]
                number_mode = True
            braille_text += NUMBERS2BRAILLE[char]
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                braille_text += ENGLISH2BRAILLE["CAPITAL"]
                braille_text += ENGLISH2BRAILLE[char.lower()]
            else:
                braille_text += ENGLISH2BRAILLE[char]
        elif char in ENGLISH2BRAILLE:
            braille_text += ENGLISH2BRAILLE[char]
            number_mode = False
    return braille_text



def translate2english(braille):
    english_text = ""
    number_mode = False
    capital_mode = False
    i = 0

    while i < len(braille):
        pattern = braille[i:i + 6]
        i += 6

        if pattern == "O.OOOO":
            number_mode = True
            continue
        elif pattern == ".....O":
            capital_mode = True
            continue
        elif pattern == "......":
            english_text += " "
            number_mode = False
            capital_mode = False
            continue

        if number_mode:
            for number, braille_rep in NUMBERS2BRAILLE.items():
                if pattern == braille_rep:
                    english_text += number
                    break
        else:
            char = BRAILLE2ENGLISH.get(pattern, "")
            if capital_mode:
                english_text += char.upper()
                capital_mode = False
            else:
                english_text += char

    return english_text


def main():

    input_text = " ".join(sys.argv[1:])
    #input_text = sys.argv[1]

    if all(c in "O." for c in input_text):
        translated_text = translate2english(input_text)
    else:
        translated_text = translate2braille(input_text)

    print(translated_text)


if __name__ == "__main__":
    main()