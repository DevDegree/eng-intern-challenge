import sys

ENGLISH_BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'capital': '.....O', 'number': '.O.OOO', ' ': '......'
}

def detect_input_type(input_string):
    return 'braille' if set(input_string) <= {'O', '.'} else 'english'

def english_to_braille(english_text):
    braille_output = []
    is_number_mode = False
    for char in english_text:
        if char.isupper():
            braille_output.append(ENGLISH_BRAILLE_MAP['capital'])
            char = char.lower()
        if char.isdigit():
            if not is_number_mode:
                braille_output.append(ENGLISH_BRAILLE_MAP['number'])
                is_number_mode = True
        else:
            is_number_mode = False
        braille_output.append(ENGLISH_BRAILLE_MAP[char])
    return ''.join(braille_output)

def braille_to_english(braille_text):
    english_output = []
    is_capital_next = is_number_mode = False
    i = 0
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        if braille_char == ENGLISH_BRAILLE_MAP['capital']:
            is_capital_next = True
        elif braille_char == ENGLISH_BRAILLE_MAP['number']:
            is_number_mode = True
        else:
            char = next(k for k, v in ENGLISH_BRAILLE_MAP.items() if v == braille_char)
            if is_number_mode and char in 'abcdefghij':
                english_output.append(str('abcdefghij'.index(char)))
            else:
                english_output.append(char.upper() if is_capital_next else char)
                is_number_mode = False
            is_capital_next = False
        i += 6
    return ''.join(english_output)

def translate(input_string):
    if detect_input_type(input_string) == 'english':
        return english_to_braille(input_string)
    else:
        return braille_to_english(input_string)

def main():
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(translate(input_text), end='')
    else:
        raise ValueError("No input provided")

if __name__ == "__main__":
    main()
