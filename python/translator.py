import sys

# Define the Braille dictionary for letters and digits
braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'number': '.O.OOO',
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Reverse dictionaries for Braille to English
english_letters = {v: k for k, v in braille_letters.items() if k not in ['capital', 'number']}
english_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(text):
    return all(char in "O." for char in text) and len(text) % 6 == 0

def translate_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(braille_letters['capital'])
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                result.append(braille_letters['number'])
                number_mode = True
        else:
            number_mode = False

        if char in braille_letters:
            result.append(braille_letters[char])
        elif char in braille_numbers:
            result.append(braille_numbers[char])

    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    is_number = False
    while i < len(braille):
        chunk = braille[i:i+6]
        if chunk == braille_letters['capital']:
            i += 6
            chunk = braille[i:i+6]
            result.append(english_letters[chunk].upper())
        elif chunk == braille_letters['number']:
            is_number = True
        elif chunk == braille_letters[' ']:
            result.append(' ')
            is_number = False 
        else:
            if is_number:
                result.append(english_numbers[chunk])
            else:
                result.append(english_letters[chunk])
        i += 6
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text|braille>")
        sys.exit(1)
    
    input_text = " ".join(sys.argv[1:])
    
    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()