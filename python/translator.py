import sys

english_2_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......',

    # to indicate capital, decimal, or number follows
    'cap': '.....O', 'dec': '.O...O', 'num': '.O.OOO', 

    ',': '.O....', ';': '.OO...', ':': '.O.O..', '.': '.O.OO.', '!': '.OO.O.',
    '?': '.OO..O', '-': '..O.O.', '/': '.O.O..', '(': '.O.O.O', ')': 'O..O.O', 
    '<': 'OO...O', '>': '..OO.O', 
}

digits_2_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

braille_2_eng = {}
for key in english_2_braille.keys():
    braille_2_eng[english_2_braille[key]] = key

braille_2_digits = {}
for key in digits_2_braille.keys():
    braille_2_digits[digits_2_braille[key]] = key

# print(braille_2_eng, braille_2_digits)

def is_braille(input_str):
    for letter in input_str:
        if letter != 'O' and letter != '.':
            return False
    # print("len(input_str)", len(input_str))
    if len(input_str) % 6 != 0:
        return False
    return True

def translate_braille_to_english(braille_text):
    english_output = ""
    capital_next = False
    numeric_mode = False

    for i in range(0, len(braille_text), 6):
        braille_code = braille_text[i:i+6]

        eng_char = braille_2_eng[braille_code]

        if eng_char == 'cap':
            capital_next = True

        elif eng_char == 'num':
            numeric_mode = True

        elif eng_char == ' ':
            english_output += eng_char
            numeric_mode = False

        elif numeric_mode:
            english_output += braille_2_digits[braille_code]

        elif capital_next:
            english_output += eng_char.upper()
            capital_next = False

        else:
            english_output += eng_char

    return english_output

def translate_eng_to_braille(input_str):
    braille_output = ""
    num_follows = False

    for eng_char in input_str:
        if eng_char.isdigit():
            if num_follows:
                braille_output += digits_2_braille[eng_char]
            else:
                braille_output += english_2_braille['num'] + digits_2_braille[eng_char]
                num_follows = True

        elif eng_char.isupper():
            braille_output += english_2_braille['cap'] + english_2_braille[eng_char.lower()]

        elif eng_char == ' ':
            braille_output += english_2_braille[' ']
            num_follows = False

        else:
            braille_output += english_2_braille[eng_char]

    return braille_output

if __name__ == "__main__":
    input_str = " ".join(sys.argv[1:])

    if is_braille(input_str):
        output_str = translate_braille_to_english(input_str)
    else:
        output_str = translate_eng_to_braille(input_str)

    print(output_str)
# i1 = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
# print(is_braille(i1))
# r1 = translate_braille_to_english(i1)
# print('r1', r1)
# i2 = ".O.OOOOO.O..O.O..."
# print(is_braille(i2))
# r2 = translate_braille_to_english(i2)
# print('r2', r2)
# i3 = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
# r3 = translate_braille_to_english(i3)
# print('r3', r3)
# print("is_braille", r3, is_braille(r3))
# r4 = translate_eng_to_braille(r3)
# print(r4 == i3)