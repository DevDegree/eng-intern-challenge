import sys

# Braille to Characters
BRAILLE_TO_ENGLISH_LOWER = {
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

BRAILLE_TO_ENGLISH_NUMS = {
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

BRAILLE_TO_ENGLISH_SYMBOLS = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OO..": "!",
    "..O.O.": ":",
    "..O..O": ";",
    "...O..": "-",
    "..O..O": "/",
    "...O.O": "<",
    "...OO.": ">",
    "...OOO": "(",
    "..O..O": ")",
    "......": " ",
    ".....O": "CAP",  # Capital indicator
    ".O.OOO": "NUM",  # Number indicator
    "..OOO.": "DEC",  # Decimal follows indicator
}

# Characters to Braille
ENGLISH_TO_BRAILLE_LOWER = {v: k for k, v in BRAILLE_TO_ENGLISH_LOWER.items()}

ENGLISH_TO_BRAILLE_NUMS = {
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

ENGLISH_TO_BRAILLE_SYMBOLS = {
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OO..",
    ":": "..O.O.",
    ";": "..O..O",
    "-": "...O..",
    "/": "..O..O",
    "<": "...O.O",
    ">": "...OO.",
    "(": "...OOO",
    ")": "..O..O",
    "CAP": ".....O",  # Capital indicator
    "NUM": ".O.OOO",  # Number indicator
    "DEC": "..OOO.",  # Decimal follows indicator
    " ": "......",
}

def translate_to_braille(english_string):
    result = []
    is_number_mode = False

    for char in english_string:
        if char.isdigit():
            if not is_number_mode:
                result.append(
                    ENGLISH_TO_BRAILLE_SYMBOLS["NUM"]
                )  # Add number indicator before digits
                is_number_mode = True
            result.append(ENGLISH_TO_BRAILLE_NUMS[char])
        elif char == ".":
            result.append(
                ENGLISH_TO_BRAILLE_SYMBOLS["DEC"]
            )  # Decimal follows indicator
        elif char.isalpha():
            if is_number_mode:
                result.append("......")  # End number mode with space
                is_number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE_SYMBOLS["CAP"])
            result.append(ENGLISH_TO_BRAILLE_LOWER[char.lower()])
        else:
            result.append(
                ENGLISH_TO_BRAILLE_SYMBOLS.get(char, "......")
            )  # Handle other symbols or unknown as space
            is_number_mode = False  # Reset number mode
    return "".join(result)


def translate_to_english(braille_string):
    result = []
    words = braille_string.split(" ")
    is_capital = False
    is_number = False

    for word in words:
        braille_chars = [word[i : i + 6] for i in range(0, len(word), 6)]
        for char in braille_chars:
            if char == ENGLISH_TO_BRAILLE_SYMBOLS["CAP"]:  # Capital indicator
                is_capital = True
                continue
            elif char == ENGLISH_TO_BRAILLE_SYMBOLS["NUM"]:  # Number indicator
                is_number = True
                continue
            elif char == ENGLISH_TO_BRAILLE_SYMBOLS["DEC"]:  # Decimal indicator
                result.append(".")
                continue

            if is_number:
                if char in BRAILLE_TO_ENGLISH_NUMS:
                    translated_char = BRAILLE_TO_ENGLISH_NUMS[char]
                    result.append(translated_char)
                else:
                    result.append("?")  # Unknown character encountered in number
            elif char in BRAILLE_TO_ENGLISH_LOWER:
                translated_char = BRAILLE_TO_ENGLISH_LOWER[char]
                if is_capital:
                    translated_char = translated_char.upper()
                    is_capital = False
                result.append(translated_char)
            elif char in BRAILLE_TO_ENGLISH_SYMBOLS:
                result.append(BRAILLE_TO_ENGLISH_SYMBOLS[char])
            else:
                result.append("?")  # Unknown character

        result.append(" ")  # Space between words
        is_number = False  # Reset number mode after each word
    return "".join(result).strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text_to_translate>")
        return

    input_text = " ".join(sys.argv[1:])

    if all(c in "O. " for c in input_text): 
        translated_text = translate_to_english(input_text)
    else:
        translated_text = translate_to_braille(input_text)

    print(translated_text)

if __name__ == "__main__":
    main()

