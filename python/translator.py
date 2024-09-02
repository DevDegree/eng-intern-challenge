import sys

# dictionary that stores the alphabet character to braille mapping
char_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

# dictionary that stores the special characters to braille mapping
special_chars = {
    ',': '.O....', ';': '.OO...', ':': '.O.O..', '.': '.O.OO.', '!': '.OO.O.', 
    '?': '.OO..O', '-': '..O.O.', '/': '.O.O..', '(': '.O.O.O', ')': 'O..O.O', 
    '<': 'OO...O', '>': '..OO.O', 'capital_indicator': '.....O', 'number_indicator': '.O.OOO'
}

# dictionary that stores the numbers to braille mapping
digit_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# reverse mappings for braille to english 
braille_to_char = {v: k for d in (char_to_braille, special_chars) for k, v in d.items()}
braille_to_digit = {v: k for k, v in digit_to_braille.items()}

#converts braille string to english text
def braille_to_english(braille_str):
    output = []
    index = 0
    capitalize = False
    is_number = False

    while index < len(braille_str):
        segment = braille_str[index:index+6]
        if segment == special_chars['capital_indicator']:
            capitalize = True
        elif segment == special_chars['number_indicator']:
            is_number = True
        elif segment in braille_to_char:
            character = braille_to_char[segment]
            if is_number and segment in braille_to_digit:
                output.append(braille_to_digit[segment])
            else:
                if capitalize:
                    character = character.upper()
                    capitalize = False
                output.append(character)
            if character == ' ':
                is_number = False
        index += 6

    return ''.join(output)

#converts english text to braille string
def english_to_braille(text):
    output = []
    is_number = False

    for character in text:
        if character.isupper():
            output.append(special_chars['capital_indicator'])
            character = character.lower()

        if character.isdigit():
            if not is_number:
                output.append(special_chars['number_indicator'])
                is_number = True
            output.append(digit_to_braille[character])
        else:
            output.append(char_to_braille.get(character, special_chars.get(character, '')))
            if character == ' ':
                is_number = False

    return ''.join(output)

#checks if the input text is in braille format
def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

#does the conversion between braille to english and vice versa
def convert(text):
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
        print(convert(input_string), end='')
    else:
        print("Please provide a string to translate.")