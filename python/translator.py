import sys

ENGLISH_TO_BRAILLE = {
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
}

NUMBERS_TO_BRAILLE = {
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

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"

BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}


def is_braille(input: str) -> bool:
    return all(char in [".", "O"] for char in input)


def to_braille(input: str) -> str:
    output = []
    number_mode = False

    for char in input:
        if char.isdigit():
            if not number_mode:
                output.append(NUMBER_FOLLOWS)
                number_mode = True
            output.append(NUMBERS_TO_BRAILLE.get(char, SPACE))
        else:
            if number_mode:
                number_mode = False

            if char.isupper():
                output.append(CAPITAL_FOLLOWS)
                output.append(ENGLISH_TO_BRAILLE.get(char.lower(), SPACE))
            elif char == " ":
                output.append(SPACE)
            else:
                output.append(ENGLISH_TO_BRAILLE.get(char, SPACE))

    return "".join(output)


def to_english(input: str) -> str:
    output = []
    braille_cells = [input[i : i + 6] for i in range(0, len(input), 6)]
    number_mode = capitalize_next = False

    for i in range(len(braille_cells)):
        cell = braille_cells[i]

        if cell == NUMBER_FOLLOWS:
            number_mode = True
            continue
        elif cell == CAPITAL_FOLLOWS:
            capitalize_next = True
            continue
        elif cell == SPACE:
            output.append(" ")
            number_mode = capitalize_next = False
            continue

        if number_mode:
            char = BRAILLE_TO_NUMBERS.get(cell, " ")
            output.append(char)
        else:
            char = BRAILLE_TO_ENGLISH.get(cell, " ")
            if capitalize_next and char != " ":
                char = char.upper()
                capitalize_next = False
            output.append(char)

    return "".join(output)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text_to_translate>")
        sys.exit(1)

    input = " ".join(sys.argv[1:])
    if is_braille(input):
        translated = to_english(input)
    else:
        translated = to_braille(input)
    print(translated)


if __name__ == "__main__":
    main()
