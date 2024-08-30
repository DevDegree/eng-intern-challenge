import sys

# Define the special Braille symbols
capital_follows = '.....O'
number_follows = '.O.OOO'
decimal_follows = '.O...O'
space = '......'

# Define the Braille maps for numbers, letters, and punctuation
braille_map_num = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
}

braille_map_alph = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' ',
}

braille_map_decimals = {
    '..O...': ',',
    'O.O...': ';',
    '..OO..': ':',
    '..OO.O': '.',
    'OO....': '!',
    'O...O.': '?',
    '....O.': '-',
    '....OO': '/',
    '..O..O': '<',
    '..OO..': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
}

reverse_braille_map_alph = {v: k for k, v in braille_map_alph.items()}
reverse_braille_map_num = {v: k for k, v in braille_map_num.items()}
reverse_braille_map_decimals = {v: k for k, v in braille_map_decimals.items()}

def translate_to_braille(text):
    res = ""
    next_is_num = False 
    for c in text:
        if c.isupper():
            res += capital_follows
            res += reverse_braille_map_alph[c.lower()]
            next_is_num = False
        elif c.isdigit():
            if not next_is_num:
                res += number_follows
                next_is_num = True 
            res += reverse_braille_map_num[c]
        elif c in reverse_braille_map_alph:
            res += reverse_braille_map_alph[c]
            next_is_num = False 
        elif c in reverse_braille_map_decimals:
            res += decimal_follows
            res += reverse_braille_map_decimals[c]
            next_is_num = False 
        elif c == ' ':
            res += space
            next_is_num = False  
        else:
            raise ValueError(f"Character not supported: {c}")
    assert len(res) % 6 == 0, "Invalid Braille result length"
    return res

def translate_to_english(braille):
    assert len(braille) % 6 == 0, "Invalid Braille input length"
    next_is = None
    result = ""
    for chunk in [braille[i:i+6] for i in range(0, len(braille), 6)]:
        if chunk == capital_follows:
            next_is = 'CAP'
        elif chunk == decimal_follows:
            next_is = 'DECIMAL'
        elif chunk == number_follows:
            next_is = 'NUM'
        elif chunk == space:
            result += ' '
            next_is = None
        else:
            if next_is == 'CAP':
                result += braille_map_alph[chunk].upper()
                next_is = None
            elif next_is == 'NUM':
                result += braille_map_num[chunk]
            elif next_is == 'DECIMAL':
                result += braille_map_decimals[chunk]
                next_is = None
            else:
                result += braille_map_alph[chunk]
    return result

def main():
    text_in = " ".join(sys.argv[1:])
    is_braille = sorted(set(text_in)) == ['.', 'O']

    if is_braille:
        print(translate_to_english(text_in))
    else:
        print(translate_to_braille(text_in))

if __name__ == "__main__":
    main()
