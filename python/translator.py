import sys

# English to Braille Mappings
text_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.',
    'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', 
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO',
}

# Braille to English Mappings
braille_to_text_map = {}
for key, value in text_to_braille_map.items():
    braille_to_text_map[value] = key


def to_english(braille_text):
    result = []
    i = 0

    # keeps track of numbers and capital letters
    is_capital = False
    is_number = False

    while i < len(braille_text):
        symbol = braille_text[i:i+6]
        if symbol == text_to_braille_map['capital']:
            is_capital = True
        elif symbol == text_to_braille_map['number']:
            is_number = True
        else:
            if is_capital:
                result.append(braille_to_text_map[symbol].upper())
                is_capital = False
            elif is_number and braille_to_text_map[symbol].isdigit():
                result.append(braille_to_text_map[symbol])
            else:
                result.append(braille_to_text_map[symbol])
            is_number = False
        i += 6
    return ''.join(result)

def to_braille(text):

    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(text_to_braille_map['capital'])
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                result.append(text_to_braille_map['number'])
                number_mode = True
        else:
            number_mode = False
        result.append(text_to_braille_map.get(char, ''))
    
    return ''.join(result)


# Check if the input is Braille or English
def is_braille(input_str):
    for c in input_str:
        if c not in 'O.':
            return False
    return True

def main():
    input_text = ' '.join(sys.argv[1:]).strip()

    # chooses which translation is requried
    if is_braille(input_text):
        result = to_english(input_text)
    else:
        result = to_braille(input_text)
    
    # output translation
    print(result)

if __name__ == "__main__":
    main()

    
