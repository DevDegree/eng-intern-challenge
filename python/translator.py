import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O.OO..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O.OOO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O.OOOO', ' ': '......', '0': '.O.OO.', '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..', '5': 'O.OO..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '.': '......', ',': '......', '?': '......'
}

reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def english_to_braille(text):
    braille_text = ""
    for char in text:
        if char.isupper():
            braille_text += 'O.O...O...O.....'  # Capital indicator
        if char.lower() in braille_dict:
            braille_text += braille_dict[char.lower()]
        elif char == ' ':
            braille_text += braille_dict[' ']
        else:
            braille_text += '......'  # For any unexpected characters
    return braille_text

def braille_to_english(text):
    english_text = ""
    i = 0
    while i < len(text):
        if text[i:i+6] == 'O.O...O...O.....':  # Capital indicator
            i += 6
            if i + 6 <= len(text):
                braille_char = text[i:i+6]
                english_text += reverse_braille_dict.get(braille_char, '?').upper()
                i += 6
        else:
            braille_char = text[i:i+6]
            english_text += reverse_braille_dict.get(braille_char, '?')
            i += 6
    return english_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 translator.py <string>")
        sys.exit(1)
    
    input_string = sys.argv[1]
    print(f"Debug: Input string = '{input_string}'")  # Debug print

    if all(c in 'O.' for c in input_string):
        # Input is Braille
        output = braille_to_english(input_string)
    else:
        # Input is English
        output = english_to_braille(input_string)
    
    print(f"Debug: Output = '{output}'")  # Debug print
    print(output)

if __name__ == '__main__':
    main()
