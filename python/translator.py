import sys

def translator(input):
    unique = set(input)
    check = set()
    check.add('O')
    check.add('.')
    braille = ''
    if unique == check and len(input) % 6 == 0:
        braille = input
    if braille:
        return brailleToEnglish(input)
    return englishToBraille(input)


def englishToBraille(input):
    charToBrl= {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'o': 'O..OO.', ' ': '......', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', 'r': 'O.OOO.'}
    numToBrl = {
        '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'}
    capitalFollows = '.....O'
    numberFollows = '.O.OOO'
    
    res = ''
    enterNumber = False

    for i in input:
        if not i.isdigit() and enterNumber:
            enterNumber = False
            if i.isupper():
                res += capitalFollows
                res += charToBrl[i.lower()]
            else:
                res += charToBrl[i]
            continue
        if enterNumber:
            res +=numToBrl[i]
            continue

        if i.isdigit() and not enterNumber:
            enterNumber = True
            res += numberFollows
            res +=numToBrl[i]
            continue

        if i.isupper():
            res += capitalFollows
            res += charToBrl[i.lower()]
        else:
            res += charToBrl[i]
    return res

def brailleToEnglish(input):
    i = 0
    s = ''
    res = []
    # Using sliding window technique to get each braille representation of length 6
    for j in range(len(input)):
        s += input[j]
        if j - i + 1 == 6:
            # store each one in res list
            res.append(s)
            s = ''
            i = j+1
    # Using two dictionary to store to map braille to english and vice-versa
    map = ({'O.....':'a','O.O...':'b','OO....':'c','OO.O..':'d','O..O..':'e','OOO...':'f','OOOO..':'g','O.OO..':'h','.OO...':'i','.OOO..':'j',
        'O...O.':'k','O.O.O.':'l','OO..O.':'m','OO.OO.':'n', 'OOO.O.':'p','OOOOO.':'q','.OO.O.':'s','.OOOO.':'t','O...OO':'u','O.O.OO':'v',
        'O..OO.':'o','......':' ','.OOO.O':'w','OO..OO':'x','OO.OOO':'y','O..OOO':'z','O.OOO.':'r'})
    mapInteger = {'.OOO..':'0','O.....':'1','O.O...':'2' ,'OO....':'3','OO.O..':'4','O..O..':'5','OOO...':'6','OOOO..':'7','O.OO..':'8','.OO...':'9'}
    answer = ''
    enterCapital = False
    capitalFollows = '.....O'
    numberFollows = '.O.OOO'
    enterNumber = False
    space = '......'
    for i in res:
        if i == space and enterNumber:
            enterNumber = False
            answer += map[i]
            continue
        if i == numberFollows:
            enterNumber = True
            continue
        if enterNumber:
            answer += mapInteger[i]
            continue
        if i == capitalFollows:
            enterCapital = True
            continue
        if enterCapital:
            answer += map[i].upper()
            enterCapital = False
        else:
            answer += map[i]
    return answer


if __name__ == "__main__":
    args = sys.argv[1:]
    input_string = ' '.join(args)
    print(translator(input_string))