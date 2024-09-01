import sys

braille_chars = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
}

braille_nums = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

braille_rules = {
  'capital_follows': '.....O',
  'number_follows': '.O.OOO',
}

def is_braille(input):
    if all(char in 'O.' for char in input):
        if len(input) % 6 == 0:
            return True
    return False

def english_to_braille(text):
    result = []
    is_number_mode = False
    for char in text:
        if char.isupper():
            result.append(braille_rules['capital_follows'])
            char = char.lower()
        if char.isdigit():
            if not is_number_mode:
                result.append(braille_rules['num'])
                is_number_mode = True
            result.append(braille_nums[char])
        else:
            if is_number_mode:
                is_number_mode = False
            result.append(braille_chars[char])
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    while i < len(braille):
        
        six_chars = braille[i:i+6]
        if six_chars == braille_rules['capital_follows']:
            i += 6 
            six_chars = braille[i:i+6]
            result.append(find_letter(six_chars).upper())
        elif six_chars == braille_rules['number_follows']:
            i += 6
            six_chars = braille[i:i+6]
            result.append(find_number(six_chars))
        else:
            result.append(find_letter(six_chars))
        i += 6
    return ''.join(result)

def find_letter(str):
    for k,v in braille_chars.items():
        if str == v:
            return k
        
def find_number(str):
    for k,v in braille_nums.items():
        if str == v:
            return k

def detect_and_translate(input):
    if is_braille(input):
        return braille_to_english(input)
    else:
        return english_to_braille(input)

if __name__ == "__main__":
    input = " ".join(sys.argv[1:])
    output = detect_and_translate(input)
    print(output)