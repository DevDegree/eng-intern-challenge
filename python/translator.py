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
    """
    This function takes str input as english letters and/or numbers to translate
    to braille characters and vice versa.
    """

    user_input = ' '.join(args[1:])
    input_char_set = set(user_input)

    # Input as English letters and/or numbers.
    if  not ('O' in input_char_set \
        and '.' in input_char_set \
        and len(input_char_set)==2):

        eng_sep = list(user_input)
        eng_bra_phrase = []
        num_mode = False
        for e in eng_sep:
            # Input is number.
            if e.isdigit():
                # Add number signifier to the beginning of the block of numbers.
                if not num_mode:
                    eng_bra_phrase.append(number_follows)
                    num_mode = True
                # Translate number to braille.
                eng_bra_phrase.append(num_to_braille[e])
            # Input is text.
            else:
                # Add capital signifier if the letter is capital.
                if e.isupper():
                    eng_bra_phrase.append(capital_follows)
                # Translate letter to braille.
                eng_bra_phrase.append(eng_to_braille[e.lower()])

        print (''.join(eng_bra_phrase))

    # Input as braille.
    else:

        braille_to_char = {v:k for k,v in eng_to_braille.items()}
        braille_to_num = {v:k for k,v in num_to_braille.items()}

        # Separate the braille input text into six character blocks to read the
        # letters/numbers individually.
        braille_separated = [user_input[i:i+6] for i in range(0, len(user_input), 6)]
        res = []
        idx = 0
        while idx < len(braille_separated):
            # Detect braille number signifier.
            if braille_separated[idx] == number_follows:
                while braille_separated[idx] != braille_space and idx < len(braille_separated):
                    res.append(braille_to_num[braille_separated[idx]])
                    i += 1
            # Detect braille capital signifier.
            elif braille_separated[idx] == capital_follows:
                res.append(braille_to_char[braille_separated[idx+1]])
                i += 2
            # Translate from braille to English letter/number.
            else:
                res.append(braille_to_char[braille_separated[idx]])
                i += 1

        print(''.join(res))



if __name__ == "__main__":
    translator(sys.argv)
