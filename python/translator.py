alphabet_translation = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',

    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

brail_to_nums={
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

baril_to_alphabet= {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'v', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z', '.OOO.O': 'w'
}



def word_to_brail(str):
    word=[]
    state = 'alph'
    str.strip()
    for char in str:
        if char == ' ':
            word.append("......")
            continue
        if char.isdigit() and state!='num':
            word.append('.O.OOO')
            state = 'num'
        
        elif char.isalpha():
            if state!='alpha':
                state = "alpha"
            
            if char.isupper():
                word.append(".....O")
        word.append(alphabet_translation[char.lower()])

    return ''.join(word)

def brail_to_word(str):
    word=[]
    state = 'alph'
    cells = [str[i:i + 6] for i in range(0, len(str), 6)]
    nextUpper = False

    for cell in cells:
        if cell == '......':
            word.append(" ")
            continue
        if state == 'alph':
            if cell == '.O.OOO':
                state = 'num'
                continue
            elif cell == '.....O':
                nextUpper = True
                continue
            else:
                if nextUpper:
                    word.append(baril_to_alphabet[cell].upper())
                    nextUpper=False
                else:
                    word.append(baril_to_alphabet[cell])
        else:
             word.append(brail_to_nums[cell])
            
    return ''.join(word)

