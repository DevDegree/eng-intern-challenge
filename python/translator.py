import sys

# Braille representations
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    'cap': '.....O',
    'num': '.O.OOO',
}

inverse_braille_dict = {v: k for k, v in braille_dict.items() if k not in ['cap', 'num']}

# Mapping between letters and digits
letter_to_digit = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
                   'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}
digit_to_letter = {v: k for k, v in letter_to_digit.items()}

def is_braille(s):
    return all(c in 'O.' for c in s) and len(s.replace(' ', '')) % 6 == 0

def english_to_braille(text):
    result = []
    for word in text.split(' '):
        word_braille = []
        num_mode = False
        for char in word:
            if char.isdigit():
                if not num_mode:
                    word_braille.append(braille_dict['num'])
                    num_mode = True
                letter = digit_to_letter[char]
                word_braille.append(braille_dict[letter])
            else:
                if num_mode:
                    num_mode = False
                if char.isupper():
                    word_braille.append(braille_dict['cap'])
                word_braille.append(braille_dict.get(char.lower(), '......'))
        result.append(''.join(word_braille))
    return '......'.join(result)

def braille_to_english(braille_text):
    result = []
    index = 0
    braille_chars = []
    while index < len(braille_text):
        braille_chars.append(braille_text[index:index+6])
        index += 6
    num_mode = False
    i = 0
    while i < len(braille_chars):
        char = braille_chars[i]
        if char == '......':
            result.append(' ')
            num_mode = False  # Reset number mode after space
            i += 1
        elif char == braille_dict['cap']:
            i += 1
            if i < len(braille_chars):
                next_char = braille_chars[i]
                letter = inverse_braille_dict.get(next_char, '')
                result.append(letter.upper())
            i += 1
        elif char == braille_dict['num']:
            num_mode = True
            i += 1
        else:
            letter = inverse_braille_dict.get(char, '')
            if num_mode:
                digit = letter_to_digit.get(letter, '')
                result.append(digit)
            else:
                result.append(letter)
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])
    if is_braille(input_text.replace(' ', '')):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))
