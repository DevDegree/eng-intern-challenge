import sys

input = sys.argv[1:]
input_string = " ".join(input)
output = ""

braille_dict_letters = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO"
}

special_symbols = {
    "cap_follows": ".....O",
    "decimal_follows": ".O...O",
    "number_follows": ".O.OOO",
    "space": "......"
}

number_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

def get_key(val, dictionary):
    """Fetch the key corresponding to a value in a given dictionary."""
    for key, value in dictionary.items():
        if val == value:
            return key
    return None

def process_english_to_braille(input_string):
    """Convert English string to Braille."""
    output = ""
    char_is_num = False

    for char in input_string:
        if char.isupper():
            output += special_symbols["cap_follows"]
            output += braille_dict_letters[char.lower()]
            char_is_num = False
        elif char.isdigit():
            if not char_is_num:
                output += special_symbols["number_follows"]
                char_is_num = True
            output += number_braille[char]
        elif char == ' ':
            output += special_symbols["space"]
            char_is_num = False
        else:
            output += braille_dict_letters[char]
            char_is_num = False
    return output

def process_braille_to_english(input_string):
    """Convert Braille string to English."""
    output = ""
    char_is_num = False
    count = 0

    while count < len(input_string):
        chunk = input_string[count:count+6]

        if chunk == special_symbols["cap_follows"]:
            char_is_num = False
            next_char = get_key(input_string[count+6:count+12], braille_dict_letters)
            if next_char:
                output += next_char.upper()
                count += 12
            else:
                count += 6
        elif chunk == special_symbols["number_follows"]:
            char_is_num = True
            count += 6
        elif chunk == special_symbols["space"]:
            output += ' '
            char_is_num = False
            count += 6
        else:
            if char_is_num:
                number_char = get_key(chunk, number_braille)
                if number_char:
                    output += number_char
                    count += 6
                else:
                    char_is_num = False
            else:
                letter_char = get_key(chunk, braille_dict_letters)
                if letter_char:
                    output += letter_char
                    count += 6
    return output

# Detect mode (English to Braille or Braille to English)
def detect_mode(input_string):
    """Detect whether input is English or Braille."""
    if '.' in input_string or 'O' in input_string:
        return "braille_to_english"
    else:
        return "english_to_braille"

# Main function to drive the translation
def translate(input_string):
    """Handle the translation based on detected input mode."""
    mode = detect_mode(input_string)
    if mode == "english_to_braille":
        return process_english_to_braille(input_string)
    else:
        return process_braille_to_english(input_string)

# Execute translation
output = translate(input_string)
print(output)
