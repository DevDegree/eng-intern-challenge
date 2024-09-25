import sys

# Braille dictionary mapping

braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_special = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OOO',
    '(': 'O.O..O', ')': '.O.OO.'
}


braille_caps_pre = ".....O"
braille_num_pre = ".O.OOO"
braille_space = "......"
braille_dec_pre = ".O...O"


numbers = "0123456789"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_chars = "!?,.:;-/()<>"


def is_braille(input_string):
    """ Check if the input string is braille """
    return all(c == "O" or c == "." for c in input_string)


def translate_to_braille(english_string):
    result = []
    number_mode = False  # to track number mode

    for i, char in enumerate(english_string):
        if char == " ":
            result.append(braille_space)
            number_mode = False  # exit number mode on space
        elif char in caps:
            result.append(braille_caps_pre)
            result.append(braille_letters[char.lower()])
            number_mode = False
        elif char in numbers:
            if not number_mode:
                result.append(braille_num_pre)  # enter number mode
                number_mode = True
            result.append(braille_numbers[char])
        elif char == ".":
            if number_mode and (i + 1 < len(english_string) and english_string[i + 1].isdigit()):
                result.append(braille_dec_pre)  # braille for decimal point
            else:
                result.append(braille_special["."])  # braille for regular period
            number_mode = False  # period ends number mode
        elif char in special_chars:
            result.append(braille_special[char])
            # number_mode = False  # special characters exit number mode
        else:
            if number_mode:
                result.append(braille_space)  # exit number mode before translating letters
                number_mode = False
            result.append(braille_letters[char])

    return "".join(result)


def translate_to_english(braille_string):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    
    while i < len(braille_string):
        symbol = braille_string[i:i+6]
        
        if symbol == braille_caps_pre:
            capitalize_next = True
            i += 6
            continue
        elif symbol == braille_num_pre:
            number_mode = True
            i += 6
            continue
        elif symbol == braille_space:
            result.append(" ")
            i += 6
            number_mode = False  # space exits number mode
            continue
        elif symbol == braille_dec_pre:
            result.append(".")
            i += 6
            continue
        
        # different dictionaries based on mode
        if number_mode:
            char = next(key for key, value in braille_numbers.items() if value == symbol)
        elif symbol in braille_special.values():
            char = next(key for key, value in braille_special.items() if value == symbol)
        else:
            char = next(key for key, value in braille_letters.items() if value == symbol)

        # capitalize the next letter if required
        if capitalize_next:
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)
        
        i += 6
    
    return "".join(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        sys.exit(1)
    
    input_string = sys.argv[1]
    
    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))
