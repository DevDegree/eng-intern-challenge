import sys

# Braille translation dictionary (alphabet and numbers)// taken from google
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'number': '.O.OOO',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Reverse Braille translation dictionary
reverse_braille = {v: k for k, v in braille_alphabet.items()}

def english_to_braille(text):
    output = []
    for char in text:
        if char.isupper():
            output.append(braille_alphabet['capital'])
            output.append(braille_alphabet[char.lower()])
        elif char.isdigit():
            output.append(braille_alphabet['number'])
            output.append(braille_alphabet[char])
        else:
            output.append(braille_alphabet[char])
    return ''.join(output)

def braille_to_english(braille):
    output = []
    i = 0
    capital_flag = False
    number_flag = False

    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_alphabet['capital']:
            capital_flag = True
        elif symbol == braille_alphabet['number']:
            number_flag = True
        else:
            char = reverse_braille.get(symbol, '')
            if capital_flag:
                output.append(char.upper())
                capital_flag = False
            elif number_flag:
                output.append(char)
                number_flag = False
            else:
                output.append(char)
        i += 6
    return ''.join(output)

def is_braille(input_str):
    return all(char in 'O.' for char in input_str)

def main():
    print("Translator script running...", file=sys.stderr)  # Debug message
    
    input_str = ' '.join(sys.argv[1:])
    
    if is_braille(input_str):
        print("Brail to english translation is ",braille_to_english(input_str))
    else:
        print("English to brail translation is ",english_to_braille(input_str))

if __name__ == "__main__":
    main()
