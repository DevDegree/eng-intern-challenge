import sys

def eng2bra(eng_str):
    #translates an english string to braille
    bra_list = []
    num_seen = False
    BRA_DICT = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
        'z': 'O..OOO', 'CAPITAL': '.....O', 'NUMBER': '.O.OOO', '1': 'O.....', 
        '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
        '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', ' ': '......'
    }

    for char in eng_str:

        if char.isdigit():
            if not num_seen:
                num_seen = True
                bra_list.append(BRA_DICT['NUMBER'])
        elif char == ' ':
            num_seen = False
        # A number sequence was not ended with a space
        elif num_seen:
            return ''
        elif char.isupper():
                bra_list.append(BRA_DICT['CAPITAL'])
                char = char.lower()

        bra_list.append(BRA_DICT[char])
    
    return "".join(bra_list)

def bra2eng(bra_str):
    #split the bra_str into bra_list
    eng_list = []
    bra_list = [bra_str[i:i+6] for i in range(0, len(bra_str), 6)]
    BRA2ENG = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '.....O': 'CAPITAL', '.O.OOO': 'NUMBER', '......': ' '
    }

    BRA2NUM = {
        'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 
        'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
    }

    #iterate through bra_list
    num_follow = False
    capital_follow = False

    for bra_char in bra_list:
        #check if char is num follow
        eng_char = BRA2ENG[bra_char]

        # We assume the next character can only be a number or a space
        if num_follow and eng_char != ' ' and bra_char not in BRA2NUM:
            return ''

        # We assume the next character can only be a letter
        if capital_follow and eng_char in {'CAPITAL', ' ', 'NUMBER'}:
            return ''

        if eng_char == 'NUMBER': 
            num_follow = True
        elif eng_char == 'CAPITAL':
            capital_follow = True
        elif eng_char == ' ':
            num_follow = False
            eng_list.append(' ')
        else:
            if num_follow:
                eng_list.append(BRA2NUM[bra_char])
            else:
                if capital_follow:
                    capital_follow = False
                    eng_char = eng_char.upper()

                eng_list.append(eng_char)
    
    return ''.join(eng_list)

def main():
    if len(sys.argv) == 1:
        return

    arg = ' '.join(sys.argv[1:])
    #check if it is braille by looking at the first 6 digits of the first arg. if it contains a ., it is braille. Otherwise, it is english

    if len(arg) < 6:
        # it is english
        print(eng2bra(arg))
    else:
        for i in range(6):
            if arg[i] == '.':
                # it is braille
                print(bra2eng(arg))
                return

        #it is english
        print(eng2bra(arg))

main()