# Mapping Braille symbols to English letters
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", 
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", 
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "CAPITAL", ".O.OOO": "NUMBER", "......": " "
}

# Braille numbers map to the same symbols as letters 'a' to 'j'
braille_to_number = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", 
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

# Mapping English letters and numbers to their Braille equivalents
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", 
    "0": ".OOO..", " ": "......"
}

# Special Braille signs for capitalization and numbers
CAPITAL_SIGN = ".....O"
NUMBER_SIGN = ".O.OOO"

def is_braille(input_str):
    """Check if the input is Braille (only contains 'O' and '.')"""
    return all(char in 'O.' for char in input_str)

def translate_braille_to_english(braille_str):
    """Convert a Braille string to English"""
    result = []
    is_capital = False
    is_number = False

    # Process Braille 6 characters at a time (as each Braille symbol is 6 characters long)
    for i in range(0, len(braille_str), 6):
        braille_char = braille_str[i:i+6]

        # Handle capital letters
        if braille_char == CAPITAL_SIGN:
            is_capital = True
            continue

        # Handle numbers
        if braille_char == NUMBER_SIGN:
            is_number = True
            continue

        # If in number mode, translate the Braille symbol to a number
        if is_number:
            char = braille_to_number.get(braille_char, '')
            if char:
                result.append(char)
            else:
                is_number = False  # Exit number mode if we encounter a non-number
        else:
            # Translate Braille symbol to a letter
            char = braille_to_english.get(braille_char, '')
            if is_capital:
                char = char.upper()  # Capitalize the next letter
                is_capital = False  # Reset capital mode
            result.append(char)

    return ''.join(result)

def translate_english_to_braille(english_str):
    """Convert an English string to Braille"""
    result = []
    is_in_number_mode = False  # Track if we are in number mode
    
    # Process each character in the input string
    for char in english_str:
        if char == ' ':
            result.append(english_to_braille[char])  # Add Braille for space
            is_in_number_mode = False  # Reset number mode when we hit a space
            continue

        # Handle capital letters
        if char.isupper():
            result.append(CAPITAL_SIGN)  # Add capital sign before uppercase letters
            char = char.lower()

        # Handle numbers
        if char.isdigit():
            if not is_in_number_mode:
                result.append(NUMBER_SIGN)  # Add number sign once before digits
                is_in_number_mode = True
            result.append(english_to_braille[char])
        else:
            is_in_number_mode = False  # Exit number mode after a non-number
            braille_char = english_to_braille.get(char, '')
            result.append(braille_char)

    return ''.join(result)

def main():
    import sys

    # Check if any input is provided
    if len(sys.argv) < 2:
        print("Please provide input to translate.")
        return ""

    # Join all arguments into a single string to handle multi-word input
    input_str = ' '.join(sys.argv[1:])

    # Determine whether the input is Braille or English and translate accordingly
    if is_braille(input_str):
        output = translate_braille_to_english(input_str)
    else:
        output = translate_english_to_braille(input_str)

    return output  # Return the result for testing purposes

if __name__ == "__main__":
    result = main()
    if result:  # Only print if there is a valid result
        print(result)

