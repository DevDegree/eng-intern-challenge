import sys

# Braille mappings
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'cap': '.....O', 'num': '.O.OOO',
    '0': '.OOOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
}

inverse_braille_map = {v: k for k, v in braille_map.items() if k not in ['cap', 'num']}

def is_braille(s):
    return all(c in 'O.' for c in s)

def split_braille(s):
    return [s[i:i+6] for i in range(0, len(s), 6)]

def braille_to_text(braille_str):
    tokens = split_braille(braille_str)
    result = ''
    i = 0
    cap_next = False
    num_mode = False
    while i < len(tokens):
        token = tokens[i]
        if token == braille_map['cap']:
            cap_next = True
            i += 1
            continue
        elif token == braille_map['num']:
            num_mode = True
            i += 1
            continue
        char = inverse_braille_map.get(token, '')
        if num_mode:
            if char.isdigit():
                result += char
            else:
                num_mode = False
                result += char
        else:
            if cap_next:
                result += char.upper()
                cap_next = False
            else:
                result += char
        i += 1
    return result

def text_to_braille(text):
    result = ''
    num_mode = False
    for char in text:
        if char.isupper():
            result += braille_map['cap']
            result += braille_map[char.lower()]
        elif char.isdigit():
            if not num_mode:
                result += braille_map['num']
                num_mode = True
            result += braille_map[char]
        else:
            if num_mode:
                num_mode = False
            result += braille_map.get(char, '')
    return result

def main():
    input_str = ' '.join(sys.argv[1:])
    if is_braille(input_str.replace(' ', '')):
        print(braille_to_text(input_str))
    else:
        print(text_to_braille(input_str))

if __name__ == '__main__':
    main()
