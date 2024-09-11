import sys

english2braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'cap': '.....O', 'num': '.O.OOO',
}

braille2alphabet = {v: k for k, v in english2braille.items() if k.isalpha()}
braille2digit = {v: k for k, v in english2braille.items() if k.isdigit()}


def to_braille(input_str):
    result = []
    index = 0
    while index < len(input_str):
        char = input_str[index]
        if char.isupper():
            result.append(english2braille['cap'])
            char = char.lower()
        elif char.isdigit():
            result.append(english2braille['num'])
            while index < len(input_str) and input_str[index].isdigit():
                result.append(english2braille[input_str[index]])
                index += 1
            continue
        result.append(english2braille.get(char, '......'))
        index += 1
    return ''.join(result)


def to_english(braille_str):
    result = []
    index = 0
    while index < len(braille_str):
        symbol = braille_str[index:index + 6]

        if symbol == english2braille['num']:
            index += 6
            while index < len(braille_str):
                symbol = braille_str[index:index + 6]
                if symbol not in braille2digit:
                    break
                result.append(braille2digit[symbol])
                index += 6
            continue

        if symbol == english2braille['cap']:
            index += 6
            symbol = braille_str[index:index + 6]
            result.append(braille2alphabet.get(symbol, ' ').upper())
        else:
            result.append(braille2alphabet.get(symbol, ' '))
        index += 6
    return ''.join(result)


def detect_and_translate(input_str):
    if all(c in 'O.' for c in input_str) and len(input_str) % 6 == 0:
        return to_english(input_str)
    return to_braille(input_str)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])
    print(detect_and_translate(input_str))
