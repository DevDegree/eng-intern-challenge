import sys

# braille mappings
braille_to_english = {
    # alphabet: a-z
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
    "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
    ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z",
    # numbers: 0-9
    ".OOO..": "0", "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
    "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
    # special characters/cases: capitalization, numbers, and space
    ".....O": "CAPITAL", 
    ".O.OOO": "NUMBER", 
    "......": " ", 
}

# creating a reverse mapping from english characters to braille patterns
english_to_braille = {v: k for k, v in braille_to_english.items() if v not in ("CAPITAL", "NUMBER", " ")}

# special braille characters/cases for capitalization, numbers, and space
braille_capital = ".....O"
braille_number = ".O.OOO"
braille_space = "......"

# function for translating from english to braille
def translate_to_braille(text):
    braille_text = []
    for char in text:
        if char.isupper(): # handling case with capital letters
            braille_text.append(braille_capital)
            braille_text.append(english_to_braille[char.lower()])
        elif char.isdigit(): # handling case with numbers
            braille_text.append(braille_number)
            braille_text.append(english_to_braille[char])
        elif char == " ": # handling case with space / whitespace
            braille_text.append(braille_space)
        else: # handling case with lowercase letters
            braille_text.append(english_to_braille[char])
    return "".join(braille_text)

# function for translating from braille to english
def translate_to_english(braille):
    english_text = []
    is_capital = False
    is_number = False
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]
        if braille_char == braille_capital: # if the next character is a capital
            is_capital = True
            continue
        elif braille_char == braille_number: # if the next character is a number
            is_number = True
            continue
        elif braille_char == braille_space: # if the next character is a space
            english_text.append(" ")
            is_capital = False
            is_number = False
            continue

        char = braille_to_english.get(braille_char, "?")
        if is_number and char.isdigit(): # adding the numbers
            english_text.append(char)
        elif is_capital: # adding the capital letters
            english_text.append(char.upper())
            is_capital = False
        else: # adding the lowercase letters
            english_text.append(char)
    return "".join(english_text)

# main function
def main():
    if len(sys.argv) < 2:
        print("Please provide an input string to translate.")
        return

    # combining all arguments for multi-word input
    input_string = " ".join(sys.argv[1:])

    # determing if the input is Braille or English
    if set(input_string).issubset({'O', '.'}):
        # if the input is in braille
        print(translate_to_english(input_string))
    else:
        # if the input is in english
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()
