import sys

alphabet = {
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
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

specials = {
    'capital_follows': '.....O',
    'decimal_follows': '.O...O',
    'number_follows': '.O.OOO'
}


def english_to_braille(text):
    result = []
    isnumber = False
    for c in text:
        if c == ' ':
            isnumber = False
        if c.isdigit() and not isnumber:
            result.append(specials['number_follows'])
            isnumber = True
        if c.isupper():
            result.append(specials['capital_follows'])
            c = c.lower()
        result.append(alphabet[c])
    return ''.join(result)


def braille_to_english(text):
    result = []
    iscapital = False
    isnumber = False
    for i in range(len(text) // 6):
        word = text[i * 6:(i + 1) * 6]
        if word == specials['capital_follows']:
            iscapital = True
        elif word == specials['number_follows']:
            isnumber = True
        else:
            for eng, bra in alphabet.items():
                if bra == word:
                    if eng == ' ':
                        isnumber = False
                        result.append(' ')
                        break
                    if isnumber and eng.isdigit():
                        result.append(eng)
                        break
                    elif not isnumber and iscapital:
                        result.append(eng.upper())
                        iscapital = False
                        break
                    elif not isnumber:
                        result.append(eng)
                        break
    return ''.join(result)


def main():
    text = ' '.join(sys.argv[1:])
    if len(text) % 6 > 0:
        print(english_to_braille(text))
    else:
        for c in text:
            if c != '.' and c != 'O':
                print(english_to_braille(text))
                return
        print(braille_to_english(text))


if __name__ == '__main__':
    main()
