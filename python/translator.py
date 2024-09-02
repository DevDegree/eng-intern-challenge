import sys

# Braille dictionary mapping letters and numbers to Braille patterns
braille_dict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "capital follows": ".....O", " ": "......",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    "number follows": ".O.OOO"
}
# Reverse dictionary for translation from Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def translate_to_braille(text):
    """
    Translates English text to Braille.
    """
    result = []
    in_number_mode = False

    for i, char in enumerate(text):
        if char.isupper():
            # Add capitalization indicator and convert to lowercase
            result.append(braille_dict["capital follows"])
            result.append(braille_dict[char.lower()])
            in_number_mode = False  # Reset number mode after a capital letter
        elif char.isdigit():
            # Add number indicator if not already in number mode
            if not in_number_mode:
                result.append(braille_dict["number follows"])
                in_number_mode = True
            result.append(braille_dict[char])
        elif char == " ":
            # Handle spaces
            result.append("......")
            in_number_mode = False  # Reset number mode after a space
        else:
            # Handle lowercase letters
            if in_number_mode:
                in_number_mode = False  # Switch back to letter mode if necessary
            result.append(braille_dict.get(char.lower(), "......"))  # Default to space for unknown characters

    return "".join(result)

def translate_to_english(braille):
    """
    Translates Braille to English text.
    """
    result = []
    i = 0
    in_capital_mode = False
    in_number_mode = False

    while i < len(braille):
        char = braille[i:i+6]

        if char == braille_dict["capital follows"]:
            # Capitalization indicator, switch to capital mode
            in_capital_mode = True
            in_number_mode = False  # Ensure we're not in number mode
            i += 6
        elif char == braille_dict["number follows"]:
            # Number indicator, switch to number mode
            in_number_mode = True
            in_capital_mode = False  # Ensure we're not in capital mode
            i += 6
        elif char == "......":  # Space
            result.append(" ")
            in_number_mode = False  # Return to letter mode after space
            in_capital_mode = False
            i += 6
        else:
            if in_number_mode:
                # Convert Braille symbol to digit
                for key, value in braille_dict.items():
                    if value == char and key.isdigit():
                        result.append(key)
                        break
            else:
                # Convert Braille symbol to letter
                for key, value in braille_dict.items():
                    if value == char and key.isalpha():
                        if in_capital_mode:
                            result.append(key.upper())
                            in_capital_mode = False  # Reset capital mode
                        else:
                            result.append(key)
                        break
            i += 6

    return "".join(result)

def main():
    """
    Main function to handle input and determine translation direction.
    """
    # Get the input text from command line arguments
    input_text = " ".join(sys.argv[1:])

    # Determine if the input is Braille or English
    if all(c in "O." for c in input_text):  # Check if the input is Braille
        output = translate_to_english(input_text)
    else:
        output = translate_to_braille(input_text)

    print(output)

if __name__ == "__main__":
    main()
