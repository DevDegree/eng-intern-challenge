import sys

eng_to_braille = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
                  'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
                  'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 
                  'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
                  'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
                  'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
                  's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
                  'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
                  'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 
                  '.': '..O.OO', ',': '..O...', '!': '..OO.O',
                  '?': '..O.O.', ':': '...OOO', ';': '...O.O', 
                  '(': '...OO.', ')': '.OOO.O'}

num_to_braille = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', 
                  '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
                  '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
                  '0': '.OOO..'}

braille_to_eng = dict((b, e) for e, b in eng_to_braille.items())
braille_to_num = dict((b, e) for e, b in num_to_braille.items())

capital_follows = '.....O'
number_follows = '.O.OOO'


def english_to_braille(input):
    """Translate english to braille."""
    eng_chars = list(input)
    braille_output = ''
    prev_num_flag = False

    for i in eng_chars:
        if i.isupper():
            braille_output += capital_follows + eng_to_braille[i.lower()]
        elif i.isnumeric():
            if not prev_num_flag:
                prev_num_flag = True
                braille_output += number_follows + num_to_braille[i]
            else:
                braille_output += num_to_braille[i]
        else:
            braille_output += eng_to_braille[i]

    return(braille_output)


def braille_to_english(input):
    """Translate braille to english."""
    n = 6 # number of braille dots per character
    braille_chars = [input[i:i+n] for i in range(0, len(input), n)]
    output = ''
    capital_flag = False
    num_flag = False
    
    for i in braille_chars:
        # check for capitals, numbers, and spaces:
        if i == capital_follows:
            capital_flag = True
        elif i == number_follows:
            num_flag = True
        elif i == eng_to_braille[" "]:
            num_flag = False
            output += braille_to_eng[i]
        else:
            if capital_flag:
                output += braille_to_eng[i].upper()
                capital_flag = False
            elif num_flag:
                output += braille_to_num[i]
            else:
                output += braille_to_eng[i]
    
    return output


def main():
    input = ' '.join(sys.argv[1:]).strip()

    try:
        # determine whether the input is braille or english:
        if set(input).issubset(set('O.')) & (len(input) % 6 == 0):
            # note: assumes english if only braille symbols are used but is 
            #       incomplete i.e. if not divisible by 6.
            output = braille_to_english(input)
        else:
            output = english_to_braille(input)
    except Exception as inst:
        print(inst)

    print(output)


if __name__ == "__main__":
    main()