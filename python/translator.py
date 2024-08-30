import sys

english_to_braille = {
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
    'capital_follows': '.....O',
    'number_follows':  '.O.OOO',
    ' ': '......',
}

braille_to_english = {v: k for k, v in english_to_braille.items()}

def translate_to_english(input_string):
    translated_string = ""
    capital_follows = False
    number_follows = False

    for i in range(0, len(input_string), 6):
        braille_symbol = input_string[i:i+6]

        english_char = braille_to_english[braille_symbol]

        if english_char == 'capital_follows':
            capital_follows = True
            continue
        elif english_char == 'number_follows':
            number_follows = True
            continue
        elif english_char == ' ':
            number_follows = False
            translated_string += ' '
            continue

        if number_follows:
            number = str(ord(english_char) - ord('a') + 1)
            if number == '10':
                number = '0'
            translated_string += number
        elif capital_follows:
            translated_string += english_char.upper()
            capital_follows = False
        else:
            translated_string += english_char

    return translated_string

def translate_to_braille(input_string):
    translated_string = ""
    number_follows = False
    
    for char in input_string:
        if char.isupper():
            translated_string += english_to_braille['capital_follows']
            translated_string += english_to_braille[char.lower()]
        elif char.isdigit():
            if not number_follows:
                translated_string += english_to_braille['number_follows']
                number_follows = True
            number = str(ord(char) - ord('0'))
            if number == '0':
                number = '10'
            translated_string += english_to_braille[chr(ord('a') + int(number) - 1)]
        elif char == ' ':
            translated_string += english_to_braille[' ']
            number_follows = False
        else:
            translated_string += english_to_braille[char]

    return translated_string

def is_braille(input_string):
    if len(input_string) % 6 != 0:
        return False
    return all(char in {'O', '.'} for char in input_string)

def main():
    input_string = " ".join(sys.argv[1:])
    result = ""

    if is_braille(input_string):
        result = translate_to_english(input_string)
    else:
        result = translate_to_braille(input_string)

    print(result)

if __name__ == "__main__":
    main()
