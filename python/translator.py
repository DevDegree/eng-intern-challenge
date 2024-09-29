import sys

# Defines The Braille Map For Lowercase Letters And Symbols
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.'
}

# Defines The Braille Map For Numbers
braille_number_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Initializes The Indicators
capital_indicator = '.....O'
number_indicator = '.O.OOO'

# Extends The Braille Map For Uppercase Letters
for letter in 'abcdefghijklmnopqrstuvwxyz':
    braille_map[letter.upper()] = capital_indicator + braille_map[letter]

# Creates A Reverse Map (Braille-to-English)
english_map = {}
english_number_map = {}

for key, value in braille_map.items():
    english_map[value] = key

for key, value in braille_number_map.items():
    english_number_map[value] = key

# Checks If The Input String Is Braille
def is_braille(input_str):
    for c in input_str:
        if c not in 'O.':
            return False
    return True

# Converts English to Braille
def english_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(number_indicator)  # Adds The Number Indicator
                number_mode = True  # Sets The Program To Number Mode
            result.append(braille_number_map[char])  # Adds Braille For The Digit
        elif char == ' ':  # Handles Spaces
            result.append('......')  # Adds Braille For The Space
            number_mode = False  # Resets Number Mode
        else:
            if number_mode:
                number_mode = False  # Reset Number Mode
            result.append(braille_map.get(char))

    return ''.join(result)

# Converts Braille to English
def braille_to_english(braille):
    result = []
    i = 0
    number_mode = False

    while i < len(braille):
        chunk = braille[i:i + 6]

        # Checks For The Capital Letter Indicator
        if chunk == capital_indicator:
            next_chunk = braille[i + 6:i + 12]

            if next_chunk in english_map:
                result.append(english_map[next_chunk].upper())
            i += 12

        # Checks For The Number Indicator And Switches The Mode
        elif chunk == number_indicator:
            number_mode = True
            i += 6

        else:
            if number_mode:
                result.append(english_number_map[chunk])
            elif chunk in english_map:
                result.append(english_map[chunk])
            else:
                result.append(' ')
            i += 6
    return ''.join(result)

# Main function
def main():
    input_str = sys.argv[1]

    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == "__main__":
    main()
