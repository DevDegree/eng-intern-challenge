
import sys

# Braille alphabet and special symbols
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '.O.OOO', ',': '.O....', '?': '.OO.OO', '!': '.O.OO.', ';': '.OO...',
    'capital': '.....O', 'number': '.O.O..'
}

# Reverse dictionary for braille to english
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Check if the input is Braille
def is_braille(text):
    return all(c in {'O', '.', ' '} for c in text)

# For Converting English to Braille
def english_to_braille(text):
    result = []
    for char in text:
        if char.isdigit():
            result.append(braille_dict['number'])
        elif char.isupper():
            result.append(braille_dict['capital'])
        result.append(braille_dict[char.lower()])
    return ''.join(result)

# For converting Braille to English
def braille_to_english(braille_text):
    braille_chars = [braille_text[i:i + 6] for i in range(0, len(braille_text), 6)]
    result = []
    capital_next = False
    number_next = False

    for char in braille_chars:
        if char == braille_dict['capital']:
            capital_next = True
        elif char == braille_dict['number']:
            number_next = True
        else:
            if capital_next:
                result.append(reverse_braille_dict[char].upper())
                capital_next = False
            elif number_next:
                result.append(reverse_braille_dict[char])
                number_next = False
            else:
                result.append(reverse_braille_dict[char])
    return ''.join(result)

# Main function to detect input type and translate
def translate(input_str):
    if is_braille(input_str):
        return braille_to_english(input_str)
    else:
        return english_to_braille(input_str)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        sys.exit(1)

    input_str = sys.argv[1]
    output = translate(input_str)
    print(output)
