
import sys

#  mapping of letters and numbers to Braille
braille_alphabet = {
    'a': [1],
    'b': [1,2],
    'c': [1,4],
    'd': [1,4,5],
    'e': [1,5],
    'f': [1,2,4],
    'g': [1,2,4,5],
    'h': [1,2,5],
    'i': [2,4],
    'j': [2,4,5],
    'k': [1,3],
    'l': [1,2,3],
    'm': [1,3,4],
    'n': [1,3,4,5],
    'o': [1,3,5],
    'p': [1,2,3,4],
    'q': [1,2,3,4,5],
    'r': [1,2,3,5],
    's': [2,3,4],
    't': [2,3,4,5],
    'u': [1,3,6],
    'v': [1,2,3,6],
    'w': [2,4,5,6],
    'x': [1,3,4,6],
    'y': [1,3,4,5,6],
    'z': [1,3,5,6],
}

# Numbers 1-0 correspond to letters a-j with a number sign prefix
braille_numbers = {
    '1': braille_alphabet['a'],
    '2': braille_alphabet['b'],
    '3': braille_alphabet['c'],
    '4': braille_alphabet['d'],
    '5': braille_alphabet['e'],
    '6': braille_alphabet['f'],
    '7': braille_alphabet['g'],
    '8': braille_alphabet['h'],
    '9': braille_alphabet['i'],
    '0': braille_alphabet['j'],
}

# Special Braille characters
capital_sign = [6]
number_sign = [3,4,5,6]
space_sign = []

# Map dot positions to indices in the 6-character string
dot_to_index = {
    1: 0,
    2: 2,
    3: 4,
    4: 1,
    5: 3,
    6: 5,
}

def dots_to_braille(dots):
    braille = ['.' for _ in range(6)]
    for dot in dots:
        index = dot_to_index[dot]
        braille[index] = 'O'
    return ''.join(braille)

def is_braille_input(input_str):
    return all(c in {'O', '.', ' '} for c in input_str)

def translate_to_braille(text):
    result = []
    words = text.split(' ')
    for word in words:
        i = 0
        while i < len(word):
            char = word[i]
            if char.isupper():
                result.append(dots_to_braille(capital_sign))
                char = char.lower()
            if char.isdigit():
                result.append(dots_to_braille(number_sign))
                while i < len(word) and word[i].isdigit():
                    num_char = word[i]
                    dots = braille_numbers[num_char]
                    result.append(dots_to_braille(dots))
                    i += 1
                continue
            elif char.isalpha():
                dots = braille_alphabet[char]
                result.append(dots_to_braille(dots))
            i += 1
        result.append(dots_to_braille(space_sign))  
    return ''.join(result).rstrip('.')

def braille_to_dots(braille_str):
    dots = []
    for i, c in enumerate(braille_str):
        if c == 'O':
            index = i % 6
            for dot, idx in dot_to_index.items():
                if idx == index:
                    dots.append(dot)
                    break
    return sorted(dots)

def translate_to_english(braille):
    result = []
    i = 0
    chars = [braille[j:j+6] for j in range(0, len(braille), 6)]
    capitalize_next = False
    number_mode = False
    while i < len(chars):
        braille_char = chars[i]
        dots = braille_to_dots(braille_char)
        if dots == capital_sign:
            capitalize_next = True
        elif dots == number_sign:
            number_mode = True
        elif dots == space_sign:
            result.append(' ')
            number_mode = False
        else:
            if number_mode:
                for key, value in braille_numbers.items():
                    if value == dots:
                        result.append(key)
                        break
            else:
                for key, value in braille_alphabet.items():
                    if value == dots:
                        char = key.upper() if capitalize_next else key
                        result.append(char)
                        break
            capitalize_next = False
        i += 1
    return ''.join(result)

def main():
    args = sys.argv[1:]
    input_str = ' '.join(args)
    if is_braille_input(input_str):
        # Input is Braille, translate to English
        print(translate_to_english(input_str))
    else:
        # Input is English, translate to Braille
        print(translate_to_braille(input_str))

if __name__ == '__main__':
    main()
