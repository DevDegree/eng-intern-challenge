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


print((word_to_brail('Abc 123 xYz')))
# for index, char in enumerate(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"):
#     print(char, end="")
#     if index != 0 and (index+1)%6 == 0:
#         print()