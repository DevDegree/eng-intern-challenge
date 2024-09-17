import sys

english_dict = {
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
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OO..',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO'
}

braille_dict_letters = {
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
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OO..': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
    '.....O': 'capital',
    '.O...O': 'decimal',
    '.O.OOO': 'number'
}

braille_dict_numbers = {
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
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OO..': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
    '.....O': 'capital',
    '.O...O': 'decimal',
    '.O.OOO': 'number'
}

# check will just assume length of any multiple of 6, and 'O' or '.' in strings, is braille
def check_is_braille(text):
    for c in text:
        if c != 'O' and c != '.':
            return False
    return False if len(text) % 6 != 0 else True

def translate_eng(sentence):
    res = ''
    for i in range(len(sentence)):
        isNumbers = False
        for c in sentence[i]:
            if not isNumbers and ord('0') <= ord(c) and ord(c) <= ord('9'):
                res += english_dict['number']
                isNumbers = True
            elif ord('A') <= ord(c) and ord(c) <= ord('Z'):
                isNumbers = False
                res += english_dict['capital']
                res += english_dict[chr(ord(c) + 32)] # special case, adjust the char
                continue
            res += english_dict[c]

        if i < len(sentence) - 1:
            res += english_dict[' ']
    return res

def translate_braille(text):
    res = ''
    curr_dict = braille_dict_letters
    apply_caps = False
    num_groups = int(len(text) / 6)
    for i in range(num_groups):
        group = ''
        for j in range(6):
            group += text[i * 6 + j]
        char = curr_dict[group]
        if char == ' ':
            curr_dict = braille_dict_letters
            res += char
        elif apply_caps:
            res += chr(ord(char) - 32)
            apply_caps = False
        elif char == 'capital':
            apply_caps = True
        elif char == 'number':
            curr_dict = braille_dict_numbers
        else:
            res += char
    return res


# MAIN:
# Notes:
    # left to right, top to bottom (right to left was a typo?)
    # Wrong test case:
        # Input: .....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..
        # Output: Abc 123


def main():
    sentence = []
    for word in sys.argv[1:]:
        sentence.append(word)

    is_braille = False # init to false, any case where more than one word in sentence, must be english, due to spaces in text

    if len(sentence) == 0:
        return
    elif len(sentence) == 1:
        is_braille = check_is_braille(sentence[0])
    res = translate_braille(sentence[0]) if is_braille else translate_eng(sentence)
    print(res)

if __name__ == '__main__':
    main()
