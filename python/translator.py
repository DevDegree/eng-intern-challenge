import string

# Define Braille key map
braille_dict = {
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
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '.....O': 'capital_follow',  
    '.O...O': 'decimal_follow',  
    '.O.OOO': 'number_follow',  
    '..OO.O': '.',  
    '..O...': ',',  
    '..O.OO': '?',  
    '..OOO.': '!',  
    '..OO..': ':',  
    '..O.O.': ';',  
    '....OO': '-',  
    '.O..O.': '/',  
    '.OO..O': '<',  
    'O..OO.': '>',  
    'O.O..O': '(',  
    '.O.OO.': ')',  
    '......': ' ',  
}

# Get a reverse dictionary to use Braille patterns as keys
braille_dict_reverse = {v: k for k, v in braille_dict.items()}

# Translate English to Braille
def english_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append('.O.OOO')  # Number indicator
                number_mode = True
            result.append(braille_dict[char])
        else:
            if char.isupper():
                result.append('.....O')  # Capital indicator
                result.append(braille_dict[char.lower()])
            else:
                result.append(braille_dict.get(char.lower(), char))
            number_mode = False
    return ''.join(result)

# Translate Braille to English
def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    while i < len(braille):
        chunk = braille[i:i+6]
        if chunk == '.....O':  # Capital indicator
            capitalize_next = True
            i += 6
        elif chunk == '.O.OOO':  # Number indicator
            number_mode = True
            i += 6
        else:
            char = braille_dict_reverse.get(chunk, '?')
            if number_mode:
                if char in 'abcdefghij':
                    char = str(ord(char) - ord('a') + 1)
                    if char == '10':
                        char = '0'
            elif char in '1234567890':
                char = chr(ord('a') + int(char) - 1)
                if char == 'j':
                    char = 'i'
            
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            
            result.append(char)
            i += 6

            if char == ' ':
                number_mode = False

    return ''.join(result)

def main():
    while True:
        user_input = input("Enter text to translate (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            break
        
        if all(c in '.O' for c in user_input):
            result = braille_to_english(user_input)
            print(result)
        else:
            result = english_to_braille(user_input)
            print(result)

if __name__ == "__main__":
    main()


