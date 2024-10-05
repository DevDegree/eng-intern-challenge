import sys

braille_alphabet = {
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
    'z': 'O..OOO'
}

braille_numbers = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOOOO'
}

braille_punctuation = {
    '.': '..OO.O'
}

braille_special = {
    'cap': '.....O',
    'decimal': '.O...O',
    'num': '.O.OOO',
    'space': '......'
}

braille_to_alphabet = {v: k for k, v in braille_alphabet.items()}
braille_to_numbers = {v: k for k, v in braille_numbers.items()}
braille_to_punctuation = {v: k for k, v in braille_punctuation.items()}

def english_to_braille(text):
    result = []
    num_mode = False
    for char in text:
        if char.isdigit():
            if not num_mode:
                result.append(braille_special['num'])
                num_mode = True
            result.append(braille_numbers[char])
        else:
            if char.isspace():
                result.append(braille_special['space'])
                num_mode = False
            elif char.isupper():
                result.append(braille_special['cap'])
                result.append(braille_alphabet[char.lower()])
            elif char in braille_punctuation:
                result.append(braille_punctuation[char])
            else:
                result.append(braille_alphabet[char])
                num_mode = False
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    num_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_special['space']:
            result.append(' ')
            num_mode = False
        elif symbol == braille_special['cap']:
            next_symbol = braille[i + 6:i + 12]
            result.append(braille_to_alphabet[next_symbol].upper())
            i += 6
        elif symbol == braille_special['num']:
            num_mode = True
        elif num_mode:
            result.append(braille_to_numbers[symbol])
        else:
            if symbol in braille_to_punctuation:
                result.append(braille_to_punctuation[symbol])
            elif symbol in braille_to_alphabet:
                result.append(braille_to_alphabet[symbol])
        i += 6

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("no")
        return
    input_text = ' '.join(sys.argv[1:])
    if all(c in 'O.' for c in input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()
