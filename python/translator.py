import sys

# English to braille
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'CAPITAL': '.....O', 'DECIMAL': '.O...O', 'NUMBER': '.O.OOO', '.': '..OO.O',
    ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '>': 'O..OO.', '<': '.OO..O', '(': 'O.O..O',
    ')': '.O.OO.', ' ': '......'
}

def translate_to_braille(text):
    braille_text = ""
    isNumber = False
    for char in text:
        if char.isnumeric() and not isNumber:
            braille_text += braille_map['NUMBER']
            isNumber = True
        if char.isupper():
            braille_text += braille_map['CAPITAL']
        if char.lower() in braille_map:
            braille_text += braille_map[char.lower()]
        elif char == " ":
            braille_text += braille_map[' ']
            isNumber = False
    return braille_text

def main():
    if len(sys.argv) < 2:
        print("Translator requires at least one argument")
        sys.exit(1)
    input_text = ' '.join(sys.argv[1:])

    braille_pattern = r'^[.O]*$'

    if(re.search(braille_pattern, input_text)):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()