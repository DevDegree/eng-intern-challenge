# Braille dictionary
dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
}

# Braille dictionary for the digits
num_dict = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
            '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'}

# Special prefixes
capital_prefix = '.....O'
num_prefix = '.O.OOO'

# Reverse dictionary for Braille to English
english_dict = {v: k for k, v in dict.items()}
english_dict_nums = {v: k for k, v in num_dict.items()}

def translate_to_braille(text):
    translated = []
    is_digit = False

    for char in text:
        if char.isdigit():
            if not is_digit:
                is_digit = True
                translated.append(num_prefix)
            translated.append(dict[char])
        elif char.isupper():
            translated.append(capital_prefix + dict[char.lower()])
            is_digit = False
        elif char == ' ':
            translated.append(dict[char])
            is_digit = False
        else:
            translated.append(dict[char])
            is_digit = False

    return ''.join(translated)


def translate_to_english(braille):
    translated = []
    i = 0
    is_num = False

    while i < len(braille):
        if braille[i:i+6] == capital_prefix:
            i += 6
            translated.append(english_dict[braille[i:i+6]].upper())
            i += 6
        elif braille[i:i+6] == num_prefix:
            i += 6
            translated.append(english_dict_nums[braille[i:i+6]])
            is_num = True
            i += 6
        else:
            if not is_num:
                char = english_dict[braille[i:i+6]]
            elif is_num:
                char = english_dict_nums[braille[i:i+6]]
            translated.append(char)
            i += 6
            if char == ' ':
                is_num = False

    return ''.join(translated)


def main():
    input_text = input("Enter the text or Braille: ")

    if set(input_text) <= {'O', '.', ' '}:
        print("Translated to English:", translate_to_english(input_text))
    else:
        print("Translated to Braille:", translate_to_braille(input_text))

if __name__ == "__main__":
    main()

