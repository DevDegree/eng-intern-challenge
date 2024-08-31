import sys

# Create a dictionaries to store the braille alphabet, numbers, symbols, and indicators using O for raised dots and . 
braille_alphabet = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
}

braille_symbols = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
}

braille_numbers = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
}

braille_indicators = {
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
}


# Create a function to translate a string to braille
def to_braille(text):
    braille_text = ''
    number_mode = False
    for letter in text:
        if letter.isupper():
            braille_text += braille_indicators['capital']
            letter = letter.lower()
        if letter.isdigit():
            if not number_mode:
                braille_text += braille_indicators['number']
                number_mode = True
            braille_text += braille_numbers[letter]
        else:
            number_mode = False
            braille_text += braille_alphabet[letter]
    return braille_text

# Create a function to translate braille to a string
def to_text(braille_text):
    text = ''
    capital = False
    number = False
    for i in range(0, len(braille_text), 6):
        letter = braille_text[i:i+6]
        if letter == braille_indicators['capital']:
            capital = True
            continue
        if letter == braille_indicators['number']:
            number = True
            continue
        for key, value in braille_alphabet.items():
            if value == letter:
                if capital:
                    text += key.upper()
                    capital = False
                elif number:
                    # since it's a number we need to use braille_numbers dictionary
                    for key, value in braille_numbers.items():
                        if value == letter:
                            text += key
                            break
                else:
                    text += key
                break
    return text

# Main method to call the proper translation braille or english and ask for user input
def main():
    input_text = ' '.join(sys.argv[1:])

    if '.' in input_text or 'O' in input_text:
        print(to_text(input_text))
    else:
        print(to_braille(input_text))

if __name__ == "__main__":
    main()



