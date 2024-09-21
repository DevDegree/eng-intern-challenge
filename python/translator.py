import sys

braille_alpha = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Braille special symbols
braille_capital = '.....O'
braille_number = '.O.OOO'

# Reverse mappings
reverse_braille_alpha = {v: k for k, v in braille_alpha.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(text):
    # Check if the input is Braille (contains only 'O' and '.')
    return all(c in 'O.' for c in text)

def translate_to_braille(text):
    result = []
    number_mode = False  # Track if we're in number mode
    for char in text:
        if char.isupper():
            result.append(braille_capital)  # Append capital symbol for uppercase letters
            result.append(braille_alpha[char.lower()])
            number_mode = False  # Exit number mode when encountering a letter
        elif char.isdigit():
            if not number_mode:
                result.append(braille_number)  # Append number symbol once for digits
                number_mode = True
            result.append(braille_numbers[char])
        else:
            result.append(braille_alpha[char])
            number_mode = False  # Exit number mode when encountering a non-number
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_capital:
            i += 6
            symbol = braille[i:i+6]
            result.append(reverse_braille_alpha[symbol].upper())
        elif symbol == braille_number:
            i += 6
            while i < len(braille) and braille[i:i+6] in reverse_braille_numbers:
                symbol = braille[i:i+6]
                result.append(reverse_braille_numbers[symbol])
                i += 6
            continue
        else:
            result.append(reverse_braille_alpha[symbol])
        i += 6
    return ''.join(result)

def translate(text):
    if is_braille(text):
        return translate_to_english(text)
    else:
        return translate_to_braille(text)
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide input arguments.")
    else:
        elements = sys.argv[1:]  # All arguments after the script name
        res = ""
        for i in range(len(elements) - 1):
            res += translate(elements[i]) + translate(" ")

        res += translate(elements[-1])

        print(res)