import sys

# Alphabet -> Braille
alphabet_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '.': '.O.O.O', ',': 'O.....', '!': 'OOO...', '?': '.O.OO.', 
    '-': 'O....O', ':': 'OO.O..', ';': 'O.O...', "'": 'O....O',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

# Braille -> Alphabet
braille_alphabet = {}

# Special Characters
special_chars = {}

for k, v in alphabet_braille.items():
    if k.isalpha():
        braille_alphabet[v] = k
    if k in ['.', ',', '-', ':', ';', '!', '?', "'"]:
        special_chars[v] = k

# Number -> Braille
number_dict = {
    '1': 'O.....',  
    '2': 'O.O...',  
    '3': 'OO....',  
    '4': 'OO.O..',  
    '5': 'O..O..',  
    '6': 'OOO...',  
    '7': 'OOOO..',  
    '8': 'O.OO..',  
    '9': '.OO...',  
    '0': '.OOO..'   
}

def translate_to_braille(text):
    solution = []
    number_mode = False  # Store if in number mode

    for char in text:
        if char.isupper():
            solution.append(alphabet_braille['capital'])
            solution.append(alphabet_braille[char.lower()])
            number_mode = False 
        elif char.isdigit():
            if not number_mode:
                solution.append(alphabet_braille['number']) 
                number_mode = True 
            solution.append(number_dict[char])
        else:
            if number_mode and char == ' ':
                number_mode = False
            solution.append(alphabet_braille.get(char, '......'))

    return ''.join(solution)

def translate_to_english(braille):
    solution = []
    check_capital = False
    number_mode = False
    braille_buffer = ''

    for char in braille:
        braille_buffer += char
        if len(braille_buffer) == 6:
            if braille_buffer == alphabet_braille['capital']:
                check_capital = True
            elif braille_buffer == alphabet_braille['number']:
                number_mode = True
            elif braille_buffer == '......':
                solution.append(' ')
                number_mode = False
            else:
                if number_mode:
                    char = next((key for key, value in number_dict.items() if value == braille_buffer), '')
                else:
                    char = braille_alphabet.get(braille_buffer, '') or special_chars.get(braille_buffer, '')
                    if check_capital:
                        char = char.upper()
                        check_capital = False 
                solution.append(char)
            braille_buffer = ''

    return ''.join(solution)


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_or_braille>")
        return

    input_text = ' '.join(sys.argv[1:]) # Get all input text

    if all(char in 'O.' for char in input_text.replace(' ', '')):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
