import sys

# Braille to English mapping
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", 
    # ".....O": "capital", ".O...O": "decimal", ".O.OOO": "number", 
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", 
    # "O..OO.": ">",
    "O.O..O": "(", ".O.OO.": ")", "......": " ",
}

# Numbers in Braille (after the number prefix)
braille_to_numbers = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

# English to Braille mapping
english_to_braille = {v: k for k, v in braille_to_english.items()}

# numbers to Braille mapping
numbers_to_braille = {v: k for k, v in braille_to_numbers.items()}

# Capitalization and numbers
capital_prefix = ".....O"  # Indicates the following letter is capital
number_prefix = ".O.OOO"   # Indicates the following characters are numbers
decimal_prefix = ".O...O"

# Function to translate Braille to English
def braille_to_text(braille):
    text = ""
    is_capital = False
    is_number = False
    is_decimal = False
    braille_chars = [braille[i:i + 6] for i in range(0, len(braille), 6)]

    for char in braille_chars:
        if char == capital_prefix:
            is_capital = True
            continue
        elif char == number_prefix:
            is_number = True
            continue
        elif char == decimal_prefix:
            continue

        translated_char = braille_to_english.get(char, "?")

        if is_number:
            translated_char = braille_to_numbers.get(char, "?")
            # Stay in number mode until a space or another non-number character appears
            if translated_char != "?":
                text += translated_char
                continue
            else:
                is_number = False  # End number mode if not a valid number char

        if is_capital:
            translated_char = translated_char.upper()
            is_capital = False

        text += translated_char

    return text

# Function to translate English to Braille
def text_to_braille(text):
    braille = ""
    in_number_mode = False  # Flag to track if we are in number mode

    for char in text:
        if char.isupper():
            braille += capital_prefix
            char = char.lower()
            in_number_mode = False  # Exit number mode when encountering letters
        if char.isdigit():
            if not in_number_mode:  # Only prepend the number prefix if not already in number mode
                braille += number_prefix
                in_number_mode = True
            braille += numbers_to_braille.get(char, "")
        else:
            braille += english_to_braille.get(char, "")
            in_number_mode = False

    return braille

# Main function to detect input and perform translation
def main():

    # Join all arguments into a single string to handle multiple inputs correctly
    input_string = " ".join(sys.argv[1:])

    # Determine if the input is Braille or English
    if all(c in "O." for c in input_string) and len(input_string) % 6 == 0:
        # Input is Braille
        result = braille_to_text(input_string)
    else:
        # Input is English
        result = text_to_braille(input_string)

    print(result)

if __name__ == "__main__":
    main()

