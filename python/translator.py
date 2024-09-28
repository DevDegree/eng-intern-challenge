import sys

CAPITAL = '.....O'
NUMBER = '.O.OOO'

eng_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......', '.': '..O.OO', ',': '..O...', '!': '..OO.O', '?': '..O.O.',
    ':': '...OOO', ';': '...O.O', '(': '...OO.', ')': '.OOO.O'
}

braille_to_eng = {}
for letter, braille_symbol in eng_to_braille.items():
    braille_to_eng[braille_symbol] = letter

num_to_letter = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}

letter_to_num = {}

for digit, letter in num_to_letter.items():
    letter_to_num[letter] = digit

def is_braille(input_text):
    for char in input_text:
        if char not in {'.', 'O'}:
            return False
    return True

def english_to_braille(input_text):
    braille_output = []
    number_mode = False

    for char in input_text:
        if char.isupper():
            braille_output.append(CAPITAL)
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                braille_output.append(NUMBER)
                number_mode = True

            letter = num_to_letter[char]

            braille_output.append(eng_to_braille[letter])
        else:
            if char == ' ':
                number_mode = False

            braille_output.append(eng_to_braille.get(char, ' '))

    return ''.join(braille_output)

def braille_to_english(input_text):
    eng_output = []
    capital = False
    number = False

    for i in range(0, len(input_text), 6):
        b_char = input_text[i:i + 6]

        if b_char == CAPITAL:
            capital = True
            continue
        elif b_char == NUMBER:
            number = True
            continue

        eng_char = braille_to_eng.get(b_char, '')

        if not eng_char:
            continue

        if number:
            if eng_char in letter_to_num:
                eng_char = letter_to_num[eng_char]
            else:
                number = False  
        
        if eng_char == ' ':
            number = False  

        if capital:
            eng_char = eng_char.upper()
            capital = False

        eng_output.append(eng_char)

    return ''.join(eng_output)


if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    if is_braille(input_text):
        output = braille_to_english(input_text)
    else:
        output = english_to_braille(input_text)
    print(output)
