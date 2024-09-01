import sys

# Updated Braille dictionary for English letters, and numbers
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    
    ' ': '......'
}
braillenum_dict = {  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',}

# Special indicators in Braille
CAPITAL_INDICATOR = '.....O'
NUMBER_INDICATOR = '.O.OOO'
DECIMAL_INDICATOR = '.O...O'

# Reverse dictionary for translating Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}
reverse_num_dict = {v: k for k, v in braillenum_dict.items()}
def is_braille(s):
    """Check if the input string is Braille."""
    return all(c in 'O.' for c in s) and len(s) % 6 == 0

def translate_to_braille(text):
    """Translate English text to Braille."""
    braille = ''
    number_mode = False

    for char in text:
        if char.isupper():
            braille += CAPITAL_INDICATOR
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                braille += NUMBER_INDICATOR
                number_mode = True
            braille += braillenum_dict[char]
        elif char == '.':
            braille += DECIMAL_INDICATOR
        elif char == ' ':
            braille += '......'
            number_mode = False  # Reset number mode after a space
        else:
            braille += braille_dict.get(char, '......')
    
    return braille

def translate_to_english(braille):
    """Translate Braille to English text."""
    english = ''
    i = 0
    capitalize_next = False
    number_mode = False

    # Ensure the Braille input length is a multiple of 6
    if len(braille) % 6 != 0:
        raise ValueError("The Braille input length must be a multiple of 6.")

    while i < len(braille):
        symbol = braille[i:i+6]

        if symbol == CAPITAL_INDICATOR:
            capitalize_next = True
            i += 6
            continue
        elif symbol == NUMBER_INDICATOR:
            number_mode = True
            i += 6
            continue
        elif symbol == DECIMAL_INDICATOR:
            english += '.'
            i += 6
            continue
        elif symbol == '......':  # Handle spaces
            english += ' '
            number_mode = False  # Reset number mode on space
            i += 6
            continue
        else:
            if number_mode and symbol in reverse_num_dict:
                digit = reverse_num_dict[symbol]
                if digit.isdigit():
                    english += digit
                else:
                    number_mode = False  # Exit number mode if it's not a digit
            elif symbol in reverse_braille_dict:
                char = reverse_braille_dict[symbol]
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                english += char

        i += 6
        print(f"Symbol: {symbol}, Number mode: {number_mode}, Capitalize next: {capitalize_next}, English so far: {english}")

    return english

def main():
    """Main function to determine input type and perform translation."""
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text or braille>")
        return

    input_text = sys.argv[1]

    if is_braille(input_text):
        output = translate_to_english(input_text)
    else:
        output = translate_to_braille(input_text)

    print(output)

if __name__ == "__main__":
    main()
