import sys
import re

# Dictionary mapping the braille to English letters and numbers
char_to_braille = {
    'A': "O.....",
    'B': "O.O...",
    'C': "OO....",
    'D': "OO.O..",
    'E': "O..O..",
    'F': "OOO...",
    'G': "OOOO..",
    'H': "O.OO..",
    'I': ".OO...",
    'J': ".OOO..",
    'K': "O...O.",
    'L': "O.O.O.",
    'M': "OO..O.",
    'N': "OO.OO.",
    'O': "O..OO.",
    'P': "OOO.O.",
    'Q': "OOOOO.",
    'R': "O.OOO.",
    'S': ".OO.O.",
    'T': ".OOOO.",
    'U': "O...OO",
    'V': "O.O.OO",
    'W': ".OOO.O",
    'X': "OO..OO",
    'Y': "OO.OOO",
    'Z': "O..OOO",
    '.': "..OO.O",
    ',': "..O...",
    '?': "..O.OO",
    '!': "..OOO.",
    ':': "..OO..",
    ';': "..O.O.",
    '-': "....OO",
    '<': ".OO..O",
    '>': "O..OO.",
    '(': "O.O..O",
    ')': ".O.OO.",
    ' ': "......",
    'capital_follows': ".....O",
    'decimal_follows': ".O...O",
    'number_follows': ".O.OOO"
}

num_to_braille = {
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO.."
}

braille_to_char = {v: k for k, v in char_to_braille.items()}
braille_to_num = {v: k for k, v in num_to_braille.items()}

def eng_to_braille(text):
    res = ""
    prev = ""
    for i, c in enumerate(text):
        if c.isdigit():
            if text[i-1].isdigit():
                res += num_to_braille[c]
            else:
                res += char_to_braille['number_follows']
                res += num_to_braille[c]
        elif not(c.isalnum()):
            res += char_to_braille.get(c)
        elif c.isupper():
            res += char_to_braille['capital_follows']
            res += char_to_braille[c.upper()]
        elif c == '.':
            if i > 0 and text[i-1].isdigit():
                res += char_to_braille['decimal_follows']
            else:
                res += char_to_braille['.']
        
        else:
            res += char_to_braille.get(c.upper())

    return res

def braille_to_eng(braille):
    lst = [braille[i:i+6] for i in range(0, len(braille), 6)]
    res = ""
    capitalize = False
    number = False
    decimal = False
    has_open = False
    for i in range(len(lst)):
        ele = lst[i]
        cur = braille_to_char[ele]
        if cur == 'capital_follows':
            capitalize = True
        elif cur == 'number_follows':
            number = True
        elif cur == 'decimal_follows':
            decimal = True
        elif cur == ' ':
            res += cur
            number = False
            decimal = False
        elif capitalize:
            res += cur
            capitalize = False
        elif decimal and cur in 'ABCDEFGHIJ':
            res += '.'
            res += braille_to_num[ele]
            decimal = False
        elif number and cur in 'ABCDEFGHIJ':
            res += braille_to_num[ele]
        elif cur == '<':
            res += cur
            has_open = True
        elif (has_open and cur == '>' and i == len(lst) - 1) or (has_open and cur == '>' and lst[i+1] == char_to_braille[' ']): 
            res += cur
            has_open = False
        else:
            if cur == '>':
                res += 'o'
            else:
                res += cur.lower()
    return res



def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    text = ' '.join(sys.argv[1:])
    if len(text) % 6 == 0 and all(c in 'O.' for c in text):
        # translate to english
        english_out = braille_to_eng(text)
        print(english_out)
        
    else:
        # translate to braille
        braille_out = eng_to_braille(text)
        print(braille_out)

if __name__ == "__main__":
    main()


