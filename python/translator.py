import sys

def main():
    if len(sys.argv) < 2:
        raise ValueError("Usage: python translator.py <argument>")

    alpha_to_braille = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
        'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
        's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO',
    }
    num_to_braille = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
        '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    }
    chr_to_braille = {
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
        '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
        ' ': '......', 'capital': '.....O', 'number': '.O.OOO',
    }

    braille_to_alpha = {v: k for k, v in alpha_to_braille.items()}
    braille_to_num = {v: k for k, v in num_to_braille.items()}
    braille_to_chr = {v: k for k, v in chr_to_braille.items()}

    all_brailles = set(braille_to_alpha) | set(braille_to_num) | set(braille_to_chr)

    input_str = ' '.join(sys.argv[1:])

    # check if the input_str is letters or braille. If braille, will return list of brailes.
    def is_braille(s):
        if len(s) % 6 == 0:
            brailles = [s[i:i + 6] for i in range(0, len(s), 6)]
            return brailles if all(b in all_brailles for b in brailles) else False
        return False

    braille_str = is_braille(input_str)

    output, is_num, is_capital = '', False, False

    if braille_str:
        for b in braille_str:
            if is_num and b in braille_to_num:
                output += braille_to_num.get(b, '')
            elif b in braille_to_alpha:
                output += braille_to_alpha[b].upper() if is_capital else braille_to_alpha[b]
                is_capital = False
            elif b in braille_to_chr:
                if braille_to_chr[b] == 'number':
                    is_num = True
                elif braille_to_chr[b] == 'capital':
                    is_capital = True
                else:
                    if braille_to_chr[b] == ' ':
                        is_num = False
                    output += braille_to_chr[b]
    else:
        for c in input_str:
            if c.isalpha():
                if c.isupper():
                    output += chr_to_braille['capital']
                    c = c.lower()
                output += alpha_to_braille[c]
            elif c.isnumeric():
                if not is_num:
                    output += chr_to_braille['number']
                    is_num = True
                output += num_to_braille[c]
            else:
                if c == ' ':
                    is_num = False
                output += chr_to_braille.get(c, '')

    print(output)

if __name__ == "__main__":
    main()