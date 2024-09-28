import collections
# Braille mappings
BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# 42a -> .O.OOOOO.O..O.O...O.....

# Reverse map for Braille to English
ENGLISH_MAP = collections.defaultdict(list)
for k, v in BRAILLE_MAP.items():
    # sequence = [number , letter] (since sequence can be both a number and a letter)
    ENGLISH_MAP[v].append(k)


def to_braille(text: str) -> str:
    braille = ""
    digit = 0
    for char in text:
        if char.isupper():
            braille += BRAILLE_MAP['cap'] + BRAILLE_MAP[char.lower()]
        elif ord(char) == 32:
            digit = 0
            braille += BRAILLE_MAP[char]
        elif char.isdigit() and digit:
            braille += BRAILLE_MAP[char]
        elif char.isdigit():
            braille += BRAILLE_MAP['num'] + BRAILLE_MAP[char]
            digit = 1
        else:
            braille += BRAILLE_MAP[char]
    return braille


def to_english(braille: str) -> str:
    english = ""
    i = 0
    is_capital = False
    is_number = False

    while i < len(braille):
        char = braille[i:i+6]

        if char == '.....O':  # Capitalize next letter
            is_capital = True
            i += 6
            continue
        elif char == '.O.OOO':  # Start number sequence
            is_number = True
            i += 6
            continue
        elif char == '......':  # Space
            english += ' '
        else:
            if is_number:
                # Numbers are the second item in the list
                english += ENGLISH_MAP[char][1]
            else:
                # Letters are the first item in the list
                letter = ENGLISH_MAP[char][0]
                if is_capital:
                    letter = letter.upper()
                    is_capital = False
                english += letter

        i += 6

        # Reset the number flag after a space
        if char == '......':
            is_number = False

    return english


def main():
    import sys
    args = sys.argv[1:]
    if len(args) == 0:
        sys.exit(1)

    input_text = " ".join(args)

    if all(c in 'O.oO ' for c in input_text):
        # Likely Braille input
        output = to_english(input_text)
    else:
        # Likely English input
        output = to_braille(input_text)
    print(output)


main()
