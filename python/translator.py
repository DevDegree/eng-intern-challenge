import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'dec': '.O...O', 'num': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}

braille_num_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

reverse_braille_dict = {value: key for key, value in braille_dict.items()}
reverse_braille_num_dict = {value: key for key, value in braille_num_dict.items()}

def append_braille_num(translated_text, char, is_number):
    # if the last char was a number, just append the number's braille
    if is_number:
        translated_text += braille_num_dict[char]
    # if the last char was not a number, append the 'number next' braille and the number's braille
    else: 
        translated_text += braille_dict['num']
        translated_text += braille_num_dict[char]
    return translated_text

def append_braille_capital(translated_text, char):
    translated_text += braille_dict['cap']
    translated_text += braille_dict[char.lower()]
    return translated_text

def append_eng_letter(translated_text, braille, i, cap_character):
    # if braille is an uppercase letter
    if cap_character:
        translated_text += reverse_braille_dict[braille[i:i+6]].upper()
        cap_character = False
    # if braille is a lowercase letter
    else:
        translated_text += reverse_braille_dict[braille[i:i+6]]
    return translated_text, cap_character
    
def translate_to_braille(text):
    translated_text = ''
    is_number = False
    for char in text:
        # if char is a number
        if char.isdigit():
            translated_text = append_braille_num(translated_text, char, is_number)
            is_number = True
        # if char is a capital letter
        elif char not in braille_dict:
            translated_text = append_braille_capital(translated_text, char)
            is_number = False
        # if char is a lowercase letter
        else:
            translated_text += braille_dict[char.lower()]
            is_number = False
    return translated_text

def translate_to_english(braille):
    translated_text = ''
    cap_character = False
    num_character = False
    for i in range(0, len(braille), 6):
        # if next is capital
        if reverse_braille_dict[braille[i:i+6]] == 'cap':
            cap_character = True
        # if next is a number
        elif reverse_braille_dict[braille[i:i+6]] == 'num':
            num_character = True
        # if braille is a space
        elif reverse_braille_dict[braille[i:i+6]] == ' ':
            num_character = False
            translated_text += ' '
        # if braille is a letter
        elif not num_character:
            translated_text, cap_character = append_eng_letter(translated_text, braille, i, cap_character)
        # if braille is a number
        else:
            translated_text += reverse_braille_num_dict[braille[i:i+6]]
    return translated_text

def main():
    input_text = " ".join(sys.argv[1:])
    braille_input = True

    for char in input_text:
        # if the input is in braille
        if char in 'O.' and len(input_text) % 6 == 0:
            braille_input = True
        # if the input is in english
        else:
            translated_text = translate_to_braille(input_text)
            braille_input = False
            break
    if braille_input == True:
        translated_text = translate_to_english(input_text)

    print(translated_text)

if __name__ == "__main__":
    main()