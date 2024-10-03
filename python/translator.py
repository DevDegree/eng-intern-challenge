import argparse


def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('input_string', type=str)
    args = parser.parse_args()
    text = args.input_string
    
    uppercase = '.....O'
    number = '.O.OOO'
    en_to_br_dict = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
        'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
        'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
        'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
    }
    number_to_braille_dict = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...'
    }
    braille_to_number_dict = {v: k for k, v in number_to_braille_dict.items()}
    br_to_en_dict = {v: k for k, v in en_to_br_dict.items()}

    def is_braille_input(text):
        if len(text) % 6 != 0:
            return False
        return all(c in '.O' for c in text)
    
    ret = ''
    if is_braille_input(text):
        i = 0
        isUpper = False
        isNumber = False
        while i < len(text):
            character = text[i:i + 6]
            i += 6
            if isUpper:
                ret += br_to_en_dict[character].upper()
                isUpper = False
                continue
            if isNumber:
                if character == '......':
                    ret += ' '
                    isNumber = False
                    continue
                ret += braille_to_number_dict[character]
            if character == uppercase:
                isUpper = True
                continue
            if character == number:
                isNumber = True
                continue
            ret += br_to_en_dict[character]
    else:
        i = 0
        isNumber = False
        while i < len(text):
            if text[i] == ' ':
                ret += '......'
                isNumber = False
            if text[i].isalpha():
                if text[i].isupper():
                    ret += uppercase                
                ret += en_to_br_dict[text[i].lower()]
            elif text[i].isdigit():
                if not isNumber:
                    ret += number
                    isNumber = True
                number_to_braille_dict[text[i]]
            i += 1
    print(ret)
    return ret

if __name__ == "__main__":
    main()
