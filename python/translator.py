import sys

# Braille character-to-text mappings
braille_to_text_map = {
    "......": " ", "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", 
    "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", 
    ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", 
    "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", 
    ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", 
    "OO.OOO": "y", "O..OOO": "z"
}

# Braille numeral-to-text mappings
braille_to_number_map = {
    ".OOOO.": "0", "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", 
    "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
    ".....O": "CAP", ".O.OOO": "NUM"
}

# Text-to-Braille mappings
text_to_braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "0": ".OOOO.", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    " ": "......"
}

# Prefixes for special cases
number_prefix = ".O.OOO"
capital_prefix = ".....O"

def is_english_text(input_str):
    """Checks if the input is valid text (letters, numbers, or spaces)."""
    return all(char.isalnum() or char.isspace() for char in input_str)

def is_braille_pattern(input_str):
    """Checks if the input is valid Braille (only contains Braille dots and spaces)."""
    clean_str = input_str.replace(' ', '')
    return all(dot in 'O.' for dot in clean_str) and len(clean_str) % 6 == 0

def convert_text_to_braille(input_str):
    """Transforms English text into its Braille equivalent."""
    braille_result = []
    number_mode = False

    for char in input_str:
        if char.isdigit():
            if not number_mode:
                braille_result.append(number_prefix)
                number_mode = True
            braille_result.append(text_to_braille_map[char])
        elif char.isalpha():
            if char.isupper():
                braille_result.append(capital_prefix)
                char = char.lower()
            braille_result.append(text_to_braille_map[char])
            number_mode = False
        elif char == ' ':
            braille_result.append(text_to_braille_map[' '])
            number_mode = False
    return ''.join(braille_result)

def convert_braille_to_text(input_str):
    """Converts Braille sequences back to plain English text."""
    output_text = []
    index = 0
    number_mode = False

    braille_chunks = [input_str[i:i+6] for i in range(0, len(input_str), 6)]

    while index < len(braille_chunks):
        chunk = braille_chunks[index]

        if chunk == capital_prefix:
            number_mode = False
            index += 1
            if index < len(braille_chunks):
                chunk = braille_chunks[index]
                output_text.append(braille_to_text_map[chunk].upper())
        elif chunk == number_prefix:
            number_mode = True
        elif number_mode:
            if chunk == "......":
                number_mode = False
            else:
                output_text.append(braille_to_number_map[chunk])
        else:
            output_text.append(braille_to_text_map[chunk])

        index += 1

    return ''.join(output_text)

def main():
    user_input = ' '.join(sys.argv[1:])

    if is_braille_pattern(user_input):
        print(convert_braille_to_text(user_input))
    elif is_english_text(user_input):
        print(convert_text_to_braille(user_input))
    else:
        print("Input is invalid.")

if __name__ == "__main__":
    main()
