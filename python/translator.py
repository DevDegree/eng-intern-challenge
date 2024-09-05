import sys

braille_alphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......"
}
braille_numbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}
braille_capital = ".....O"
braille_number = ".O.OOO"


def is_braille(text):
    return all(char in 'O.' for char in text)


def b2e(text):
    inverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
    inverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

    i = 0
    res = []
    is_number_mode = False
    while i < len(text):
        char = text[i:i + 6]
        if char == braille_capital:
            next_char = text[i + 6:i + 12]
            res.append(inverse_braille_alphabet.get(next_char, "").upper())
            i += 12
        elif char == braille_number:
            is_number_mode = True
            i += 6
        elif char == "......":
            res.append(" ")
            is_number_mode = False
            i += 6
        else:
            if is_number_mode:
                res.append(inverse_braille_numbers.get(char, ""))
            else:
                res.append(inverse_braille_alphabet.get(char, ""))
            i += 6
    print('res', res)
    return ''.join(res)


def e2b(text):
    res = []
    is_number_mode = False
    for char in text:
        if char.isdigit():
            if not is_number_mode:
                res.append(braille_number)
                is_number_mode = True
            res.append(braille_numbers[char])
        elif char.isalpha():
            is_number_mode = False
            if char.isupper():
                res.append(braille_capital)
                res.append(braille_alphabet[char.lower()])
            else:
                res.append(braille_alphabet[char])
        elif char == ' ':
            is_number_mode = False
            res.append("......")
    return ''.join(res)


def main():
    if len(sys.argv) < 2:
        print('Usage: python translator.py <input_string>')
        return

    input_string = ' '.join(sys.argv[1:]).strip()

    if is_braille(input_string):
        print(b2e(input_string))
    else:
        print(e2b(input_string))


if __name__ == "__main__":
    main()
