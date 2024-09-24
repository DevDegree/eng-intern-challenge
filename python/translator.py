braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......'
}

braille_numbers = {
    '1': braille_alphabet['a'], 
    '2': braille_alphabet['b'],  
    '3': braille_alphabet['c'],  
    '4': braille_alphabet['d'],  
    '5': braille_alphabet['e'],  
    '6': braille_alphabet['f'], 
    '7': braille_alphabet['g'], 
    '8': braille_alphabet['h'], 
    '9': braille_alphabet['i'], 
    '0': braille_alphabet['j'],
}

braille_numbers_reversed = {v: k for k, v in braille_numbers.items()}
braille_alphabet_reversed = {v: k for k, v in braille_alphabet.items()}

braille_capital = '.....O'
braille_number = '.O.OOO'

def is_braille(s):
    return all(c in 'O.' for c in s)

def english_to_braille(text):
    result = []
    i = 0
    while i < len(text):
        char = text[i]
        if char.isdigit():
            if not result or result[-1] != braille_number:
                result.append(braille_number)
            while i < len(text) and text[i].isdigit():
                result.append(braille_numbers[text[i]])
                i += 1
            continue
        else:
            if char.isupper():
                result.append(braille_capital)
                result.append(braille_alphabet[char.lower()])
            else:
                result.append(braille_alphabet.get(char, '......'))
        i += 1
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    capital = False
    number = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_capital:
            capital = True
            i += 6
            continue
        elif symbol == braille_number:
            number = True
            i += 6
            continue

        if number:
            if symbol in braille_numbers_reversed:
                result.append(braille_numbers_reversed[symbol])
                i += 6
                continue
            else:
                number = False
        if symbol == braille_alphabet.get(' ', '......'):
            result.append(' ')
        elif symbol in braille_alphabet_reversed:
            char = braille_alphabet_reversed[symbol]
            result.append(char.upper() if capital else char)
            capital = False
        else:
            pass
        i += 6
    return ''.join(result)

input_string = input("Enter English or Braille ")

if is_braille(input_string):
    print(braille_to_english(input_string))
else:
    print(english_to_braille(input_string))
