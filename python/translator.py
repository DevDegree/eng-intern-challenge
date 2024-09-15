import sys

# Braille alphabet
letters = {
    'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
    'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
    'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
    'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
    'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
    'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
    'y': 'OO.OOO',    'z': 'O..OOO',    ' ': '......'
}

# Numbers in Braille
numbers = {
    '0': '.OOO..',    '1': 'O.....',    '2': 'O.O...',    '3': 'OO....',
    '4': 'OO.O..',    '5': 'O..O..',    '6': 'OOO...',    '7': 'OOOO..',
    '8': 'O.OO..',    '9': '.OO...'
}

capital_symbol = '.....O'
number_symbol = '..OO.O'

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
            result.append(numbers[char])
        else:
            is_number_mode = False
            result.append(letters[char])

    return ' '.join(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid String")
        sys.exit(1)

    text = ' '.join(sys.argv[1:])
    print(english_to_braille(text))
