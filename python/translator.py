import sys


def main():
    # Validate user input to make sure they added a string
    if len(sys.argv) != 2:
        print("Usage: python braille_translator.py <input_string>")
        sys.exit(1)

    input_string = sys.argv[1]
    print("input is " + input_string)

    # Determine if the input is Braille or English
    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))


def is_braille(input_string):
    # Check if the input only contains 'O' and '.' and is a multiple of 6
    return all(c in ['O', '.'] for c in input_string) and len(input_string) % 6 == 0


english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......"
}

braille_to_numbers = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

# Braille to English mapping (reverse of english_to_braille)
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_english[".....O"] = "Capital"  # Capital symbol in Braille
braille_to_english[".O.OOO"] = "Number"  # Number follows symbol in Braille


def translate_braille_to_english(braille_input):
    english_output = []
    capital_next = False  # Flag to track if the next character should be capitalized
    number_next = False  # Flag to track if the next characters should be numbers

    ##TODO: do I need this?
    ##TODO: Remove debugging logs
    if len(braille_input) % 6 != 0:
        print("Error: Braille input length must be a multiple of 6.")
        return ""

    for i in range(0, len(braille_input), 6):
        braille_char = braille_input[i:i + 6]  # Read 6-dot Braille character
        print(f"Processing Braille chunk: {braille_char}")

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
            print(f"Translated to number: {english_char}")  # Debugging
        else:

            english_char = braille_to_english.get(braille_char, " ")
            print(f"Translated to letter: {english_char}")  # Debugging

        # Handle capitalization
        if capital_next and english_char != " ":
            english_char = english_char.upper()
            capital_next = False

        english_output.append(english_char)

    return "".join(english_output)


def translate_english_to_braille(english_input):
    braille_output = []

    for char in english_input:
        if char.isupper():
            # Add the "capital follows" symbol before the letter
            braille_output.append(".....O")
            # Convert the character to lowercase for Braille representation
            char = char.lower()

        # Look up the Braille symbol for the current character
        braille_char = english_to_braille.get(char, "......") # I will use space for the case of an unknown character
        braille_output.append(braille_char)

    # Return the Braille translation as a single string
    return "".join(braille_output)



if __name__ == "__main__":
    main()
