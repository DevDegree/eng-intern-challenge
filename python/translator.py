import sys

# Braille dictionary with 6 dots
braille_dict = {
    "alphabet": {
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
    },
    "digits": {
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
    },
    "special_chars": {
        " ": "......",  # Space
        "cap": ".....O",  # Capital follows
        "dec": ".O...O",  # Decimal follows
        "num": ".O.OOO",  # Number follows
        ".": "..OO.O",
        ",": "..O...",
        "?": "..O.OO",
        "!": "..OOO.",
        ":": "..OO..",
        ";": "..O.O.",
        "-": "....OO",
        "/": ".O..O.",
        "<": ".OO..O",
        ">": "O..OO.",
        "(": "O.O..O",
        ")": ".O.OO.",
    },
}


# Create an empty dictionary for the reversed mappings
reverse_braille = {
    "alphabet": {},
    "digits": {},
    "special_chars": {},
}

# Populate the reverse dictionary with sub-dictionaries for each category
for category in braille_dict:
    for letter, braille in braille_dict[category].items():
        reverse_braille[category][braille] = letter


def text_to_braille(text):
    result = []
    is_capital = False
    is_number = False

    i = 0
    while i < len(text):
        char = text[i]

        if char.isdigit():
            if not is_number:
                result.append(
                    braille_dict["special_chars"]["num"]
                )  # Prefix number indicator only once per number sequence
                is_number = True
            result.append(braille_dict["digits"][char])

        elif char == "." and is_number:
            result.append(
                braille_dict["special_chars"]["dec"]
            )  # Decimal point in a number
            # No need to reset is_number here because we're still in a number sequence

        elif char.isalpha():
            if is_number:
                is_number = False  # End of number sequence
            if char.isupper():
                if not is_capital:
                    result.append(
                        braille_dict["special_chars"]["cap"]
                    )  # Prefix capital indicator, only once per capital letter
                    is_capital = True
            result.append(braille_dict["alphabet"][char.lower()])
            is_capital = False  # Reset capital indicator after adding a capital letter

        else:
            # Handle non-alphabetical, non-digit characters
            if is_number:
                is_number = False  # End of number sequence
            result.append(braille_dict["special_chars"].get(char, "......"))

        i += 1

    return "".join(result)


def braille_to_text(braille):
    i = 0
    result = []
    is_capital = False
    is_number = False

    while i < len(braille):
        symbol = braille[i : i + 6]

        if symbol == braille_dict["special_chars"]["cap"]:
            is_capital = True
            i += 6
            continue
        if symbol == braille_dict["special_chars"]["num"]:
            is_number = True
            i += 6
            continue
        if symbol == braille_dict["special_chars"]["dec"] and is_number:
            result.append(".")
            i += 6
            continue

        # If the symbol is a space, reset the is_number flag
        if symbol == braille_dict["special_chars"][" "]:
            is_number = False

        # Determine the category of the symbol
        char = None
        if is_number:
            char = reverse_braille["digits"].get(symbol)
        else:
            for category in reverse_braille:
                if category == "digits":
                    continue
                if symbol in reverse_braille[category]:
                    char = reverse_braille[category][symbol]
                    break

        if char:
            if is_number and char.isdigit():  # Ensures numeric context is handled
                result.append(char)
            elif char.isalpha():  # Handles alphabetic characters
                if is_capital:
                    char = char.upper()
                    is_capital = False
                result.append(char)
            else:  # Handles spaces and punctuation
                result.append(char)
                is_capital = False  # Reset flags on special characters
                is_number = False
        else:
            # Reset flags if the symbol does not match any known characters
            is_capital = False
            is_number = False

        i += 6  # Move to the next braille symbol segment

    return "".join(result)


def detect_input_type(input_string):
    # Assuming that a string containing only 'O', '.', or spaces is Braille
    if set(input_string).issubset({"O", ".", " "}):
        # Additional check for valid Braille patterns using the structured reverse_braille dictionary
        lines = input_string.strip().split()
        valid_braille = True

        for line in lines:
            # Check if the line can be divided into chunks of 6 (Braille cell size)
            if len(line) % 6 != 0:
                valid_braille = False
                break
            # Split the line into chunks of 6 characters
            chunks = [line[i : i + 6] for i in range(0, len(line), 6)]

            # Check each chunk if it is a valid Braille code in any category of reverse_braille
            for chunk in chunks:
                if not any(
                    chunk in reverse_braille[category] for category in reverse_braille
                ):
                    valid_braille = False
                    break
            if not valid_braille:
                break

        if valid_braille:
            return "braille"
    return "text"


def main():
    input_type = all(detect_input_type(arg) == "braille" for arg in sys.argv[1:])
    if input_type:
        braille_func = braille_to_text
    else:
        braille_func = text_to_braille

    input_strings = sys.argv[
        1:
    ]  # Take all command-line arguments except the script name
    for index, input_string in enumerate(input_strings):
        result = braille_func(input_string)
        print(result, end="")
        if index < len(input_strings) - 1:
            print(
                (" " if input_type == "text" else braille_dict["special_chars"][" "]),
                end="",
            )

    print()  # To ensure the final output ends with a newline


if __name__ == "__main__":
    main()
