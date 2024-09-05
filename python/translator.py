def main(input_string):
    if "O" in input_string or "." in input_string:
        # Treat as Braille input
        result = braille_to_english(input_string)
    else:
        # Treat as English input
        result = english_to_braille(input_string)
    
    print(result)

def braille_to_english(braille_string):
    braille_to_english_map = {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OOO...": "d", "O..O..": "e",
        "OO.O..": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
        "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OOO.O.": "n", "O..OO.": "o",
        "OO.OO.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OOO.OO": "y", "O..OOO": "z",
        ".O.OOO": "#",  # Number sign
        ".....O": "^",  # Capital letter sign
        "......": " ",   # Space
    }
    
    translation = []
    capitalize_next = False
    number_mode = False
    
    # Split the input string into 6-character chunks
    braille_chars = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    
    for braille_char in braille_chars:
        if braille_char == ".....O":  # Capital marker
            capitalize_next = True
        elif braille_char == ".O.OOO":  # Number marker
            number_mode = True
        elif braille_char == "......":  # Space
            translation.append(" ")
        elif braille_char in braille_to_english_map:
            char = braille_to_english_map[braille_char]
            if number_mode:
                char = convert_to_number(char)  # Handle number conversion
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            translation.append(char)
    
    return ''.join(translation)

def english_to_braille(english_string):
    english_to_braille_map = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OOO...", "e": "O..O..",
        "f": "OO.O..", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OOO.O.", "o": "O..OO.",
        "p": "OO.OO.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OOO.OO", "z": "O..OOO",
        "capital": ".....O", "number": ".O.OOO", " ": "......",
    }
    
    translation = []
    for char in english_string:
        if char.isupper():
            translation.append(english_to_braille_map["capital"])
            char = char.lower()
        if char.isdigit():
            translation.append(english_to_braille_map["number"])
            char = convert_to_braille_digit(char)
        if char in english_to_braille_map:
            translation.append(english_to_braille_map[char])
    
    return ''.join(translation)

def convert_to_number(char):
    # Map letters to numbers (Braille digits mode)
    letter_to_number_map = {
        "a": "1", "b": "2", "c": "3", "d": "4", "e": "5",
        "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"
    }
    return letter_to_number_map.get(char, char)

def convert_to_braille_digit(digit):
    # Convert a digit to its Braille representation
    digit_to_braille_map = {
        "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OOO...", "5": "O..O..",
        "6": "OO.O..", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
    }
    return digit_to_braille_map.get(digit, digit)

test_input = "python"  # This is an example input
main(test_input)
