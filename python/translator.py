
import argparse

braille_nums = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

braille_nums_reversed = {v: k for k, v in braille_nums.items()}

braille_chars = {
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
    ' ': '......',
    'capital': '.....O',
    'number': '.O.OOO'    
}

braille_chars_reversed = {v: k for k, v in braille_chars.items()}

def english_to_braille(sentence):
    braille_string = ""
    parsing_num = False
    for char in sentence:
        if char.isdigit():
            if not parsing_num:
                braille_string += braille_chars['number']
                parsing_num = True
                braille_string += braille_nums[char]
            else:
                braille_string += braille_nums[char]
        elif char == ' ':
            if parsing_num:
                parsing_num = False
            braille_string += braille_chars[' ']
        else:
            if char.isupper():
                braille_string += braille_chars['capital']
            braille_string += braille_chars[char.lower()]
    return braille_string

def braille_to_english(braille):
    english_string = ''
    parsing_num = False
    is_capital = False
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        if symbol == braille_chars['number']:
            parsing_num = True
            continue
        if parsing_num:
            if symbol == braille_chars[' ']:
                english_string += ' '
                parsing_num = False
            else:
                english_string += braille_nums_reversed[symbol]
        else:
            if symbol == braille_chars['capital']:
                is_capital = True
                continue
            if is_capital:
                english_string += braille_chars_reversed[symbol].upper()
                is_capital = False
            else:
                english_string += braille_chars_reversed[symbol]               
    return english_string

                
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("args", nargs="+")
    args = parser.parse_args()
    combined_args = " ".join(args.args)

    if len(args.args) == 1:
        str_is_english = False
        for char in args.args[0]:
            if char != 'O' and char != '.':
                str_is_english = True
                break
        if str_is_english:
            print(english_to_braille(args.args[0]))
        else:
            print(braille_to_english(args.args[0]))
    else:
        print(english_to_braille(combined_args))

if __name__ == '__main__':
    main()
