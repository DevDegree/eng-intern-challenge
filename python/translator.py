import sys

lang_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', ',': '.O....', ';': '.OO...', ':': '.O.O..',
    '.': '.O.OO.', '!': '.OO.O.', '?': '.OO..O', '-': '..O.O.', '/': '.O.O..',
    '(': '.O.O.O', ')': 'O..O.O', '<': 'OO...O', '>': '..OO.O',
    'capital_follows': '.....O', 'number_follows': '.O.OOO'
}

num_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_to_lang_map = {v: k for k, v in lang_to_braille_map.items()}
braille_to_num_map = {v: k for k, v in num_map.items()}

def braille_to_lang(braille_str):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille_str):
        char = braille_str[i:i+6]
        if char == lang_to_braille_map['capital_follows']:
            capitalize_next = True
        elif char == lang_to_braille_map['number_follows']:
            number_mode = True
        elif char in braille_to_lang_map:
            letter = braille_to_lang_map[char]
            if number_mode and char in braille_to_num_map:
                result.append(braille_to_num_map[char])
            else:
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                result.append(letter)
            if letter == ' ':
                number_mode = False
        i += 6

    return ''.join(result)

def lang_to_braille(text_str):
    result = []
    number_mode = False

    for char in text_str:
        if char.isupper():
            result.append(lang_to_braille_map['capital_follows'])
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                result.append(lang_to_braille_map['number_follows'])
                number_mode = True
            result.append(num_map[char])
        else:
            result.append(lang_to_braille_map[char])
            if char == ' ':
                number_mode = False

    return ''.join(result)

def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def translate_text(text):
    if is_braille(text):
        return braille_to_lang(text)
    else:
        return lang_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(translate_text(input_text), end='')
    else:
        print("Enter a string please")