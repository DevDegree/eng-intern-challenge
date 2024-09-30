from sys import argv

BRAILLE_TO_ABC = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",
}
BRAILLE_TO_NUM = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}
BRAILLE_SPACE, BRAILLE_CAPITAL, BRAILLE_DECIMAL, BRAILLE_NUMBER = (
    "......",
    ".....O",
    ".O...O",
    ".O.OOO",
)
ABC_TO_BRAILLE = dict((abc, braille) for braille, abc in BRAILLE_TO_ABC.items())
NUM_TO_BRAILLE = dict((num, braille) for braille, num in BRAILLE_TO_NUM.items())


def is_braille(text: str) -> bool:
    return "." in text  # no braille character with only dots


def english_to_braille(english: str) -> str:
    braille = ""
    num_next = False
    for char in english:
        if char.isdigit():
            if not num_next:
                num_next = True
                braille += BRAILLE_NUMBER
            braille += NUM_TO_BRAILLE[char]
            continue
        elif char.isupper():
            braille += BRAILLE_CAPITAL
        elif char.isspace():
            num_next = False
        braille += ABC_TO_BRAILLE[char.lower()]
    return braille


def braille_to_english(braille: str) -> str:
    english = ""
    num_next, cap_next = False, False
    braille = [braille[i : i + 6] for i in range(0, len(braille), 6)]
    for char in braille:
        if num_next:
            english += BRAILLE_TO_NUM[char]
        elif cap_next:
            english += BRAILLE_TO_ABC[char].upper()
            cap_next = False
        elif char == BRAILLE_SPACE:
            english += " "
            num_next = False
        elif char == BRAILLE_CAPITAL:
            cap_next = True
        elif char == BRAILLE_NUMBER:
            num_next = True
        else:
            english += BRAILLE_TO_ABC[char]
    return english


def main():
    input_text = " ".join(argv[1:])
    if not input_text:
        print("Input cannot be blank")
        print(english_to_braille("Input cannot be blank"))
    elif is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))


if __name__ == "__main__":
    main()
