import sys

# Braille Mappings
braille_letters = {
    # Letters a-z
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    
    # Special symbols
    'capital': '.....O',  # Capitalization marker
}

braille_numbers = {
    # Numbers 0-9 (Braille numbers follow the letters a-j)
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    
    # Special symbols
    'number': '.O.OOO',   # Number follows marker
}

# Reverse mappings
reverse_letters = {v: k for k, v in braille_letters.items()}
reverse_numbers = {v: k for k, v in braille_numbers.items()}

# Detect whether input is Braille or English
def detect_input_type(input_str):
    return 'braille' if all(c in 'O.' for c in input_str) else 'english'

# Translate from English to Braille
def translate_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isupper():
            result.append(braille_letters['capital'])
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result.append(braille_numbers['number'])
                number_mode = True
            result.append(braille_numbers.get(char, ''))
        else:
            number_mode = False  # Deactivate number mode when a non-digit is encountered
            result.append(braille_letters.get(char, ''))
    return ''.join(result)

# Translate from Braille to English
def translate_to_english(braille):
    result = []
    i = 0
    capital_mode = False
    number_mode = False
    
    while i < len(braille):
        braille_char = braille[i:i+6]
        if braille_char == braille_letters['capital']:
            capital_mode = True
        elif braille_char == braille_numbers['number']:
            number_mode = True
        else:
            char = reverse_letters.get(braille_char, reverse_numbers.get(braille_char, ''))
            if capital_mode:
                char = char.upper()
                capital_mode = False
            if number_mode:
                if char.isdigit():
                    number_mode = False  # Deactivate number mode after translating the number
                else:
                    char = ''  # Clear char if not a digit
            if char:  # Only append if char is not empty
                result.append(char)
        i += 6
    
    return ''.join(result)

# Main function to run the translator
def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    input_str = " ".join(sys.argv[1:])
    if detect_input_type(input_str) == 'english':
        print(translate_to_braille(input_str), end='')
    else:
        print(translate_to_english(input_str), end='')

if __name__ == "__main__":
    main()
