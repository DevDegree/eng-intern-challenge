import sys
letter_to_braille = {'a':'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'}
charnum_to_braille = {'1':'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'}
text = ' '.join(sys.argv[1::])
result = ''
# Variables for english to braille
capital_follows = '.....O'
number_follows = '.O.OOO'
space_encountered = True

# Variables for braille to english
capitalize = False
number_next = False


is_Braille = False
if '.' in text:
    is_Braille = True

if not is_Braille:
    for ch in text:
        if ch.isupper():
            result += capital_follows + letter_to_braille[ch.lower()]

        elif ch.isdigit():
             if space_encountered is True:
                space_encountered = False
                result += number_follows
             result += charnum_to_braille[ch]

        else:
            if ch  == ' ':
                space_encountered = True       
            result += letter_to_braille[ch]

else:
    curr_ch = text[:6]
    text = text[6::]


    while curr_ch:
        if curr_ch == capital_follows:
            capitalize = True
            curr_ch = text[:6]
            text = text[6::]
        elif curr_ch == number_follows:
            number_next == True
            curr_ch = text[:6]
            text = text[6::]
        
        if capitalize:
            result += list(letter_to_braille.keys())[list(letter_to_braille.values()).index(curr_ch)].capitalize()
            curr_ch = text[:6]
            text = text[6::]
            capitalize = False
        
        elif number_next:
            result += list(charnum_to_braille.keys())[list(charnum_to_braille.values()).index(curr_ch)]
            curr_ch = text[:6]
            text = text[6::]
        else:
            if curr_ch == '......':
                number_next = False
            result += list(letter_to_braille.keys())[list(letter_to_braille.values()).index(curr_ch)]
            curr_ch = text[:6]
            text = text[6::]

sys.stdout.write(result)
