braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '.': '.OOOO.', ' ': '......', 
    ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
}
number_dict = { 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0':'.OOO..'}
reverse_braille_dict = {x:y for y, x in braille_dict.items()}
reverse_number_dict = {x:y for y, x in number_dict.items()}
uppercase_indicator = '.....O'
decimal_indicator = '.O...O'
number_indicator = '.O.OOO'

def text_to_braille(text):
    braille_result = []
    is_number_mode = False

    for char in text:
        if char == ' ':     #space, possible end of number
            braille_result.append('......')
            is_number_mode = False
        elif char.isupper():
            braille_result.append(uppercase_indicator)
            braille_result.append(braille_dict.get(char.lower()))
        elif char == '.':     #decimal
            braille_result.append(decimal_indicator)
            braille_result.append(braille_dict.get(char))
        elif char.isdigit():#number
            if not is_number_mode:#start of number insert num_indicator
                braille_result.append(number_indicator)
                is_number_mode = True
            braille_result.append(number_dict.get(char))
        elif char in braille_dict:
            is_number_mode = False
            braille_result.append(braille_dict.get(char))

    return ''.join(braille_result)

def braille_to_text(braille_list):
    text_result = []
    is_number_mode = False
    i = 0
    while i < len(braille_list):
        braille = braille_list[i]
        if braille == uppercase_indicator: #case 1: Uppercase
            i += 1
            braille = braille_list[i]
            text_result.append(reverse_braille_dict.get(braille).upper())
        elif braille == number_indicator:
            is_number_mode = True
        elif braille == decimal_indicator:
            i += 1
            braille = braille_list[i]
            if is_number_mode:
                text_result.append(reverse_number_dict.get(braille))
            else:
                text_result.append(reverse_braille_dict.get(braille))
        elif braille == '......':
            is_number_mode = False
            text_result.append(' ')
        else:
            if is_number_mode:
                text_result.append(reverse_number_dict.get(braille))
            else:
                text_result.append(reverse_braille_dict.get(braille))
        i += 1
    return ''.join(text_result)

def main():
    import sys
    input_text = ' '.join(sys.argv[1:])

    if all(char in 'O.' for char in input_text):#braille
        braille_list = []
        for i in range(0, len(input_text), 6):
            braille_list.append(input_text[i:i+6]) #split into array consisting of 6 char each
        decoded_text = braille_to_text(braille_list)
        print(decoded_text)
    else:#text
        braille = text_to_braille(input_text)
        print (braille)

if __name__ == "__main__":
    main()

