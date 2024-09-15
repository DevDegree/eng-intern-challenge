import sys

def main(txt):
    brl_map = brl_dict()
    
    if is_brl(txt):
        print(to_eng(txt, brl_map))
    else:
        print(to_brl(txt, brl_map))

def is_brl(s):
    return all(c in 'O.' for c in s)

def rev_map(b_map):
    return {v: k for k, v in b_map.items()}

def brl_dict():
    return {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', 'cap': '.....O', 'num': '.O.OOO', ' ': '......'
    }

def to_brl(txt, b_map):
    out = []
    nm = 0
    
    for ch in txt:
        if ch == ' ':
            out.append(b_map[' '])
            nm = 0
        elif ch.isdigit():
            if not nm:
                out.append(b_map['num'])
                nm = 1
            out.append(b_map['j'] if ch == '0' else b_map[chr(ord('a') + int(ch) - 1)])
        elif ch.isupper():
            out.append(b_map['cap'])
            out.append(b_map[ch.lower()])
            nm = 0
        else:
            out.append(b_map[ch])
            nm = 0
    
    return ''.join(out)

def to_eng(brl_txt, b_map):
    r_map = rev_map(b_map)
    out = []
    i = 0
    cap = 0
    nm = 0
    
    while i < len(brl_txt):
        sym = brl_txt[i:i+6]
        
        if sym == b_map['num']:
            nm = 1
        elif sym == b_map[' ']:
            out.append(' ')
            nm = 0
        elif sym == b_map['cap']:
            cap = 1
        elif nm:
            let = r_map[sym]
            out.append('0' if let == 'j' else str(ord(let) - ord('a') + 1))
        else:
            let = r_map[sym]
            out.append(let.upper() if cap else let)
            cap = 0
        
        i += 6
    
    return ''.join(out)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        txt = " ".join(sys.argv[1:])
        main(txt)
    else:
        print("give input str to translate")
