
import sys

braille_to_english = {
    #English letters
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
    "O..O..": "e","OOO...": "f", "OOOO..": "g", "O.OO..": "h",
    ".OO...": "i", ".OOO..": "j","O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o","OOO.O.": "p",
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y","O..OOO": "z",

    # Space
    "......": " ",

    # Punctuation
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    ".O.OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",

    # Indicators
    ".....O": "capital follows",  # Capital follows indicator
    ".O.OOO": "number follows",    # Number follows indicator
}

english_to_braille = {
    # English letters
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",

    # Space
    " ": "......",

    # Punctuation
    ".": "..OO.O",  # Period
    ",": "..O...",  # Comma
    "?": "..O.OO",  # Question Mark
    "!": "..OOO.",  # Exclamation Mark
    ":": "..OO..",  # Colon
    ";": "..O.O.",  # Semi-colon
    "-": "....OO",  # Hyphen
    "/": ".O..O.",  # Slash
    "<": ".OO..O",  # Less than
    ">": ".O.OO.",  # Greater than
    "(": "O.O..O",  # Opening parenthesis
    ")": ".O.OO.",  # Closing parenthesis

    # Indicators
    "capital follows": ".....O",  # Capital follows indicator
    "number follows": ".O.OOO",   # Number follows indicator
}

braille_to_number = {
    # Digits
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "O",
}

number_to_braille = {
    # Digits
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

def translate_to_eng(braille_sequence):
    result = []

    caps_lock = False
    num_mode = False
    for i in range(0, len(braille_sequence),6):
        braille_char = braille_sequence[i:i+6]
        if braille_to_english[braille_char] == "capital follows":
            caps_lock = True
            continue
        if braille_to_english[braille_char] == "number follows":
            num_mode = True
            continue
        if braille_to_english[braille_char] == " ":
            num_mode = False
            result.append(" ")
            continue

        if num_mode:
            result.append(braille_to_number[braille_char])
        elif caps_lock:
            result.append((braille_to_english[braille_char]).upper())
            caps_lock = False
        else:
            result.append((braille_to_english[braille_char]))

    return ''.join(result)

def translate_to_braille(english_sequence):
    result = []
    caps_lock = False
    num_mode = False
    for char in english_sequence:
        if char.isdigit():
            if not num_mode:
                num_mode = True
                result.append(english_to_braille["number follows"])
            result.append(number_to_braille[char])
            continue
        elif char == " ":
            num_mode = False
            result.append(english_to_braille[char])
            continue
        elif char.isupper():
            result.append(english_to_braille["capital follows"])

        result.append(english_to_braille[char.lower()]) #Note that if char is not a letter of the alphabet, .lower() simply returns the char itself

    return ''.join(result)
def isBrailleSequence(sequence):
    return all(c in '.O' for c in sequence)
def main():
    input = ' '.join(sys.argv[1:])
    if isBrailleSequence(input):
        print(translate_to_eng(input))
    else:
        print(translate_to_braille(input))

if __name__ == "__main__":
    main()