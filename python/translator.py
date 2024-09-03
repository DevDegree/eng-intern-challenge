import sys

# Braille to English Mapping
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "capital", ".O.OOO": "number",
    ".O....": "1", ".OO...": "2", "O..O..": "3", "O..OO.": "4", "O..OOO": "5",
    "O.O...": "6", "O.OO..": "7", "O.OOO.": "8", ".O.O..": "9", ".O.OO.": "0",
    "......": " ", ".O..O.": ".", "..O.O.": ",", "..O...": "!", "..OO..": "?",
    "..OOO.": "'", "....O.": "-", "....OO": "/", "..OO.O": ":", "..OO..": ";",
    ".O.OO.": "<", ".OO.O.": ">", "....O.": "(", "....O.": ")", "......": " "
}

# English to Braille Mapping
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "capital": ".....O", "number": ".O.OOO",
    "1": ".O....", "2": ".OO...", "3": "O..O..", "4": "O..OO.", "5": "O..OOO",
    "6": "O.O...", "7": "O.OO..", "8": "O.OOO.", "9": ".O.O..", "0": ".O.OO.",
    " ": "......", ".": ".O..O.", ",": "..O.O.", "!": "..O...", "?": "..OO..",
    "'": "..OOO.", "-": "....O.", "/": "....OO", ":": "..OO.O", ";": "..OO..",
    "<": ".O.OO.", ">": ".OO.O.", "(": "....O.", ")": "....O."
}

# Special symbols
capital_indicator = ".....O"  # Braille capital follows
number_indicator = ".O.OOO"   # Braille number follows

def translate_to_braille(text):
    braille_text = []
    for char in text:
        if char.isupper():
            braille_text.append(capital_indicator)
            char = char.lower()
        if char.isdigit():
            braille_text.append(number_indicator)
        braille_text.append(english_to_braille.get(char, "......"))  # Default to space if not found
    return "".join(braille_text)

def translate_to_english(braille):
    english_text = []
    index = 0
    is_capital = False
    is_number = False
    
    while index < len(braille):
        symbol = braille[index:index+6]
        if symbol == capital_indicator:
            is_capital = True
            index += 6
            continue
        elif symbol == number_indicator:
            is_number = True
            index += 6
            continue
        char = braille_to_english.get(symbol, " ")
        if is_capital:
            char = char.upper()
            is_capital = False
        elif is_number:
            char = char  # The char remains the same for numbers
            is_number = False
        english_text.append(char)
        index += 6
    return "".join(english_text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <input string>")
        sys.exit(1)

    input_string = sys.argv[1]
    if all(c in "O." for c in input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()
