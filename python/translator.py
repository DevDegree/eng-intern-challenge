import sys

# symbols not required by spec
EN_TO_BR = {
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
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..',
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...', 
    '0': '.OOO..',
    ' ': '......',
    'cap': '.....O',  # capital follows
    'num': '.O.OOO'   # number follows
}

BR_TO_EN_ALPHA = {v: k for k, v in EN_TO_BR.items() if k.isalpha() or k == ' '}
BR_TO_EN_NUM = {v: k for k, v in EN_TO_BR.items() if k.isdigit()}

def main():
    if len(sys.argv) < 2:
        print('Error: Argument required')
        sys.exit(1)

    input_txt = ' '.join(sys.argv[1:])
    output_txt = ''
    
    is_braille = True
    for ch in input_txt:
        if ch not in ('O', '.'):
            is_braille = False
            break

    if is_braille:
        output_txt = braille_to_english(input_txt)
    else:
        output_txt = english_to_braille(input_txt) 

    print(output_txt)

def braille_to_english(input_txt):
    cap = False
    num = False
    translated_text = ''

    for i in range(0, len(input_txt), 6):
        ch = input_txt[i: i+6]
        transl_ch = BR_TO_EN_ALPHA[ch]

        if transl_ch == 'cap':
            cap = True
            continue
        elif transl_ch == 'num':
            num = True
            continue
        elif cap == True:
            translated_text += transl_ch.upper()
            cap = False
        elif num == True:
            if translated_text == ' ':
                translated_text += transl_ch
                num = False
            else:
                translated_text += BR_TO_EN_NUM[ch]
        else:
            translated_text += transl_ch

    return translated_text

def english_to_braille(input_txt):
    num = False
    translated_text = ''

    for ch in input_txt:
        transl_ch = EN_TO_BR[ch.lower()]
        if ch.isupper():
            translated_text += EN_TO_BR['cap'] + transl_ch
        elif ch.isalpha():
            translated_text += transl_ch
        elif ch == ' ':
            translated_text += transl_ch
            num = False
        elif ch.isdigit() and num:
            translated_text += transl_ch
        elif ch.isdigit() and not num:
            translated_text += EN_TO_BR['num'] + transl_ch
            num = True
    
    return translated_text

if __name__ == "__main__":
    main()
