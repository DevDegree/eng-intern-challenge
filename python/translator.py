import sys

if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    allowed_chars = {'.', 'O'}

    has_dot = '.' in input_string
    has_O = 'O' in input_string

    if has_dot and has_O:
        type = "Braille"
    else:
        type = "Alphanumeric"

    final_string = ""

    char_map = {
        'A': '.....OO.....',
        'B': '.....OO.O...',
        'C': '.....OOO....',
        'D': '.....OOO.O..',
        'E': '.....OO..O..',
        'F': '.....OOOO...',
        'G': '.....OOOOO..',
        'H': '.....OO.OO..',
        'I': '.....O.OO...',
        'J': '.....O.OOO..',
        'K': '.....OO...O.',
        'L': '.....OO.O.O.',
        'M': '.....OOO..O.',
        'N': '.....OOO.OO.',
        'O': '.....OO..OO.',
        'P': '.....OOOO.O.',
        'Q': '.....OOOOOO.',
        'R': '.....OO.OOO.',
        'S': '.....O.OO.O.',
        'T': '.....O.OOOO.',
        'U': '.....OO...OO',
        'V': '.....OO.O.OO',
        'W': '.....O.OOO.O',
        'X': '.....OOO..OO',
        'Y': '.....OOO.OOO',
        'Z': '.....OO..OOO',
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': '.OO...',
        'j': '.OOO..',
        'k': 'O...O.',
        'l': 'O.O.O.',
        'm': 'OO..O.',
        'n': 'OO.OO.',
        'o': 'O..OO.',
        'p': 'OOO.O.',
        'q': 'OOOOO.',
        'r': 'O.OOO.',
        's': '.OO.O.',
        't': '.OOOO.',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO',
        '0': '.O.OOO.000..',
        '1': '.O.OOOO.....',
        '2': '.O.OOOO.O...',
        '3': '.O.OOOOO....',
        '4': '.O.OOOOO.O..',
        '5': '.O.OOOO..O..',
        '6': '.O.OOOOOO...',
        '7': '.O.OOOOOOO..',
        '8': '.O.OOOO.OO..',
        '9': '.O.OOO.OO...',
        ',': '..O...',
        '?': '..O.OO',
        '!': '..OOO.',
        ':': '..OO..',
        ';': '..O.O.',
        '-': '....OO',
        '/': '.O..O.',
        '<': '.O....O.O..O',
        '>': '.O.....O.OO.',
        '(': 'O.O..O',
        ')': '.O.OO.',
        ' ': '......',
        '.': '..OO.O'
    }

    reverse_char_map = {v: k for k, v in char_map.items()}

    if type == "Alphanumeric":
        prev_char = ''
        for char in input_string:
            if(prev_char.isnumeric() & char.isnumeric()):
                mapped_char = char_map.get(char, '')
                final_string += mapped_char[6:]
            else:
                mapped_char = char_map.get(char, '')
                final_string += mapped_char

            prev_char = char

        print(final_string)

    else:
        final_string = ""
        flag_capital=0
        flag_digit=0
        flag_decimal=0
        flag_grtr_less=0

        for i in range(0, len(input_string), 6):
            braille_char = input_string[i:i+6]
            if braille_char == '......':
                flag_digit = 0

            if flag_capital==1:
                braille_char = '.....O'+braille_char
                flag_capital=0
                flag_digit = 0

            if flag_digit==1:
                braille_char = '.O.OOO'+braille_char


            if flag_decimal==1:
                braille_char = '.O...O'+braille_char
                flag_decimal=0

            if flag_grtr_less==1:
                braille_char = '.O....'+braille_char
                flag_grtr_less=0


            mapped_char = reverse_char_map.get(braille_char, '')
            # print(mapped_char)

            if(braille_char == '.....O'):
                flag_capital=1
                continue
            if(braille_char == '.O.OOO'):
                flag_digit=1
                continue
            if(braille_char == '.O...O'):
                flag_decimal=1
                continue
            if(braille_char == '.O....'):
                flag_grtr_less=1
                continue

            final_string += mapped_char

        print(final_string)
