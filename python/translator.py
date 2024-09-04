
import sys

english_braille = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
                   'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
                   'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
                   'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
                   'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
                   'z': 'O..OOO', 'cap': '.....O', 'dec': '.O...O', 'num': '.O.OOO'}
braille_english = {v: k for k, v in english_braille.items()}

braille_num = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
               '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
               '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
               ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', 
               '(': 'O.O..O', ')': '.O.OO.', ' ': '......'}
english_num = {v: k for k, v in braille_num.items()}

def english_to_braille(text):
    res = []
    isnum = False
    for char in text:
        # print(char)
        if char.isupper():
            res.append(english_braille['cap'])
            # print(english_braille['cap'])
            char = char.lower()
        if char.isdigit():
            if not isnum:
                res.append(english_braille['num'])
            isnum = True
            res.append(braille_num[char])
            # print(english_braille['num'])
            # print(braille_num[char])
            
        elif not char.isalpha():
            res.append(braille_num[char])
            isnum = False
            # print(braille_num[char])
        else:
            res.append(english_braille[char])
            isnum = False
            # print(english_braille[char])
    return ''.join(res)

def braille_to_english(text):
    res = []
    iscap = False
    isnum = False
    for i in range(0, len(text), 6):
        braille = text[i:i+6]
        # print(braille)
        if braille in braille_english:
            char = braille_english[braille]
        elif braille in english_num:
            char = english_num[braille]
        # print(char)
        if char == 'cap':
            iscap = True
            continue
        if char == 'num':
            isnum = True
            continue
        if char == ' ':
            isnum = False

        if iscap:
            res.append(char.upper())
            iscap = False
        elif isnum:
            res.append(english_num[braille])
        else:
            res.append(char)
        
    return ''.join(res)

def is_braille(text):
    for char in text:
        if char not in 'O.':
            return False
    return True

def main():
    if len(sys.argv) < 2:
        print("invalid input")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        translated_text = braille_to_english(input_text)
    else:
        translated_text = english_to_braille(input_text)
    
    print(translated_text)

if __name__ == "__main__":
    main()


