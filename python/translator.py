import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOOO.', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOOO..',
    '.': '..OO.O', ',': '..O...', '?': '..O..O', '!': '..OOOO.', ';': 'O.O.O.', ':': 'OO..O.', '-': '....OO', '/': '....O.', '<': 'OO..OO', '>': 'OOOO..',
    '(': '.OOOOO', ')': '.OOOOO', ' ': '......',
    'capitalize': '.....O',
    'number': '.O.OOO'
}

english_dict_letters = {v: k for k, v in braille_dict.items() if k.isalpha()}
english_dict_numbers = {v: k for k, v in braille_dict.items() if k.isdigit()}

def english_to_braille(s):
    res = ""
    num = False
    for char in s:
        if char.isdigit() and not num:
            res += braille_dict['number']
            num = True
        elif char == " ":
            res += braille_dict[' ']
            num = False
        elif char.isupper() and char.isalpha():
            res += braille_dict['capitalize']
            char = char.lower()
            num = False
        res += braille_dict[char]
    return res

def braille_to_english(s):
    res = ""
    i = 0
    capitalize = False
    is_number = False
    while i < len(s):
        if i + 6 <= len(s):
            symbol = s[i:i+6]
            if symbol == braille_dict['capitalize']:
                capitalize = True
                print("hi")
                i += 6
                continue
            elif symbol == braille_dict['number']:
                is_number = True
                i += 6
                continue
            elif symbol == "......":
                res+= " "
                is_number= False
                i+=6
                continue
            if capitalize and not is_number:
                char = english_dict_letters.get(symbol, '')
                char = char.upper()
                res+= char
                capitalize = False
                i+=6
                continue
            if is_number and not capitalize:
                char = english_dict_numbers.get(symbol,'')
                
            else:
                char = english_dict_letters.get(symbol, '')

            res += char
            i += 6
        else:
            break
    return res

def main():
    statement = len(sys.argv)
    res = ""
    for i in range(1, statement-1):
        input_str = (sys.argv[i])
        
        if all(c in 'O.' for c in input_str):
            res += braille_to_english(input_str)
        else:
            res += english_to_braille(input_str)+"......"
    input_str = sys.argv[statement-1]
    if all(c in 'O.' for c in input_str):
        res += braille_to_english(input_str)
    else:
        res += english_to_braille(input_str)

    print(res)

if __name__ == "__main__":
    main()