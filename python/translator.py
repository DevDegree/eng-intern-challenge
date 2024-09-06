braille_map = {
    # Letters
    'a': "0.....", 'b': "0.0...", 'c': "00....", 'd': "00.0..", 'e': "0..0..",
    'f': "000...", 'g': "0000..", 'h': "0.00..", 'i': ".00...", 'j': ".000..",
    'k': "0...0.", 'l': "0.0.0.", 'm': "00..0.", 'n': "00.00.", 'o': "0..00.",
    'p': "000.0.", 'q': "00000.", 'r': "0.000.", 's': ".00.0.", 't': ".0000.",
    'u': "0...00", 'v': "0.0.00", 'w': ".000.0", 'x': "00..00", 'y': "00.000",
    'z': "0..000",

    # Numbers (Braille uses the letters a-j with the number sign for digits 0-9)
    '#': ".000..",  # Number sign
    '1': "0.....",  # Same as 'a'
    '2': "0.0...",  # Same as 'b'
    '3': "00....",  # Same as 'c'
    '4': "00.0..",  # Same as 'd'
    '5': "0..0..",  # Same as 'e'
    '6': "000...",  # Same as 'f'
    '7': "0000..",  # Same as 'g'
    '8': "0.00..",  # Same as 'h'
    '9': ".00...",  # Same as 'i'
    '0': ".000..",  # Same as 'j'
    "CAPITAL": ".....0",  # Capital follows symbol
    "DECIMAL": ".0...0", # Decimal follows symbol
    "NUMBER": ".0.000", # Number follows symbol

    # Common punctuation
    '.': "..00.0",  # Period
    ',': "..0...",  # Comma
    ';': "..0.0.",  # Semicolon
    ':': "..00..",  # Colon
    '?': "..0.00",  # Question mark
    '!': "..000.",  # Exclamation mark
    '/': ".0..0.",  # Black slash
    '<': ".00..0",  # Left caret
    '>': "0..00.",  # Right caret
    '-': "....00",  # Hyphen
    '(': ".00.00",  # Left parenthesis
    ' ': "......",  # Space
    ')': ".00.00",  # Right parenthesis (same as left)
    
}

# Reverse mapping for decoding Braille to English
reverse_braille_map = {v: k for k, v in braille_map.items()}

def trans_to_braille(text):
    result = []
    for char in text:
        if char.isdigit():
            result.append(braille_map['#'])
            for digit in char:
                result.append(braille_map[digit])
        elif char.isupper():
            result.append(braille_map["CAPITAL"])
            result.append(braille_map[char])
        elif char in braille_map:
            result.append(braille_map[char])
        else:
            break
    return result

    