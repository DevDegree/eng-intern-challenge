import sys

map = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
       'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
       'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
       'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
       'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
       'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
       'y': 'OO.OOO', 'z': 'O..OOO', '1': 'a', '2': 'b', '3': 'c',
       '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
       '0': 'j', 'num': '.O.OOO', 'cap': '.....O', 'dec': '.O...O',
       '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
       ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
       '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': 'O..OO.',
       'space': '......'}

idk = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i',
    '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm',
    'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w',
    'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z', '.O.OOO': 'num', '.....O':
        'cap', '.O...O': 'dec', '..OO.O': '.', '..O...': ',', '..O.OO': '?',
    '..OOO.': '!', '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
    '.OO..O': '<', 'O.O..O': '(', '.O.OO.': ')', '......': 'space'
}

numMap = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3',
    'OO.O..': '4', 'O..O..': '5', 'OOO...': '6',
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.000..': '0'}

keys = list(map.values())


def translateWord(words):
    result = ""
    nums = False
    for word in words:
        for c in word:
            if c.isalpha():
                if c.isupper():
                    result += map['cap'] + map[c.lower()]
                else:
                    result += map[c]
            elif c.isnumeric():
                if nums:
                    result += map[map[c]]
                else:
                    nums = True
                    result += map['num'] + map[map[c]]
            else:
                result += map[c]
        if nums:
            nums = False
        result += map['space']
    result = result[:-6]
    print(result)


def translateB(words):
    i = 0
    number = False
    capital = False
    result = ""
    split_string = [words[i:i + 6] for i in range(0, len(words), 6)]
    for i in range(len(split_string)):
        if split_string[i] == map['space']:
            result += " "
            number = False
        elif split_string[i] == map['num']:
            number = True
        elif split_string[i] == map['cap']:
            capital = True
        else:
            if number:
                result += numMap[split_string[i]]
            else:
                if capital:
                    result += idk[split_string[i]].upper()
                    capital = False
                else:
                    result += idk[split_string[i]]
    print(result)


isB = True

if len(sys.argv) > 2:
    translateWord(sys.argv[1:])
else:
    text = sys.argv[1]
    if len(text) % 6 == 0:
        for t in text:
            if t != 'O' and t != '.':
                isB = False
                break
        if isB:
            translateB(sys.argv[1])
        else:
            translateWord(sys.argv[1:])
    else:
        translateWord(sys.argv[1:])
