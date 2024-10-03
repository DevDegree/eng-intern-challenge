import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......'
}

braille_digits = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_capital = '.....O'
braille_number = '.O.OOO'

reverse_braille = {v: k for k, v in braille_alphabet.items()}
reverse_braille.update(braille_digits)

def is_braille(input_string):
    return all(char in 'O.' for char in input_string)

def english_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(braille_capital)
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                result.append(braille_number)
                number_mode = True
            result.append(braille_digits[char])
        elif char in braille_alphabet:
            result.append(braille_alphabet[char])
            number_mode = False
        else:
            result.append('......')

    return ''.join(result)

def braille_to_english(braille_text):
    result = []
    i = 0
    capital_next = False
    number_mode = False

    while i < len(braille_text):
        symbol = braille_text[i:i+6]
        
        if symbol == braille_capital:
            capital_next = True
            i += 6
            continue
        elif symbol == braille_number:
            number_mode = True
            i += 6
            continue

        if symbol in reverse_braille:
            char = reverse_braille[symbol]
            if number_mode and char in braille_digits.values():
                char = next(k for k, v in braille_digits.items() if v == symbol)
            if capital_next:
                char = char.upper()
                capital_next = False
            result.append(char)
        else:
            result.append(' ') 
        i += 6

    return ''.join(result)

def main():
    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        output = braille_to_english(input_string)
    else:
        output = english_to_braille(input_string)

    print(output)

if __name__ == "__main__":
    main()