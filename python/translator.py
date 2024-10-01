import sys

# Braille representations using 'O' for raised dots and '.' for flat dots
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO'
}

# Reverse mapping from Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Maps numbers to corresponding letters (1 -> a, 2 -> b, etc.)
number_to_letter = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
                    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}

# Function to convert English to Braille
def english_to_braille(text):
    braille_output = ""
    is_number = False

    for char in text:
        if char.isdigit() and not is_number:
            braille_output += braille_dict['number']  # Number indicator
            is_number = True
        elif char.isalpha() and char.isupper():
            braille_output += braille_dict['capital']  # Capital letter indicator
            char = char.lower()
            is_number = False
        elif char == ' ':
            is_number = False

        braille_output += braille_dict.get(char, '......')  # Space or default Braille

    return braille_output

# Function to convert Braille to English
def braille_to_english(braille):
    english_output = ""
    i = 0
    is_capital = False
    is_number = False

    while i < len(braille):
        symbol = braille[i:i+6]

        if symbol == braille_dict['capital']:
            is_capital = True
            i += 6
            continue
        elif symbol == braille_dict['number']:
            is_number = True
            i += 6
            continue
        elif symbol == '......':  # Space in Braille
            is_number = False
            english_output += ' '
            i += 6
            continue

        if is_number and symbol in reverse_braille_dict:
            num_char = reverse_braille_dict[symbol]
            english_output += num_char
        elif not is_number and symbol in reverse_braille_dict:
            char = reverse_braille_dict[symbol]
            if is_capital:
                english_output += char.upper()
                is_capital = False
            else:
                english_output += char
        i += 6

    return english_output

# Detect whether input is English or Braille, then translate accordingly
def detect_and_translate(input_string):
    # If the input is purely Braille (contains only 'O' and '.'), translate to English
    if all(c in 'O.' for c in input_string):
        return braille_to_english(input_string)
    # Otherwise, assume it's English and translate to Braille
    else:
        return english_to_braille(input_string)

# Main execution block
if __name__ == "__main__":
    # Take the input from the command line arguments
    input_text = " ".join(sys.argv[1:])
    output_text = detect_and_translate(input_text)
    print(output_text)

