# Braille dictionary for letters, numbers, and punctuation
braille_dict = {
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..', 
    'f': '000...', 'g': '0000..', 'h': '0.00..', 'i': '.00...', 'j': '.000..',
    'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.', 'o': '0..00.', 
    'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.00.0.', 't': '.0000.', 
    'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000', 
    'z': '0..000',
    '1': '0.....', '2': '0.0...', '3': '00....', '4': '00.0..', '5': '0..0..', 
    '6': '000...', '7': '0000..', '8': '0.00..', '9': '.00...', '0': '.000..',
    ' ': '......', '.': '..00.0', ',': '..0...', '?': '..0.00', '!': '..000.',
    "'": '....0.', '-': '....00', ':': '..00..', ';': '..0.0.', '#': '.000..'
}

# Reverse dictionary for Braille-to-English translation
inverse_braille_dict = {v: k for k, v in braille_dict.items()}

def translate_to_braille(text):
    result = []
    for char in text:
        if char.isupper():
            result.append('.....0')
            result.append(braille_dict[char.lower()])
        else:
            result.append(braille_dict[char])
    return ' '.join(result)

def translate_to_english(braille):
    result = []
    capitalize_next = False
    number_mode = False

    for symbol in braille.split(' '):
        if symbol == '.000..':
            number_mode = True
        elif symbol == '.....0':
            capitalize_next = True
        else:
            if number_mode:
                char = inverse_braille_dict.get(symbol, '')
                if char.isdigit():
                    result.append(char)
                number_mode = False
            else:
                char = inverse_braille_dict.get(symbol, '')
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                result.append(char)

    return ''.join(result)

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text or braille>")
        return

    input_text = sys.argv[1]
    if '0' in input_text or '.' in input_text:
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == '__main__':
    main()
