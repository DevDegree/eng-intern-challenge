
import sys

# Map for converting braille to characters
alphabet_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'capitalize': '.....O', 'number': '.O.OOO'
}

number_to_braille = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

CAPITALIZE = '.....O'
NUMBER = '.O.OOO'
SPACE = '......'


braille_to_alphabet = {v: k for k, v in alphabet_to_braille.items()}
braille_to_number = {v: k for k, v in number_to_braille.items()}

def is_braille(message):
    return all(char in 'O.' for char in message)

def english_to_braille(message):
    result = []
    number_mode = False

    for char in message:
        if char.isalpha():
            if char.isupper():
                result.append(CAPITALIZE)
                char = char.lower()
            result.append(alphabet_to_braille[char])
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                result.append(NUMBER)
                number_mode = True
            result.append(number_to_braille[char])
        elif char.isspace():
            result.append(alphabet_to_braille[char])
            number_mode = False

    return ''.join(result)

def braille_to_english(message):
    result = []
    number_mode = False
    i = 0

    while i < len(message):
        symbol = message[i:i+6]

        if symbol == SPACE:
            number_mode = False
        
        if symbol == CAPITALIZE:
            i += 6

            symbol = message[i:i+6]

            result.append(braille_to_alphabet[symbol].upper())
        
        elif symbol == NUMBER:
            number_mode = True
            i += 6
            continue

        elif symbol in braille_to_alphabet and number_mode is False:
            result.append(braille_to_alphabet[symbol])
            number_mode = False
        
        elif symbol in braille_to_number:
            result.append(braille_to_number[symbol])
        
        else:
            result.append(' ')

        i += 6

    return ' '.join(result)

def main():
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])

        if is_braille(message):
            print(braille_to_english(message))
        else:
            print(english_to_braille(message))
    
if __name__ == "__main__":
    main()
