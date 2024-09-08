import sys

# Braille dictionary (O = raised dot, . = flat area)
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
    ".O.OOO": "1", ".O.O.O": "2", "OO...O": "3", "OO.O.O": "4", "O.O..O": "5",
    "OOO..O": "6", "OOOO.O": "7", "O.OO.O": "8", ".OO...": "9", ".OO.OO": "0",
    "......": " ", ".....O": "capital", ".O..OO": "number"
}

english_to_braille = {v: k for k, v in braille_to_english.items() if v not in ['capital', 'number', ' ']}

# Helper function to detect if input is Braille
def is_braille(input_string):
    return all(c in "O." for c in input_string)

# Function to translate Braille to English
def braille_to_text(braille):
    chars = [braille[i:i + 6] for i in range(0, len(braille), 6)]
    result = []
    capital_flag = False
    number_flag = False

    for char in chars:
        if char == "......":  # Space
            result.append(" ")
            number_flag = False  # Reset number flag on space
        elif char == ".....O":  # Capital flag
            capital_flag = True
        elif char == ".O..OO":  # Number flag
            number_flag = True
        else:
            if number_flag:
                result.append(braille_to_english[char])  # Treat as number
            else:
                letter = braille_to_english[char]
                if capital_flag:
                    letter = letter.upper()
                    capital_flag = False
                result.append(letter)
    
    return "".join(result)

# Function to translate English to Braille
def text_to_braille(text):
    result = []
    for char in text:
        if char.isupper():
            result.append(".....O")  # Capital flag
            result.append(english_to_braille[char.lower()])
        elif char.isdigit():
            result.append(".O..OO")  # Number flag
            result.append(english_to_braille[char])
        elif char == " ":
            result.append("......")
        else:
            result.append(english_to_braille[char])
    return "".join(result)

# Main function to handle command line arguments
def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)

    input_string = " ".join(sys.argv[1:])

    if is_braille(input_string):  # If input is Braille
        print(braille_to_text(input_string))
    else:  # If input is English
        print(text_to_braille(input_string))

if __name__ == "__main__":
    main()

