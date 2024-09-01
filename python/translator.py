import sys  # cmd args


braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', 
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(",  
    ".O.OO.": ")",  
    'cap': '.....O', # next val is cap
    ' ': '......', 
    'num': '.O.OOO', # next val is number

}

braille_dict_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

inverse_braille_dict = inverse_braille_dict = {v: k for k, v in braille_dict.items()}

def english_to_braille(text):

    braille_result = []
    is_number = False
    for char in text:
        if char.isdigit():
            if not is_number:
                braille_result.append(braille_dict['num'])
                is_number = True
            braille_result.append(braille_dict_numbers[char])
        elif char.isalpha():
            if is_number:
                braille_result.append(braille_dict[' '])
                is_number = False
            if char.isupper():
                braille_result.append(braille_dict['cap'])
            braille_result.append(braille_dict[char.lower()])
        else:
            if is_number:
                is_number = False
            braille_result.append(braille_dict[char])

    return ''.join(braille_result)


def braille_to_english(text_braille):
    english_result = []
    index = 0
    
    while index < len(text_braille):
        char = text_braille[index:index+6]

        if char == braille_dict['num']:
            index += 6
            while index < len(text_braille) and text_braille[index:index+6] != braille_dict[' ']:
                english_result.append(str(list(braille_dict_numbers.values()).index(text_braille[index:index+6]) + 1))
                index += 6
            continue
        elif char == braille_dict['cap']:
            index += 6
            next_char = text_braille[index:index+6]
            english_result.append(inverse_braille_dict[next_char].upper())
        else:
            english_result.append(inverse_braille_dict[char])

        index += 6
    return ''.join(english_result)

if __name__ == "__main__":
    input_text = sys.argv[1:]

    if len(sys.argv) != 2:
        print("Invalid input, one argument expected")
        sys.exit(1)
    input_string = ''.join(input_text) 

    is_braille = True

    for char in input_string:
        if char not in '.O':
            is_braille = False
            break

    if is_braille:
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

