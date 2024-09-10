# P.S. Created using any sorces available
import sys # for command line input

# Creating the dictionary 0for the braille and eng lang

braille_to_english = {
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

    ".O.OOOO": "#",
    ".....O": "^",
    "......": " ",

    ".O....": "1", 
    ".O.O..": "2", 
    ".OO...": "3", 
    ".OO.O.": "4", 
    ".O..O.": "5",
    ".OOO..": "6", 
    ".OOOO.": "7", 
    ".O.OO.": "8", 
    "..OO..": "9", 
    "..OOO.": "0",

    # "......": " ",
    ".O....": ".",
    "O.....": ",",
    ".OO.O.": "?",
    ".O.O.O": "!",
    ".O.O..": ":",
    ".OO.O.": ";",
    ".OOO.O": "-",
    ".O..OO": "/",
    "O..O.O": "<",
    "O..OO.": ">",
    "O.O.OO": "(",
    "OOO.OO": ")",
    #"O.O.O.": "[",
    #"OOO.O.": "]",
}

english_to_braille = {v: k for k, v in braille_to_english.items()}
english_to_braille.update({
    "1": ".O....", "2": ".O.O..", "3": ".OO...", "4": ".OO.O.", "5": ".O..O.",
    "6": ".OOO..", "7": ".OOOO.", "8": ".O.OO.", "9": "..OO..", "0": "..OOO.",
    " ": "......", ".": ".O....", ",": "O.....", "?": ".OO.O.", "!": ".O.O.O",
    ":": ".O.O..", ";": ".OO.O.", "-": ".OOO.O", "/": ".O..OO", "<": "O..O.O",
    ">": "O..OO.", "(": "O.O.OO", ")": "OOO.OO", "[": "O.O.O.", "]": "OOO.O.",
})


capital_prefix = ".....O" # Capital follows
number_prefix = ".O.OOOO" # Number follows

# Condition to check and execute code if the language found is braille

def is_braille(input_str):
    return all(c == 'O' or c == '.' for c in input_str)

def translate_braille_to_english(braille_input):
    english_output = []
    i = 0
    number_mode = False
    while i < len(braille_input):
        # Take the next 6 characters (one Braille character)
        symbol = braille_input[i:i+6]
        i += 6
        
        if symbol == capital_prefix:
            next_symbol = braille_input[i:i+6]
            i += 6
            english_output.append(braille_to_english[next_symbol].upper())
        elif symbol == number_prefix:
            number_mode = True
        elif symbol == "......":
            english_output.append(" ")
            number_mode = False
        else:
            if number_mode and symbol in braille_to_english:
                numbers = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5",
                           "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"}
                english_output.append(numbers[braille_to_english[symbol]])
            else:
                english_output.append(braille_to_english[symbol])

    return ''.join(english_output)

# Applying translation from english to braille

def translate_english_to_braille(english_input):
    braille_output = []
    for char in english_input:
        if char.isupper():
            braille_output.append(capital_prefix)
            char = char.lower()
        if char.isdigit():
            braille_output.append(number_prefix)
            number_mode = False
            char = { "1": "a", "2": "b", "3": "c", "4": "d", "5": "e",
                     "6": "f", "7": "g", "8": "h", "9": "i", "0": "j" }[char]
        braille_output.append(english_to_braille[char])

    return ''.join(braille_output)

# Execution

def main():
    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))

if __name__ == "__main__":
    main()
