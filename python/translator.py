import sys
# Mapping Braille to English and English to Braille
english_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',  # Space
}

char_number_map = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"}
number_char_map = {v: k for k, v in char_number_map.items()}

capital_follows = '.....O'
number_follows = '.O.OOO'

# Reverse map for translation from Braille to English
braille_english_map = {v: k for k, v in english_braille_map.items()}

def translate(input_str):
    # Check if the input is in Braille or English
    if set(input_str).issubset({'O', '.'}):
        # Input is Braille
        return translate_braille_to_english(input_str)
    else:
        # Input is English
        return translate_english_to_braille(input_str)

def translate_braille_to_english(braille_str):
    output = []
    is_capital = False
    is_number = False

    # Split Braille input into 6-character chunks
    braille_chars = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]

    for braille_char in braille_chars:
        if braille_char == capital_follows:
            is_capital = True
        elif braille_char == number_follows:
            is_number = True
        elif braille_char == '......':
            output.append(' ')  # space
            is_number = False  # Reset number mode on space
        else:
            char = braille_english_map.get(braille_char, '')
            if is_number:
                output.append(char_number_map[char])
            else:
                if is_capital:
                    output.append(char.upper())
                    is_capital = False
                else:
                    output.append(char)

    return ''.join(output)

def translate_english_to_braille(english_str):
    output = []
    is_number = False

    for char in english_str:
        if char.isupper():
            output.append(capital_follows)
            output.append(english_braille_map[char.lower()])
        elif char.isdigit():
            if not is_number:
                output.append(number_follows)
                is_number = True
            output.append(english_braille_map[number_char_map[char]])  
        elif char == ' ':
            output.append(english_braille_map[' '])
            is_number = False  # Reset number mode on space
        else:
            output.append(english_braille_map[char])

    return ''.join(output)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])
    print(translate(input_str))

