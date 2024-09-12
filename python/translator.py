import sys
# Mappinf from English characters to Braille
eng_to_braille = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OOO...",
    "e": "O..O..",
    "f": "OO.O..",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OOO.O.",
    "o": "O..OO.",
    "p": "OO.OO.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OOO.OO",
    "z": "O..OOO",
    " ": "......",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OOO...",
    "5": "O..O..",
    "6": "OO.O..",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

# Mapping from braille to english characters
braille_to_eng = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OOO...": "d",
    "O..O..": "e",
    "OO.O..": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OOO.O.": "n",
    "O..OO.": "o",
    "OO.OO.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OOO.OO": "y",
    "O..OOO": "z",
    "......": " ",
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OOO...": "4",
    "O..O..": "5",
    "OO.O..": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

braille_capital = "..O..."
braille_number = ".O.OOO"

# Helper function to check if input is braille
def is_braille(input_string):
    for char in input_string:
        if char != 'O' and char != '.':
            return False
    return True

# Function to convert English to Braille
def english_to_braille(input_text):
    result = []
    for char in input_text:
        if char.isupper():
            result.append(braille_capital)
            char = char.lower()
        if char.isdigit():
            result.append(braille_number)
        result.append(eng_to_braille.get(char, ""))
    return "".join(result)

# Function to convert Braille to English
def braille_to_english(input_text):
    result = []
    i = 0
    while i < len(input_text):
        char = input_text[i:i+6]
        if char == braille_capital:
            i += 6
            next_char = input_text[i:i+6]
            result.append(braille_to_eng[next_char].upper())
        elif char == braille_number:
            i += 6
            while i < len(input_text):
                next_char = input_text[i:i+6]
                if next_char == "......":
                    break
                result.append(braille_to_eng.get(next_char, ""))
        else:
            result.append(braille_to_eng.get(char, ""))
        i += 6
    return "".join(result)

# Main function
def main():
    if len(sys.argv) != 2:
        print("Incorrect format, use: python translator.py <text>")
        return

    input_text = sys.argv[1]
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()
 