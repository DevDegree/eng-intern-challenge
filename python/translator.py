# SOROUSH MOUSSAVI
# APBTMLG

import sys

def parse_eng(table, str):

    ret = ''

    # CONVERT ENGLISH CHARACTERS TO BRAILLE 
    for i in range(len(str)):
        if i > 0: 
            # IDENTIFY DECIMAL POINTS (PERIODS WHERE THERE IS A NUMBER RIGHT AFTER)
            if i < len(str)-1:
                if str[i] == '.' and str[i+1].isnumeric():
                    ret += tobr(table, 'decpt', not (str[i-1].isnumeric() or str[i-1] == '.'))
                    continue
                
            # ADD TO THE TRANSLATED STRING THE BRAILLE CONVERSION
            ret += tobr(table, str[i], str[i].isnumeric() and not (str[i-1].isnumeric() or str[i-1] == '.'))
        
        else:
            # IDENTIFY DECIMAL POINTS (PERIODS WHERE THERE IS A NUMBER RIGHT AFTER)
            if len(str) != 1:
                if str[0] == '.' and str[1].isnumeric():
                    ret += tobr(table, 'decpt', True)
                    continue

            ret += tobr(table, str[0], str[0].isnumeric())

    return ret

def parse_br(table, str):
    

    if len(str) % 6 != 0:
        print('ERROR -- STRING LENGTH MOD 6 MUST EQUAL 0')
        return
    
    ret = ''
    cap = False
    num = False

    # CONVERT BRAILLE CHARACTERS TO ENGLISH 
    for i in range(len(str)//6):

        # DIVIDE BRAILLE CHARACTERS INTO GROUPS OF SIX
        brch = str[6*i:6*(i+1)]

        # IDENTIFY CAP-FOLLOW AND NUM-FOLLOW BRAILLE CHARACTERS
        if brch == '.....O':
            cap = True
            continue
        if brch == '.O.OOO':
            num = True
            continue
        
        # ADD ONE OF THREE CHARACTERS -- A CAPITAL, NUMERICAL, OR DEFAULT
        if cap:
            ret += toeng(table,brch,True,False)
            cap = False
        
        elif num:
            ch = toeng(table,brch,False,True)
            if ch == '......':
                num = False
            if ch == 'decpt': ch = '.'
            ret += ch

        else: ret += toeng(table,brch,False,False)

    return ret
        
def tobr(table, ch, new_num):
    # CONVERT INDIVIDUAL ENGLISH CHARACTER TO BRAILLE
    return ('.....O' if ch.isupper() else ('.O.OOO' if new_num else '')) + table[ch.lower()]

def toeng(table, brch, capital, numeric):
    # CONVERT INDIVIDUAL BRAILLE CHARACTER TO ENGLISH
    for char, br in table.items():
        if br == brch:
            ch = char
            if not numeric: 
                if capital : ch = ch.upper()
                break
    return ch


def main():

    # ENGLISH-BRAILLE CONVERSION DICT
    table = {

        'a' : 'O.....', 'b' : 'O.O...', 'c' : 'OO....', 'd' : 'OO.O..',
        'e' : 'O..O..', 'f' : 'OOO...', 'g' : 'OOOO..', 'h' : 'O.OO..',
        'i' : '.OO...', 'j' : '.OOO..', 'k' : 'O...O.', 'l' : 'O.O.O.',
        'm' : 'OO..O.', 'n' : 'OO.OO.', 'o' : 'O..OO.', 'p' : 'OOO.O.',
        'q' : 'OOOOO.', 'r' : 'O.OOO.', 's' : '.OO.O.', 't' : '.OOOO.',
        'u' : 'O...OO', 'v' : 'O.O.OO', 'w' : '.OOO.O', 'x' : 'OO..OO',
        'y' : 'OO.OOO', 'z' : 'O..OOO',

        '1' : 'O.....', '2' : 'O.O...', '3' : 'OO....', '4' : 'OO.O..', '5' : 'O..O..', 
        '6' : 'OOO...', '7' : 'OOOO..', '8' : 'O.OO..', '9' : '.OO...', '0' : '.OOO..',
        'decpt' : '.O...O',

        '.' : '..OO.O', ',' : '..O...', '?' : '..O.OO',
        '.' : '..OOO.', ':' : '..OO..', ';' : '..O.O.',
        '-' : '....OO', '/' : '.O..O.', '<' : '.OO..O',
        '>' : 'O..OO.', '(' : 'O.O..O', ')' : '.O.OO.',

        ' ' : '......',

    }

    if len(sys.argv) < 2:
        print("ERROR -- EXPECTED AN ARGUMENT")
        return
    
    str = ' '.join(sys.argv[1:])

    # VERIFY ALL CHARACTERS ARE EITHER '.' or 'O' -- PARSE EITHER AS ENGLISH OR BRAILLE
    is_eng = False

    for char in str:
        if char != '.' and char != 'O':
            is_eng = True
            break
    
    if is_eng: print(parse_eng(table, str))
    else: print(parse_br(table, str))
        
if __name__ == '__main__':
    main()