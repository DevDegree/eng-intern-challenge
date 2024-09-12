import sys


engToBrailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
}

numToBrailleMap = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..',
}

brailToEngMap = {value: key for key, value in engToBrailleMap.items()}
brailToNumMap = {value: key for key, value in numToBrailleMap.items()}

capitalFollows = '.....O'
numberFollows = '.O.OOO'
space = '......'


def isBraille(input : str):
    # braille comes in packs of six chars !!
    if len(input) % 6 != 0: return False
    # 
    for ch in input:
        if ch != 'O' and  ch!='.': return False
    return True


def brailleToEng(input : str):
    # take chars 6 by 6 -> if its capitalFollows capitalize the next char, 
    # else if its numberFollows take all the chars as number until next space
    eng=[]
    i = 0
    shouldCapitalize = False
    shouldParseAsNum = False
    while i < len(input):
        ch = input[i:i+6]
        if ch == capitalFollows:
            shouldCapitalize = True
        elif ch == numberFollows:
            shouldParseAsNum = True
        elif ch==space:
            # TODO: should i make shouldCapitalize false too ?
            shouldParseAsNum = False # end parsing numbers
            eng.append(' ')
        else:
            if shouldParseAsNum:
                if ch in brailToNumMap:
                    eng.append(brailToNumMap.get(ch))
                else:
                    # TODO: throw exception
                    print('wrong input, expected number at index', i, '  character= ', ch)
                    return
            else:
                if ch in brailToEngMap:
                    letter=brailToEngMap.get(ch)
                    if shouldCapitalize:
                        letter = letter.upper()
                        shouldCapitalize = False
                    eng.append(letter)
                else:
                    # TODO: throw exception
                    print('wrong input, unknown character at index', i, '  character= ', ch)
                    return
        i+=6
    return ''.join(eng)




def engToBraille(input : str):
    braille=[]
    i = 0
    hasAlreadyInsertedNumFollowsChar = False
    while i < len(input):
        ch = input[i]
        if ch == ' ':
            isParsingNumber = False
            braille.append(space)
        elif ch.isdigit():
            if isParsingNumber == False:
                braille.append(numberFollows)
                isParsingNumber = True
            braille.append(numToBrailleMap.get(ch))
        elif ch.isalpha():
            if ch.isupper():
                braille.append(capitalFollows)
            
            braille.append(engToBrailleMap.get(ch.lower()))
        else:
            print('wrong input, unknown character at index', i, '  character= ', ch)
            return
        i=i+1
    return ''.join(braille)

        




def main():
    if len(sys.argv) <= 1:
        print("must pass either a braille or english text as an argument")
        sys.exit(1)

    # get the bash command argument
    input = ' '.join(sys.argv[1:]).strip()

    if isBraille(input):
        print(brailleToEng(input))
    else:
        print(engToBraille(input))

if __name__ == '__main__':
    main()