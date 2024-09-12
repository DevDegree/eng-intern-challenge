import argparse

# Mapping of Braille codes to English letters
braille_to_text = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z"
}

# Braille code for numbers
braille_to_num = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

# Mapping Braille codes to punctuation and special characters
braille_to_symbols = {
    "......": " ", "..OO.O": ".", "..O...": ",", "..OOO.": "!", "..O.OO": "?",
    "....OO": "-", "..OO..": ":", "..O.O.": ";", ".O..O.": "/", ".OO..O": "<",
    "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")"
}

# Reverse dictionaries for English to Braille conversion
text_to_braille = {v: k for k, v in braille_to_text.items()}
num_to_braille = {v: k for k, v in braille_to_num.items()}
symbols_to_braille = {v: k for k, v in braille_to_symbols.items()}

# Braille modifiers
braille_capital = ".....O"
braille_number = ".O.OOO"
braille_space = "......"
braille_decimal = ".O...O"


# Argument parser for command-line interface
def get_input_arguments():
    parser = argparse.ArgumentParser(description="Translate between Braille and English.")
    parser.add_argument("text", nargs='+', help="Input text or Braille to translate.")
    return parser.parse_args()

# Function to check if a given string is a Braille pattern
def is_braille_input(text):
    return all(ch in "O." for ch in text)

# Function to translate from English to Braille
def english_to_braille(text):
    result = []
    number_mode = False

    for ch in text:
        if ch.isupper():
            result.append(braille_capital)
            ch = ch.lower()

        if ch == " ":
            result.append(braille_space)
            number_mode = False  # Exit number mode when encountering a space
        elif ch.isdigit():
            if not number_mode:
                result.append(braille_number)  # Enter number mode by adding number symbol
                number_mode = True
            result.append(num_to_braille[ch])  # Append Braille number
        elif ch == "." and number_mode:
            result.append(braille_decimal)
        elif ch in text_to_braille:
            number_mode = False  # Exit number mode when encountering a letter
            result.append(text_to_braille[ch])
        elif ch in symbols_to_braille:
            number_mode = False  # Exit number mode when encountering a symbol
            result.append(symbols_to_braille[ch])
        else:
            raise ValueError(f"Unrecognized character '{ch}' for Braille translation.")

    return ''.join(result)

# Function to translate from Braille to English
def braille_to_english(braille_text):
    result = []
    number_mode = False
    i = 0

    while i < len(braille_text):
        code = braille_text[i:i+6]

        if code == braille_capital:
            i += 6
            code = braille_text[i:i+6]
            result.append(braille_to_text[code].upper())
        elif code == braille_space:
            result.append(" ")
        elif code == braille_number:
            number_mode = True
            i += 6
            continue  # Skip the rest of the loop to correctly process the next number
        elif number_mode and code == braille_decimal:
            result.append(".")
        elif number_mode and code in braille_to_num:
            result.append(braille_to_num[code])
        elif code in braille_to_text:
            number_mode = False
            result.append(braille_to_text[code])
        elif code in braille_to_symbols:
            result.append(braille_to_symbols[code])
        else:
            raise ValueError(f"Unrecognized Braille code '{code}'.")

        i += 6

    return ''.join(result)


# Main function to handle input and translation logic
if __name__ == "__main__":
    args = get_input_arguments()
    input_text = " ".join(args.text)

    if is_braille_input(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))
