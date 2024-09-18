import sys

ENGLISH_TO_BRAILLE_LETTERS = {
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
    "capital": ".....O",
    "number": ".O.OOO",
}

ENGLISH_TO_BRAILLE_DIGITS = {
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

# Reverse mapping
BRAILLE_TO_ENGLISH_LETTERS = {v: k for k, v in ENGLISH_TO_BRAILLE_LETTERS.items()}
BRAILLE_TO_ENGLISH_DIGITS = {v: k for k, v in ENGLISH_TO_BRAILLE_DIGITS.items()}


def is_braille(input_string):
    stripped_input = input_string.strip()
    for char in stripped_input:
        if char not in ["O", ".", " "]:
            return False
    return True


def translate_to_braille(s):
    translation = ""

    for char in s:
        if char.isalpha():
            if char.isupper():
                translation += ENGLISH_TO_BRAILLE_LETTERS["capital"]
            translation += ENGLISH_TO_BRAILLE_LETTERS[char.lower()]
        elif char.isdigit():
            translation += ENGLISH_TO_BRAILLE_LETTERS["number"]
            translation += ENGLISH_TO_BRAILLE_DIGITS[char]
        elif char == " ":
            translation += ENGLISH_TO_BRAILLE_LETTERS[" "]
        else:
            # Raise error for unsupported characters.
            raise ValueError(f"Unsupported character: {char}")

    return translation


def translate_to_english(braille_string):
    translation = ""
    capital_flag = False
    number_flag = False

    for index in range(0, len(braille_string), 6):  # Step of 6 since each braille symbol is 6 characters long
        braille_slice = braille_string[index:index + 6]

        if braille_slice == ENGLISH_TO_BRAILLE_LETTERS["capital"]:
            capital_flag = True
        elif braille_slice == ENGLISH_TO_BRAILLE_LETTERS["number"]:
            number_flag = True
        elif braille_slice == ENGLISH_TO_BRAILLE_LETTERS[" "]:
            translation += " "
            number_flag = False
        else:
            mapping = BRAILLE_TO_ENGLISH_DIGITS if number_flag else BRAILLE_TO_ENGLISH_LETTERS
            char = mapping.get(braille_slice)

            # Raise error for unsupported characters
            if char is None:
                raise ValueError(f"Unsupported braille pattern: {braille_slice}")

            translation += char.upper() if capital_flag else char

            # Reset flags.
            capital_flag = False
            number_flag = False

    return translation


def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))


if __name__ == "__main__":
    main()
