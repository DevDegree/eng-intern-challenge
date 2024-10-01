from typing import Dict

REFERENCE_KEY = [
    ("a", "O....."),
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
    (".", "..OO.O"),
    (",", "..O..."),
    ("?", "..O.OO"),
    ("!", "..OOO."),
    (":", "..OO.."),
    (";", "..O.O."),
    ("-", "....OO"),
    ("/", ".O..O."),
    ("<", ".OO.O."),
    (">", "O..OO."),
    ("(", "O.O..O"),
    (")", ".O.OO."),
    (" ", "......"),
    ("capital", ".....O"),
    ("number", ".O.OOO"),
]

ENG_TO_BRAILLE: Dict[str, str] = {}
BRAILLE_TO_ENG: Dict[str, str] = {}
for entry in REFERENCE_KEY:
    ENG_TO_BRAILLE[entry[0]] = entry[1]
    BRAILLE_TO_ENG[entry[1]] = entry[0]

# for number in range(1, 11):
#     to_braille = ENG_TO_BRAILLE[chr(ord("a") + number - 1)]
#     assoc_number = number % 10
#     ENG_TO_BRAILLE[assoc_number] = to_braille
#     BRAILLE_TO_ENG[to_braille] = assoc_number
