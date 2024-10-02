import sys

# Dictionary mapping characters to their Braille representations (in binary)
BRAILLE_MAP = {
    'a': 0b100000, 'b': 0b101000, 'c': 0b110000, 'd': 0b110100, 'e': 0b100100,
    'f': 0b111000, 'g': 0b111100, 'h': 0b101100, 'i': 0b011000, 'j': 0b011100,
    'k': 0b100010, 'l': 0b101010, 'm': 0b110010, 'n': 0b110110, 'o': 0b100110,
    'p': 0b111010, 'q': 0b111110, 'r': 0b101110, 's': 0b011010, 't': 0b011110,
    'u': 0b100011, 'v': 0b101011, 'w': 0b011101, 'x': 0b110011, 'y': 0b110111,
    'z': 0b100111,
    '1': 0b100000, '2': 0b101000, '3': 0b110000, '4': 0b110100, '5': 0b100100,
    '6': 0b111000, '7': 0b111100, '8': 0b101100, '9': 0b011000, '0': 0b011100,
    '.': 0b001101, ',': 0b001000, '?': 0b001011, '!': 0b001110, '-': 0b000011,
    ':': 0b001100, ';': 0b001010, '(': 0b101001, ')': 0b010110, '/': 0b010010,
    '\'': 0b000010, '"': 0b001010, '*': 0b000110, '@': 0b000101, '&': 0b101101,
    ' ': 0b000000,
    'capital': 0b000001,
    'number': 0b010111,
    'decimal': 0b000101,
}

# Reverse mapping of BRAILLE_MAP for easy lookup
BRAILLE_REVERSE_MAP = {v: k for k, v in BRAILLE_MAP.items()}

def translate_to_braille(text):
    """
    Translate text to Braille binary representation.
    """
    translated = []
    number_mode = False

    for char in text:
        if char == ' ':
            translated.append(BRAILLE_MAP[' '])
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                translated.append(BRAILLE_MAP['number'])
                number_mode = True
            translated.append(BRAILLE_MAP[char])
        elif char == '.':
            if number_mode:
                translated.append(BRAILLE_MAP['decimal'])
            else:
                translated.append(BRAILLE_MAP.get(char, 0))
            number_mode = False
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                translated.append(BRAILLE_MAP['capital'])
                char = char.lower()
            translated.append(BRAILLE_MAP.get(char, 0))

    return translated

def translate_to_english(braille_binary):
    """
    Translate Braille binary representation to English text.
    """
    translated = []
    index = 0
    number_mode = False
    capital_mode = False

    while index < len(braille_binary):
        braille_char = braille_binary[index]

        if braille_char == BRAILLE_MAP[' ']:
            translated.append(' ')
            number_mode = False
            capital_mode = False
        elif braille_char == BRAILLE_MAP['number']:
            number_mode = True
        elif braille_char == BRAILLE_MAP['decimal']:
            translated.append('.')
        elif braille_char == BRAILLE_MAP['capital']:
            capital_mode = True
        else:
            if number_mode:
                char = BRAILLE_REVERSE_MAP.get(braille_char, '?')
                if char in 'abcdefghij':
                    digit = str((ord(char) - ord('a') + 1) % 10)
                    translated.append(digit)
                else:
                    translated.append('?')
            else:
                char = BRAILLE_REVERSE_MAP.get(braille_char, '?')
                if capital_mode:
                    char = char.upper()
                    capital_mode = False
                translated.append(char)
        index += 1

    return ''.join(translated)

def binary_to_braille_dots(binary):
    """
    Convert binary representation to Braille dot pattern.
    """
    return ''.join('O' if binary & (1 << (5-i)) else '.' for i in range(6))

def braille_dots_to_binary(dots):
    """
    Convert Braille dot pattern to binary representation.
    """
    return sum(1 << (5-i) for i, char in enumerate(dots) if char == 'O')

def main():
    """
    Main function to handle command-line input and output.
    """
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_or_braille>")
        sys.exit(1)

    text_input = ' '.join(sys.argv[1:])

    # Check if input is Braille dots or text
    if all(c in 'O.' for c in text_input):
        # Convert Braille dots to binary and translate to English
        braille_binary = [braille_dots_to_binary(text_input[i:i+6]) for i in range(0, len(text_input), 6)]
        print(translate_to_english(braille_binary))
    else:
        # Translate text to Braille and convert to dot pattern
        braille_binary = translate_to_braille(text_input)
        print(''.join(binary_to_braille_dots(char) for char in braille_binary))

if __name__ == "__main__":
    main()