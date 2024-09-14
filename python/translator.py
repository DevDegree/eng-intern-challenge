import sys

# English to Braille dictionary for letters and punctuation
ENGLISH_TO_BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
    ':': '..OO..', ';': '..O.O.', ' ': '......', 'capital': '.....O'
}

# English to Braille dictionary for numbers
ENGLISH_TO_BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'number': '.O.OOO'
}

# Braille to English dictionary for letters and punctuation
BRAILLE_TO_ENGLISH_LETTERS = {value: key for key, value in ENGLISH_TO_BRAILLE_LETTERS.items()}

# Braille to English dictionary for numbers
BRAILLE_TO_ENGLISH_NUMBERS = {value: key for key, value in ENGLISH_TO_BRAILLE_NUMBERS.items()}

def braille_to_english(braille_str):
    """Converts Braille to English, distinguishing between numbers and letters."""
    braille_str = braille_str.replace(' ', '')  # Normalize the input string
    english_text = []
    is_capital = False
    is_number = False

    for i in range(0, len(braille_str), 6):
        curr_braille = braille_str[i:i+6]

        # Handle capital and number markers
        if curr_braille == '.....O':
            is_capital = True
            continue
        elif curr_braille == '.O.OOO':
            is_number = True
            continue

        # Handle letters and numbers separately
        if is_number:
            # Look up in the number dictionary
            if curr_braille in BRAILLE_TO_ENGLISH_NUMBERS:
                translated_char = BRAILLE_TO_ENGLISH_NUMBERS[curr_braille]
                english_text.append(translated_char)
            else:
                return f"Invalid Braille number pattern: {curr_braille}"
        else:
            # Look up in the letter dictionary
            if curr_braille in BRAILLE_TO_ENGLISH_LETTERS:
                translated_char = BRAILLE_TO_ENGLISH_LETTERS[curr_braille]
                if is_capital:
                    translated_char = translated_char.upper()
                    is_capital = False  # Reset the capital marker
                english_text.append(translated_char)
            else:
                return f"Invalid Braille letter pattern: {curr_braille}"

    return ''.join(english_text)

def english_to_braille(english_str):
    """Converts English to Braille, distinguishing between numbers and letters."""
    braille_text = []
    is_number = False

    for char in english_str:
        if char.isupper():  # Handle capital letters
            braille_text.append(ENGLISH_TO_BRAILLE_LETTERS['capital'])  # Add capital marker
            char = char.lower()  # Convert to lowercase

        if char.isdigit():  # Handle numbers
            if not is_number:
                braille_text.append(ENGLISH_TO_BRAILLE_NUMBERS['number'])  # Add number marker once
                is_number = True
            braille_text.append(ENGLISH_TO_BRAILLE_NUMBERS[char])
        elif char == ' ':  # Handle spaces
            is_number = False
            braille_text.append(ENGLISH_TO_BRAILLE_LETTERS[' '])  # Add space marker for spaces
        else:
            is_number = False  # Reset number mode after letters
            braille_text.append(ENGLISH_TO_BRAILLE_LETTERS[char])  # Append Braille translation of letter

    return ''.join(braille_text)  # Return concatenated Braille string

def detect_input_type(input_str):
    """Detect whether the input is Braille or English text."""
    # If the input contains only 'O' and '.', it is Braille
    if all(c in 'O.' for c in input_str.replace(' ', '')):
        return "braille"
    else:
        return "english"

def main():
    # Check if command-line arguments were passed
    if len(sys.argv) > 1:
        # Join the arguments to form the input string
        input_str = " ".join(sys.argv[1:])

    # Detect whether the input is Braille or English
    input_type = detect_input_type(input_str)

    if input_type == "braille":
        result = braille_to_english(input_str)
        print(result)
    else:
        result = english_to_braille(input_str)
        print(result)

if __name__ == '__main__':
    main()
