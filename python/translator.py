import sys

# Get the input arguments
input_data = sys.argv[1:]
input_text = " ".join(input_data)
translated_output = ""

# Dictionary mapping for Braille letters
braille_to_letter = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO"
}

# Special symbols mapping for Braille
special_braille = {
    "capital": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO",
    "space": "......"
}

# Braille for numbers (1-10)
braille_numbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "10": ".OOO.."
}

# Function to find a letter or number based on the Braille pattern
def braille_lookup(braille_code, mode):
    if mode == "letter":
        for char, pattern in braille_to_letter.items():
            if braille_code == pattern:
                return char
    elif mode == "number":
        for digit, pattern in braille_numbers.items():
            if braille_code == pattern:
                return digit
    return None

# Determine the conversion mode: Braille to English or English to Braille
convert_mode = 0 if '.' in input_text else 1
numeric_mode = False

if convert_mode == 1:
    # English to Braille
    for char in input_text:
        if char.isupper():
            numeric_mode = False
            translated_output += special_braille["capital"]
            translated_output += braille_to_letter[char.lower()]
        elif char.isdigit():
            if not numeric_mode:
                numeric_mode = True
                translated_output += special_braille["number"]
            translated_output += braille_numbers[char]
        elif char == ' ':
            numeric_mode = False
            translated_output += special_braille["space"]
        else:
            numeric_mode = False
            translated_output += braille_to_letter[char]
else:
    # Braille to English
    idx = 0
    while idx < len(input_text):
        segment = input_text[idx:idx+6]
        if segment == special_braille["capital"]:
            numeric_mode = False
            letter = braille_lookup(input_text[idx+6:idx+12], "letter")
            translated_output += letter.upper()
            idx += 12
        elif segment == special_braille["number"] or numeric_mode:
            if not numeric_mode:
                numeric_mode = True
                number = braille_lookup(input_text[idx+6:idx+12], "number")
                translated_output += number
                idx += 12
            else:
                number = braille_lookup(segment, "number")
                translated_output += number
                idx += 6
                if braille_lookup(input_text[idx:idx+6], "number") is None:
                    numeric_mode = False
        elif segment == special_braille["space"]:
            numeric_mode = False
            translated_output += ' '
            idx += 6
        else:
            numeric_mode = False
            translated_output += braille_lookup(segment, "letter")
            idx += 6

print(translated_output)

