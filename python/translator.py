import sys


braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', 
}


braille_capital = '.....O'
braille_number = '.O.OOO'
braille_digits = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}


english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_digits = {v: k for k, v in braille_digits.items()}

def is_braille(input_str):
   
    return all(c in 'O.' for c in input_str)

def translate_to_braille(text):
    result = []
    is_number = False 

    for char in text:
        if char.isupper():
            result.append(braille_capital)
            char = char.lower()

        if char.isdigit():
            if not is_number:  
                result.append(braille_number)
                is_number = True
            result.append(braille_digits[char])
        else:
            if is_number:
                is_number = False  
            result.append(braille_alphabet.get(char, '......'))  
    
    return ''.join(result)

def translate_to_english(braille):
    result = []
    is_capital = False  
    is_number = False  

    
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        if symbol == braille_capital:
            is_capital = True
        elif symbol == braille_number:
            is_number = True
        else:
            if is_number:
                result.append(english_digits.get(symbol, ' '))
                is_number = False
            else:
                char = english_alphabet.get(symbol, ' ')
                if is_capital:
                    result.append(char.upper())
                    is_capital = False
                else:
                    result.append(char)
    
    return ''.join(result)

def main():
    
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return
    
    input_str = ' '.join(sys.argv[1:])
    
    if is_braille(input_str):
      
        print(translate_to_english(input_str))
    else:
      
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    main()
