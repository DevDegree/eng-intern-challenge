import sys

ENG_TO_BRAILLE= {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO'
}

NUM_TO_BRAILLE = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

OTHER_TO_BRAILLE= {
    'capital': '.....O', 'number': '.O.OOO', 'decimal': '.OOO.O', 'space': '......', '.': '..OO.O', ',': '..O...', ';': '..OO..', ':': '..OO..', '?': '..O.OO',
    '!': '..OOO.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.',
    '>': 'O..OO.', '<': '.OO..O',
}

def check_is_braille(input: str) -> bool:
    if len(input) % 6 != 0:
        return False
    for char in input:
        if char not in ['.', 'O', '0', '1']:
            return False
    return True

def english_to_braille(input_text: str) -> str:
    braille_output = ''
    is_number_mode = is_capital_mode = False

    for char in input_text:
        if char.isnumeric():
            if not is_number_mode:
                braille_output += OTHER_TO_BRAILLE['number']
                is_number_mode = True
            braille_output += NUM_TO_BRAILLE[char]
        elif char.isalpha():
            if char.isupper() and not is_capital_mode:
                braille_output += OTHER_TO_BRAILLE['capital']
                is_capital_mode = True
            braille_output += ENG_TO_BRAILLE[char.lower()]
        elif char == ' ':
            braille_output += OTHER_TO_BRAILLE['space']
            is_number_mode = is_capital_mode = False
        elif char in OTHER_TO_BRAILLE:
            braille_output += OTHER_TO_BRAILLE[char]
        else:
            sys.exit(1)
    return braille_output

def braille_to_english(braille_input: str) -> str:
    english_output = ''
    is_capital_next = is_number_mode = False
    braille_to_eng = {v: k for k, v in ENG_TO_BRAILLE.items()}
    braille_to_num = {v: k for k, v in NUM_TO_BRAILLE.items()}

    for i in range(0, len(braille_input), 6):
        braille_char = braille_input[i:i + 6]
        if braille_char == OTHER_TO_BRAILLE['capital']:
            is_capital_next = True
        elif braille_char == OTHER_TO_BRAILLE['number']:
            is_number_mode = True
        elif braille_char == OTHER_TO_BRAILLE['space']:
            english_output += ' '
            is_number_mode = False
        elif braille_char in braille_to_eng and not is_number_mode:
            letter = braille_to_eng[braille_char]
            english_output += letter.upper() if is_capital_next else letter
            is_capital_next = False
        elif braille_char in braille_to_num:
            english_output += braille_to_num[braille_char]
            is_number_mode = True
        elif braille_char in OTHER_TO_BRAILLE.values():
            english_output += next(k for k, v in OTHER_TO_BRAILLE.items() if v == braille_char)
            is_number_mode = False

    return english_output

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    input_args = sys.argv[1:]
    if check_is_braille(input_args[0]):
        output = braille_to_english(input_args[0])
    else:
        output = english_to_braille(' '.join(input_args))
    print(output)

if __name__ == '__main__':
    main()