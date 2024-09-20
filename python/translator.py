import sys

# Braille mappings for letters and digits
letter_to_braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
}

digit_to_braille_map = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}

# Reverse mappings for converting Braille back to text
braille_to_letter_map = {}
braille_to_digit_map = {}
for letter, braille_code in letter_to_braille_map.items():
    braille_to_letter_map[braille_code] = letter
for digit, braille_code in digit_to_braille_map.items():
    braille_to_digit_map[braille_code] = digit

# Function to check if the input is entirely made of Braille characters
def is_braille_input(input_string):
    allowed_braille_characters = ["O", "."]
    for character in input_string:
        if character not in allowed_braille_characters:
            return False
    return True

# Function to convert Braille to text
def braille_to_text(braille_string):
    is_capital = False
    is_number = False
    translated_text = ""

    index = 0
    while index < len(braille_string):
        current_braille_chunk = braille_string[index:index + 6]

        if current_braille_chunk == ".....O":  # Capital letter indicator
            is_capital = True
        elif current_braille_chunk == ".O.OOO":  # Number indicator
            is_number = True
        elif current_braille_chunk == "......":  # Space
            translated_text += " "
            is_number = False
        else:
            if is_number:
                translated_text += braille_to_digit_map.get(current_braille_chunk, "")
            else:
                current_letter = braille_to_letter_map.get(current_braille_chunk, "")
                if is_capital:
                    translated_text += current_letter.upper()
                    is_capital = False
                else:
                    translated_text += current_letter

        index += 6

    return translated_text

# Function to convert text to Braille
def text_to_braille(input_text):
    braille_output = ""
    number_mode = False

    for character in input_text:
        if character.isupper():
            braille_output += ".....O"  # Capital letter indicator
            character = character.lower()

        if character.isalpha():
            braille_output += letter_to_braille_map[character]
        elif character.isdigit():
            if not number_mode:
                braille_output += ".O.OOO"  # Number indicator
                number_mode = True
            braille_output += digit_to_braille_map[character]
        elif character == " ":
            braille_output += "......"
            number_mode = False

    return braille_output

# Function to handle user input, checking whether it is Braille or text
def process_input_string(input_string):
    if is_braille_input(input_string):
        return braille_to_text(input_string)
    else:
        return text_to_braille(input_string)

def main():
    if len(sys.argv) <= 1:
        return

    # Gather input data from command-line arguments
    input_data = ""
    argument_index = 1
    while argument_index < len(sys.argv):
        input_data += sys.argv[argument_index] + " "
        argument_index += 1

    input_data = input_data.strip()
    result = process_input_string(input_data)
    print(result)

if __name__ == "__main__":
    main()
