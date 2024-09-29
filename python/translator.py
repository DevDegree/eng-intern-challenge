import sys

# Braille mapping dictionaries
char_to_braille_mapping = {
    # Letters
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

    # Space
    " ": "......",

    # Punctuation
    ".": "..OO.O",  # Period
    ",": "..O...",  # Comma
    "?": "..O.OO",  # Question Mark
    "!": "..OOO.",  # Exclamation Mark
    ":": "..OO..",  # Colon
    ";": "..O.O.",  # Semicolon
    "-": "....OO",  # Hyphen
    "/": ".O..O.",  # Slash
    "<": ".OO..O",  # Less than
    "(": "O.O..O",  # Open parenthesis
    ")": ".O.OO.",  # Close parenthesis

    # Special indicators
    "capital follows": ".....O",  # Capital follows indicator
    "decimal follows": ".0...0",  # Decimal follows indicator
    "number follows": ".O.OOO"    # Number follows indicator
}

digit_to_braille_mapping = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

def english_to_braille(text):
    braille = ""
    is_number = False
    is_decimal = False

    for i, char in enumerate(text):
        if char.isupper():
            # Add the capital follows indicator and convert to lowercase
            braille += char_to_braille_mapping["capital follows"]
            char = char.lower()

        if char.isdigit():
            if not is_number:
                # Add number follows indicator at the start of numbers
                braille += char_to_braille_mapping["number follows"]
                is_number = True

            # If we're in decimal mode, add the decimal follows indicator
            if is_decimal:
                braille += char_to_braille_mapping["decimal follows"]
                is_decimal = False

            braille += digit_to_braille_mapping[char]
        
        elif char == '.':
            # If a decimal point is found, set the decimal mode flag
            is_decimal = True
        
        else:
            # Exit number mode when a non-digit character is encountered
            if is_number:
                is_number = False

            # Handle space explicitly
            if char == " ":
                braille += char_to_braille_mapping[" "]
            # Add the Braille equivalent for other characters if they exist in the mapping
            elif char in char_to_braille_mapping:
                braille += char_to_braille_mapping[char]

    return braille


def main():
    input_text = ' '.join(sys.argv[1:])

    english_to_braille_output = english_to_braille(input_text)
    print(english_to_braille_output)

if __name__ == "__main__":
    main()  # Call the main function when the script is run
