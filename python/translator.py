
import sys

dictionary_english_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', 
    'capital': '.....O', 'number': '.O.OOO'
}

braille_to_english = {v: k for k, v in dictionary_english_braille.items()}

def is_braille(input_str):
    """ Check if the input string is Braille by checking if it consists of only O and . """
    return all(c in 'O.' for c in input_str)

def translate_to_braille(english_str):

    """ Translates an English string to Braille. """
    result = []
    isfirstdigit = True
    for char in english_str:
        if char.isupper():
            result.append(dictionary_english_braille['capital'])
            char = char.lower()
        if char.isdigit():
            if (isfirstdigit):
                result.append(dictionary_english_braille['number'])
                isfirstdigit = False
                if (char == ' '):
                    isfirstdigit = True
        result.append(dictionary_english_braille.get(char, ''))
    return ''.join(result)

def translate_to_english(braille_str):
    result = []
    i = 0
    capital_next = False
    number_mode = False
    
    while i < len(braille_str):
        symbol = braille_str[i:i+6]
        
        if symbol == dictionary_english_braille['capital']:
            capital_next = True
            i += 6
            continue
        elif symbol == dictionary_english_braille['number']:
            number_mode = True
            i += 6
            continue
        
        char = braille_to_english.get(symbol, ' ')
        if capital_next:
            char = char.upper()
            capital_next = False
        if number_mode and char.isalpha():
            char = str(ord(char) - ord('a') + 1) 
            number_mode = False
        result.append(char)
        i += 6
    return ''.join(result)

def main():

    input_str = ' '.join(sys.argv[1:]) 
    if is_braille(input_str):
        result += translate_to_english(input_str)
        print(result)
    else:
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    main()
