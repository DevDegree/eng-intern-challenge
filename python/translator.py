from sys import argv
from types import SimpleNamespace
from itertools import islice

# Upper cell Braille symbols encoded in binary in reverse(i.e. 'OO..O.' maps to '010011' in binary)
UPPER_CELL = (1, 0b101, 0b11, 0b1011, 0b1001, 0b111, 0b1111, 0b1101, 0b110, 0b1110)

A_J = UPPER_CELL
K_T = tuple(cell | 0b10000 for cell in UPPER_CELL)
U_Z = (*(cell | 0b110000 for cell in UPPER_CELL[:2]), 0b101110, *(cell | 0b110000 for cell in UPPER_CELL[2:5]))

english = SimpleNamespace()
english.LETTERS = A_J + K_T + U_Z
english.NUMBERS = UPPER_CELL

braille = SimpleNamespace()
braille.LETTERS = {cell: chr(i + ord('a')) for i, cell in enumerate(english.LETTERS)}
braille.NUMBERS = {cell: str(i + 1) for i, cell in enumerate(english.NUMBERS)}

braille.CAPITAL_FOLLOWS = 0b100000
braille.NUMBER_FOLLOWS = 0b111010
braille.SPACE = 0


def isbraille(s):
    if not isinstance(s, str):
        raise TypeError("Argument is not a str")
    return all(c in '.O' for c in s) and not len(s) % 6


def binary_braille(s):
    """
    Converts a braille sequence to a binary number.

    :param s: a string representing a braille character
    :return: a binary number
    """
    if not isinstance(s, str):
        raise TypeError("Argument is not a str")
    if not isbraille(s) and len(s) != 6:
        raise ValueError("Argument is not in braille.")

    bb = 0
    for c in s[::-1]:
        bb <<= 1
        if c == 'O':
            bb |= 1
    return bb


def braille_ify(b):
    """
    Converts a binary number to the braille version.

    :param b: a binary number
    :return: a braille character
    """
    if not isinstance(b, int):
        raise TypeError("Argument is not a number")

    bl = []
    b_copy = b
    while b_copy:
        if b_copy & 1:
            bl.append('O')
        else:
            bl.append('.')
        b_copy >>= 1
    return ''.join(bl).ljust(6, '.')


def braille_to_english(s):
    if not isinstance(s, str):
        raise TypeError("Argument is not a str")
    if not isbraille(s):
        raise ValueError("Argument is not in braille.")

    flag = -1
    iterator = iter(s)
    while batch := ''.join(islice(iterator, 6)):
        bb = binary_braille(batch)
        if bb == braille.SPACE:
            yield ' '
            flag = -1
        elif flag == braille.CAPITAL_FOLLOWS:
            yield braille.LETTERS[bb].upper()
            flag = -1
        elif flag == braille.NUMBER_FOLLOWS:
            yield braille.NUMBERS[bb]
        elif bb in (braille.CAPITAL_FOLLOWS, braille.NUMBER_FOLLOWS):
            flag = bb
        else:
            yield braille.LETTERS[bb]


def english_to_braille(s):
    if not isinstance(s, str):
        raise TypeError("Argument is not a str")

    flag = False
    for c in s:
        if c.isalpha():
            if c.isupper():
                yield braille_ify(braille.CAPITAL_FOLLOWS)
            index = ord(c.lower()) - ord('a')
            yield braille_ify(english.LETTERS[index])
        elif c.isdigit():
            if not flag:
                yield braille_ify(braille.NUMBER_FOLLOWS)
                flag = True
            yield braille_ify(english.NUMBERS[int(c) - 1])
        else:
            yield braille_ify(braille.SPACE)
            flag = False


def main():
    s = ' '.join(argv[1:])
    result = braille_to_english(s) if isbraille(s) else english_to_braille(s)
    print(''.join(result))


if __name__ == '__main__':
    main()
