# Braille Translator code

import sys

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital', '.O.OOO': 'number'
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

number_mapping = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}

def braille_to_text(braille):
    text = ""
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == '.....O':  
            capitalize_next = True
        elif symbol == '.O.OOO':  
            number_mode = True
        else:
            char = braille_to_english.get(symbol, '')
            
            if number_mode and char in 'abcdefghij':
                char = [k for k, v in number_mapping.items() if v == char][0]
            elif not number_mode and capitalize_next:
                char = char.upper()
                capitalize_next = False
            
            text += char
            
            if char == ' ':
                number_mode = False

        i += 6

    return text

def text_to_braille(text):
    braille = ""
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille += english_to_braille['number']
                number_mode = True
            braille += english_to_braille[number_mapping[char]]
        elif char.isalpha():
            if number_mode:
                braille += '......'  
                number_mode = False
            if char.isupper():
                braille += english_to_braille['capital']
            braille += english_to_braille[char.lower()]
        elif char == ' ':
            braille += english_to_braille[char]
            number_mode = False
    
    return braille

def translate(input_string):
    if set(input_string).issubset({'O', '.'}):
        return braille_to_text(input_string)
    else:
        return text_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <input_string>")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])
    result = translate(input_string)
    print(result)
