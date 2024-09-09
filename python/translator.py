import argparse

braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', 
}

number_map = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..', 
    '8': 'O.OO..',
    '9': '.OO...',
}

capital_indicator = '.....O'
number_indicator = '.O.OOO'


def translate_to_braille(text):
    braille = ''
    is_number = False

    for char in text:
        if char.isupper():
            braille += capital_indicator
            char = char.lower()

        if char.isdigit():
            if not is_number:
                braille += number_indicator
                is_number = True
            braille += number_map.get(char, '')
        else:
            if is_number:
                is_number = False
            braille += braille_map.get(char, '')

    return braille

def translate_to_english(braille):
    english = ''
    is_capital = False
    is_number = False

    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]

    braille_to_english = {v: k for k, v in braille_map.items()}
    braille_to_number = {v: k for k, v in number_map.items()}

    for braille_char in braille_chars:

        if braille_char == capital_indicator:
            is_capital = True
            continue
        if braille_char == number_indicator:
            is_number = True
            continue
        if braille_char == '......': 
            english += ' '
            is_number = False 
            continue
        if is_number:
            letter = braille_to_number.get(braille_char, '')
            english +=letter
            continue
            
        letter = braille_to_english.get(braille_char, '')
        if is_capital:
            letter = letter.upper()
            is_capital = False
        english += letter

    return english


def detect(text):
    if all(c in 'O.' for c in text):
        return translate_to_english(text)
    else:
        return translate_to_braille(text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('text', nargs='*')

    args = parser.parse_args()
    input_text = ' '.join(args.text)
    result = detect(input_text)
    print(f"{result}")

if __name__ == "__main__":
    main()