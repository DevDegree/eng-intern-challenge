import sys


# Separate the Braille dictionaries for letters and numbers
# Braille to English dictionary for letters

braille_to_english_letters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z'
}

# Braille to English dictionary for numbers

braille_to_english_numbers = {
    '.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9'
}

# Special symbols
special_symbols = {
    '.....O': 'capital follows',
    '.O.OOO': 'number follows',
    '......': ' '
}

# Braille punctuation
braille_punctuation = {
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':',
    '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>',
    'O.O..O': '(', '.O.OO.': ')'
}

# Separate the dictionaries for letters and numbers for English to Braille

# English to Braille dictionary for letters
english_to_braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

# English to Braille dictionary for numbers
english_to_braille_numbers = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Special Braille symbols
special_symbols_reverse = {
    'capital follows': '.....O',
    'number follows': '.O.OOO',
    ' ': '......'
}

# Braille punctuation
english_to_braille_punctuation = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}


def translate_braille_to_english(braille_str):
    # Split Braille input into 6-character chunks
    braille_chars = [braille_str[i:i + 6] for i in range(0, len(braille_str), 6)]

    capital_mode = False
    number_mode = False
    english_output = []

    for char in braille_chars:
        if char in special_symbols:
            if special_symbols[char] == 'capital follows':
                capital_mode = True
            elif special_symbols[char] == 'number follows':
                number_mode = True
            elif special_symbols[char] == ' ':
                english_output.append(' ')
                number_mode = False
            continue

        if number_mode:
            if char in braille_to_english_numbers:
                english_output.append(braille_to_english_numbers[char])
        elif char in braille_to_english_letters:
            letter = braille_to_english_letters[char]
            if capital_mode:
                letter = letter.upper()
                capital_mode = False
            english_output.append(letter)
        elif char in braille_punctuation:
            english_output.append(braille_punctuation[char])

    return ''.join(english_output)


def translate_english_to_braille(english_str):
    braille_output = []
    number_mode = False

    for char in english_str:
        if char.isdigit():
            if not number_mode:
                braille_output.append(special_symbols_reverse['number follows'])
                number_mode = True
            braille_output.append(english_to_braille_numbers[char])
        elif char.isalpha():
            if number_mode:
                braille_output.append(' ')
                number_mode = False

            if char.isupper():
                braille_output.append(special_symbols_reverse['capital follows'])
                braille_output.append(english_to_braille_letters[char.lower()])
            else:
                braille_output.append(english_to_braille_letters[char])
        elif char in english_to_braille_punctuation:
            braille_output.append(english_to_braille_punctuation[char])
        elif char == ' ':
            braille_output.append(special_symbols_reverse[' '])

    return ''.join(braille_output)

def is_braille(input_str):
    # Check if the string contains only 'O', '.' and its length is a multiple of 6
    if all(c in ['O', '.'] for c in input_str) and len(input_str) % 6 == 0:
        return True
    return False

def detect_and_translate(input_str):
    if is_braille(input_str):
        return translate_braille_to_english(input_str)
    else:
        return translate_english_to_braille(input_str)

def main():
    # Get command-line arguments
    arguments = sys.argv[1:]
    # # Process each argument
    translated_results = []
    for arg in arguments:
        translated_results.append(detect_and_translate(arg))

    # Print the concatenated result
    result = '......'.join(translated_results)
    print(result)

if __name__ == "__main__":
    main()
