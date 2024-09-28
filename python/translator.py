import sys

# Braille dictionary for converting English to Braille
braille_mapping = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital_marker': '.....O', 'number_marker': '.O.OOO'
}

# Reverse Braille dictionary for converting Braille back to English (for letters only)
reverse_braille_mapping_letters = {v: k for k, v in braille_mapping.items() if not k.isdigit()}
# Reverse Braille dictionary for converting Braille back to English (for numbers only)
reverse_braille_mapping_numbers = {v: k for k, v in braille_mapping.items() if k.isdigit()}


# Converts English text into Braille
def english_to_braille_conversion(text: str) -> str:
    braille_output = ''
    in_number_mode = False  # Flag to check if we are in number mode

    for char in text:
        if char.isdigit() and not in_number_mode:
            braille_output += braille_mapping['number_marker']
            in_number_mode = True
        if char == ' ':
            in_number_mode = False  # Reset number mode if a space is found
        if char.isupper():
            braille_output += braille_mapping['capital_marker']
        # Add the Braille representation of the character
        braille_output += braille_mapping.get(char.lower(), '')
    return braille_output

# Converts Braille text back into English
def braille_to_english_conversion(braille: str) -> str:
    english_output = ''
    index = 0

    while index < len(braille):
        symbol = braille[index:index + 6]
        if symbol == braille_mapping['capital_marker']:
            # The next character is capital
            index += 6
            symbol = braille[index:index + 6]
            english_output += reverse_braille_mapping_letters[symbol].upper()
        elif symbol == braille_mapping['number_marker']:
            index += 6
            # Continue reading numbers until a space is found
            while index < len(braille):
                number_symbol = braille[index:index + 6]
                if number_symbol == '......':  # A space indicates end of number mode
                    break
                english_output += reverse_braille_mapping_numbers[number_symbol]
                index += 6
            continue
        else:
            english_output += reverse_braille_mapping_letters.get(symbol, '')
        index += 6
    return english_output

# Determines if the input text is Braille or English
def detect_braille_or_english(text: str) -> bool:
    # If the text contains only 'O' and '.', it's Braille
    return all(char in 'O.' for char in text)

def main():
    # Join the input arguments into a string
    input_text = ' '.join(sys.argv[1:])

    # Detect whether the input is Braille or English and process accordingly
    if detect_braille_or_english(input_text):
        print(braille_to_english_conversion(input_text))
    else:
        print(english_to_braille_conversion(input_text))

if __name__ == "__main__":
    main()
    