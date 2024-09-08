import sys

ALPHANUM_BRAILLE = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    'cap': ".....O",
    'num': ".O.OOO",
    ' ': "......",
    '0': ".OOO..",
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO..."
}

BRAILLE_ALPHA = {
    v: k for k, v in ALPHANUM_BRAILLE.items() if k.isalpha() or k == ' '
}

BRAILLE_NUM = {
    v: k for k, v in ALPHANUM_BRAILLE.items() if k.isdigit() or k == ' '
}


def english_to_braille(input_str):
    result = []
    number_mode = False
    for char in input_str:
        if char.isdigit():
            if not number_mode:
                result.append(ALPHANUM_BRAILLE['num'])
                number_mode = True
            result.append(ALPHANUM_BRAILLE[char])
        elif char.isalpha():
            if char.isupper():
                result.append(ALPHANUM_BRAILLE['cap'])
                result.append(ALPHANUM_BRAILLE[char.lower()])
            else:
                result.append(ALPHANUM_BRAILLE[char])
            number_mode = False
        elif char == ' ':
            result.append(ALPHANUM_BRAILLE[' '])
            number_mode = False
    return ''.join(result)


def braille_to_english(braille_str):

    result = []
    number_mode = False
    capital_mode = False
    for i in range(0, len(braille_str), 6):
        symbol = braille_str[i:i+6]
        if symbol == ALPHANUM_BRAILLE['num']:
            number_mode = True
            continue
        elif symbol == ALPHANUM_BRAILLE['cap']:
            capital_mode = True
            continue

        if number_mode:
            result.append(BRAILLE_NUM[symbol])
        else:
            char = BRAILLE_ALPHA[symbol]
            if capital_mode:
                result.append(char.upper())
                capital_mode = False
            else:
                result.append(char)

        if symbol == ALPHANUM_BRAILLE[' ']:
            number_mode = False
    return ''.join(result)


def main():
    args = sys.argv[1:]
    input_str = ' '.join(args)

    if all(c in ['O', '.'] for c in input_str) and len(input_str) % 6 == 0:
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))


if __name__ == "__main__":
    main()
