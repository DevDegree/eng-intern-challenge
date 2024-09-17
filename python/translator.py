import sys

def main():
    is_braille = True
    if len(sys.argv) == 1:
        return ''
    else:
        s = ' '.join(sys.argv[1:])
        is_braille = check_is_braille(s)
    
    output = ''
    if is_braille:
        output = to_text(s)
    else:
        output = to_braille(s)
      
    print(output)
        
def check_is_braille(s):
    if (len(s) % 6 != 0):
        return False
    if (not set(s).issubset({'O', '.'})):
        return False
    for i in range(0, len(s), 6):
        if (s[i:i+6] not in to_text_dict().keys()):
            return False
    
    return True
    
def to_braille(s):
    dict = to_braille_dict()
    braille = ''
    nums = {'1','2','3','4','5','6','7','8','9','0'}
    num = False
    for i in s:
        if (i.lower() not in dict.keys()):
            return ''
        elif (i.isupper()):
            braille += dict['capital_follows']
            braille += dict[i.lower()]
        elif (i in nums):
            if (not num):
                braille += dict['number_follows']
                num = True
            braille += dict[i]
        else:
            braille += dict[i]
            
        if (i == ' '):
            num = False
            
    return braille

def to_text(s):
    dict = to_text_dict()
    ol = overlap()
    text = ''
    caps = False
    num = False
    for i in range(0, len(s), 6):
        curr = s[i:i+6]
        if (dict[curr] == 'capital_follows'):
            caps = True
        elif (dict[curr] == 'number_follows'):
            num = True
        elif (caps):
            if (dict[curr] in {'1','2','3','4','5','6','7','8','9','0'}):
                text += ol[dict[curr]].upper()
            else: text += dict[curr].upper()
            caps = False
        elif (num):
            text += dict[curr]
        else:
            if (dict[curr] == ' '):
                num = False
            if (dict[curr] in {'1','2','3','4','5','6','7','8','9','0'}):
                text += ol[dict[curr]]
            else: text += dict[curr]
            
    return text
            
def to_braille_dict():
    text_to_braille = {}
    text_to_braille['a'] = 'O.....'
    text_to_braille['b'] = 'O.O...'
    text_to_braille['c'] = 'OO....'
    text_to_braille['d'] = 'OO.O..'
    text_to_braille['e'] = 'O..O..'
    text_to_braille['f'] = 'OOO...'
    text_to_braille['g'] = 'OOOO..'
    text_to_braille['h'] = 'O.OO..'
    text_to_braille['i'] = '.OO...'
    text_to_braille['j'] = '.OOO..'
    text_to_braille['k'] = 'O...O.'
    text_to_braille['l'] = 'O.O.O.'
    text_to_braille['m'] = 'OO..O.'
    text_to_braille['n'] = 'OO.OO.'
    text_to_braille['o'] = 'O..OO.'
    text_to_braille['p'] = 'OOO.O.'
    text_to_braille['q'] = 'OOOOO.'
    text_to_braille['r'] = 'O.OOO.'
    text_to_braille['s'] = '.OO.O.'
    text_to_braille['t'] = '.OOOO.'
    text_to_braille['u'] = 'O...OO'
    text_to_braille['v'] = 'O.O.OO'
    text_to_braille['w'] = '.OOOOO'
    text_to_braille['x'] = 'OO..OO'
    text_to_braille['y'] = 'OO.OOO'
    text_to_braille['z'] = 'O..OOO'
    text_to_braille['1'] = 'O.....'
    text_to_braille['2'] = 'O.O...'
    text_to_braille['3'] = 'OO....'
    text_to_braille['4'] = 'OO.O..'
    text_to_braille['5'] = 'O..O..'
    text_to_braille['6'] = 'OOO...'
    text_to_braille['7'] = 'OOOO..'
    text_to_braille['8'] = 'O.OO..'
    text_to_braille['9'] = '.OO...'
    text_to_braille['0'] = '.OOO..'
    text_to_braille['capital_follows'] = '.....O'
    text_to_braille['decimal_follows'] = '.O...O'
    text_to_braille['number_follows'] = '.O.OOO'
    text_to_braille['.'] = '..OO.O'
    text_to_braille[','] = '..O...'
    text_to_braille['?'] = '..O.OO'
    text_to_braille['!'] = '..OOO.'
    text_to_braille[':'] = '..OO..'
    text_to_braille[';'] = '..O.O.'
    text_to_braille['-'] = '....OO'
    text_to_braille['/'] = '.O..O.'
    text_to_braille['<'] = '.OO..O'
    text_to_braille['>'] = 'O..OO.'
    text_to_braille['('] = 'O.O..O'
    text_to_braille[')'] = '.O.OO.'
    text_to_braille[' '] = '......'

    return text_to_braille

def to_text_dict():
    tbd = to_braille_dict()
    braille_to_text = {}
    for key in tbd.keys():
        braille_to_text[tbd[key]] = key
        
    return braille_to_text

def overlap_dict():
    d = {}
    d['a'] = '1'
    d['b'] = '2'
    d['c'] = '3'
    d['d'] = '4'
    d['e'] = '5'
    d['f'] = '6'
    d['g'] = '7'
    d['h'] = '8'
    d['i'] = '9'
    d['j'] = '0'
    return d

def overlap():
    d = {}
    d['1'] = 'a'
    d['2'] = 'b'
    d['3'] = 'c'
    d['4'] = 'd'
    d['5'] = 'e'
    d['6'] = 'f'
    d['7'] = 'g'
    d['8'] = 'h'
    d['9'] = 'i'
    d['0'] = 'j'
    return d

    
if __name__ == "__main__":
    main()