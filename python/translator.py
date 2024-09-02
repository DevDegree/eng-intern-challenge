import sys

BRAILLE_TO_ENG = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital next', '.O.OOO': 'number next'
}

ENG_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENG.items()}

NUM_MAPPING = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

def braille_to_eng_translate(braille):
    i = 0
    result = []
    cap_next_char = False
    in_num_mode = False

    while i < len(braille):
        cur_char = braille[i:i+6]

        if cur_char == ENG_TO_BRAILLE["capital next"]:
            cap_next_char = True
        elif cur_char == ENG_TO_BRAILLE['number next']:
            in_num_mode = True
        elif cur_char in BRAILLE_TO_ENG:
            letter = BRAILLE_TO_ENG[cur_char]
            if in_num_mode and letter in NUM_MAPPING:
                result.append(NUM_MAPPING[letter])
            else:
                if cap_next_char:
                    letter = letter.upper()
                    cap_next_char = False
                result.append(letter)
                if letter == ' ':
                    in_num_mode = False
        i += 6

    return ''.join(result)

def eng_to_braille_translate(english):
    result = []
    in_number_mode = False

    for char in english:
        if char.isupper():
            result.append(ENG_TO_BRAILLE['capital next'])
            char = char.lower()

        if char.isdigit():
            if not in_number_mode:
                result.append(ENG_TO_BRAILLE['number next'])
                in_number_mode = True
            char = list(NUM_MAPPING.keys())[list(NUM_MAPPING.values()).index(char)]
        elif in_number_mode:
            in_number_mode = False

        result.append(ENG_TO_BRAILLE[char])

    return ''.join(result)

def translate_str(input_string):
    if set(input_string).issubset({'O', '.'}):
        return braille_to_eng_translate(input_string)
    else:
        return eng_to_braille_translate(input_string)

if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    result = translate_str(input_string)
    sys.stdout.write(result)
    sys.stdout.flush()