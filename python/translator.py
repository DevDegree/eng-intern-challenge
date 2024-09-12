import sys


char_to_braille = {
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
    ' ': '......',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '..O..O',
    '/': '..O..O',
    '<': '..O.O.',
    '>': '..OO.O',
    '(': '..OO..',
    ')': '..OO..',
}

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
    '.': '...O.O',
    ' ': '......',
}

braille_to_char = {v: k for k, v in char_to_braille.items()}
braille_to_num = {v: k for k, v in num_to_braille.items()}
        

def english_to_braille_convert(text):
    res = []
    num = False
    dec = False

    for char in text:
        if char.isalpha():
            if num or dec:
                num = False
                dec = False
            if char.isupper():
                res.append('.....O')
            res.append(char_to_braille[char.lower()])
        elif char.isdigit():
            if not (num or dec):
                res.append('.O.OOO')
                num = True
            res.append(num_to_braille[char])
        elif char == '.':
            if not num:
                res.append(char_to_braille['.'])
            else:
                res.append('.O...O')
                dec = True
                num = False
        else:
            num = False
            dec = False
            res.append(char_to_braille.get(char, '......'))

    return ''.join(res)

def braille_to_english_convert(text):
    capital = False
    num = False
    dec = False
    i = 0
    res = []

    while i < len(text):
        chunk = text[i:i+6]
    
        if chunk == '.....O':
            capital = True
        elif chunk == '.O.OOO':
            num = True
        elif chunk == '.O...O':
            dec = True
            res.append('.')
        
        else:
            if num or dec:
                val = braille_to_num.get(chunk, '')
                if val in "1234567890":
                    res.append(val)
                elif val == " ":
                    num = False
                    dec = False
                    res.append(' ')
                else:
                    num = False
                    dec = False
            else:
                val = braille_to_char.get(chunk, '')
                if val:
                    if val.isalpha() and capital:
                        val = val.upper()
                        capital = False
                    res.append(val)
                else:
                    print(f"Unknown braille character: {chunk}")
        i += 6
    
    return ''.join(res)

def translate(text):
    if all(char in '0.' for char in text):
        return braille_to_english_convert(text)
    else:
        return english_to_braille_convert(text)

def main():
    if len(sys.argv) < 2:
        print('Usage: python translator.py <text>')
        sys.exit(1)

    text = ' '.join(sys.argv[1:])
    print(translate(text))

if __name__ == '__main__':
    main()