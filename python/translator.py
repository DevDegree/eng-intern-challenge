import sys

# Create a dictionary for Braille equivalents of lowercase alphabet and space.
braille_char_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

# Braille mapping for numbers.
braille_num_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Special Braille indicators.
capital_indicator = '.....O'
number_indicator = '.O.OOO'

# Reverse mappings for decoding Braille back to English.
reverse_braille_char_map = {v: k for k, v in braille_char_map.items()}
reverse_braille_num_map = {v: k for k, v in braille_num_map.items()}

# Function to check if the input string follows Braille format.
def check_if_braille(input_str):
    return all(ch in "O." for ch in input_str) and len(input_str) % 6 == 0


# Function to convert Braille back to English text.
def braille_to_english(braille):
    decoded = []
    next_upper = False
    num_mode = False

    i = 0
    while i < len(braille):
        current_symbol = braille[i:i+6]
        if current_symbol == capital_indicator:
            next_upper = True
        elif current_symbol == number_indicator:
            num_mode = True
        else:
            if num_mode:
                decoded.append(reverse_braille_num_map.get(current_symbol, ''))
                num_mode = False
            elif next_upper:
                decoded.append(reverse_braille_char_map.get(current_symbol, '').upper())
                next_upper = False
            else:
                decoded.append(reverse_braille_char_map.get(current_symbol, ''))
        i += 6

    return ''.join(decoded)


# Function to convert English text to Braille.
def english_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(number_indicator)
                number_mode = True
            result.append(braille_num_map[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(capital_indicator)
            result.append(braille_char_map[char.lower()])
        elif char == ' ':
            result.append(braille_char_map[' '])
            number_mode = False

    return ''.join(result)

# Main function to handle input and determine translation direction.
def main():
    # Combine command-line arguments into a single string.
    input_data = ' '.join(sys.argv[1:])

    # Determine if the input is Braille or plain text, then perform translation.
    if check_if_braille(input_data):
        print(braille_to_english(input_data))
    else:
        print(english_to_braille(input_data))

# Execute the main function if the script is run directly.
if __name__ == "__main__":
    main()


