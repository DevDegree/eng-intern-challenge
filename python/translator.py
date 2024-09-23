import sys

# Mapping of Braille to English letters
braille_to_english = {
    "0.....": "A", "0.0...": "B", "00....": "C", "00.0..": "D", "0..0..": "E",
    "000...": "F", "0000..": "G", "0.00..": "H", ".00...": "I", ".000..": "J",
    "0....0": "K", "0.0..0": "L", "00...0": "M", "00.0.0": "N", "0..0.0": "O",
    "000..0": "P", "0000.0": "Q", "0.00.0": "R", ".00..0": "S", ".000.0": "T",
    "0....00": "U", "0.0..00": "V", ".000000": "W", "00...00": "X", "00.0.00": "Y", "0..0.00": "Z",
    ".0.000": " ",  # Space
    ".....0": "NUMBER",  # Number indicator
    "......": "CAPITAL",  # Capital letter indicator
}

# Mapping of English letters to Braille
english_to_braille = {
    "a": "0.....", "b": "0.0...", "c": "00....", "d": "00.0..", "e": "0..0..",
    "f": "000...", "g": "0000..", "h": "0.00..", "i": ".00...", "j": ".000..",
    "k": "0....0", "l": "0.0..0", "m": "00...0", "n": "00.0.0", "o": "0..0.0",
    "p": "000..0", "q": "0000.0", "r": "0.00.0", "s": ".00..0", "t": ".000.0",
    "u": "0....00", "v": "0.0..00", "w": ".000000", "x": "00...00", "y": "00.0.00", "z": "0..0.00",
    " ": ".0.000"  # Space
}

# Mapping for numbers in Braille
number_map = {
    "1": "0.....", "2": "0.0...", "3": "00....", "4": "00.0..", "5": "0..0..",
    "6": "000...", "7": "0000..", "8": "0.00..", "9": ".00...", "0": ".000.."
}

# Check if the input is Braille (contains only '.' and '0')
def is_braille(input_string):
    braille_words = input_string.split(" ")
    # Ensure each word has 6 characters and only consists of '0' and '.'
    return all(len(word) == 6 and set(word).issubset({"0", "."}) for word in braille_words)

# Convert Braille to English
def braille_to_text(braille_string):
    braille_words = braille_string.split(" ")
    english_output = ""
    capital_next = False  # Track if the next letter should be capitalized
    number_next = False   # Track if the next sequence is a number

    for braille_char in braille_words:
        if braille_char == "......":
            capital_next = True  # Capital indicator found
        elif braille_char == ".....0":
            number_next = True  # Number indicator found
        elif braille_char in braille_to_english:
            letter = braille_to_english[braille_char]
            if capital_next:
                letter = letter.upper()
                capital_next = False  # Reset capitalization after use
            english_output += letter
        else:
            english_output += "?"  # Unrecognized character

    return english_output

# Convert English to Braille
def text_to_braille(text_string):
    braille_output = ""
    for char in text_string:
        if char.isupper():
            braille_output += "...... "  # Add capital indicator
            braille_output += english_to_braille[char.lower()] + " "
        elif char.isdigit():
            braille_output += ".....0 "  # Add number indicator
            braille_output += number_map[char] + " "
        elif char == " ":
            braille_output += ".0.000 "  # Add space
        else:
            braille_output += english_to_braille[char] + " "

    return braille_output.strip()

# Main program function
def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    input_string = sys.argv[1]
    
    # Detect whether the input is Braille or English
    if is_braille(input_string):
        # If input is Braille, convert to English
        print(braille_to_text(input_string))
    else:
        # If input is English, convert to Braille
        print(text_to_braille(input_string))

if __name__ == "__main__":
    main()


