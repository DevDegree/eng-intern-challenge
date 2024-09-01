import sys, re

# English to braille dict
braille_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'CAPITAL': '.....O', 'DECIMAL': '.O...O', 'NUMBER': '.O.OOO', '.': '..OO.O',
    ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '(': 'O.O..O',
    ')': '.O.OO.', ' ': '......'
}

# braille to English dict
english_map = {n: i for i, n in braille_map.items()}

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

def translate_to_english(text):
    english_text = ""
    braille_chars = [text[i:i+6] for i in range(0, len(text), 6)]
    isCapital, isNumber = False, False
    for braille in braille_chars:
        if braille == braille_map['CAPITAL']:
            isCapital = True
            continue
        elif braille == braille_map['NUMBER']:
            isNumber = True
            continue
        elif braille == braille_map[' ']:
            english_text += " "
            isNumber = False
            continue
        else:
            if(isNumber):
                english_text += str(ord(english_map[braille]) - 96)
                continue
            elif(isCapital):
                english_text += english_map[braille].upper()
                isCapital = False
                continue
            else:
                english_text += english_map[braille]
    return english_text


def main():
    # Checks if a string has been passed to the CLI
    if len(sys.argv) < 2:
        print("Translator requires at least one argument")
        sys.exit(1)

    # Takes all arguments passed in, and joins them with a space in between
    input_text = ' '.join(sys.argv[1:])

    # regex for "." and "O"
    braille_pattern = r'^[.O]*$'

    # If text is braille convert to English, otherwise do the opposite
    if(re.search(braille_pattern, input_text)):
        try:
            print(translate_to_english(input_text))
        except (KeyError):
            print("Braille letter not found")
    else:
        try:
            print(translate_to_braille(input_text))
        except:
            print("Please enter a valid string")

if __name__ == "__main__":
    main()