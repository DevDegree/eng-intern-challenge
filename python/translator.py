import sys

class Language:
    ENGLISH = 1
    BRAILLE = 2

braille_digit_map = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

english_to_braille_map = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
    '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...",
    '0': ".OOO..", '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': "..OOO.",
    ':': "..OO..", ';': "..O.O.", '-': "....OO", '/': ".O..O.", '<': ".OO..O",
    '>': "O..OO.", '(': "O.O..O", ')': ".O.OO.", ' ': "......"
}

braille_to_english_map = {v: k for k, v in english_to_braille_map.items()}

def language_identifier(input_str):
    return Language.BRAILLE if all(char in 'O.' for char in input_str) else Language.ENGLISH

def english_to_braille(input_str):
    res = ""
    number_next = True
    decimal_next = False
    for ch in input_str:
        if ch.isdigit():
            res += categorize_string(ch, number_next, decimal_next)
            number_next = False
        elif ch.isspace():
            res += categorize_string(ch, False, decimal_next)
            number_next = True
        elif ch in [',', '.']:
            decimal_next = True
            res += categorize_string(ch, False, decimal_next)
        else:
            res += categorize_string(ch, False, decimal_next)
    return res

def categorize_string(ch, prefix, decimal_next):
    if ch.isdigit():
        if prefix:
            return ".O.OOO" + english_to_braille_map[ch]
        else:
            return english_to_braille_map[ch]
    elif decimal_next:
        decimal_next = False
        return ".O...O"
    elif ch.isalpha() and ch.isupper():
        return ".....O" + english_to_braille_map[ch.lower()]
    elif ch.isalpha() or ch.isspace():
        return english_to_braille_map[ch]
    else:
        return english_to_braille_map[ch]

def braille_to_english(input_str):
    res = ""
    capital_next = False
    number_next = False
    i = 0
    while i < len(input_str):
        if i + 6 > len(input_str):
            break

        braille_cell = input_str[i:i+6]

        if braille_cell == ".....O":
            capital_next = True
            i += 6
            continue
        if braille_cell == ".O.OOO":
            number_next = True
            i += 6
            continue
        if braille_cell == ".O...O":
            res += ","
            i += 6
            continue

        if braille_cell == "......":
            number_next = False
            res += " "
            i += 6
            continue

        if braille_cell == "O..OO.":
            before_char = braille_to_english_map.get(input_str[i-6:i], "")
            if before_char.isalpha() or before_char.isspace():
                res += "o"
            else:
                res += ">"
            i += 6
            continue

        if capital_next:
            res += braille_to_english_map[braille_cell].upper()
            capital_next = False
            i += 6
            continue

        if number_next:
            if braille_cell in braille_digit_map:
                res += braille_digit_map[braille_cell]
            i += 6
            continue

        res += braille_to_english_map[braille_cell]
        i += 6

    return res

def main():
    if len(sys.argv) > 1:
        input_str = " ".join(sys.argv[1:])
        if language_identifier(input_str) == Language.BRAILLE:
            print(braille_to_english(input_str))
        else:
            print(english_to_braille(input_str))
    else:
        print("Error: No input provided")

if __name__ == "__main__":
    main()
