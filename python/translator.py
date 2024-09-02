import sys

# Braille alphabet and number mappings
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Special Braille symbols
braille_capital = '.....O'
braille_number = '.O.OOO'

# Reverse mappings for translation
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(input_str):
    # Check if the input consists only of 'O', '.', and spaces
    return all(c in 'O.o ' for c in input_str)

def translate_to_braille(text):
    braille = []
    number_mode = False
    for char in text:
        if char.isupper():
            braille.append(braille_capital)
            char = char.lower()
            number_mode = False
        if char.isdigit():
            if not number_mode:
                braille.append(braille_number)
                number_mode = True
            braille.append(braille_numbers[char])
        else:
            braille.append(braille_alphabet.get(char, '......'))
            number_mode = False
    return ''.join(braille)

def translate_to_english(braille):
    english = []
    i = 0
    number_mode = False
    while i < len(braille):
        symbol = braille[i:i + 6]
        if symbol == braille_capital:
            i += 6
            next_symbol = braille[i:i + 6]
            english.append(reverse_braille_alphabet.get(next_symbol, '').upper())
        elif symbol == braille_number:
            i += 6
            number_mode = True
            continue
        elif number_mode and symbol in reverse_braille_numbers:
            english.append(reverse_braille_numbers[symbol])
        else:
            english.append(reverse_braille_alphabet.get(symbol, ''))
            number_mode = False
        i += 6
    return ''.join(english)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        # Input is Braille, translate to English
        output = translate_to_english(input_str)
    else:
        # Input is English, translate to Braille
        output = translate_to_braille(input_str)

    print(output)
