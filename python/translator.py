import sys

toBraille = {}
toEnglish = {}
toDigit = {}
toBraille['a'] = 'O.....'
toBraille['b'] = 'O.O...'
toBraille['c'] = 'OO....'
toBraille['d'] = 'OO.O..'
toBraille['e'] = 'O..O..'
toBraille['f'] = 'OOO...'
toBraille['g'] = 'OOOO..'
toBraille['h'] = 'O.OO..'
toBraille['i'] = '.OO...'
toBraille['j'] = '.OOO..'
toBraille['k'] = 'O...O.'
toBraille['l'] = 'O.O.O.'
toBraille['m'] = 'OO..O.'
toBraille['n'] = 'OO.OO.'
toBraille['o'] = 'O..OO.'
toBraille['p'] = 'OOO.O.'
toBraille['q'] = 'OOOOO.'
toBraille['r'] = 'O.OOO.'
toBraille['s'] = '.OO.O.'
toBraille['t'] = '.OOOO.'
toBraille['u'] = 'O...OO'
toBraille['v'] = 'O.O.OO'
toBraille['w'] = '.OOO.O'
toBraille['x'] = 'OO..OO'
toBraille['y'] = 'OO.OOO'
toBraille['z'] = 'O..OOO'

toBraille['1'] = 'O.....'
toBraille['2'] = 'O.O...'
toBraille['3'] = 'OO....'
toBraille['4'] = 'OO.O..'
toBraille['5'] = 'O..O..'
toBraille['6'] = 'OOO...'
toBraille['7'] = 'OOOO..'
toBraille['8'] = 'O.OO..'
toBraille['9'] = '.OO...'
toBraille['0'] = '.OOO..'

toBraille['space'] = '......'
toBraille['capital'] = '.....O'
toBraille['number'] = '.O.OOO'


def brailleToEnglish(braille):
    # assumes a valid, well-formed braille string
    ret = ''
    numTokens = len(braille)/6
    indToken = 0
    isNumber = 0
    while indToken < numTokens:
        token = braille[6*indToken : 6*indToken+6]
        if toEnglish[token] == 'space':
            ret += ' '
            isNumber = 0
        elif toEnglish[token] == 'capital':
            indToken += 1
            if indToken < numTokens:
                token = braille[6*indToken : 6*indToken+6]
                ret += toEnglish[token].upper()
        elif toEnglish[token] == 'number':
            isNumber = 1
        elif isNumber:
            ret += toDigit[token]
        else:
            ret += toEnglish[token]
        indToken += 1
    return ret

def englishToBraille(words):
    # assumes a list of valid, well-formed alphanumeric strings
    ret = ''
    for ind in range(0, len(words)):
        word = words[ind]
        isNumber = 0
        for char in word:
            if char.isupper():
                ret += toBraille['capital']
            elif isNumber==0 and char.isdigit():
                ret += toBraille['number']
                isNumber = 1
            ret += toBraille[char.lower()]
        if ind != len(words)-1:
            ret += toBraille['space']
    return ret

def main():
    words = sys.argv[1:]

    if len(words) == 0:
        return 0
    
    for word in toBraille.keys():
        if word.isdigit():
            toDigit[toBraille[word]] = word
        else:
            toEnglish[toBraille[word]] = word
    
    if '.' in words[0]:
        print(brailleToEnglish(words[0]))
    else:
        print(englishToBraille(words))

if __name__ == '__main__':
    main()
