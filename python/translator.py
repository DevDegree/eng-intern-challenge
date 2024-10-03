import sys

# Braille to English translation dict
braille_to_text_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", "..OO.O": ".", "..O...": ",", "..O.OO": "?",
    "..OOO.": "!", "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/",
    ".OO..O": "<", "O.O..O": "(", ".O.OO.": ")", ".....O": "CAP", ".O.OOO": "NUM"
}

# Reverse dict
text_to_braille_map = {v: k for k, v in braille_to_text_map.items()}

# Number mappings (special case for Braille)
digits_to_braille_map = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO..."
}

def convert_text_to_braille(text):
    """Converts English text to Braille."""
    braille_output = []
    is_number_mode = False

    for char in text:
        if char.isdigit():
            if  is_number_mode == False:
                braille_output.append(".O.OOO")  # Number follows indicator
                is_number_mode = True
            braille_output.append(digits_to_braille_map[char])
        elif char.isalpha():
            if is_number_mode:
                braille_output.append("......")  # Reset number mode with a space
                is_number_mode = False
            if char.isupper():
                braille_output.append(".....O")  # Capital follows indicator
            braille_output.append(text_to_braille_map[char.lower()])
        else:
            if is_number_mode:
                is_number_mode = False  # Reset number mode if encountering a non-digit
            braille_output.append(text_to_braille_map[char])

    return ''.join(braille_output)

def convert_braille_to_text(braille_input):
    """Converts Braille to English text."""
    english_output = []
    i = 0
    braile_pattern_chars = 6
    while i < len(braille_input):
        braille_char = braille_input[i:i+braile_pattern_chars]

        if braille_char == ".....O":  # Capital indicator
            i += braile_pattern_chars
            next_braille_char = braille_input[i:i+6]
            english_output.append(braille_to_text_map[next_braille_char].upper())
        elif braille_char == ".O.OOO":  # Number indicator
            i += braile_pattern_chars
            while i < len(braille_input) and braille_input[i:i+6] != "......":
                digit_braille = braille_input[i:i+6]
                digit = str(list(digits_to_braille_map.values()).index(digit_braille) + 1)
                english_output.append(digit)
                i += braile_pattern_chars
            # Skip the space after number mode
            continue
        else:
            english_output.append(braille_to_text_map.get(braille_char, ""))
        i += braile_pattern_chars

    return ''.join(english_output)

def detect_input_type(input_string):
    """Detects if the input is Braille or English text."""
    # Check if all characters are either 'O' or '.'
    if all(char in 'O.' for char in input_string):
        return "braille"
    else:
        return "text"

def main():
    """Main function to handle command-line inputs and conversion."""
    # Gather the input from command-line arguments
    input_data = ' '.join(sys.argv[1:])

    # Detect the type of input and convert accordingly
    input_type = detect_input_type(input_data)

    if input_type == "braille":
        # Convert Braille to English
        print(convert_braille_to_text(input_data))
    else:
        # Convert English to Braille
        print(convert_text_to_braille(input_data))

if __name__ == "__main__":
    main()