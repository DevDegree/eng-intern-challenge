English = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
           '.', ',', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')', ' ']
Braille = [
    'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..',  # a-j
    'O.. .O.', 'O.O.O.', 'OO..O.', 'OO.OO.', 'O..OO.', 'OOO.O.', 'OOOOO.', 'O.OOOO.', '.OO.O.', '.OOOO.',  # k-t
    'O...OO', 'O.O.OO', '.OOO.O', 'OO..OO', 'OO.OOO', 'O..OOO',  # u-z
    'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..',  # 1-9
    '..OO.O', '..O...', '..O.OO', '..OOO.', '..OO..', '..O.O.', '....OO', '.O..O.', '.O.O.O', 'O.O.O.',  # ., !, ?, ;, :, (, ), -
    'O.O..O', '.O.OO.', '......'
]
capital = '.....O'
number = '.O.OOO'
decimal = '.O...O'

def convert_to_braille(text):
    braille = ''
    for char in text:
        if char == '.':
            braille += decimal + Braille[English.index('.')]
        elif char.isdigit():
            braille += number + Braille[English.index(char)]
        elif char.isupper():
            braille += capital + Braille[English.index(char.lower())]
        elif char in English:
            braille += Braille[English.index(char)]
        else:
            braille += '??????'  
    return braille.strip()

def convert_to_text(braille):
    text = ''
    capitalize_next = False
    number_mode = False
    i = 0
    while i < len(braille):
        b = braille[i:i+6]
        
        if b == capital:
            capitalize_next = True
            i += 6  
        elif b == number:
            number_mode = True
            i += 6  
        elif b == decimal:
            text += '.'
            i += 6 
        elif b in Braille:
            if number_mode:
                text += English[Braille.index(b)+26]
                number_mode = False
            elif capitalize_next:
                text += English[Braille.index(b)].upper()
                capitalize_next = False
            else:
                text += English[Braille.index(b)]
            i += 6  
        else:
            text += '?'  
            i += 6 
    
    return text

def is_braille(text):
    valid_chars = {'O', '.'}
    return all(char in valid_chars for char in text)

if __name__ == '__main__':
    import sys
    input_text = ''.join(sys.argv[1:])
    if is_braille(input_text):
        print(convert_to_text(input_text))
    else:
        print(convert_to_braille(input_text))
