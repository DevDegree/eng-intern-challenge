# Dictionary to map English letters to Braille
english_to_braille = {
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..',
    'f': '000...', 'g': '0000..', 'h': '0.00..', 'i': '.00...', 'j': '.000..',
    'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.', 'o': '0..00.',
    'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.00.0.', 't': '.0000.',
    'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000',
    'z': '0..000', ' ': '......', '1': '0.....', '2': '0.0...', '3': '00....',
    '4': '00.0..', '5': '0..0..', '6': '000...', '7': '0000..', '8': '0.00..',
    '9': '.00...', '0': '.000..'
}

# Reverse dictionary for Braille to English
braille_to_english = {v: k for k, v in english_to_braille.items()}

def translate_to_braille(text):
    braille_text = []
    for char in text.lower():
        if char in english_to_braille:
            braille_text.append(english_to_braille[char])
        else:
            raise ValueError(f"Character '{char}' cannot be translated to Braille.")
    return ' '.join(braille_text)

def translate_to_english(braille):
    braille_chars = braille.split(' ')
    english_text = []
    for braille_char in braille_chars:
        if braille_char in braille_to_english:
            english_text.append(braille_to_english[braille_char])
        else:
            raise ValueError(f"Braille sequence '{braille_char}' cannot be translated to English.")
    return ''.join(english_text)

import argparse

def main():
    parser = argparse.ArgumentParser(description="Braille to English and English to Braille Translator")
    parser.add_argument('input', type=str, help='The string to be translated (Braille or English)')
    args = parser.parse_args()
    
    input_text = args.input.strip()

    # Determine if the input is Braille or English
    if all(c in '0. ' for c in input_text):  # Braille contains only 0, ., and spaces
        try:
            translated_text = translate_to_english(input_text)
        except ValueError as e:
            print(e)
            return
    else:
        try:
            translated_text = translate_to_braille(input_text)
        except ValueError as e:
            print(e)
            return

    print(translated_text)

if __name__ == '__main__':
    main()
