import sys

# Define mappings for English alphabets to Braille
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......'
}

# Define mappings for digits to Braille
number_to_braille = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Reverse dictionaries for decoding Braille
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_numbers = {v: k for k, v in number_to_braille.items()}

# Special symbols for Braille
special_symbols = {
    'capital': '.....O',
    'number': '.O.OOO'
}

def is_braille(input_str):
    """ Check if the input string is entirely composed of Braille characters. """
    return all(char in 'O.' for char in input_str) and len(input_str) % 6 == 0

def braille_to_text(braille_str):
    """ Convert Braille string to English text. """
    output = []
    is_capital = False
    is_number = False

    for i in range(0, len(braille_str), 6):
        symbol = braille_str[i:i+6]

        if symbol == special_symbols['capital']:
            is_capital = True
            continue
        elif symbol == special_symbols['number']:
            is_number = True
            continue

        if symbol == english_to_braille[' ']:
            output.append(' ')
            is_number = False  # Reset number mode on space
        elif is_number:
            output.append(braille_to_numbers.get(symbol, ''))
        else:
            char = braille_to_english.get(symbol, '')
            if is_capital:
                char = char.upper()
                is_capital = False
            output.append(char)

    return ''.join(output)

def text_to_braille(text_str):
    """ Convert English text to Braille. """
    output = []
    is_number = False

    for char in text_str:
        if char.isdigit():
            if not is_number:
                output.append(special_symbols['number'])
                is_number = True
            output.append(number_to_braille[char])
        elif char.isupper():
            output.append(special_symbols['capital'] + english_to_braille[char.lower()])
        elif char == ' ':
            output.append(english_to_braille[' '])
            is_number = False  # Reset number mode on space
        else:
            output.append(english_to_braille[char.lower()])

    return ''.join(output)

def main():
    """ Main function to handle the translation based on input. """
    if len(sys.argv) < 2:
        print("No input provided.")
        return

    input_str = ' '.join(sys.argv[1:])
    result = braille_to_text(input_str) if is_braille(input_str) else text_to_braille(input_str)
    print(result)

if __name__ == "__main__":
    main()
