import sys

# Braille alphabet mappings
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 'cap': '.....O',
    'num': '.O.OOO',
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', 
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings for Braille to English
english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_numbers = {v: str(k) for k, v in braille_numbers.items()}

def english_to_braille(text):
    braille = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille.append(braille_alphabet['num'])
                number_mode = True
            braille.append(braille_numbers[char])
        else:
            #switch to non digit mode once there's space or anything non digit
            if number_mode:
                number_mode = False
            if char.isupper():
                braille.append(braille_alphabet['cap'])
                char = char.lower()
            braille.append(braille_alphabet[char])
    return ''.join(braille)

def braille_to_english(braille):
    english = []
    number_mode = False
    i = 0
    while i < len(braille):
        current_symbol = braille[i:i + 6]
        if current_symbol == braille_alphabet['num']:
            number_mode = True
            i += 6
            continue
        elif current_symbol == braille_alphabet['cap']:
            # directly add the next letter and go forward 12 char
            next_symbol = (braille[i+6:i + 12])
            english.append(english_alphabet[next_symbol].upper())
            i += 12
            continue
        
        if number_mode:
            if current_symbol == '......':  # reset number mode after space
                number_mode = False
                continue
            english.append(english_numbers[current_symbol])
        else:
            english.append(english_alphabet[current_symbol])
        i += 6
    return ''.join(english)

def detect_braille_or_english(input_str):
    if all(c in ['O', '.'] for c in input_str):
        return 'braille'
    return 'english'

def translate(input_str):
    if detect_braille_or_english(input_str) == 'english':
        return english_to_braille(input_str)
    else:
        return braille_to_english(input_str)

if __name__ == "__main__":
    input_str = ' '.join(sys.argv[1:])
    print(translate(input_str))


