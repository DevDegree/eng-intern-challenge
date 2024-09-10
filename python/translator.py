import sys

# Braille mapping for letters, capital, numbers, and space
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
}


braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Determine if the input string is Braille or English.
def is_braille(input_string):
    return all(c in ['O', '.'] for c in input_string)

# Translate Braille to English.
def translate_to_english(braille_string):
    result = []
    i = 0
    is_capital = False
    is_number = False
    
    while i < len(braille_string):
        symbol = braille_string[i:i+6]
        
        if symbol == '.....O':  # Capital follow symbol
            is_capital = True
        elif symbol == '.O.OOO':  # Number follow symbol
            is_number = True
        else:
            if is_number:
                for key, value in braille_numbers.items():
                    if symbol == value:
                        char = key
            else:
                for key, value in braille_alphabet.items():
                    if symbol == value:
                        char = key
                if is_capital:
                    char = char.upper()
                    is_capital = False
            result.append(char)
        i += 6  # Move to the next Braille symbol

    return ''.join(result)

# Translate English to Braille.
def translate_to_braille(english_string):
    result = []
    first_num = True
    
    for char in english_string:
        if char.isdigit():
            if first_num==True:
                num_char = '.O.OOO'
                result.append(num_char)
                first_num = False
            
            char = braille_numbers[char]
        else:
            if char.isupper():
                upper_char = '.....O'
                result.append(upper_char)
                char = char.lower()
            char = braille_alphabet[char]
        result.append(char)  
    
    return ''.join(result)

def main():

    input_string = ' '.join(sys.argv[1:])
    
    # Check if the input is Braille or English
    if is_braille(input_string):
        # Braille to English translation
        translated_text = translate_to_english(input_string)
    else:
        # English to Braille translation
        translated_text = translate_to_braille(input_string)

    print(translated_text)
    
    
if __name__ == '__main__':
    main()

