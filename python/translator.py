import sys

# Manual Mapping.
alphabet_to_brallie = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital_follows': '.....O', 'decimal_follows': '.O...O', 'number_follows': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', 
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '<': '.OO..O',
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    ' ': '......'
}

# Reversing the dictionary
braille_to_alphabet = {value: key for key, value in alphabet_to_brallie.items()}

# Number
numbers = {str(i): alphabet_to_brallie[str(i)] for i in range(10)}

# Check if the input is English or Braille
def isEnglishOrBraille(input):
    return 'braille' if len(input) % 6 == 0 and all(c in {'.', 'O', ' '} for c in input) else 'english'

# English To Braille Translation
def english_to_braille(english_phrase):
    braille_phrase = []
    is_number = False
    for char in english_phrase:
        if is_number and char == '.':
            braille_phrase.append(alphabet_to_brallie['decimal_follows'])
        else:
            if char.isupper():
                braille_phrase.append(alphabet_to_brallie['capital_follows'])
            if char.isdigit() and not is_number:
                braille_phrase.append(alphabet_to_brallie['number_follows'])
                is_number = True
            if char == ' ':
                is_number = False
            braille_phrase.append(alphabet_to_brallie[char.lower()])
    return ''.join(braille_phrase)

# Braille to English Translation
def braille_to_english(braille):
    english_phrase = []
    is_number = is_capital = False
    for char in braille:
        if char == alphabet_to_brallie['number_follows']:
            is_number = True
        elif char == alphabet_to_brallie[' ']:
            is_number = False
            english_phrase.append(' ')
        elif char == alphabet_to_brallie['decimal_follows']:
            english_phrase.append('.')
        elif is_number:
            english_phrase.append(braille_to_alphabet[char])  
        elif char == alphabet_to_brallie['capital_follows']:
            is_capital = True
        else:
            letter = braille_to_alphabet[char]
            english_phrase.append(letter.upper() if is_capital else letter)
            is_capital = False
    return ''.join(english_phrase)

def main():
    input = ' '.join(sys.argv[1:])
    if isEnglishOrBraille(input) == 'english':
        print(english_to_braille(input), end='')
    else:
        print(braille_to_english([input[i:i+6] for i in range(0, len(input), 6)]), end='')

if __name__ == '__main__':
    main()
