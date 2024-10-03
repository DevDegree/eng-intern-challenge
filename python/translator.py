def translate_to_english(string : str, braille_map : map):
    new_string = ''
    number_mode = False
    capitalize = False
    for i in range(0, len(string), 6):
        braille_string = string[i:i+6]
        if braille_string not in braille_map: # Error case
            continue
        text = braille_map[braille_string]
        if text == 'CAPITAL':
            capitalize = True
            continue
        if text == 'NUMBER':
            number_mode = True
            continue
        if text == ' ':
            number_mode = False
        elif(capitalize):
            text = text.upper()
            capitalize = False
        elif(number_mode):
            # 'a' to 'i' is 1 to 10, then 'j' is 0, hence the mod 10
            nb_val = (ord(text) - ord('a') + 1) % 10
            text = str(nb_val)

        new_string += text

    return new_string

def translate_to_braille(string : str, char_map : map):
    new_string = ''
    number_mode = False
    for char in string:
        if char.isupper():
            new_string += char_map['CAPITAL']
            new_string += char_map[char.lower()]
            continue
        if char.isdigit():
            if not number_mode:
                new_string += char_map['NUMBER']
                number_mode = True
            ascii_digit = int(char) + ord('a') - 1
            if ascii_digit < ord('a'):
                ascii_digit = ord('j')
            char = chr(ascii_digit)
            new_string += char_map[char]
            continue
        if char not in char_map: # Error case
            continue
        if char == ' ':
            number_mode = False

        new_string += char_map[char]

    return new_string

def construct_maps():
    char_to_braille_map = {
    'a' : 'O.....', 'b' : 'O.O...', 'c' : 'OO....', 'd' : 'OO.O..', 'e' : 'O..O..',
    'f' : 'OOO...', 'g' : 'OOOO..', 'h' : 'O.OO..', 'i' : '.OO...', 'j' : '.OOO..',
    'k' : 'O...O.', 'l' : 'O.O.O.', 'm' : 'OO..O.', 'n' : 'OO.OO.', 'o' : 'O..OO.',
    'p' : 'OOO.O.', 'q' : 'OOOOO.', 'r' : 'O.OOO.', 's' : '.OO.O.', 't' : '.OOOO.',
    'u' : 'O...OO', 'v' : 'O.O.OO', 'w' : '.OOO.O', 'x' : 'OO..OO', 'y' : 'OO.OOO',
    'z' : 'O..OOO', ' ' : '......', 'CAPITAL' : '.....O', 'NUMBER' : '.O.OOO'
    }
    braille_to_char_map = {value: key for key, value in char_to_braille_map.items()}

    return char_to_braille_map, braille_to_char_map

def main():
    input_string = ' '.join(sys.argv[1:])

    char_map, braille_map = construct_maps()

    is_braille = all(char in 'O.' for char in input_string)

    if is_braille:
        translated_string = translate_to_english(input_string, braille_map)
    else:
        translated_string = translate_to_braille(input_string, char_map)

    print(translated_string)

if __name__ == "__main__":
    main()
