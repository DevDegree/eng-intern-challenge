import sys

# Braille dictionary
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO'
}

number_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
}

# Reverse dictionary for Braille to English
reverse_braille = {v: k for k, v in braille_map.items()}
reverse_number = {v: k for k, v in number_map.items()}

def check_braille(s):
    valid = "O."
    for c in s:
        if c not in valid:
            return False
    return True

def braille_to_english(s):
    output = []
    number = False
    capital = False
    for i in range(0,len(s),6):
        token = s[i:i+6]
        if reverse_braille[token] == "capital":
            capital = True
            continue
        if reverse_braille[token] == "number":
            number = True
            continue
        if number:
            ch = reverse_number[token]
            if ch == " ":
                number = False
            output.append(ch)
            continue
        if capital:
            ch = reverse_braille[token]
            ch = ch.upper()
            output.append(ch)
            capital = False
            continue
        output.append(reverse_braille[token])
    return "".join(output)

def english_to_braille(s):
    output = []
    number = False
    for c in s:
        if c.isupper():
            output.append(braille_map["capital"])
            output.append(braille_map[c.lower()])
            continue
        if c.isdigit():
            if not number:
                number = True
                output.append(braille_map["number"])
            output.append(number_map[c])
            continue
        number = False
        output.append(braille_map[c])
    return "".join(output)

input_string = ' '.join(sys.argv[1:])
    
if check_braille(input_string):
    print(braille_to_english(input_string))
else:
    print(english_to_braille(input_string))
