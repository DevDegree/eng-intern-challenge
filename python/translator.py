import sys

braille_char = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

brail_num = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

capital = '.....O'
space = '......'
num = '.O.OOO'

def is_braille(str):
    # It is a braille
    if len(str) == 1:
        str = ''.join(str)
        if all(c in ['O', '.'] for c in str):
            return 1
    
    # Invalid format
    for word in str:
        if not all(c.isalnum() or c.isspace() for c in word):
            return -1
    
    # It is an english sentence/word
    return 0

def braille_to_english(str):
    str = ''.join(str)
    result = []
    is_number = False
    i = 0
    
    while i < len(str):
        key = str[i:i+6]
        if key == num:
            is_number = True
        elif key == capital:
            i += 6
            key = str[i:i+6]
            for letter, braille_code in braille_char.items():
                if braille_code == key:
                    result.append(letter.upper())
                    break
        elif key == space:
            if not is_number:
                result.append(' ')
            else:
                is_number  = False
        else:
            if is_number:
                for number, braille_code in brail_num.items():
                    if braille_code == key:
                        result.append(number)
                        break
            else:
                for letter, braille_code in braille_char.items():
                    if braille_code == key:
                        result.append(letter)
                        break
        i += 6
        
    return ''.join(result)
    

def english_to_braille(str):
    str = ' '.join(str)
    result = []
    is_number = False
    
    for char in str:
        if char.isspace():
            result.append(space)
        elif char.isalpha():
            if is_number:
                is_number = False # Convert from number to char need to add space
                result.append(space)
            if char.isupper():
                result.append(capital)
            result.append(braille_char[char.lower()])
        else:
            if not is_number:
                result.append(num)
                is_number = True
            result.append(brail_num[char])
    
    return ''.join(result)

            
def main():
    if len(sys.argv) < 2:
        print("Remember to input a string for translation")
        return
    
    check = is_braille(sys.argv[1:])
    
    if check == 1:
        translated = braille_to_english(sys.argv[1:])
    elif check == 0: 
        translated = english_to_braille(sys.argv[1:])
    else:
        return
    
    print(translated)
    
if __name__ == "__main__":
    main()