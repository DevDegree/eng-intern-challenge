import sys

# Define Braille dictionary (O = raised, . = not raised)
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', ' ': '......'
}

# Reverse dictionary for Braille to English conversion
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Special Braille characters
capital_indicator = '.....O'
number_indicator = '.O.OOO'

# Helper function to detect if the string is Braille or English
def is_braille(input_str):
    return all(c in 'O.' for c in input_str)

# Function to convert Braille to English
def braille_to_english(braille):
    result = []
    i = 0
    capital = False
    number = False
    
    # Loop over every 6-character segment
    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == capital_indicator:
            capital = True
        elif symbol == number_indicator:
            number = True
        else:
            if number:
                char = reverse_braille_dict.get(symbol, '')
                result.append(char)
                number = False 
            else:
                char = reverse_braille_dict.get(symbol, '')
                if capital:
                    result.append(char.upper())
                    capital = False  
                else:
                    result.append(char)
        i += 6
    return ''.join(result)

# Function to convert English to Braille
def english_to_braille(english):
    result = []
    number = False
    
    for char in english:
        if char.isupper():
            result.append(capital_indicator)
            result.append(braille_dict[char.lower()])
        elif char.isdigit():
            if not number:
                result.append(number_indicator)
                number = True
            result.append(braille_dict[char])
        else:
            if number:
                number = False
            result.append(braille_dict[char])
    
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        translated = braille_to_english(input_str)
    else:
        translated = english_to_braille(input_str)

    print(translated.strip())

if __name__ == "__main__":
    main()