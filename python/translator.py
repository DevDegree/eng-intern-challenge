import sys


BRAILLE_ALPHABET = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ': "......"
}

BRAILLE_NUMBERS = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."
}

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"


def is_braille(text):
    """Checks if the text consists only of valid Braille characters."""
    return all(c in BRAILLE_ALPHABET.values() or c in BRAILLE_NUMBERS.values() for c in text)


def translate(text, to_braille=True):
    """
    Translates text between English and Braille.

    Args:
        text (str): The text to translate.
        to_braille (bool, optional): If True, translates from English to Braille.
            If False, translates from Braille to English. Defaults to True.

    Returns:
        str: The translated text.
    """

    translated_text = ""
    in_number_mode = False

    for char in text:
        if to_braille:
            if char.isupper():
                translated_text += CAPITAL_FOLLOWS + BRAILLE_ALPHABET[char.lower()]
            elif char.isalpha():
                translated_text += BRAILLE_ALPHABET[char]
            elif char.isdigit():
                if not in_number_mode:
                    translated_text += NUMBER_FOLLOWS
                    in_number_mode = True
                translated_text += BRAILLE_NUMBERS[char]
            elif char == " ":
                translated_text += BRAILLE_ALPHABET[' ']
                in_number_mode = False
            else:
                raise ValueError(f"Unknown character: {char}")
        else:
            letter = text[:6]
            if letter == CAPITAL_FOLLOWS:
                translated_text += next(
                    char.upper()
                    for char, braille in BRAILLE_ALPHABET.items()
                    if braille == text[6:12]
                )
                text = text[12:]
            elif letter == NUMBER_FOLLOWS:
                in_number_mode = True
                text = text[6:]
            elif letter == BRAILLE_ALPHABET[' ']:
                translated_text += " "
                in_number_mode = False
                text = text[6:]
            else:
                if in_number_mode:
                    translated_text += next(
                        num
                        for num, braille in BRAILLE_NUMBERS.items()
                        if braille == letter
                    )
                else:
                    translated_text += next(
                        char
                        for char, braille in BRAILLE_ALPHABET.items()
                        if braille == letter
                    )
                text = text[6:]

    return translated_text


def main():
    """Gets user input, translates it, and prints the result."""

    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    text = " ".join(sys.argv[1:])

    if is_braille(text):
        translated_text = translate(text, to_braille=False)
    else:
        translated_text = translate(text)

    print(translated_text)


if __name__ == "__main__":
    main()