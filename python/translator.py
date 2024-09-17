import sys

# English to Braille mappings
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......"
}

# Braille to numbers mapping
braille_to_numbers = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

# Braille to English mapping (reverse of english_to_braille)
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_english[".....O"] = "Capital"  # Capital symbol in Braille
braille_to_english[".O.OOO"] = "Number"  # Number follows symbol in Braille


def main():
    # Validating user input to make sure they provided input
    if len(sys.argv) < 2:
        print("Usage: python braille_translator.py <input_string>")
        sys.exit(1)

    input_string = " ".join(sys.argv[1:])

    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))


def is_braille(input_string):
    """
    Check if the input string consists only of Braille characters (O, .)
    and is valid in terms of length (multiple of 6).
    """
    return all(c in ['O', '.'] for c in input_string) and len(input_string) % 6 == 0


def translate_braille_to_english(braille_input):
    """
    Translate Braille input into English text.
    """
    english_output = []
    capital_next = False  # Flag to track if the next character should be capitalized
    number_next = False  # Flag to track if the next characters should be numbers

    for i in range(0, len(braille_input), 6):
        braille_char = braille_input[i:i + 6]  # Read 6-dot Braille character

        if braille_char == ".....O":
            capital_next = True
            continue

        if braille_char == ".O.OOO":
            number_next = True
            continue

        if braille_char == "......":
            english_output.append(" ")
            number_next = False
            continue

        if number_next:
            # Translate to numbers after the "number follows" symbol
            english_char = braille_to_numbers.get(braille_char, " ")
            if english_char == " ":
                number_next = False
        else:
            english_char = braille_to_english.get(braille_char, " ")

        # Handle capitalization
        if capital_next and english_char != " ":
            english_char = english_char.upper()
            capital_next = False

        english_output.append(english_char)

    return "".join(english_output)


def translate_english_to_braille(english_input):
    """
    Translate English text into Braille.
    """
    braille_output = []
    number_mode = False  # Flag to track if we are translating numbers

    for char in english_input:
        if char.isdigit():
            if not number_mode:
                # Add the "number follows" symbol before the first number
                braille_output.append(".O.OOO")
                number_mode = True

            # Translate the number to Braille by converting the number to its corresponding ASCII letter
            # ('1' -> 'a', '2' -> 'b', etc.). This works because numbers 1-9 are represented in Braille by
            # the same patterns as the letters a-j.
            braille_char = english_to_braille[chr(ord('a') + int(char) - 1)]
            braille_output.append(braille_char)
        else:
            if char.isupper():
                braille_output.append(".....O")
                char = char.lower()

            if number_mode:
                # If we were in number mode and encounter a non-number, reset number mode
                number_mode = False

            braille_char = english_to_braille.get(char, "......")  # I decided to use a space for unknown characters
            braille_output.append(braille_char)

    return "".join(braille_output)


if __name__ == "__main__":
    main()
