import sys
#define braille dictonary.
change_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....',
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....',
    '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'cap': '.....O', 'num': '.O.OOO', ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '...OOO',
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '<': '.OO..O',
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
}
#define english dictonary.
change_english = {v: k for k, v in change_braille.items()}
def e_b(input):
    output = ''
    num = False
    for c in input:
        if num:
            if c == ' ': 
                num = False
        elif c.isdigit():
            output += change_braille['num']
            num = True
        elif c.isupper():
            output += change_braille['cap']
            c = c.lower()
        output += change_braille[c]
    return output
def b_e(input):
    output = ''
    cap = False
    num = False

    chut = [input[i:i+6] for i in range(0, len(input), 6)]
    
    for c in chut:
        if change_english[c] == 'cap':
            cap = True
            continue
        if change_english[c] == 'num':
            num = True
            continue
        
        if num:
            output += change_english[c]
            if change_english[c] == ' ':
                num = False
        else:
            jay = change_english[c]
            if jay < 'A' and jay != ' ': 
                jay = chr(ord(jay) + 48) if jay != '0' else 'j'
            if cap:
                output += jay.upper()
                cap = False
            else:
                output += jay
    return output

if __name__ == "__main__":
    answer = ''
    for i in range(1, len(sys.argv)):
        input = sys.argv[i]
        if '.' in input: # check what input is.
            if i > 1: # Add space between words
                answer += ' '
            answer += b_e(input)
        else:
            if i > 1: # Add space between words
                answer += '......'
            answer += e_b(input)
    print(answer)

#written by jay patel
