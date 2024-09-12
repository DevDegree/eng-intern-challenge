import sys

# Updated Braille representations for English letters and numbers based on the image
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......'
}

# Reverse map to translate from Braille to English
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}

# Braille symbols for capitalization and numbers
braille_capital = '.....O'
braille_number = '.O.OOO'

def is_braille(input_str):
    """Checks if the input is Braille based on the character pattern."""
    return all(c in "O." for c in input_str)

def translate_to_braille(text):
    """Translates English text to Braille."""
    result = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(braille_number)
                number_mode = True
            result.append(braille_alphabet[char])
        elif char.isalpha():
            if char.isupper():
                result.append(braille_capital)
            result.append(braille_alphabet[char.lower()])
            number_mode = False
        elif char in braille_alphabet:
            result.append(braille_alphabet[char])
            number_mode = False
        elif char == ' ':
            result.append(braille_alphabet[' '])
            number_mode = False

    return ''.join(result)

def translate_to_english(braille_text):
    """Translates Braille text to English."""
    result = []
    i = 0
    number_mode = False
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        
        if braille_char == braille_capital:
            i += 6
            braille_char = braille_text[i:i+6]
            result.append(reverse_braille_alphabet[braille_char].upper())
        elif braille_char == braille_number:
            number_mode = True
        else:
            char = reverse_braille_alphabet.get(braille_char, '?')
            if number_mode and char.isdigit():
                result.append(char)
            else:
                result.append(char)
            number_mode = False
        i += 6

    return ''.join(result)

def braille_translator(input_string):
    """Determines if input is Braille or English and translates accordingly."""
    if is_braille(input_string):
        return translate_to_english(input_string)
    else:
        return translate_to_braille(input_string)

def main():
    input_text = ' '.join(sys.argv[1:])
    translation = braille_translator(input_text)
    print(translation)

if __name__ == "__main__":
    main()
