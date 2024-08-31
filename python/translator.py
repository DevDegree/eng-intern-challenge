import sys

# Dictionaries to map between English and Braille
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z",
    ".....O": "capitalize", ".O.OOO": "number",
    "......": " "
}

english_to_braille = {v: k for k, v in braille_to_english.items() if v != "capitalize" and v != "number"}

# Function to check if the input string is Braille
def is_braille(s):
    return all(c in "O." for c in s)

# Function to translate from Braille to English
def translate_braille_to_english(input_string):
    translated = []
    i = 0
    while i < len(input_string):
        braille_char = input_string[i:i + 6]
        i += 6
        if braille_to_english[braille_char] == "capitalize":
            braille_char = input_string[i:i + 6]
            translated.append(braille_to_english[braille_char].upper())
            i += 6
        elif braille_to_english[braille_char] == "number":
            braille_char = input_string[i:i + 6]
            while braille_char != "......":
                translated.append(braille_to_english[braille_char])
                i += 6
                braille_char = input_string[i:i + 6]
        else:
            translated.append(braille_to_english[braille_char])
    return "".join(translated)

# Function to translate from English to Braille
def translate_english_to_braille(input_string):
    translated = []
    for char in input_string:
        if char.isupper():
            translated.append(".....O")  # Capitalization symbol
            translated.append(english_to_braille[char.lower()])
        elif char.isdigit():
            translated.append(".O.OOO")  # Number symbol
            translated.append(english_to_braille[char])
        else:
            translated.append(english_to_braille[char])
    return "".join(translated)

# Function to determine if the input is Braille or English and translate it
def translate(input_string):
    if is_braille(input_string):
        return translate_braille_to_english(input_string)
    else:
        return translate_english_to_braille(input_string)

# Main execution
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        print(translate(input_string))
    else:
        print("Error: No input string provided.")
