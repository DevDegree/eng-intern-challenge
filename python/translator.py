import sys


dict_bra_to_num = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}

dict_bra_to_other = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' ',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    # 'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')'
}

dict_eng_to_bra = {
    '1' : 'O.....',
    '2' : 'O.O...',
    '3' : 'OO....',
    '4' : 'OO.O..',
    '5' : 'O..O..',
    '6' : 'OOO...',
    '7' : 'OOOO..',
    '8' : 'O.OO..',
    '9' : '.OO...',
    '0' : '.OOO..',
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : 'O.O.O.',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO',
    ' ' : '......',
    '.' : '..OO.O',
    ',' : '..O...',
    '?' : '..O.OO',
    '!' : '..OOO.',
    ':' : '..OO..',
    ';' : '..O.O.',
    '-' : '....OO',
    '/' : '.O..O.',
    '(' : 'O.O..O',
    ')' : '.O.OO.'
}


def translator(lst):
    trans_res = ''
    lst_index = 0
    while lst_index < len(lst):
        # try to determine OOOOOO or ...... is Braille or English
        is_bra = True if len(lst[lst_index]) % 6 == 0 else False  # Check if the lst[lst_index] is in the format of Braille 
        if is_bra:
            for ch in lst[lst_index]:
                if ch != '.' and ch != 'O':
                    is_bra = False
                    break
        if is_bra:
            index = 0
            next_capital = False
            next_num = False
            while index < len(lst[lst_index]):
                next_bra_word = ''
                for i in range(6):
                    next_bra_word += lst[lst_index][index+i]
                if next_bra_word == '.....O':
                    next_capital = True
                elif next_bra_word == '.O.OOO':
                    next_num = True
                else:
                    if next_capital:
                        trans_res += dict_bra_to_other[next_bra_word].upper()
                        next_capital = False
                    elif next_num:
                        if next_bra_word == '......':
                            trans_res += ' '
                            next_num = False
                        elif next_bra_word == '.O...O' or next_bra_word == '..OO.O':
                            trans_res += '.'
                        elif next_bra_word in dict_bra_to_num:
                            trans_res += dict_bra_to_num[next_bra_word]
                        else:
                            next_num = False
                            continue
                    else:
                        trans_res += dict_bra_to_other[next_bra_word]
                index += 6
            if lst_index < len(lst) - 1:
                trans_res += ' '
        else:
            index = 0
            while index < len(lst[lst_index]):
                if lst[lst_index][index].isalpha() and lst[lst_index][index].isupper():
                    trans_res += '.....O'
                    trans_res += dict_eng_to_bra[lst[lst_index][index].lower()]
                elif '0' <= lst[lst_index][index] <= '9':
                    trans_res += '.O.OOO'
                    while index < len(lst[lst_index]) and ('0' <= lst[lst_index][index] <= '9' or lst[lst_index][index] == '.'):
                        if lst[lst_index][index] == '.':
                            trans_res += '.O...O'
                        else:
                            trans_res += dict_eng_to_bra[lst[lst_index][index]]
                        index += 1
                    if index >= len(lst[lst_index]):
                        break
                    else:
                        trans_res += '......'
                        index -= 1
                else:
                    trans_res += dict_eng_to_bra[lst[lst_index][index]]
                index += 1
            if lst_index < len(lst) - 1:
                trans_res += '......'
                    
        lst_index += 1
                    
    return trans_res
    
if __name__ == '__main__':
    output = translator(sys.argv[1:])
    print(output)
