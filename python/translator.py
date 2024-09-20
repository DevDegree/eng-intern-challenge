import sys

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
}
NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}
SPECIAL_BRAILLE = {
    'capital_next': '.....O', 'number_next': '.O.OOO',
}
BRAILLE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {value: key for key, value in NUMBER_TO_BRAILLE.items()}


def is_braille(string: str) -> bool:
    for char in string:
        if char not in ".O":
            return False
    return len(string) % 6 == 0


def to_braille(string: str) -> str:
    braille = ""
    digit_mode = False
    for char in string:
        if char.isupper():
            braille += SPECIAL_BRAILLE['capital_next']
            braille += ENGLISH_TO_BRAILLE[char.lower()]
            digit_mode = False
        elif char.isdigit():
            if not digit_mode:
                braille += SPECIAL_BRAILLE['number_next']
                digit_mode = True
            braille += NUMBER_TO_BRAILLE[char]
        else:
            braille += ENGLISH_TO_BRAILLE[char]
            digit_mode = False
    return braille


def to_english(string: str) -> str:
    english = ""
    digit_mode = False
    capital_mode = False
    for i in range(0, len(string), 6):
        braille = string[i: i+6]
        if braille == SPECIAL_BRAILLE['capital_next']:
            capital_mode = True
            digit_mode = False
        elif braille == SPECIAL_BRAILLE['number_next']:
            digit_mode = True
            capital_mode = False
        else:
            if digit_mode:
                if braille == ENGLISH_TO_BRAILLE[' ']:
                    digit_mode = False
                    capital_mode = False
                    english += " "
                else:
                    english += BRAILLE_TO_NUMBER[braille]
            else:
                if capital_mode:
                    english += BRAILLE_TO_ENGLISH[braille].upper()
                else:
                    english += BRAILLE_TO_ENGLISH[braille]
                capital_mode = False
    return english


def main():
    args = sys.argv[1:]
    string = " ".join(args)
    if is_braille(string):
        print(to_english(string))
    else:
        print(to_braille(string))


# def tests():
#     assert to_braille(
#         "Hello world") == ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
#     assert to_english(
#         ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..") == "Hello world"

#     assert to_braille("42") == ".O.OOOOO.O..O.O..."
#     assert to_english(".O.OOOOO.O..O.O...") == "42"

#     assert to_braille(
#         "Abc 123") == ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
#     assert to_english(
#         ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....") == "Abc 123"

#     assert to_braille(
#         "Abc 123 xYz") == ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
#     assert to_english(
#         ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO") == "Abc 123 xYz"

#     t = "Nabil Mansour 1311233 adasd 131 1312 asdas awasdasASADJahsjHAJSJHJAJHAHJ2131312 a"
#     assert to_english(to_braille(t)) == t

#     print("All tests good")


if __name__ == '__main__':
    # tests()
    main()
