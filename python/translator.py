braille_to_english_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", 
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", 
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "CAPITAL", ".O.OOO": "NUMBER", "......": " "
}

braille_to_digit_map = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", 
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

english_to_braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", 
    "0": ".OOO..", " ": "......"
}

CAPITAL_INDICATOR = ".....O"
NUMBER_INDICATOR = ".O.OOO"

def check_if_braille(input_text):
    """Verify if the input consists only of Braille symbols."""
    return all(char in 'O.' for char in input_text)

def braille_to_english(input_braille):
    """Convert a Braille string to its equivalent English text."""
    translation = []
    capitalize_next = False
    number_mode = False

    # Read Braille in chunks of 6 characters
    for idx in range(0, len(input_braille), 6):
        braille_char = input_braille[idx:idx + 6]

        # Handle capital letters
        if braille_char == CAPITAL_INDICATOR:
            capitalize_next = True
            continue

        # Handle numbers
        if braille_char == NUMBER_INDICATOR:
            number_mode = True
            continue

        # Translate based on number mode or letter mode
        if number_mode:
            translated_char = braille_to_digit_map.get(braille_char, '')
            if translated_char:
                translation.append(translated_char)
            else:
                number_mode = False  # Exit number mode if invalid
        else:
            translated_char = braille_to_english_map.get(braille_char, '')
            if capitalize_next:
                translated_char = translated_char.upper()  # Capitalize next letter
                capitalize_next = False
            translation.append(translated_char)

    return ''.join(translation)

def english_to_braille(input_text):
    """Convert an English text to its Braille equivalent."""
    translation = []
    in_number_mode = False

    # Process each character in the input string
    for char in input_text:
        if char == ' ':
            translation.append(english_to_braille_map[char])
            in_number_mode = False  # Reset number mode after space
            continue

        # Capitalization handling
        if char.isupper():
            translation.append(CAPITAL_INDICATOR)
            char = char.lower()

        # Number handling
        if char.isdigit():
            if not in_number_mode:
                translation.append(NUMBER_INDICATOR)  # Add number sign
                in_number_mode = True
            translation.append(english_to_braille_map[char])
        else:
            in_number_mode = False  # Exit number mode after non-digit
            braille_char = english_to_braille_map.get(char, '')
            translation.append(braille_char)

    return ''.join(translation)

def process_translation(input_text):
    """Determine if the input is Braille or English and convert accordingly."""
    if check_if_braille(input_text):
        return braille_to_english(input_text)
    else:
        return english_to_braille(input_text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("No input provided for translation.")
    else:
        input_data = ' '.join(sys.argv[1:])
        result = process_translation(input_data)
        if result:
            print(result)
