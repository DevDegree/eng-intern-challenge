import sys

#CONSTANTS
BRAILLLE_SET = {"O", "."}
ALPHANUMERICALS_TO_BRAILLE = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...",
        "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",
        "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.",
        "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
        "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO",
        "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.", " ": "......", "capital": ".....O",
        "decimal": ".O...O", "number": ".O.OOO"
    }

BRAILLE_TO_ALPHANUMERICALS = {value: key for key, value in ALPHANUMERICALS_TO_BRAILLE.items()}

# Checks is the input string is alphanumerical or baille
def is_baille(sequence_chars):
    if len(sequence_chars) % 6 == 0 and set(sequence_chars) - BRAILLLE_SET == set({}):
        return True
    return False

# Translates the sequence of characters depending on if it is alphanumerical or baille
def translate(sequence_chars):
    n = 6
    text_array = []
    translated_string = ""
    is_capital = False
    if is_baille(sequence_chars):
        for i in range(0, len(sequence_chars), n):
            text_array.append(sequence_chars[i:i+n])
        for el in text_array:
            if BRAILLE_TO_ALPHANUMERICALS.get(el) == "decimal" or BRAILLE_TO_ALPHANUMERICALS.get(el) == "number":
                continue
            elif BRAILLE_TO_ALPHANUMERICALS.get(el) == "capital":
                is_capital = True
                continue
            elif is_capital:
                translated_string = translated_string + BRAILLE_TO_ALPHANUMERICALS.get(el).upper()
                is_capital = False
            else:
                translated_string = translated_string + BRAILLE_TO_ALPHANUMERICALS.get(el)
        return translated_string
    else:
        translated_string = ""
        previous_char = ""
        for character in sequence_chars:
            if character.isupper():
                translated_string = translated_string + ALPHANUMERICALS_TO_BRAILLE.get("capital")
                translated_string = translated_string + ALPHANUMERICALS_TO_BRAILLE.get(character.lower())
                previous_char = character
            elif character.isnumeric():
                translated_string = translated_string + ALPHANUMERICALS_TO_BRAILLE.get("number")
                translated_string = translated_string + ALPHANUMERICALS_TO_BRAILLE.get(character)
                previous_char = character
            elif character == '.' and previous_char.isnumeric():
                translated_string = translated_string + ALPHANUMERICALS_TO_BRAILLE.get("decimal")
                translated_string = translated_string + ALPHANUMERICALS_TO_BRAILLE.get(character)
                previous_char = character
            else:
                translated_string = translated_string + ALPHANUMERICALS_TO_BRAILLE.get(character)
                previous_char = character
        return translated_string


if __name__ == "__main__":
    print(translate(' '.join(sys.argv[1:])))
