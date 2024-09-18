import sys

def braille_translator(input_string):
    braille_alphabet = {
        'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
        'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
        'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
        'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
        'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
        'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
        'y': 'OO.OOO',    'z': 'O..OOO',    ' ': '......',
    }
    
    numbers = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }
    
    capital_symbol = '.....O'  
    number_symbol = '.O.OOO'  
    
    is_braille = all(c in 'O.' for c in input_string.replace(' ', '')) and len(input_string.replace(' ', '')) % 6 == 0
    
    if is_braille:
        result = ""
        is_capital = False
        is_number = False
        i = 0
        while i < len(input_string):
            symbol = input_string[i:i+6]
            if symbol == capital_symbol:
                is_capital = True
            elif symbol == number_symbol:
                is_number = True
            else:
                if is_number:
                    for digit, braille in numbers.items():
                        if braille == symbol:
                            result += digit
                            is_number = False  
                            break
                else:
                    for char, braille in braille_alphabet.items():
                        if braille == symbol:
                            if is_capital:
                                result += char.upper()
                                is_capital = False  
                            else:
                                result += char
                            break
            i += 6
        return result
    else:
        result = ""
        is_number = False
        for char in input_string:
            if char.isdigit():
                if not is_number:
                    result += number_symbol
                    is_number = True
                result += numbers[char]
            else:
                if char.isupper():
                    result += capital_symbol + braille_alphabet[char.lower()]
                else:
                    result += braille_alphabet.get(char, '......')
                is_number = False  
        return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])
        print(braille_translator(input_string), end='')
    else:
        print("Please provide a string to translate.")

