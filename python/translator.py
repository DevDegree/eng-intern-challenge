import sys

# Braille dictionary for translation (source: the root repo read.me)

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', "'": '....O.'
}

# Special symbols used in Braille
capital_follows = '.....O'  # Indicates that the following letter is capitalized
decimal_follows = '.O...O'  # Indicates the start of a decimal point
number_follows = '.O.OOO'   # Indicates that the following characters are numbers

def english_to_braille(text):
    braille_output = []
    in_number_mode = False

    # Iterate through each character in the input text
    for char in text:
        if char.isdigit():
            # If it's a digit, add the number_follows indicator if not already in number mode
            if not in_number_mode:
                braille_output.append(number_follows)
                in_number_mode = True
            braille_output.append(braille_dict[char])
        elif char == '.':
            # Handle the decimal point by adding the decimal_follows indicator
            braille_output.append(decimal_follows)
            braille_output.append(braille_dict[char])
        elif char.isalpha():
            # Handle letters (both uppercase and lowercase)
            in_number_mode = False
            if char.isupper():
                braille_output.append(capital_follows)
            braille_output.append(braille_dict[char.lower()])
        elif char == ' ':
            # Handle spaces
            in_number_mode = False
            braille_output.append('......')
        else:
            # Handle any other punctuation or characters
            braille_output.append(braille_dict.get(char, '......'))
    
    # Return the concatenated Braille translation as a single string
    return ''.join(braille_output)

def braille_to_english(braille):
    english_output = []
    i = 0
    in_number_mode = False

    # Iterate through the Braille input in chunks of 6 characters
    while i < len(braille):
        symbol = braille[i:i+6]

        if symbol == number_follows:
            # Switch to number mode when encountering the number_follows indicator
            in_number_mode = True
            i += 6
            continue
        elif symbol == decimal_follows:
            # Handle decimal points
            english_output.append('.')
            i += 6
            continue
        elif symbol == capital_follows:
            # Handle capitalized letters
            i += 6
            next_symbol = braille[i:i+6]
            letter = list(braille_dict.keys())[list(braille_dict.values()).index(next_symbol)].upper()
            english_output.append(letter)
        elif symbol == '......':
            # Handle spaces
            english_output.append(' ')
            in_number_mode = False
        else:
            # Convert Braille symbols back to their corresponding English characters
            if in_number_mode:
                number_index = list(braille_dict.values()).index(symbol)
                if 0 <= number_index <= 9:
                    english_output.append(str(number_index + 1))
            else:
                english_output.append(list(braille_dict.keys())[list(braille_dict.values()).index(symbol)])
        i += 6

    # Return the concatenated English translation as a single string
    return ''.join(english_output)

def detect_input_type(text):
    # Check if the input text consists only of Braille characters (O and .)
    return all(c in 'O.' for c in text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text>")
        sys.exit(1)

    # Join command-line arguments to form the input text
    input_text = ' '.join(sys.argv[1:])
    
    # Determine whether the input is Braille or English, then translate
    if detect_input_type(input_text):
        translation = braille_to_english(input_text)
    else:
        translation = english_to_braille(input_text)
    
    # Output the translation
    print(translation)