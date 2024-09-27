import sys

# Braille dictionary for letters, numbers, and symbols
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    ',': '..O...', ';': '..OO..', ':': '...O..', '.': '..OOO.', '!': '..OOO.', '?': '..O.O.', '(': '.O.OO.', ')': '.O.OO.', '-': '....O.'
}

# Reverse dictionary to map Braille back to characters
english_dict = {v: k for k, v in braille_dict.items()}

# Capital and number follow symbols in Braille
capital_follow = '.....O'
number_follow = '.O.OOO'

def translate_to_braille(text):
    braille_output = []
    number_mode = False

    for char in text:
        if char.isdigit() and not number_mode:
            braille_output.append(number_follow)
            number_mode = True

        elif char.isalpha():
            if char.isupper():
                braille_output.append(capital_follow)
            char = char.lower()
            number_mode = False  # Exit number mode on encountering a letter

        braille_output.append(braille_dict.get(char, '......'))  # Default to space if character is not found

    return ''.join(braille_output)

def translate_to_english(braille):
    english_output = []
    i = 0
    number_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == capital_follow:
            next_symbol = braille[i+6:i+12]
            if next_symbol in english_dict:
                english_output.append(english_dict[next_symbol].upper())
            i += 12
        
        elif symbol == number_follow:
            number_mode = True
            i += 6
        
        else:
            if symbol in english_dict:
                if number_mode and english_dict[symbol].isdigit():
                    english_output.append(english_dict[symbol])
                else:
                    english_output.append(english_dict[symbol])
            i += 6
            
    return ''.join(english_output)

def main():
    input_text = ' '.join(sys.argv[1:])
    
    if all(char in 'O.' for char in input_text):
        # Input is Braille
        print(translate_to_english(input_text))
    else:
        # Input is English
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()

