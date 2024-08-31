import sys

# Braille mappings for letters, digits, and special indicators
ENG_TO_BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......',

    # Indicators for capital, number follows
    'cap': '.....O', 'num': '.O.OOO', 
}

ENG_TO_BRAILLE_DIGITS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Reverse mappings for translation from Braille to English
BRAILLE_TO_ENG_ALPHABET = {braille: eng for eng, braille in ENG_TO_BRAILLE_ALPHABET.items()}
BRAILLE_TO_ENG_DIGITS = {braille: eng for eng, braille in ENG_TO_BRAILLE_DIGITS.items()}

def is_braille(input_str: str) -> bool:
    """Check if the input string is in Braille format (contains only 'O' and '.' characters)."""
    return all(char in 'O.' for char in input_str) and len(input_str) % 6 == 0

def translate_braille_to_eng(input_str: str) -> str:
    """Translate a Braille string to its English equivalent."""
    english = ""
    cap_follows = False
    num_follows = False

    for i in range(0, len(input_str), 6):
        braille_char = input_str[i:i+6]
        eng_char = BRAILLE_TO_ENG_ALPHABET.get(braille_char, '')

        if eng_char == 'cap':
            cap_follows = True
        elif eng_char == 'num':
            num_follows = True
        elif eng_char == ' ':
            english += ' '
            num_follows = False
        elif num_follows:
            english += BRAILLE_TO_ENG_DIGITS.get(braille_char, '')
        elif cap_follows:
            english += eng_char.upper()
            cap_follows = False
        else:
            english += eng_char

    return english

def translate_eng_to_braille(input_str: str) -> str:
    """Translate an English string to its Braille equivalent."""
    braille = ""
    num_follows = False

    for eng_char in input_str:
        if eng_char.isdigit():
            if not num_follows:
                braille += ENG_TO_BRAILLE_ALPHABET['num']
                num_follows = True
            braille += ENG_TO_BRAILLE_DIGITS[eng_char]
        elif eng_char.isupper():
            braille += ENG_TO_BRAILLE_ALPHABET['cap']
            braille += ENG_TO_BRAILLE_ALPHABET[eng_char.lower()]
            num_follows = False
        elif eng_char == ' ':
            braille += ENG_TO_BRAILLE_ALPHABET[' ']
            num_follows = False
        else:
            braille += ENG_TO_BRAILLE_ALPHABET[eng_char]
            num_follows = False

    return braille

if __name__ == "__main__":
    input_str = " ".join(sys.argv[1:])

    if is_braille(input_str):
        output_str = translate_braille_to_eng(input_str)
    else:
        output_str = translate_eng_to_braille(input_str)

    print(output_str, end='')
