
import sys


NON_NUMBERS = set(
    [("a", "O....."),
    ("b", "O.O..."),
    ("c", "OO...."),
    ("d", "OO.O.."),
    ("e", "O..O.."),
    ("f", "OOO..."),
    ("g", "OOOO.."),
    ("h", "O.OO.."),
    ("i", ".OO..."),
    ("j", ".OOO.."),
    ("k", "O...O."),
    ("l", "O.O.O."),
    ("m", "OO..O."),
    ("n", "OO.OO."),
    ("o", "O..OO."),
    ("p", "OOO.O."),
    ("q", "OOOOO."),
    ("r", "O.OOO."),
    ("s", ".OO.O."),
    ("t", ".OOOO."),
    ("u", "O...OO"),
    ("v", "O.O.OO"),
    ("w", ".OOO.O"),
    ("x", "OO..OO"),
    ("y", "OO.OOO"),
    ("z", "O..OOO"),
    (" ", "......")]
)

    
NUMBERS = set(
    [("0", ".OOO.."),
    ("1", "O....."),
    ("2", "O.O..."),
    ("3", "OO...."),
    ("4", "OO.O.."),
    ("5", "O..O.."),
    ("6", "OOO..."),
    ("7", "OOOO.."),
    ("8", "O.OO.."),
    ("9", ".OO...")]
)

    

MODIFIERS = set(
    [("capital", ".....O"),
    ("number", ".O.OOO")]
)

def generate_braille_dicts():
    non_numbers = {}
    for letter, braille in NON_NUMBERS:
        non_numbers[braille] = letter

    numbers = {}
    for number, braille in NUMBERS:
        numbers[braille] = number

    modifiers = {}
    for modifier, braille in MODIFIERS:
        modifiers[braille] = modifier

    return non_numbers, numbers, modifiers


def generate_eng_dicts():
    non_numbers = {}
    for letter, braille in NON_NUMBERS:
        non_numbers[letter] = braille

    numbers = {}
    for number, braille in NUMBERS:
        numbers[number] = braille

    modifiers = {}
    for modifier, braille in MODIFIERS:
        modifiers[modifier] = braille

    return non_numbers, numbers, modifiers


def is_braille(input):
    return all((char == "." or char == "O") for char in input)


def translate_braille(braille):
    non_numbers, numbers, modifiers = generate_braille_dicts()

    is_number = False
    is_capital = False

    acc = ""

    for i in range(0, len(braille), 6):
        char = braille[i:i+6]

        if char in modifiers:
            is_number = "number" == modifiers[char]
            is_capital = "capital" == modifiers[char]
            continue


        if is_number:
            if " " == non_numbers[char]:
                acc += non_numbers[char]
                is_number = False
                continue

            acc += numbers[char]
            continue

        if is_capital:
            acc += non_numbers[char].upper()
            is_capital = False
            continue

        acc += non_numbers[char]
    
    return acc

def translate_english(english):
    non_numbers, numbers, modifiers = generate_eng_dicts()

    is_number = False

    acc = ""

    for char in english:
        if is_number:
            if char == " ":
                acc += non_numbers[char]
                is_number = False
                continue

            acc += numbers[char]
            continue

        if char in numbers:
            is_number = True
            acc += modifiers["number"]
            acc += numbers[char]
            continue

        if char.isupper():
            acc += modifiers["capital"]
            char = char.lower()

        acc += non_numbers[char]

    return acc


input = " ".join(sys.argv[1:])

print(translate_braille(input)) if is_braille(input) else print(translate_english(input))

