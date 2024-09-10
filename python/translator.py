import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <English or Braille>")
        sys.exit(1)

    s = sys.argv[1]
    res = ''
    switch = 0
    caps = 0

    eng_to_br = {
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
        'capital': '.....O',
        'numbers': '.O.OOO'
    }

    br_to_eng = { v: k for k, v in eng_to_br.items() }


    # English to Braille
    if s.find('.') == -1:
        for c in s:
            if c.isalpha():
                if not c.islower():
                    res += eng_to_br['capital']
                res += eng_to_br[c.lower()]
            elif c.isdigit():
                if switch == 0:
                    switch = 1
                    res += eng_to_br['numbers']
                if c == '0':
                    ch = 10 + 96
                else:
                    ch = int(c) + 96
                res += eng_to_br[chr(ch)]
            elif c == ' ':
                if switch == 1:
                    switch = 0
                res += eng_to_br[' ']

    # Braille to English
    else:
        a = []
        for i in range(0, len(s), 6):
            a.append(s[i:i+6])
        for c in a:
            if br_to_eng[c] == 'capital':
                caps = 1
                continue
            elif br_to_eng[c] == 'numbers':
                switch = 1
                continue
            elif br_to_eng[c] == ' ':
                res += ' '
                if switch: switch = 0
                continue
            elif switch:
                n = ord(br_to_eng[c]) - 96
                if n == 10: res += '0'
                else: res += str(n)
                if caps: caps = 0
            else:
                if caps:
                    res += br_to_eng[c].upper()
                    caps = 0
                else:
                    res += br_to_eng[c].lower()

    print(res)

if __name__ == "__main__":
    main()

