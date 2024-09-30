import sys

def trans_eng_to_bra(input_string):
    bra_trans = ''
    alpha_mode = True
    
    for letter in input_string:
        if letter.isupper():
            if alpha_mode:
            # Handle uppercase letters
                full_trans = ENGLISH2BRAILLE['capital_follows'] + ENGLISH2BRAILLE[letter.lower()]
            else:
                full_trans = ENGLISH2BRAILLE['capital_follows'] + ENGLISH2BRAILLE[letter.lower()]
                alpha_mode = True
            bra_trans += full_trans
        elif letter.isdigit():
            if alpha_mode:
            # Handle numbers
                full_trans = ENGLISH2BRAILLE["number_follows"]+NUMBERS2BRAILLE[letter]
                alpha_mode = False
            else:
                full_trans = NUMBERS2BRAILLE[letter]
            bra_trans += full_trans
        elif letter == ' ':
            # Handle spaces
            bra_trans += ENGLISH2BRAILLE[' ']
        else:
            if alpha_mode:
                full_trans = ENGLISH2BRAILLE[letter]
            else:
                full_trans = ENGLISH2BRAILLE[letter]
                alpha_mode = True

            bra_trans += full_trans
    return bra_trans

def trans_bra_to_eng(input_string):
    eng_trans = ''
    alpha_mode = True 
    i = 0

    while i < len(input_string):
        braille_char = input_string[i:i+6]

        if braille_char == ENGLISH2BRAILLE['capital_follows']:
            # Handle uppercase letters
            next_braille = input_string[i+6:i+12]
            if next_braille in BRAILLE2ENGLISH:
                eng_trans += BRAILLE2ENGLISH[next_braille].upper()
            i += 12  
        elif braille_char == ENGLISH2BRAILLE['number_follows']:
            alpha_mode = False
            i += 6 
        elif braille_char == ENGLISH2BRAILLE[' ']:
            # Handle spaces
            eng_trans += ' '
            alpha_mode = True  # Reset to alphabetic mode after a space
            i += 6  
        else:
            if not alpha_mode and braille_char in BRAILLE2NUMBER:
                eng_trans += BRAILLE2NUMBER[braille_char]
            elif alpha_mode and braille_char in BRAILLE2ENGLISH:
                eng_trans += BRAILLE2ENGLISH[braille_char]
            i += 6  # Move to the next Braille character

    return eng_trans

def main(input_string):
    first_letter = input_string[0]
    if first_letter.isdigit() or first_letter.isspace() or first_letter.isupper() or first_letter.islower():
        return trans_eng_to_bra(input_string)
    else:
        return trans_bra_to_eng(input_string)


BRAILLE2ENGLISH = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "capital_follows", ".O.OOO": "number_follows", "......": " ",  
}

BRAILLE2NUMBER = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}

ENGLISH2BRAILLE = {value: key for key, value in BRAILLE2ENGLISH.items()}

NUMBERS2BRAILLE = {value: key for key, value in BRAILLE2NUMBER.items()}

if __name__ == '__main__':
    input_string = ' '.join(sys.argv[1:])
    result = main(input_string)