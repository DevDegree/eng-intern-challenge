import sys

# Braille alphabet
braille_alphabet = {
    'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
    'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
    'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
    'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
    'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
    'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
    'y': 'OO.OOO',    'z': 'O..OOO',    ' ': '......'
}

# Numbers in Braille
braille_numbers = {
    '0': '.OOO..',    '1': 'O.....',    '2': 'O.O...',    '3': 'OO....',
    '4': 'OO.O..',    '5': 'O..O..',    '6': 'OOO...',    '7': 'OOOO..',
    '8': 'O.OO..',    '9': '.OO...'
}

# Braille symbols
capital_symbol = '.....O'
number_symbol = '.O.OOO'
decimal = '.O...O'

def english_to_braille(text):
    result = []
    is_number_mode = False

    for char in text:
        if char.isupper():
            result.append(capital_symbol)
            char = char.lower()

        if char.isdigit():
            if not is_number_mode:
                result.append(number_symbol)
                is_number_mode = True
            result.append(braille_numbers[char])
        else:
            is_number_mode = False
            result.append(braille_alphabet[char])

    return ''.join(result)

def braille_to_english(braille):
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    result = []
    is_capital = False
    is_number_mode = False
    
    reverse_alphabet = {v: k for k, v in braille_alphabet.items()}
    reverse_numbers = {v: k for k, v in braille_numbers.items()}

    for char in braille_chars:
        if char == capital_symbol:
            is_capital = True
        elif char == number_symbol:
            is_number_mode = True
        else:
            if is_number_mode:
                if char in reverse_numbers:
                    result.append(reverse_numbers[char])
                else:
                    is_number_mode = False
            
            if not is_number_mode:
                if char in reverse_alphabet:
                    letter = reverse_alphabet[char]
                    if is_capital:
                        letter = letter.upper()
                        is_capital = False
                    result.append(letter)
                else:
                    result.append('?')

            if char == braille_alphabet[' ']:
                is_number_mode = False

    return ''.join(result)

def is_braille(text):
    return all(c in 'O.' for c in text)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid String")
        sys.exit(1)

    text = ' '.join(sys.argv[1:])
    if is_braille(text):
        print(braille_to_english(text), end='')
    else:
        print(english_to_braille(text), end='')
    