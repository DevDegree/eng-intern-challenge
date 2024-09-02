import sys


BRAILLE_CHARS = {
    "letters": {
        chr(i): dots for i, dots in enumerate("O.....", ord('a'))
    },
    "numbers": {
        chr(i): dots for i, dots in enumerate("O.....", ord('1'))
    },
}

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"


def is_braille(text):
    """Checks if the text consists only of valid Braille characters."""
    return all(c in BRAILLE_CHARS for c in text)


def translate(text, to_braille=True):

    translated_text = ""
    in_number_mode = False

    for char in text:
        if to_braille:
            if char.isupper():
                translated_text += CAPITAL_FOLLOWS + BRAILLE_CHARS["letters"][char.lower()]
            elif char.isalpha():
                translated_text += BRAILLE_CHARS["letters"][char]
            elif char.isdigit():
                if not in_number_mode:
                    translated_text += NUMBER_FOLLOWS
                    in_number_mode = True
                translated_text += BRAILLE_CHARS["numbers"][char]
            elif char == " ":
                translated_text += BRAILLE_CHARS["space"]
                in_number_mode = False
            else:
                raise ValueError(f"Unknown character: {char}")
        else:
            letter = text[:6]
            if letter == CAPITAL_FOLLOWS:
                translated_text += BRAILLE_CHARS["letters"][text[6:12]].upper()
                text = text[12:]
            elif letter == BRAILLE_CHARS["space"]:
                translated_text += " "
                in_number_mode = False
                text = text[6:]
            else:
                if in_number_mode:
                    translated_text += next(
                        num
                        for num, braille in BRAILLE_CHARS["numbers"].items()
                        if braille == letter
                    )
                else:
                    translated_text += next(
                        char
                        for char, braille in BRAILLE_CHARS["letters"].items()
                        if braille == letter
                    )
                text = text[6:]

    return translated_text


def main():

    if len(sys.argv) < 2:
        sys.exit(1)

    text = " ".join(sys.argv[1:])

    if is_braille(text):
        translated_text = translate(text, to_braille=False)
    else:
        translated_text = translate(text)

    print(translated_text)


if __name__ == "__main__":
    main()