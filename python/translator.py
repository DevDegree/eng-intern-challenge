import sys;

letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', " ": "......"
}

letters_reverse = {val : key for key, val in letters.items()}

numbers= {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

numbers_reverse = {val : key for key, val in numbers.items()}

symbols = {
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
    "(": "O.O..O", ")": ".O.OO."
}

symbols_reverse = {val : key for key, val in symbols.items()}

type = {
    'capital': ".....O", "decimal": ".O...O", "number": ".O.OOO"
}
type_reverse = {val : key for key, val in type.items()}



def to_braille(lst):
    braille_str = ''
    for item in lst:
        if braille_str:
            braille_str += letters[" "]
        if item[0] in numbers:
            if '.' in item:
                braille_str += type['decimal']
            braille_str += type['number']
        for chr in item:
            if chr in symbols.keys():
                braille_str += symbols[chr]
            elif chr in numbers.keys():
                braille_str += numbers[chr]
            elif chr.isupper():
                braille_str += type['capital']
                braille_str += letters[chr.lower()]
            else:
                braille_str += letters[chr]
    return braille_str


def to_english(lst):
    english_str = ''
    capital = False
    number = False
    for item in lst:
        idx = 0
        while (idx < len(item)):
            braille_chr = item[idx: idx+6]
            mode = ''
            if braille_chr in type.values():
                mode = type_reverse[braille_chr]
                if mode == "capital":
                    capital = True
                else:
                    number = True
                idx += 6
                continue

            if braille_chr == letters[' '] and number:
                number = False
                english_str += ' '
            elif capital:
                capital = False
                english_str += letters_reverse.get(braille_chr).upper()
            elif number:
                if braille_chr in numbers.values():
                    english_str += numbers_reverse.get(braille_chr)
                else:
                    english_str += "."
            elif braille_chr in letters.values():
                english_str += letters_reverse.get(braille_chr)
            elif braille_chr in symbols.values():
                english_str += symbols_reverse.get(braille_chr)
            idx += 6
    return english_str


def translate(lst):
    if not list:
        return ""
    for item in lst:
        if not all(c in ['.', 'O'] for c in item):
            return to_braille(lst)
    return to_english(lst)


if __name__ == "__main__":
    print(translate(sys.argv[1:]))

