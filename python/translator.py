import sys #to run the command line interface
import re
RULES_TO_BRAILLE={
    'capital':'.....O',
    'decimal':'.O...O',
    'number':'.O.OOO'
}
SYMBOLS_TO_BRAILLE={
    '.':'..OO.O',
    ',':'..O...',
    '?':'..O.OO',
    '!':'..OOO.',
    ':':'..OO..',
    ';':'..O.O.',
    '-':'....OO',
    '/':'.O..O.',
    '<':'.OO..O',
    '>':'O..OO.',
    '(':'O.O..O',
    ')':'.O.OO.',
    ' ':'......'
}
LETTERS_TO_BRAILLE={
    'a':'O.....',
    'b':'O.O...',
    'c':'OO....',
    'd':'OO.O..',
    'e':'O..O..',
    'f':'OOO...',
    'g':'OOOO..',
    'h':'O.OO..',
    'i':'O.O...',
    'j':'.OOO..',
    'k':'O...O.',
    'l':'O.O.O.',
    'm':'OO..O.',
    'n':'OO.OO.',
    'o':'O..OO.',
    'p':'OOO.O.',
    'q':'OOOOO.',
    'r':'O.OOO.',
    's':'.OO.O.',
    't':'.OOOO.',
    'u':'O...OO',
    'v':'O.O.OO',
    'w':'.OOO.O',
    'x':'OO..OO',
    'y':'OO.OOO',
    'z':'O..OOO'
}
NUMBERS_TO_BRAILLE={
    '1':'O.....',
    '2':'O.O...',
    '3':'OO....',
    '4':'OO.O..',
    '5':'O..O..',
    '6':'OOO...',
    '7':'OOOO..',
    '8':'O.OO..',
    '9':'O.O...',
    '0':'.OOO..',     
}
BRAILLE_TO_LETTERS = {v: k for k, v in LETTERS_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}
BRAILLE_TO_SYMBOLS = {v: k for k, v in SYMBOLS_TO_BRAILLE.items()}
BRAILLE_TO_RULES = {v: k for k, v in RULES_TO_BRAILLE.items()}


def check_input(text):
    for char in text:
        if char!="O" and char!=".":
            return english_to_braille(text)
    return braille_to_english(text)

def english_to_braille(text):
    result=''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result+=RULES_TO_BRAILLE['capital']
            result+=LETTERS_TO_BRAILLE[char.lower()]
        elif char.isdigit():
            result+=RULES_TO_BRAILLE['number']
            result+=NUMBERS_TO_BRAILLE[char]
        elif char in SYMBOLS_TO_BRAILLE:
            result+=SYMBOLS_TO_BRAILLE[char]    
    return result
def braille_to_english(text):
    result=''
    i=0
    while i<len(text):
        if text[i:i+6] in BRAILLE_TO_RULES:
            result+=BRAILLE_TO_RULES[text[i:i+6]]
            i+=6
        elif text[i:i+6] in BRAILLE_TO_LETTERS:
            result+=BRAILLE_TO_LETTERS[text[i:i+6]]
            i+=6
        elif text[i:i+6] in BRAILLE_TO_NUMBERS:
            result+=BRAILLE_TO_NUMBERS[text[i:i+6]]
            i+=6
        elif text[i:i+6] in BRAILLE_TO_SYMBOLS:
            result+=BRAILLE_TO_SYMBOLS[text[i:i+6]]
            i+=6
    return result

def main():
    if len(sys.argv) < 2:
        print("Error: Not enough arguments")
        sys.exit(1)
    text = ' '.join(sys.argv[1:])
    print(check_input(text))
if __name__ == '__main__':
    main()
