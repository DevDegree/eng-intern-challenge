import sys

# Braille mapping
braille_dict = {
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..',
    'f': '000...', 'g': '0000..', 'h': '0.00..', 'i': '.00...', 'j': '.000..',
    'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.', 'o': '0..00.',
    'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.00.0.', 't': '.0000.',
    'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000',
    'z': '0..000', ' ': '......',
    'A': '.....0' + '0.....', 'B': '.....0' + '0.0...', 'C': '.....0' + '00....',
    'D': '.....0' + '00.0..', 'E': '.....0' + '0..0..', 'F': '.....0' + '000...',
    'G': '.....0' + '0000..', 'H': '.....0' + '0.00..', 'I': '.....0' + '.00...',
    'J': '.....0' + '.000..', 'K': '.....0' + '0...0.', 'L': '.....0' + '0.0.0.',
    'M': '.....0' + '00..0.', 'N': '.....0' + '00.00.', 'O': '.....0' + '0..00.',
    'P': '.....0' + '000.0.', 'Q': '.....0' + '00000.', 'R': '.....0' + '0.000.',
    'S': '.....0' + '.00.0.', 'T': '.....0' + '.0000.', 'U': '.....0' + '0...00',
    'V': '.....0' + '0.0.00', 'W': '.....0' + '.000.0', 'X': '.....0' + '00..00',
    'Y': '.....0' + '00.000', 'Z': '.....0' + '0..000',
    '1': '0.....', '2': '0.0...', '3': '00....', '4': '00.0..', '5': '0..0..',
    '6': '000...', '7': '0000..', '8': '0.00..', '9': '.00...', '0': '.000..',
}

# Reverse mapping for braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def is_braille(input_str):
    return all(c in ['0', '.'] for c in input_str.replace(' ', ''))

def translate_to_braille(english_text):
    braille_output = ''
    for char in english_text:
        if char in braille_dict:
            braille_output += braille_dict[char]
    return braille_output

def translate_to_english(braille_text):
    english_output = ''
    i = 0
    while i < len(braille_text):
        # Check for capitalization or number sequence
        if braille_text[i:i+6] == '.....0':
            i += 6
            english_output += reverse_braille_dict.get(braille_text[i:i+6], '')
        else:
            english_output += reverse_braille_dict.get(braille_text[i:i+6], '')
        i += 6
    return english_output

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 braille_translator.py '<text>'")
        sys.exit(1)

    input_text = sys.argv[1]

    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == '__main__':
    main()

