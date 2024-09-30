braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    'capital': '.....O', 
    'number': '.O.OOO', 
}

braille_to_english = {value: key for key, value in braille_alphabet.items()}

def is_braille(input_str):
    return all(char in 'O.' for char in input_str)

def encode_to_braille(input_str):
    output = ''
    number_mode = False

    for char in input_str:
        if char.isupper():
            output += braille_alphabet['capital'] 
            char = char.lower()
        elif char.isdigit():
            if not number_mode:
                output += braille_alphabet['number']  
                number_mode = True
        else:
            number_mode = False  

        output += braille_alphabet.get(char, '')

    return output

def decode_from_braille(input_str):
    output = ''
    number_mode = False

    for i in range(0, len(input_str), 6):
        braille_char = input_str[i:i + 6]
        if braille_char == braille_alphabet['capital']:
            continue  
        elif braille_char == braille_alphabet['number']:
            number_mode = True  
            continue
        elif braille_char == braille_alphabet[' ']:
            output += ' '
            number_mode = False
            continue

        decoded_char = braille_to_english.get(braille_char, '')
        if decoded_char:
            if number_mode and decoded_char.isdigit():
                output += decoded_char
            else:
                output += decoded_char.upper() if number_mode else decoded_char
                number_mode = False

    return output

def translate(input_str):
    if is_braille(input_str):
        return decode_from_braille(input_str)
    else:
        return encode_to_braille(input_str)

if __name__ == "__main__":
    import sys

    user_input = ' '.join(sys.argv[1:])
    translation = translate(user_input)
    print(translation)
