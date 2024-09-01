import sys
alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'capital_follows': '.....O', 'decimal_follows': '.O...O', 'number_follows': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO',
    '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

braille_to_char = {v: k for k, v in alphabet.items()}
numbers = {str(i): alphabet[str(i)] for i in range(10)}

def english_or_braille(input):
    return 'braille' if len(input) % 6 == 0 and set(input) <= {'.', 'O'} else 'english'

def to_braille(english_phrase):
    braille_phrase = []
    is_number = False
    for char in english_phrase:
        if is_number and char == '.':
            braille_phrase.append(alphabet['decimal_follows'])
        else:
            if char.isupper():
                braille_phrase.append(alphabet['capital_follows'])
            if char.isdigit() and not is_number:
                braille_phrase.append(alphabet['number_follows'])
                is_number = True
            if char == ' ':
                is_number = False
            braille_phrase.append(alphabet[char.lower()])
    return ''.join(braille_phrase)

def to_english(braille):
    english_phrase = []
    is_number = is_capital = False
    for char in braille:
        if char == alphabet['number_follows']:
            is_number = True
        elif char == alphabet[' ']:
            is_number = False
            english_phrase.append(' ')
        elif char == alphabet['decimal_follows']:
            english_phrase.append('.')
        elif is_number:
            english_phrase.append(braille_to_char[char])  
        elif char == alphabet['capital_follows']:
            is_capital = True
        else:
            letter = braille_to_char[char]
            english_phrase.append(letter.upper() if is_capital else letter)
            is_capital = False
    return ''.join(english_phrase)

def main():
    input_phrase = ' '.join(sys.argv[1:])
    if english_or_braille(input_phrase) == 'english':
        print(to_braille(input_phrase), end='')
    else:
        print(to_english([input_phrase[i:i+6] for i in range(0, len(input_phrase), 6)]), end='')

if __name__ == '__main__':
    main()
