import sys

englishToBraille = [
    'O.....',  # A
    'O.O...',  # B
    'OO....',  # C
    'OO.O..',  # D
    'O..O..',  # E
    'OOO...',  # F
    'OOOO..',  # G
    'O.OO..',  # H
    '.OO...',  # I
    '.OOO..',  # J
    'O...O.',  # K
    'O.O.O.',  # L
    'OO..O.',  # M
    'OO.OO.',  # N
    'O..OO.',  # O
    'OOO.O.',  # P
    'OOOOO.',  # Q
    'O.OOO.',  # R
    '.OO.O.',  # S
    '.OOOO.',  # T
    'O...OO',  # U
    'O.O.OO',  # V
    '.OOO.O',  # W
    'OO..OO',  # X
    'OO.OOO',  # Y
    'O..OOO'   # Z
]

# check if text is Braille or English
isBraille = len(sys.argv) <= 2
if len(sys.argv) == 2:
    for letter in sys.argv[1]:
        if not(letter == 'O' or letter == '.'): isBraille = False

# loop through args and translate them
for idx, arg in enumerate(sys.argv[1:], start=1):
    if isBraille:
        nextIsCapital = False
        nextIsNumber = False
        for i in range(0, len(arg), 6):
            str = arg[i:i+6]

            # process special braille strings first
            if str == '.....O': nextIsCapital = True
            elif str == '.O.OOO': nextIsNumber = True
            elif str == '......':
                print(' ', end='')
                nextIsNumber = False
            else:
                # print actual letters/digits
                if nextIsNumber:
                    print((englishToBraille.index(str)+1)%10, end='')
                elif nextIsCapital:
                    print(chr(englishToBraille.index(str)+ord('A')), end='')
                    nextIsCapital = False
                else:
                    print(chr(englishToBraille.index(str)+ord('a')), end='')

    else:
        nextIsNumber = False
        for letter in arg:
            if ('a' <= letter and letter <= 'z') or ('A' <= letter and letter <= 'Z'):
                if 'A' <= letter and letter <= 'Z':
                    print('.....O', end='')
                    print(englishToBraille[ord(letter) - ord('A')], end='')
                else:
                    print(englishToBraille[ord(letter) - ord('a')], end='')
            elif '0' <= letter and letter <= '9':
                if not(nextIsNumber):
                    print('.O.OOO', end='')
                    nextIsNumber = True
                print(englishToBraille[(ord(letter) - ord('0') - 1 + 10)%10], end='')
        
        # print space between english words, reset nextIsNumber flag
        if idx != len(sys.argv)-1:
            print('......', end='')
