import sys

ENGLISH_CHARS_TO_BRAILLE = {
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
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ":": '..OO..',
    ";": '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    "<": '.OO..O',
    ">": 'O..OO.',
    "(": 'O.O..O',
    ")": '.O.OO.',
    " ": '......',

    # Modifier Characters
    'capital': '.....O',
    'number': '.O.OOO',
}

test = {
    '.': '..OO..', 
    ',': '..O...', 
    ';': '..OO..', 
    ':': '...O..', 
    '!': '..OO.O', 
    '?': '..O.O.',
    "'": '....O.',
    '-': '....OO'
}

BRAILLE_TO_ENGLISH_CHARS = {v: k for k, v in ENGLISH_CHARS_TO_BRAILLE.items()}

ENGLISH_NUMS_TO_BRAILLE = {
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

BRAILLE_TO_ENGLISH_NUMS = {v: k for k, v in ENGLISH_NUMS_TO_BRAILLE.items()}

def braille_to_english(input_string: str) -> str:
    result = ''

    # Keep consuming characters from the input string until it is empty
    while input_string:
        char = input_string[:6]

        # Check for capital letters
        if char == ENGLISH_CHARS_TO_BRAILLE['capital']:
            input_string = input_string[6:]
            char = input_string[:6]
            result += BRAILLE_TO_ENGLISH_CHARS[char].upper()
        elif char == ENGLISH_CHARS_TO_BRAILLE['number']:
            # Numbers are always ended with a space
            # Hence, consume all the digits until a space is encountered or the end
            input_string = input_string[6:]
            char = input_string[:6]
            while input_string and char != ENGLISH_CHARS_TO_BRAILLE[' ']:
                result += BRAILLE_TO_ENGLISH_NUMS[char]
                input_string = input_string[6:]
                char = input_string[:6]
            # Insert a space after the number
            result += ' '
        else:
            result += BRAILLE_TO_ENGLISH_CHARS[char]

        # Consume character
        input_string = input_string[6:]

    return result

def english_to_braille(input_string: str) -> str:
    result = ''

    # Keep consuming characters from the input string until it is empty
    while input_string:
        char = input_string[0]

        # Check for capital letters
        if char.isupper():
            result += ENGLISH_CHARS_TO_BRAILLE['capital']
            result += ENGLISH_CHARS_TO_BRAILLE[char.lower()]
        elif char.isdigit():
            # Numbers are always ended with a space
            # Hence, consume all the digits until a space is encountered
            result += ENGLISH_CHARS_TO_BRAILLE['number']
            while char.isdigit():
                result += ENGLISH_NUMS_TO_BRAILLE[char]
                input_string = input_string[1:]
                if input_string:
                    char = input_string[0]
                else:
                    break
            # Insert a space after the number
            result += ENGLISH_CHARS_TO_BRAILLE[' ']
        else:
            result += ENGLISH_CHARS_TO_BRAILLE[char]

        # Consume character
        input_string = input_string[1:]

    return result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input>")
        sys.exit(1)

    input_string = " ".join(sys.argv[1:])
    
    # Input string is considered english if it contains characters other than O and .
    for char in input_string:
        if char not in ['O', '.']:
            result = english_to_braille(input_string)
            print(result)
            sys.exit(0)

    result = braille_to_english(input_string)
    print(result)
    sys.exit(0)