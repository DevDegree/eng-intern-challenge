import sys

# Braille to English mapping dictionary
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",  # Space
    "..OO.O": ".",  # Period
    "..O...": ",",  # Comma
    "..O.OO": "?",  # Question Mark
    "..OOO.": "!",  # Exclamation Mark
    "..OO..": ":",  # Colon
    "..O.O.": ";",  # Semicolon
    "....OO": "-",  # Hyphen
    ".O..O.": "/",  # Slash
    ".OO..O": "<",  # Less than
    "O.O..O": "(",  # Open parenthesis
    ".O.OO.": ")",  # Close parenthesis
    ".....O": "Capital follows",  # Capital follows indicator
    ".O.OOO": "Number follows"    # Number follows indicator
}

# English to Braille mapping
english_to_braille = {v: k for k, v in braille_to_english.items() if v not in ["Capital follows", "Number follows"]}

# Additional mappings for numbers in Braille
number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

def translate_to_braille(text):
    result = []
    number_mode = False  # Flag to check if we are in number mode

    for char in text:
        # Handle digits
        if char.isdigit():
            if not number_mode:  # If not already in number mode, switch to it
                result.append(".O.OOO")  # Add "Number follows" indicator
                number_mode = True  # Stay in number mode for subsequent digits
            result.append(number_to_braille[char])  # Add the Braille pattern for the number

        # Handle alphabetic characters
        elif char.isalpha():
            if number_mode:  # Automatically exit number mode if encountering a letter
                number_mode = False  # Exit number mode
            if char.isupper():  # Check if the character is uppercase
                result.append(".....O")  # Add "Capital follows" indicator
            result.append(english_to_braille[char.lower()])  # Add the Braille pattern for the letter

        # Handle space
        elif char == " ":
            result.append("......")  # Add the Braille pattern for space

        # Handle punctuation
        else:
            result.append(english_to_braille.get(char, "......"))  # Handle punctuation or unknown characters

    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    number_mode = False  # Flag to track number mode
    while i < len(braille):
        chunk = braille[i:i+6]

        if chunk == ".....O":  # Uppercase indicator
            i += 6  # Move past the indicator to the actual letter
            if i < len(braille):
                next_chunk = braille[i:i+6]
                if next_chunk in braille_to_english:
                    result.append(braille_to_english[next_chunk].upper())
        elif chunk == ".O.OOO":  # Number mode
            number_mode = True
            i += 6  # Move past the number indicator to the actual number
        elif chunk == "......":  # Space
            result.append(" ")
            number_mode = False  # Exit number mode after space
        elif chunk in braille_to_english:
            if number_mode and chunk in number_to_braille:
                result.append(str([k for k, v in number_to_braille.items() if v == chunk][0]))
            else:
                result.append(braille_to_english[chunk])
        else:
            result.append("?")  # Placeholder for unrecognized characters

        i += 6  # Increment to the next chunk after processing the current one

    return ''.join(result)

def main():
    """Main function to run the translator."""
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])  # Join all the arguments into one string

    # Determine if the input is Braille or English
    if all(char in 'O.' for char in input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
