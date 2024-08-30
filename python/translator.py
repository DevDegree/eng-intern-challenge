import sys

# Constant Dictionaries
bToE = {'O.....': ('A', '1'), 'O.O...': ('B', '2'), 'OO....': ('C', '3'), 'OO.O..': ('D', '4'), 'O..O..': ('E', '5'),
        'OOO...': ('F', '6'), 'OOOO..': ('G', '7'), 'O.OO..': ('H', '8'), '.O.O..': ('I', '9'), '.OOO..': ('J', '0'),
        'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': ('O', '>'), 'OOO.O.': 'P', 'OOOOO.': 'Q',
        'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T', 'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X',
        'OO.OOO': 'Y', 'O..OOO': 'Z', '.....O': 'capital_follows', '.O.OOO': 'number_follows', '..OO.O': '.',
        '......': ' '}
eToB = {('A', '1'): 'O.....', ('B', '2'): 'O.O...', ('C', '3'): 'OO....', ('D', '4'): 'OO.O..', ('E', '5'): 'O..O..',
        ('F', '6'): 'OOO...', ('G', '7'): 'OOOO..', ('H', '8'): 'O.OO..', ('I', '9'): '.O.O..', ('J', '0'): '.OOO..',
        'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.', 'P': 'OOO.O.', 'Q': 'OOOOO.',
        'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO',
        'Y': 'OO.OOO', 'Z': 'O..OOO', 'capital follows': '.....O', 'number follows': '.O.OOO', '.': '..OO.O',
        ' ': '......'}


def check_string(string):
    allowed_chars, res = {'O', '.'}, ''
    if all(char in allowed_chars for char in string):
        capital_follows, number_follows = False, False
        for i in range(0, len(string) - 5, 6):
            lookup = string[i:i + 6]
            if bToE[lookup] == 'capital_follows':
                capital_follows = True
            elif bToE[lookup] == 'number_follows':
                number_follows = True
            elif len(bToE[lookup]) == 1:
                if capital_follows:
                    res += bToE[lookup]
                else:
                    res += bToE[lookup].lower()
            elif len(bToE[lookup]) == 2 and ord('A') <= ord(bToE[lookup][0]) <= ord('Z') or ord('1') <= ord(
                    bToE[lookup][1]) <= ord('9'):
                if capital_follows:
                    res += bToE[lookup][0]
                    capital_follows = False
                else:
                    if not number_follows:
                        res += bToE[lookup][0].lower()
                    else:
                        res += bToE[lookup][1]
    else:
        substrings = string.split(" ")
        for subs in substrings:
            if ord('1') <= ord(subs[0]) <= ord('9'):
                res += eToB['number follows']
            for j in range(len(subs)):
                if ord('A') <= ord(subs[j]) <= ord('Z'):
                    res += eToB['capital follows']
                if ord('k') <= ord(subs[j].lower()) <= ord('z'):
                    res += eToB[subs[j].upper()]
                elif ord('a') <= ord(subs[j].lower()) <= ord('j') or ord('0') <= ord(subs[j]) <= ord('9'):
                    if ord('a') == ord(subs[j].lower()) or ord('1') == ord(subs[j]):
                        res += eToB[('A', '1')]
                    if ord('b') == ord(subs[j].lower()) or ord('2') == ord(subs[j]):
                        res += eToB[('B', '2')]
                    if ord('c') == ord(subs[j].lower()) or ord('3') == ord(subs[j]):
                        res += eToB[('C', '3')]
                    if ord('d') == ord(subs[j].lower()) or ord('4') == ord(subs[j]):
                        res += eToB[('D', '4')]
                    if ord('e') == ord(subs[j].lower()) or ord('5') == ord(subs[j]):
                        res += eToB[('E', '5')]
                    if ord('f') == ord(subs[j].lower()) or ord('6') == ord(subs[j]):
                        res += eToB[('F', '6')]
                    if ord('g') == ord(subs[j].lower()) or ord('7') == ord(subs[j]):
                        res += eToB[('G', '7')]
                    if ord('h') == ord(subs[j].lower()) or ord('8') == ord(subs[j]):
                        res += eToB[('H', '8')]
                    if ord('i') == ord(subs[j].lower()) or ord('9') == ord(subs[j]):
                        res += eToB[('I', '9')]
                    if ord('j') == ord(subs[j].lower()) or ord('0') == ord(subs[j]):
                        res += eToB[('J', '0')]
            if subs != substrings[-1]:
                res += eToB[' ']
    return res


def main():
    args = sys.argv[1:]
    string = " ".join(args)
    print(check_string(string))


if __name__ == "__main__":
    main()
