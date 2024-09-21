import sys

CAPITAL_LETTER = "capital"
DIGIT = "digit"
SPACE = " "

ENG_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", 
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", 
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", 
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO"
}
DIGITS_TO_BRAILLE = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", 
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", 
}
SPECIAL_CHARS = {
    CAPITAL_LETTER: ".....O", DIGIT: ".O.OOO", SPACE: "......",
}

BRAILLE_TO_DIGITS = {v: k for k, v in DIGITS_TO_BRAILLE.items()}
BRAILLE_TO_ENG = {v: k for k, v in ENG_TO_BRAILLE.items()}
REVERSE_SPECIAL_CHARS = {v: k for k, v in SPECIAL_CHARS.items()}


def concatinate_words(inputed_text):
    return ' '.join(inputed_text)

def translate(inputed_phrase):
    if is_braille(inputed_phrase):
        return "Translate to english"
    else:
        return translate_to_braille(inputed_phrase)

def is_braille(inputed_phrase):
    return all(char in "O." for char in inputed_phrase)


def translate_to_braille(english_phrase):
    braille_translation = ""
    prev_char = ""
    for c in english_phrase:
        if c.isalpha():
            braille_translation += translate_letter(c)
        elif c.isdigit():
            braille_translation += translate_digit(c, prev_char)
        elif c == SPACE:
            braille_translation += SPECIAL_CHARS[SPACE]
        prev_char = c
    return braille_translation

def translate_letter(c):
    letter = ""
    if c.isupper():
        letter += SPECIAL_CHARS[CAPITAL_LETTER]
    letter += ENG_TO_BRAILLE[c.lower()]
    return letter

def translate_digit(d, prev_char):
    digit = ""
    if not prev_char.isdigit():
        digit = SPECIAL_CHARS[DIGIT]
    digit += DIGITS_TO_BRAILLE[d]
    return digit


def main():
    if len(sys.argv) < 2:
        print("Please input an english or braille text to translate!")
        sys.exit(1)

    inputed_phrase = concatinate_words(sys.argv[1:])
    print(translate(inputed_phrase))

if __name__ == "__main__":
    main()