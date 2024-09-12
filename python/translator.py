
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OOO...": "d", "O..O..": "e",
    "OO.O..": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OOO.O.": "n", "O..OO.": "o",
    "OO.OO.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OOO.OO": "y",
    "O..OOO": "z", "......": " "  # Space
}

# Reverse dictionary for English to Braille
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Function to detect if input is Braille
def is_braille(input_str):
    return all(char in "O. " for char in input_str)

# Function to perform translation
def translate(input_str):
    if is_braille(input_str):
        # Split Braille symbols and translate to English
        symbols = input_str.split(" ")
        translated = "".join([braille_to_english.get(symbol, "?") for symbol in symbols])
    else:
        # Translate English to Braille
        translated = " ".join([english_to_braille.get(char.lower(), "?") for char in input_str])
    
    return translated

# Command-line execution
if _name_ == "_main_":
    import sys
    if len(sys.argv) > 1:
        input_str = sys.argv[1]
        output = translate(input_str)
        print(output)
    else:
        print("Please provide input to translate.")
