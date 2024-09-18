import sys

# Mappings for english to braille
english_to_braille = {
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

number_to_braille = {
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

# Mappings for braille to english
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_number = {v: k for k, v in number_to_braille.items()}

# Returns True if input string is in braille
def is_braille(input):
    for char in input:
        if char != "O" and char != ".":
            return False
    return True


# Convert braille to english
def convert_braille_to_english(input):
    out = ""
    capital_follows = False
    number_follows = False

    for i in range(0, len(input), 6):
        symbol = input[i : i + 6]
        if symbol == ".....O":
            capital_follows = True
            continue
        elif symbol == ".O.OOO":
            number_follows = True
            continue

        if symbol == "......":
            out += " "
            number_follows = False  # Disable number mode after a space
        elif number_follows:
            char = braille_to_number.get(symbol)
            out += char
        else:
            char = braille_to_english.get(symbol)
            out += char.upper() if capital_follows else char
            capital_follows = (
                False  # Disable capital mode immediately after a character
            )
    return out


# Convert english to braille
def convert_english_to_braille(input):
    out = ""
    number_follows = False
    for char in input:
        if char.isalpha():
            if char.isupper():
                out += ".....O"
            out += english_to_braille[char.lower()]
        elif char == " ":
            out += "......"
            number_follows = False
        elif char.isdigit():
            if not number_follows:
                out += ".O.OOO"
                number_follows = True
            out += number_to_braille[char]
    return out


def main():
    if len(sys.argv) < 2:
        # Return if no input
        return

    input = " ".join(sys.argv[1:])

    if is_braille(input):
        output = convert_braille_to_english(input)
    else:
        output = convert_english_to_braille(input)

    print(output)


if __name__ == "__main__":
    main()
