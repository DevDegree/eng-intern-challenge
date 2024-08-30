import sys

braille_mapping = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..','f': 'OOO...', 
                   'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
                   'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.','p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
                   's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO','z': 'O..OOO',
                   '.': '.O.O.O', ',': 'O.....', '!': 'OOO...', '?': '.O.OO.', 
                   '-': 'O....O', ':': 'OO.O..', ';': 'O.O...', "'": 'O....O',
                   ' ': '......', 'capital': '.....O', 'number': '.O.OOO'}

digit_mapping = {'1': 'O.....',  
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

alphabet_mapping = {}

special_mapping = {}

for char, braille in braille_mapping.items():
    if char.isalpha():
        alphabet_mapping[braille] = char
    elif char in ['.', ',', '!', '?', '-', ':', ';', "'"]:
        special_mapping[braille] = char

def english_to_braille(text):
    result = []
    is_number = False

    for char in text:
        if char.isupper():
            result.append(braille_mapping['capital'])
            result.append(braille_mapping[char.lower()])
            is_number = False 
        elif char.isdigit():
            if not is_number:
                result.append(braille_mapping['number']) 
                is_number = True 
            result.append(digit_mapping[char])
        else:
            if is_number and char == ' ':
                is_number = False
            result.append(braille_mapping.get(char, '......'))

    return ''.join(result)

def braille_to_english(braille):
    result = []
    is_caps = False
    is_number = False
    temp_braille = ''

    for char in braille:
        temp_braille += char
        if len(temp_braille) == 6:
            if temp_braille == braille_mapping['capital']:
                is_caps = True
            elif temp_braille == braille_mapping['number']:
                is_number = True
            elif temp_braille == '......':
                result.append(' ')
                is_number = False
            else:
                if is_number:
                    char = next((key for key, value in digit_mapping.items() if value == temp_braille), '')
                else:
                    char = alphabet_mapping.get(temp_braille, '') or special_mapping.get(temp_braille, '')
                    if is_caps:
                        char = char.upper()
                        is_caps = False 
                result.append(char)
            temp_braille = ''

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Cannot run python translator.py")
        return

    input_text = ' '.join(sys.argv[1:])

    if all(char in 'O.' for char in input_text.replace(' ', '')):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()
