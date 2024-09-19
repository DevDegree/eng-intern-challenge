import sys

# Dictionary for Braille letter representations
text_to_braille_letters = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
}

# Dictionary for Braille punctuation representations
text_to_braille_punctuation = {
    ' ': '......',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
}

# Dictionary for Braille number representations
text_to_braille_numbers = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

# Reversed dictionary for Braille letter representations (Braille to letters)
braille_to_text_letters = {v: k for k, v in text_to_braille_letters.items()}

# Reversed dictionary for Braille punctuation representations (Braille to punctuation)
braille_to_text_punctuation = {v: k for k, v in text_to_braille_punctuation.items()}

# Reversed dictionary for Braille number representations (Braille to numbers)
braille_to_text_numbers = {v: k for k, v in text_to_braille_numbers.items()}


# Special Braille rules for capital, number, and decimal indicators
braille_rules = {
    'capital_follows': '.....O',  # Indicates that the next letter is capitalized
    'number_follows':  '.O.OOO',  # Indicates that the following characters are numbers
    'decimal_follows': '.O...O',  # Indicates a decimal point between digits
}

# Check if the input is valid Braille, ensuring it contains only Braille dots and has a length divisible by 6
def is_braille_input(input_text):
    return all( c in '.O' for c in input_text ) and len(input_text) % 6 == 0


# Convert English text to Braille, handling letters, numbers, punctuation, and capital letters
def convert_text_to_braille(input_text):
    braille_text = ''
    is_number = False  # Tracks if we're currently in number mode (numbers being processed)
    
    for i, c in enumerate(input_text):
        # Handle capital letters
        if c.isupper():
            braille_text += braille_rules['capital_follows']
            c = c.lower()

        # Handle digits
        if c.isdigit():
            if not is_number:
                braille_text += braille_rules['number_follows']
                is_number = True
            braille_text += text_to_braille_numbers[c]
        elif c == '.':
            # Handle decimal points between digits
            if i > 0 and i < len(input_text) - 1 and input_text[i-1].isdigit() and input_text[i+1].isdigit():
                braille_text += braille_rules['decimal_follows']
            else:
                braille_text += text_to_braille_punctuation[c]  # Standard period punctuation
        # Handle letters
        elif c in text_to_braille_letters:
            braille_text += text_to_braille_letters[c]
            is_number = False  # Exit number mode when encountering a letter
        # Handle punctuation
        elif c in text_to_braille_punctuation:
            braille_text += text_to_braille_punctuation[c]
            is_number = False  # Exit number mode after punctuation

    return braille_text

# Convert Braille text back to English, handling letters, numbers, punctuation, and capital letters
def convert_braille_to_text(input_text):
    text = []               # List to accumulate the converted text characters
    is_number = False       # Tracks if we're in number mode
    is_capital = False      # Tracks if the next letter should be capitalized

    # Process each Braille character block (6 dots)
    for i in range(0, len(input_text), 6):
        a_braille = input_text[i:i+6]

        # Handle number mode
        if a_braille == braille_rules['number_follows']:
            is_number = True
            continue

        # Handle capital letters
        if a_braille == braille_rules['capital_follows']:
            is_capital = True
            continue

        # Handle decimal point
        if a_braille == braille_rules['decimal_follows']:
            text.append('.')
            continue

        # Handle spaces
        if a_braille == '......':  
            text.append(' ')
            is_number = False
            continue

        # Convert numbers if in number mode
        if is_number:
            if a_braille in braille_to_text_numbers:
                text.append(braille_to_text_numbers[a_braille])
            continue

        # Convert letters and punctuation if not in number mode
        else:
            # Convert letters
            if a_braille in braille_to_text_letters:
                letter = braille_to_text_letters[a_braille]
                if is_capital:
                    letter = letter.upper()
                    is_capital = False
                text.append(letter)
            # Convert punctuation
            elif a_braille in braille_to_text_punctuation:
                text.append(braille_to_text_punctuation[a_braille])
            is_number = False  # Reset number mode after letter or punctuation

    return ''.join(text)

    
if __name__ == '__main__':
    # Check if there is input passed via command line
    if len(sys.argv) < 2:
        sys.exit(1)
  
    # Combine command line arguments into a single string of text
    input_text = ' '.join(sys.argv[1:])

    # Determine whether the input is Braille and convert accordingly
    if is_braille_input(input_text):
        print(convert_braille_to_text(input_text))
    else:
        print(convert_text_to_braille(input_text))