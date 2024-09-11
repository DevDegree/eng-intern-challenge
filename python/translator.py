import sys

CAPS_STR = 'CAPS_FOLLOWS'
NUM_STR = 'NUM_FOLLOWS'
ENG_TO_BRAILLE = {
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
    CAPS_STR: '.....O',
    NUM_STR: '.O.OOO'
}
BRAILLE_TO_ENGLISH = {}
for k,v in ENG_TO_BRAILLE.items():
    BRAILLE_TO_ENGLISH[v] = k
for i in range(1, 11):
    ENG_TO_BRAILLE[str(i % 10)] = ENG_TO_BRAILLE[chr(ord('a') + i - 1)]

def handle_english(x: str) -> None:
    """
    Prints a sequence of braille characters based on english characters being read
    """
    res = ""
    out_nums = False
    for c in x:
        if 'A' <= c <= 'Z':
            res += ENG_TO_BRAILLE[CAPS_STR]
            out_nums = False
        elif '0' <= c <= '9' and not out_nums:
            res += ENG_TO_BRAILLE[NUM_STR]
            out_nums = True
        elif not '0' <= c <= '9':
            out_nums = False
        res += ENG_TO_BRAILLE[c.lower()]
    print(res, end='')

def handle_braile(x: str) -> None:
    """
    Prints a sequence of english characters based on braille input being read
    """
    n = len(x)
    i = 0
    prev_caps = False
    prev_num = False
    res = ""
    while i < n:
        char = x[i:i+6]
        if char == ENG_TO_BRAILLE[CAPS_STR]:
            prev_caps = True
        elif char == ENG_TO_BRAILLE[NUM_STR]:
            prev_num = True
            prev_caps = False
        elif ENG_TO_BRAILLE[' '] == char:
            res += " "
            prev_caps = False
            prev_num = False
        elif prev_caps:
            res += BRAILLE_TO_ENGLISH[char].upper()
            prev_caps = False
        elif prev_num:
            res += chr(ord(BRAILLE_TO_ENGLISH[char]) - ord('a') + ord('1'))
        else:
            res += BRAILLE_TO_ENGLISH[char]
        i += 6
    print(res)

braille = False
x = sys.argv[1]
# check if braille by seeing if first 6 characters only contain . or . and O
if len(x) >= 6:
    mp = set()
    for i in x[:6]:
        mp.add(i)
    if ((len(mp) == 1) or (len(mp) == 2 and 'O' in mp)) and '.' in mp:
        braille = True
if braille:
    handle_braile(x)
else:
    handle_english(x)
for x in sys.argv[2:]:
    if not braille:
        print(ENG_TO_BRAILLE[' '], end='')
        handle_english(x)
                 
