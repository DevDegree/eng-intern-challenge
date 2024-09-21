import sys

# Mapping from characters to Braille dots (positions 0-5 from left to right, top to bottom)
char_to_dots = {
    'a': {0},
    'b': {0,2},
    'c': {0,1},
    'd': {0,1,3},
    'e': {0,3},
    'f': {0,1,2},
    'g': {0,1,2,3},
    'h': {0,2,3},
    'i': {1,2},
    'j': {1,2,3},
    'k': {0,4},
    'l': {0,2,4},
    'm': {0,1,4},
    'n': {0,1,3,4},
    'o': {0,3,4},
    'p': {0,1,2,4},
    'q': {0,1,2,3,4},
    'r': {0,2,3,4},
    's': {1,2,4},
    't': {1,2,3,4},
    'u': {0,4,5},
    'v': {0,2,4,5},
    'w': {1,2,3,5},
    'x': {0,1,4,5},
    'y': {0,1,3,4,5},
    'z': {0,3,4,5},
    ' ': {},
    '.': {2,3,5},
    ',': {2},
    '?': {2,4,5},
    '!': {2,3,4},
    ':': {2,3},
    ';': {2,4},
    '-': {4,5},
    '/': {1,4},
    '<': {1,2,5},
    #'>': {0,3,4}, remove since this has a conflict with 'o'
    '(': {0,2,5},
    ')': {1,3,4}
}

# Digits mapping to characters
digit_to_char = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '0': 'j',
}

char_to_digit = {v: k for k, v in digit_to_char.items()}

def dots_to_pattern(dots):
    pattern = ['.' for _ in range(6)]
    for i in range(6):
        if i in dots:
            pattern[i] = 'O'
    return ''.join(pattern)

def pattern_to_dots(pattern):
    dots = []
    for index, char in enumerate(pattern):
        if char == 'O':
            dot = index_to_dot(index)
            dots.append(dot)
    return dots

def dot_to_index(dot):
    dot_to_index_map = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5}
    return dot_to_index_map[dot]

def index_to_dot(index):
    index_to_dot_map = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6}
    return index_to_dot_map[index]


capital_sign_dots = {5}
number_sign_dots = {1,3,4,5}


capital_sign_pattern = dots_to_pattern(capital_sign_dots)
number_sign_pattern = dots_to_pattern(number_sign_dots)
space_pattern = dots_to_pattern({})


pattern_to_char = {}
for char, dots in char_to_dots.items():
    pattern = dots_to_pattern(dots)
    pattern_to_char[pattern] = char

def is_braille(s):
    return all(c in ('O', '.', ' ') for c in s)

def braille_to_english(s):
    s = s.replace(' ', '')
    if len(s) % 6 != 0:
        sys.exit('Invalid number of length')
    patterns = [s[i:i+6] for i in range(0, len(s), 6)]
    output = ''
    capital_flag = False
    number_flag = False
    for pattern in patterns:
        if pattern == capital_sign_pattern:
            capital_flag = True
            continue
        elif pattern == number_sign_pattern:
            number_flag = True
            continue
        elif pattern == space_pattern:
            output += ' '
            number_flag = False  # Reset number flag after space
        elif pattern in pattern_to_char:
            char = pattern_to_char[pattern]
            if number_flag:
                if char in char_to_digit:
                    output += char_to_digit[char]
                else:
                    sys.exit('Incorrect flag ahead')
            else:
                if capital_flag:
                    output += char.upper()
                    capital_flag = False
                else:
                    output += char
        else:
            sys.exit('Incorrect Braille pattern')
    return output

def english_to_braille(s):
    output_patterns = []
    idx = 0
    while idx < len(s):
        c = s[idx]
        if c == ' ':
            output_patterns.append(space_pattern)
            idx += 1
            continue
        if c.isupper():
            output_patterns.append(capital_sign_pattern)
            c = c.lower()
        if c.isdigit():
            output_patterns.append(number_sign_pattern)
            while idx < len(s) and s[idx].isdigit():
                digit = s[idx]
                letter = digit_to_char[digit]
                pattern = dots_to_pattern(char_to_dots[letter])
                output_patterns.append(pattern)
                idx += 1
            continue
        if c in char_to_dots:
            pattern = dots_to_pattern(char_to_dots[c])
            output_patterns.append(pattern)
        else:
            sys.exit()
        idx += 1
    return ''.join(output_patterns)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit()
    inputs = sys.argv[1:]
    if is_braille(inputs[0]):
        input_str = '......'.join(inputs)
        output_str = braille_to_english(input_str)
    else:
        input_str = ' '.join(inputs)
        output_str = english_to_braille(input_str)

    print(output_str)
