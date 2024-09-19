import sys

# english letters mapped to braille
eng_to_braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
}

# numbers mapped to braille
num_to_braille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

# braille to english
braille_to_eng = {v: k for k, v in eng_to_braille.items()}
braille_to_num = {v: k for k, v in num_to_braille.items()}

# specials
capital = '.....O'
number = '.O.OOO'
space = '......'


# method to check if given string is in braille format
def is_braille(s: str):
    # braille would consist only of {O and .} and length will be miltiple of 6
    return len(s) % 6 == 0 and set(s).issubset({'O', '.'})


# method to translate braille to english
def translate_to_english(s: str):
    result = ''
    is_capital = False
    numeric_mode = False
    i = 0
    while i < len(s):

        symbol = s[i:i + 6]  # reading 6 chars at a time
        i += 6

        if symbol == capital:
            is_capital = True
            continue
        elif symbol == number:
            numeric_mode = True
            continue
        elif symbol == space:
            result += ' '
            numeric_mode = False  # numeric mode disables as soon as a space is read
            continue

        if numeric_mode:
            result += braille_to_num.get(symbol, '')
        else:
            char = braille_to_eng.get(symbol, '')
            if is_capital:
                result += char.upper()
                is_capital = False  # capital only active for one character
            else:
                result += char

    return result


# method to translate english to braille
def translate_to_braille(s: str):
    result = ''
    numeric_mode = False

    for c in s:

        if c == ' ':
            result += space
            numeric_mode = False  # numeric mode disabled as soon as space is read
            continue

        if c.isdigit():
            if not numeric_mode:
                result += number
                numeric_mode = True
            result += num_to_braille[c]
        else:
            if c.isupper():
                result += capital
            result += eng_to_braille.get(c.lower(), '')
            numeric_mode = False

    return result


def main():
    args = sys.argv[1:]

    if not args:
        return

    input_str = ' '.join(args)
    if is_braille(input_str):
        res = translate_to_english(input_str)
    else:
        res = translate_to_braille(input_str)

    print(res.strip())


if __name__ == '__main__':
    main()
