import sys

CAPNEXT = '.....O'
NUMNEXT = '.O.OOO'

br_to_eng = {
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
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
}

eng_to_br = {val: key for key, val in br_to_eng.items()}

br_to_num = {
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

num_to_br = {val: key for key, val in br_to_num.items()}

def translate_to_english(braille):
    capital = False
    number = False
    result = ''
    for i in range(0, len(braille), 6):
        char = braille[i:i+6]
        # print(char)
        if char == "......":
            result += " "
            number = False
            continue

        if char == ".O.OOO":
            number = True
            continue

        if char == CAPNEXT:
            capital = True
            continue

        if number:
            result += br_to_num[char]
        else:
            if capital:
                result += br_to_eng[char].upper()
                capital = False
            else:
                result += br_to_eng[char]
    return result

def translate_to_braille(text):
    number = False
    result = ''
    for char in text:
        if char.isupper():
            result += CAPNEXT
            char = char.lower()
        if char == ' ':
            result += '......'
            number = False
        elif char.isdigit():
            if not number:
                result += NUMNEXT
                number = True
            result += num_to_br[char]
        else:
            result += eng_to_br[char]

    return result

# print(translate_to_braille("Abc 123 xYz"))
# print(translate_to_braille("Abc 123 xYz") == ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")
# print(translate_to_english(translate_to_braille("Abc 123 xYz")))
# print(translate_to_english(translate_to_braille(" kasdjhfjk 23894 3984 fds sdfhj382348 98392")))
# print(translate_to_english(translate_to_braille(" kasdjhfjk 23894 3984 fds sdfhj382348 98392")) == " kasdjhfjk 23894 3984 fds sdfhj382348 98392")
# print(len(translate_to_braille("dfjk349 940s")))

def translate():
    cmd_input = " ".join(sys.argv[1:])
    if len(cmd_input) == 0:
        return
    if len(set(cmd_input)) == 2: # If there are only . and O in the input
        print(translate_to_english(cmd_input))
    else:
        print(translate_to_braille(cmd_input))

if __name__ == '__main__':
    translate()