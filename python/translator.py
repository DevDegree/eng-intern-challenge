import sys

eng_to_braille = {
    'a':'O.....', 'b':'O.O...', 'c':'OO....', 'd':'OO.O..',
    'e':'O..O..', 'f':'OOO...', 'g':'OOOO..', 'h':'O.OO..',
    'i':'.OO...', 'j':'.OOO..', 'k':'O...O.', 'l':'O.O.O.',
    'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.', 'p':'OOO.O.',
    'q':'OOOOO.', 'r':'O.OOO.', 's':'.OO.O.', 't':'.OOOO.',
    'u':'O...OO', 'v':'O.O.OO', 'w':'.OOO.O', 'x':'OO..OO',
    'y':'OO.OOO', 'z':'O..OOO',
    ' ':'......'
}

num_to_braille = {
    '1':'O.....', '2':'O.O...', '3':'OO....', '4':'OO.O..',
    '5':'O..O..', '6':'OOO...', '7':'OOOO..', '8':'O.OO..',
    '9':'.OO...', '0':'.OOO..',
    '.':'..OO.O', ',':'..O...', '?':'..O.OO', '!':'..OOO.',
    ':':'..OO..', ';':'..O.O.', '-':'....OO', '/':'.O..O.',
    '<':'.OO..O', '>':'O..OO.', '(':'O.O..O', ')':'.O.OO.'
}

braille_space = '......'
capital_follows = '.....O'
decimal_follows = '.O...O'
number_follows = '.O.OOO'

def translator(args):
    user_input = ' '.join(args[1:])
    input_char_set = set(user_input)

    if  not ('O' in input_char_set \
        and '.' in input_char_set \
        and len(input_char_set)==2):

        eng_sep = list(user_input)
        eng_bra_phrase = []
        num_mode = False
        for e in eng_sep:
            if e.isdigit():
                if not num_mode:
                    eng_bra_phrase.append(number_follows)
                    num_mode = True
                eng_bra_phrase.append(num_to_braille[e])
            else:
                if e.isupper():
                    eng_bra_phrase.append(capital_follows)
                eng_bra_phrase.append(eng_to_braille[e.lower()])

        print (''.join(eng_bra_phrase))

    else:
        braille_to_char = {v:k for k,v in eng_to_braille.items()}
        braille_to_num = {v:k for k,v in num_to_braille.items()}

        braille_separated = [user_input[i:i+6] for i in range(0, len(user_input), 6)]
        res = []
        idx = 0
        while idx < len(braille_separated):
            if braille_separated[idx] == number_follows:
                while braille_separated[idx] != braille_space and idx < len(braille_separated):
                    res.append(braille_to_num[braille_separated[idx]])
                    i += 1
            elif braille_separated[idx] == capital_follows:
                res.append(braille_to_char[braille_separated[idx+1]])
                i += 2
            else:
                res.append(braille_to_char[braille_separated[idx]])
                i += 1

        print(''.join(res))



if __name__ == "__main__":
    translator(sys.argv)
