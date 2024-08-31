import sys

# Dictionary to map English characters to Braille patterns
english_to_braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......",
    ".": "..OO.O", ",": "..O...", "?": "..O.O.", "!": "..OOO.", ":": "OO....",
    ";": "..0.0.", "-": "..O..O", "/": ".O..O.", "(": ".O.O.O", ")": ".O.O.O",
    "capital": ".....O", "number": ".O.OOO", "decimal": ".O...O"
}

# Reverse dictionary to map Braille patterns to English characters
braille_to_english_map = {value: key for key, value in english_to_braille_map.items()}

# Dictionary to map numbers to Braille patterns
number_to_braille_map = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Reverse dictionary to map Braille patterns to numbers
braille_to_number_map = {value: key for key, value in number_to_braille_map.items()}

# Function to check if a string is a valid Braille pattern
def is_braille_pattern(input_string):
    return all(char in 'O.' for char in input_string) and len(input_string) % 6 == 0

# Function to convert a Braille pattern string to English text
def braille_to_text(braille_string):
    if len(braille_string) % 6 != 0:
        print("Invalid Braille input: length should be a multiple of 6.")
        return ""

    # Split Braille string into 6-character cells
    braille_cells = [braille_string[i:i + 6] for i in range(0, len(braille_string), 6)]

    translated_text = []
    is_capital_next = False  # Flag to capitalize the next letter
    is_number_mode = False  # Flag to interpret following cells as numbers

    for cell in braille_cells:
        if cell == ".....O":  # Capital follows
            is_capital_next = True
        elif cell == ".O.OOO":  # Number follows
            is_number_mode = True
        elif cell == ".O...O":  # Decimal point in number mode
            translated_text.append(".")
        elif cell == "......":  # Space
            translated_text.append(" ")
            is_number_mode = False  # End number mode on space
        else:
            if is_number_mode:
                char = braille_to_number_map.get(cell, "")
            else:
                char = braille_to_english_map.get(cell, "")
                if is_capital_next:
                    char = char.upper()
                    is_capital_next = False

            translated_text.append(char)
            is_number_mode = False  # Reset number mode after processing the digit

    return "".join(translated_text)

# Function to convert English text to Braille pattern string
def text_to_braille(text_string):
    braille_pattern = []
    for char in text_string:
        if char.isupper():
            # Add capital Braille pattern before the letter
            braille_pattern.append(english_to_braille_map["capital"])
            braille_pattern.append(english_to_braille_map[char.lower()])
        elif char.isdigit():
            # Add number Braille pattern before the digit
            if not braille_pattern or braille_pattern[-1] != english_to_braille_map["number"]:
                braille_pattern.append(english_to_braille_map["number"])
            braille_pattern.append(number_to_braille_map[char])
        elif char == ".":
            # Special case for decimal point
            braille_pattern.append(english_to_braille_map["decimal"])
        else:
            # Default to space if character not found in dictionary
            braille_pattern.append(english_to_braille_map.get(char, "......"))
    return "".join(braille_pattern)

# Main function to determine if the input is Braille or English and translate accordingly
def main(input_string):
    if is_braille_pattern(input_string):
        return braille_to_text(input_string)
    else:
        return text_to_braille(input_string)

# Entry point for command-line execution
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])
        output_string = main(input_string)
        print(output_string)
    else:
        print("Please provide a string as a command-line argument.")
