# Script for finding an unused braille character for the reserved char

from braille_to_char import CHAR_TO_BRAILLE

CHARS = [".", "O"]
LEN = 6


# LEARN:
def gen_combinations(combo):
    if len(combo) == LEN:
        return [combo]

    combos = []
    for c in CHARS:
        combos.extend(gen_combinations(combo + [c]))

    return combos


combos = gen_combinations([])
unused_set = set(["".join(c) for c in combos]) - set(CHAR_TO_BRAILLE.values())
print(unused_set)
