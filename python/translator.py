import sys

# Define the Braille mapping dictionary
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    'cap': '.....O', 'num': '.O.OOO', ' ': '......'
}

# Create a reverse mapping for decoding Braille back to text
reverse_braille_map = {value: key for key, value in braille_map.items() if key not in ['cap', 'num']}

def is_braille(text):
    # Check if the input text consists only of 'O', '.', and spaces
    for char in text:
        if char not in ('O', '.', ' '):
            return False
    return True

def text_to_braille(text):
    braille_output = []
    digits = '0123456789'
    digit_to_braille = {
        '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
        '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
    }
    idx = 0
    while idx < len(text):
        ch = text[idx]
        if ch.isupper():
            braille_output.append(braille_map['cap'])
            ch = ch.lower()
        if ch in digits:
            braille_output.append(braille_map['num'])
            while idx < len(text) and text[idx] in digits:
                braille_char = digit_to_braille[text[idx]]
                braille_output.append(braille_map[braille_char])
                idx += 1
            continue
        elif ch == ' ':
            braille_output.append(braille_map[' '])
        elif ch in braille_map:
            braille_output.append(braille_map[ch])
        idx += 1
    return ''.join(braille_output)

def braille_to_text(braille):
    text_output = []
    # Remove spaces and split the Braille string into chunks of 6 characters
    braille = braille.replace(' ', '')
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capital_flag = False
    number_flag = False
    idx = 0
    while idx < len(braille_chars):
        symbol = braille_chars[idx]
        if symbol == braille_map[' ']:
            text_output.append(' ')
        elif symbol == braille_map['cap']:
            capital_flag = True
        elif symbol == braille_map['num']:
            number_flag = True
        else:
            if number_flag:
                braille_to_digit = {value: key for key, value in braille_map.items() if key in 'abcdefghij'}
                letter = braille_to_digit.get(symbol, '')
                digit_map = {
                    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
                    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
                }
                text_output.append(digit_map.get(letter, ''))
                # Exit number mode if the next symbol is not a digit
                if idx + 1 >= len(braille_chars) or braille_chars[idx + 1] not in braille_to_digit:
                    number_flag = False
            else:
                letter = reverse_braille_map.get(symbol, '')
                if capital_flag:
                    letter = letter.upper()
                    capital_flag = False
                text_output.append(letter)
        idx += 1
    return ''.join(text_output)

def main():
    # Get input from command-line arguments
    user_input = ' '.join(sys.argv[1:])
    if is_braille(user_input):
        # Translate Braille to English
        translated_text = braille_to_text(user_input)
    else:
        # Translate English to Braille
        translated_text = text_to_braille(user_input)
    print(translated_text)

if __name__ == '__main__':
    main()
