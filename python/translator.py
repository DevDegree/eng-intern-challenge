import sys


mapping_num_to_braille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

mapping_eng_to_braille = {
    # Letters
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......",
    ".": "..OO.O",
}
# Special characters (Ignored because no given requirements
# and because they have overlapping keys with english)
# ",": "..O...",
# "?": "..O.OO",
# "!": "..OOO.",
# ":": "..OO..",
# ";": "..O.O.",
# "-": "....OO",
# "/": ".O..O.",
# "<": ".OO..O",
# ">": "O..OO.",
# "(": "O.O..O",
# ")": ".O.OO.",


# Reverse mappings
mapping_braille_to_eng = {v: k for k, v in mapping_eng_to_braille.items()}
mapping_braille_to_num = {v: k for k, v in mapping_num_to_braille.items()}

# Merge mappings for english and numbers, because this translation does not have
# overlapping keys
mapping_eng_to_braille = {**mapping_eng_to_braille, **mapping_num_to_braille}

# Special braille characters
CAPITAL_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O"
NUMBER_FOLLOWS = ".O.OOO"

# Sanity check
assert all(len(v) == 6 for v in mapping_eng_to_braille.values())

# Extract CLI arguments
text = " ".join(sys.argv[1:]).strip()

# Is the input text english?
is_english = any((c not in "O.") for c in text)

# Resulting translation
result = ""


if is_english:
    result = ""
    prev = None
    is_following_numbers = False
    # Iterate over each character in the input text
    for char in text:
        if char.isupper():
            result += CAPITAL_FOLLOWS
            result += mapping_eng_to_braille[char.lower()]
            is_following_numbers = False

        elif char.isdigit():
            result += NUMBER_FOLLOWS if not is_following_numbers else ""
            result += mapping_eng_to_braille[char]
            is_following_numbers = True
        elif char == "." and prev in "0123456789":
            result += DECIMAL_FOLLOWS
        else:
            result += mapping_eng_to_braille[char]
            is_following_numbers = False

        # Keep track of the previous character
        prev = char

else:
    next_capital = False
    next_number = False
    for i in range(0, len(text), 6):

        braille_code = text[i : i + 6]
        if braille_code == CAPITAL_FOLLOWS:
            next_capital = True
        elif braille_code == NUMBER_FOLLOWS:
            next_number = True
        elif braille_code == DECIMAL_FOLLOWS:
            result += "."
        else:
            mapping_to_use = mapping_braille_to_eng
            if next_number and braille_code in mapping_braille_to_num:
                mapping_to_use = mapping_braille_to_num
            else:
                # This actually matches the assumption that we keep adding numbers
                # until we hit a 'space' or even a non-number character
                next_number = False
            to_add = mapping_to_use[braille_code]
            result += to_add.upper() if next_capital else to_add
            next_capital = False

print(result)
