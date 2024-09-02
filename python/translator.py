braille_letters_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
}

braille_digits_to_english = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", 
    "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
    ".OOO..": "0"
}

braille_symbols_to_english = {
    ".....O": "capital follows", ".O...O": "decimal follows", ".O.OOO": "number follows", 
    "..00.0": ".", "..0...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", 
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">", 
    "O.O..O": "(", ".O.OO.": ")", "......": "space"
}

english_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO",
    
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
    
    ' ': "......", '.': "..00.0", ',': "..0...", '?': "..O.OO", '!': "..OOO.",
    ':': "..OO..", ';': "..O.O.", '-': "....OO", '/': ".O..O.", '<': ".OO..O",
    '>': "O..OO.", '(': "O.O..O", ')': ".O.OO.",
    
    'capital follows': ".....O", 'decimal follows': ".O...O", 'number follows': ".O.OOO"
}

def is_braille(s):
    return all(c in 'O.' for c in s)

def english_to_braille_string(s):
    result = []
    is_number = False
    
    for char in s:
        if char.isdigit():
            if not is_number: 
                result.append(english_to_braille['number follows'])
                is_number = True
            result.append(english_to_braille[char])
        else:
            if is_number: 
                is_number = False
            if char.isupper():
                result.append(english_to_braille['capital follows'])
                result.append(english_to_braille[char.lower()])
            elif char == ' ':
                result.append(english_to_braille[' '])
            elif char in english_to_braille:
                result.append(english_to_braille[char])
            else:
                raise ValueError(f"Character '{char}' is not supported.")
                    
    return ''.join(result)

def braille_to_english_string(s):
    result = []
    is_capital = False
    is_number = False
    i = 0
    while i < len(s):
        braille_char = s[i:i+6]

        if braille_char in braille_symbols_to_english:
            symbol = braille_symbols_to_english[braille_char]
            if symbol == "capital follows":
                is_capital = True
            elif symbol == "number follows":
                is_number = True
            elif symbol == "space":
                result.append(" ")
                is_number = False  
            i += 6
            continue

        if is_number:
            char = braille_digits_to_english.get(braille_char, '')
        else:
            char = braille_letters_to_english.get(braille_char, '')

        if is_capital and char.isalpha():
            char = char.upper()
            is_capital = False  
        result.append(char)
        i += 6

    return ''.join(result)

import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(braille_to_english_string(input_string))
    else:
        print(english_to_braille_string(input_string))

if __name__ == "__main__":
    main()
