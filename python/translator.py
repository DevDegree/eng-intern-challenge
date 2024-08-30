import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',

    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    'caps': '.....O', 'num': '.O.OOO', 
    ' ': '......', '.': '..O.OO', ',': '..O...', '?': '..OO.O', '!': '..OOO.', ':': '..OO..',
    ';': 'O.OO..', '-': '....O.', '/': '.O..O.', '<': '.O..OO', '>': 'OO..O.', '(': '.O.OO.',
    ')': '.O.OOO' 
}

char_dict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z',

    '.....O': 'caps', '.O.OOO': ')', '......': ' ', '..O.OO': '.', '..O...': ',', '..OO.O': '?',
      '..OOO.': '!', '..OO..': ':', 'O.OO..': ';', '....O.': '-', '.O..O.': '/', '.O..OO': '<',
        'OO..O.': '>', '.O.OO.': '('
}

num_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}



def text_to_braille(text):
    braille_output = []
    num_flag = False

    for char in text:
        if char.isdigit():
            if not num_flag:
                braille_output.append(braille_dict['num'])
                num_flag = True
            braille_output.append(braille_dict[char])
        elif char.isalpha():
            if num_flag:
                braille_output.append('......')
                num_flag = False

            if char.isupper():
                braille_output.append(braille_dict['caps']) 
                char = char.lower()
            braille_output.append(braille_dict[char])
        elif char in braille_dict:
            braille_output.append(braille_dict[char])
            num_flag = False

    return ''.join(braille_output)



def braille_to_text(braille):
    text_output = []
    i = 0
    num_flag = False

    while i < len(braille):
        symbol = braille[i:i+6]

        if symbol == braille_dict['caps']:
            i += 6 
            next_symbol = braille[i:i+6]
            text_output.append(char_dict[next_symbol].upper())

        elif symbol == braille_dict['num']:
            num_flag = True 

        elif symbol in braille_dict.values():
            if char_dict[symbol] == ' ':
              num_flag = False
            if num_flag:
                text_output.append(num_dict[symbol])
            else:
                text_output.append(char_dict[symbol])
                

        i += 6
    return ''.join(text_output)


def main():
    text = ' '.join(sys.argv[1:])

    if all(c in 'Oo.' for c in text):
        print(braille_to_text(text))
    else: 
        print(text_to_braille(text))

if __name__ == "__main__":
    main()