import sys

# Define the Braille alphabet
alphabet_english_braille = {
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
    " ": "......",
    "CAP": ".....O",
    "NUM": ".O.OOO",
}

alphabet_braille_english = {value: key for key, value in alphabet_english_braille.items()}

# Define number-letter mappings
number_to_letter = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "0": "j",
}

letter_to_number = {value: key for key, value in number_to_letter.items()}

# Parse the input string
string = " ".join(sys.argv[1:])

# Translation function for Braille to English
def braille_to_english(string):
    caps = False
    num = False
    # Loop through the string in 6-character chunks
    for i in range(0, len(string), 6):
        char = alphabet_braille_english[string[i : i + 6]]

        # Handle "capital follows"
        if char == "CAP":
            caps = True
            continue

        # Handle "number follows"
        if char == "NUM":
            num = True
        
        # Handle spaces
        elif char == " ":
            # Reset "number follows"
            num = False
            print(" ", end="")

        # Handle numbers
        elif num:
            print(letter_to_number[char], end="")

        # Handle capital letters
        elif caps:
            print(char.upper(), end="")

        # Handle lowercase letters
        else:
            print(char, end="")

        # Reset "capital follows"
        caps = False


# Translation function for English to Braille
def english_to_braille(string):
    num = False
    # Loop through the string
    for char in string:
        # Handle numbers
        if char.isdigit():
            if not num:
                num = True
                # Print the "number follows" character
                print(alphabet_english_braille["NUM"], end="")
            print(alphabet_english_braille[number_to_letter[char]], end="")
        else:
            num = False
            # Handle capital letters
            if char.isupper():
                # Print the "capital follows" character
                print(alphabet_english_braille["CAP"], end="")
                char = char.lower()
            print(alphabet_english_braille[char], end="")

# Determine the language of the input string
def is_braille(string):
    return all(char in "O." for char in string) and len(string) % 6 == 0

if is_braille(string):
    braille_to_english(string)
else:
    english_to_braille(string)