import sys

# Mappings from character to braille
char_brl = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

# Mappings for special characters
spec_brl = {
    ',': '.O....', ';': '.OO...', ':': '.O.O..', '.': '.O.OO.', '!': '.OO.O.', 
    '?': '.OO..O', '-': '..O.O.', '/': '.O.O..', '(': '.O.O.O', ')': 'O..O.O', 
    '<': 'OO...O', '>': '..OO.O', 'cap': '.....O', 'num': '.O.OOO'
}

# Mappings for digits
dig_brl = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings for braille to character/digit
brl_char = {v: k for d in (char_brl, spec_brl) for k, v in d.items()}
brl_dig = {v: k for k, v in dig_brl.items()}

# Convert braille to English
def brl_to_eng(brl):
    res, idx, cap, num = [], 0, False, False
    while idx < len(brl):
        seg = brl[idx:idx+6]
        if seg == spec_brl['cap']:
            cap = True
        elif seg == spec_brl['num']:
            num = True
        elif seg in brl_char:
            ch = brl_char[seg]
            if num and seg in brl_dig:
                res.append(brl_dig[seg])
            else:
                if cap:
                    ch = ch.upper()
                    cap = False
                res.append(ch)
            if ch == ' ':
                num = False
        idx += 6
    return ''.join(res)

# Convert English to braille
def eng_to_brl(txt):
    res, num = [], False
    for ch in txt:
        if ch.isupper():
            res.append(spec_brl['cap'])
            ch = ch.lower()
        if ch.isdigit():
            if not num:
                res.append(spec_brl['num'])
                num = True
            res.append(dig_brl[ch])
        else:
            res.append(char_brl.get(ch, spec_brl.get(ch, '')))
            if ch == ' ':
                num = False
    return ''.join(res)

# Check if the input is braille
def is_brl(txt):
    return all(c in 'O.' for c in txt) and len(txt) % 6 == 0

# Convert between braille and English
def main():
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
        print(brl_to_eng(input_str) if is_brl(input_str) else eng_to_brl(input_str), end='')

if __name__ == "__main__":
    main()