import sys

BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......'
}

# Special Braille symbols
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'

# English to Braille:
def english_to_braille(text):
    output = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                output.append(NUMBER_FOLLOWS)
                number_mode = True
            output.append(BRAILLE_DICT[char])
        elif char == ' ':
            output.append(BRAILLE_DICT[char])
            number_mode = False
        elif char.isupper():
            output.append(CAPITAL_FOLLOWS)
            output.append(BRAILLE_DICT[char.lower()])
            number_mode = False
        else:
            output.append(BRAILLE_DICT[char])
            number_mode = False
    return ''.join(output)

def braille_to_english(braille):
    inverse_braille_dict = {v: k for k, v in BRAILLE_DICT.items() if k.isalpha() or k == ' '}
    output = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        symbol = braille[i:i+6] # Get 1 Braille character

        if symbol == CAPITAL_FOLLOWS:
            capitalize_next = True
            i += 6
            continue
        elif symbol == NUMBER_FOLLOWS:
            number_mode = True
            i += 6
            continue
        # Translate Braille to English character
        if symbol in inverse_braille_dict:
            char = inverse_braille_dict[symbol]
            if number_mode and char in 'abcdefghij':  # Convert Braille letters back to numbers
                char = str(ord(char) - ord('a') + 1)
                # If it is 'j', it is 0 and not 10
                if char == '10':
                    char = '0'

            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            output.append(char)

        if char == ' ':
            number_mode = False
        i += 6

    return ''.join(output)

def main():
    args = sys.argv[1:]
    input = ' '.join(args)

    if all(c in 'O. ' for c in input):
        print(braille_to_english(input))
    else:
        print(english_to_braille(input))

if __name__ == "__main__":
    main()