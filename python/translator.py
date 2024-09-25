import sys

# Braille alphabet mapping with capitalization and spaces
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

# Special symbol for capitalization
capital_follows = '.....O'

# Reverse mapping for Braille to English translation
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}

def is_braille(text):
    """Check if the input is Braille (O and . characters)."""
    return all(c in 'O.' for c in text)

def english_to_braille(text):
    """Convert English to Braille with capitalization."""
    braille_text = []
    for char in text:
        if char.isupper():
            braille_text.append(capital_follows)  # Add capitalization symbol
            braille_text.append(braille_alphabet[char.lower()])
        else:
            braille_text.append(braille_alphabet[char])
    return ''.join(braille_text)

def braille_to_english(text):
    """Convert Braille to English with capitalization."""
    english_text = []
    i = 0
    capitalize_next = False
    
    while i < len(text):
        symbol = text[i:i+6]
        if symbol == capital_follows:
            capitalize_next = True
            i += 6
            continue
        
        char = reverse_braille_alphabet[symbol]
        if capitalize_next:
            char = char.upper()
            capitalize_next = False
        english_text.append(char)
        i += 6

    return ''.join(english_text)

def main():
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == '__main__':
    main()
