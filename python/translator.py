import sys

# Braille to English and English to Braille translator
english_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
    '9': '.OO...', '0': '.OOO..', ' ': '......'
}

# Braille special symbols
CAPITAL = '.....O' 
NUMBER = '.O.OOO'  

# Create reverse maps
braille_to_letter_map = {v: k for k, v in english_to_braille_map.items() if k.isalpha()}
braille_to_number_map = {v: k for k, v in english_to_braille_map.items() if k.isdigit()}


# Check if input is braille
def is_braille(input_str):
    return all(c in "O. " for c in input_str)


# Translate English to Braille 
def english_to_braille(text):
    braille = []
    is_number_mode = False  

    for char in text:
        if char.isupper():
            braille.append(CAPITAL)
            braille.append(english_to_braille_map[char.lower()])
        elif char.isdigit():
            if not is_number_mode:
                braille.append(NUMBER)
                is_number_mode = True
            braille.append(english_to_braille_map[char])
        else:
            if is_number_mode and char == ' ':
                is_number_mode = False
            braille.append(english_to_braille_map.get(char, '......'))  # Default to space for unknown chars

    return ''.join(braille)


# Translate Braille to English
def braille_to_english(braille_str):
    english = []
    i = 0
    is_number_mode = False 

    while i < len(braille_str):
        symbol = braille_str[i:i+6]

        if symbol == CAPITAL:
            i += 6
            next_char = braille_to_letter_map[braille_str[i:i+6]]
            english.append(next_char.upper())
        elif symbol == NUMBER:
            is_number_mode = True
        else:
            if is_number_mode and symbol in braille_to_number_map:
                english.append(braille_to_number_map[symbol])
                if symbol == '......': 
                    is_number_mode = False
            else:
                english.append(braille_to_letter_map.get(symbol, ' '))
                if symbol == '......': 
                    is_number_mode = False
        i += 6
    return ''.join(english)


# Main function
def main(input_str):
    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
        main(input_str)
    else:
        print("Please provide a string to translate.")
