import sys

# Braille translation maps
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......'
}

# Reverse mapping for Braille to English
english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_alphabet['.....O'] = 'capital'  # Capitalization mark
english_alphabet['.O.OOO'] = 'number'   # Number mark

def translate_to_braille(text):
    result = []
    for char in text:
        if char.isupper():
            result.append('.....O')  # Capitalization marker in Braille
            result.append(braille_alphabet[char.lower()])
        elif char.isdigit():
            result.append('.O.OOO')  # Number marker in Braille
            result.append(braille_alphabet[char])
        else:
            result.append(braille_alphabet[char])
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    is_number = False
    while i < len(braille):
        symbol = braille[i:i+6]
        print(f"Processing symbol: {symbol}")  # Debugging print
        
        if len(symbol) != 6:
            print(f"Skipping invalid symbol length: {symbol}")
            i += 6
            continue
        
        if symbol == '.....O':  # Capitalization mark
            capitalize_next = True
        elif symbol == '.O.OOO':  # Number mark
            is_number = True
        else:
            if symbol not in english_alphabet:
                print(f"Skipping unknown pattern: {symbol}")
                result.append('?')
            else:
                char = english_alphabet[symbol]
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                if is_number:
                    char = str(ord(char) - ord('a') + 1)
                result.append(char)
                is_number = False  # Reset after each valid character
        
        i += 6
    return ''.join(result)


def main():
    input_text = sys.argv[1]
    if all(c in 'O.' for c in input_text):  # Detect Braille input
        print(translate_to_english(input_text))
    else:  # Assume English input
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
