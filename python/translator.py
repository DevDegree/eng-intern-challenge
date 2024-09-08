import sys

braille_alphabet = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    'cap': ".....O",
    'num': ".O.OOO",
    ' ': "......",
    '0': ".OOO..",
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO..."
}


def english_to_braille(input_str):
    result = []
    number_mode = False
    for char in input_str:
        if char.isdigit():
            if not number_mode:
                result.append(braille_alphabet['num'])
                number_mode = True
            result.append(braille_alphabet[char])
        elif char.isalpha():
            if char.isupper():
                result.append(braille_alphabet['cap'])
                result.append(braille_alphabet[char.lower()])
            else:
                result.append(braille_alphabet[char])
            number_mode = False
        elif char == ' ':
            result.append(braille_alphabet[' '])
            number_mode = False
    return ''.join(result)


def braille_to_english(braille_str):
    reverse_braille_letters = {
        v: k for k, v in braille_alphabet.items() if k.isalpha() or k == ' '}
    reverse_braille_numbers = {
        v: k for k, v in braille_alphabet.items() if k.isdigit() or k == ' '}

    result = []
    number_mode = False
    capital_mode = False
    for i in range(0, len(braille_str), 6):
        symbol = braille_str[i:i+6]
        if symbol == braille_alphabet['num']:
            number_mode = True
            continue
        elif symbol == braille_alphabet['cap']:
            capital_mode = True
            continue

        if number_mode:
            result.append(reverse_braille_numbers[symbol])
        else:
            char = reverse_braille_letters[symbol]
            if capital_mode:
                result.append(char.upper())
                capital_mode = False
            else:
                result.append(char)

        if symbol == braille_alphabet[' ']:
            number_mode = False
    return ''.join(result)


def main():
    args = sys.argv[1:]
    input_str = ' '.join(args)

    if all(c in ['O', '.'] for c in input_str) and len(input_str) % 6 == 0:
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))


if __name__ == "__main__":
    main()
