import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '.': '..OO.O', ',': '..O...', 
    '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', 
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

number_mapping = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

braille_to_char = {}
for char, pattern in braille_alphabet.items():
    if pattern not in braille_to_char:
        braille_to_char[pattern] = char
    elif char in 'abcdefghij':
        # Prioritize letters over symbols for ambiguous patterns
        braille_to_char[pattern] = char

capital_symbol = '.....O'
number_symbol = '.O.OOO'

def is_braille(text):
    return all(char in 'O.' for char in text)

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
            char = list(number_mapping.keys())[list(number_mapping.values()).index(char)]
        elif is_number_mode:
            is_number_mode = False
        result.append(braille_alphabet.get(char, ''))
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    is_capital = False
    is_number_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == capital_symbol:
            is_capital = True
        elif symbol == number_symbol:
            is_number_mode = True
        else:
            char = braille_to_char.get(symbol, '')
            if is_number_mode and char in 'abcdefghij':
                char = number_mapping[char]
            elif is_capital:
                char = char.upper()
                is_capital = False
            result.append(char)
            if char == ' ':
                is_number_mode = False
        i += 6
    return ''.join(result)

def translate(text):
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    print(translate(input_text))
