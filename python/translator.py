import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Special Braille indicators for capitalization and numbers
braille_capital = '.....O'
braille_number = '.O.OOO'

# Reverse mapping for decoding Braille
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(text):
    return all(c in "O." for c in text)

def english_to_braille(text):
    braille = []
    number_mode = False
    
    for char in text:
        if char.isupper():
            braille.append(braille_capital)
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                braille.append(braille_number)
                number_mode = True
            braille.append(braille_numbers[char])
        else:
            if number_mode and char != ' ':
                # Reset number mode if we encounter a letter or space after numbers
                number_mode = False
            braille.append(braille_alphabet[char])
    
    return ''.join(braille)

def braille_to_english(text):
    english = []
    number_mode = False
    capital_mode = False
    
    for i in range(0, len(text), 6):
        braille_char = text[i:i+6]
        
        if braille_char == braille_capital:
            capital_mode = True
            continue
        elif braille_char == braille_number:
            number_mode = True
            continue
        elif braille_char == '......':  # Space
            english.append(' ')
            number_mode = False
            continue
        
        if number_mode:
            english.append(reverse_braille_numbers.get(braille_char, '?'))
        else:
            letter = reverse_braille_alphabet.get(braille_char, '?')
            if capital_mode:
                english.append(letter.upper())
                capital_mode = False
            else:
                english.append(letter)
    
    return ''.join(english)

if __name__ == "__main__":
    # Get the input string from command line
    input_text = sys.argv[1]

    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))
