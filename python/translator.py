import sys

BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_CAPITAL = '..O...'
BRAILLE_NUMBER_FOLLOWS = '.O.OO.'
BRAILLE_TO_ENGLISH = {v: k for k, v in {**BRAILLE_ALPHABET, **BRAILLE_NUMBERS}.items()}

def is_braille(text):
    return all(char in "O." for char in text)

def translate_to_braille(text):
    braille_text = ''
    num_mode = False
    for char in text:
        if char.isupper():
            braille_text += BRAILLE_CAPITAL
            char = char.lower()
        if char.isdigit():
            if not num_mode:
                braille_text += BRAILLE_NUMBER_FOLLOWS
                num_mode = True
            braille_text += BRAILLE_NUMBERS[char]
        elif char.isalpha():
            if num_mode:
                braille_text += ' '
                num_mode = False
            braille_text += BRAILLE_ALPHABET[char]
        elif char == ' ':
            braille_text += BRAILLE_ALPHABET[' ']
    return braille_text

def translate_to_english(braille):
    english_text = ''
    i = 0
    num_mode = False
    while i < len(braille):
        braille_char = braille[i:i+6]
        if braille_char == BRAILLE_CAPITAL:
            next_char = braille[i+6:i+12]
            english_text += BRAILLE_TO_ENGLISH.get(next_char, '').upper()
            i += 12
        elif braille_char == BRAILLE_NUMBER_FOLLOWS:
            num_mode = True
            i += 6
        else:
            char = BRAILLE_TO_ENGLISH.get(braille_char, '')
            if num_mode and char.isalpha():
                char = {v: k for k, v in BRAILLE_NUMBERS.items()}.get(char, '')
            english_text += char
            i += 6
    return english_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py '<text>'")
        sys.exit(1)

    input_text = sys.argv[1]

    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()

