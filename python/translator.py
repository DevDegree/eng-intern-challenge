import sys

letter_to_braille = {
    chr(97+i): v for i, v in enumerate([
        "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...",
        ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.",
        ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"
    ])
}

number_to_braille = {
    str(i): v for i, v in enumerate([".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO..."])
}

special = {
    "space": "......",
    "capital": ".....O",
    "number": ".O.OOO"
}

def text_to_braille(text):
    braille = []
    number_mode = False

    for char in text:
        if char == " ":
            braille.append(special["space"])
            number_mode = False
        elif char.isupper():
            if number_mode:
                return None
            braille.extend([special["capital"], letter_to_braille[char.lower()]])
        elif char.isdigit():
            if not number_mode:
                braille.append(special["number"])
                number_mode = True
            braille.append(number_to_braille[char])
        else:
            if number_mode or char not in letter_to_braille:
                return None
            braille.append(letter_to_braille[char])

    return "".join(braille)

def braille_to_text(braille):
    if len(braille) % 6 != 0:
        return None

    braille_to_letter = {v: k for k, v in letter_to_braille.items()}
    braille_to_number = {v: k for k, v in number_to_braille.items()}
    braille_symbols = [braille[i:i+6] for i in range(0, len(braille), 6)]

    text = []
    word = ""
    capitalize_next = number_mode = False

    for symbol in braille_symbols:
        if symbol == special["capital"]:
            capitalize_next = True
        elif symbol == special["number"]:
            number_mode = True
        elif symbol == special["space"]:
            text.append(word)
            word = ""
            number_mode = False
        else:
            try:
                if number_mode:
                    word += braille_to_number[symbol]
                else:
                    letter = braille_to_letter[symbol]
                    word += letter.upper() if capitalize_next else letter
                    capitalize_next = False
            except KeyError:
                return None

    if word:
        text.append(word)

    return " ".join(text)

def main(args):
    if len(args) < 2:
        print("Error: Missing argument")
        sys.exit(1)

    input_text = args[1]

    if all(char in "O." for char in input_text):
        result = braille_to_text(input_text)
    else:
        result = text_to_braille(" ".join(args[1:]))

    if result is not None:
        print(result)
    else:
        print("Error: Invalid input")

if __name__ == "__main__":
    main(sys.argv)