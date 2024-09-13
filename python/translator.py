import sys

# braille to string
bs = {
    '......': ' ',
    '.....O': 'CAP',
    '.O.OOO': 'NUM'
}

bs_alpha = {
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
    'O..OOO': 'z'
}

bs_digit = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}

# string to braille
sb = {
    ' ' :'......',
    'CAP': '.....O',
    'NUM': '.O.OOO'
}

sb_alpha = {
    'a' :'O.....',
    'b' :'O.O...',
    'c' :'OO....',
    'd' :'OO.O..',
    'e' :'O..O..',
    'f' :'OOO...',
    'g' :'OOOO..',
    'h' :'O.OO..',
    'i' :'.OO...',
    'j' :'.OOO..',
    'k' :'O...O.',
    'l' :'O.O.O.',
    'm' :'OO..O.',
    'n' :'OO.OO.',
    'o' :'O..OO.',
    'p' :'OOO.O.',
    'q' :'OOOOO.',
    'r' :'O.OOO.',
    's' :'.OO.O.',
    't' :'.OOOO.',
    'u' :'O...OO',
    'v' :'O.O.OO',
    'w' :'.OOO.O',
    'x' :'OO..OO',
    'y' :'OO.OOO',
    'z' :'O..OOO'
}

sb_digit = {
    '1' :'O.....',
    '2' :'O.O...',
    '3' :'OO....',
    '4' :'OO.O..',
    '5' :'O..O..',
    '6' :'OOO...',
    '7' :'OOOO..',
    '8' :'O.OO..',
    '9' :'.OO...',
    '0' :'.OOO..'
}


def braille_to_string(braille: str) -> str:
    string = []
    cap_index = -2
    is_number = False
    for i in range(0, len(braille), 6):
        curr_braille = braille[i:i + 6]
        if curr_braille in bs:
            mapping = bs[curr_braille]
            if mapping == 'CAP':
                cap_index = i
            elif mapping == 'NUM':
                is_number = True
            elif mapping == ' ':
                is_number = False
                string.append(' ')
        else:
            if is_number:
                mapping = bs_digit[curr_braille]
                string.append(mapping)
            else:
                mapping = bs_alpha[curr_braille]
                if cap_index == i - 6:
                    mapping = mapping.upper()
                string.append(mapping)
    return ''.join(string)


def string_to_braille(string) -> str:
    braille = []
    is_number = False
    for ch in string:
        if ch.isdigit():
            if not is_number:
                braille.append(sb['NUM'])
                is_number = True
            braille.append(sb_digit[ch])
        elif ch.isalpha():
            if ch.isupper():
                braille.append(sb['CAP'])
            braille.append(sb_alpha[ch.lower()])
        elif ch == ' ':
            is_number = False
            braille.append(sb[' '])
    return ''.join(braille)


if __name__ == "__main__":
    args = sys.argv[1:]
    arg_string = ' '.join(args)
    # braille to string
    if '.' in arg_string:  # all required characters have at least one dot in their braille representation
        print(braille_to_string(arg_string.strip()))
    # string to braille
    else:
        print(string_to_braille(arg_string))