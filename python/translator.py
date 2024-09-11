# A Braille translator that converts English text to Braille and vice versa.

# Importing the necessary libraries
import sys

# Mapping of English alphabet and numbers to Braille
ALPHABET_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO"
}

NUMBER_TO_BRAILLE = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO..."
}

# Symbols for Capitalization, Number, and Space
CAPITAL = ".....O"
NUMBER = ".O.OOO"
SPACE = "......"

# Reverse the dictionary to get the English alphabet
BRAILLE_TO_ALPHABET = {value: key for key, value in ALPHABET_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {value: key for key, value in NUMBER_TO_BRAILLE.items()}

# Function to convert English text to Braille
def english_to_braille(text):
    output = []
    is_number = False  # Keep track of whether we are in number mode

    # Loop through the characters in the input text
    for char in text:
        if char.isupper():
            output.append(CAPITAL)  # Add capital indicator
            output.append(ALPHABET_TO_BRAILLE[char.lower()])  # Convert the letter to Braille
            is_number = False  # Reset number mode if a capital letter is found
        elif char.isdigit():
            if not is_number:
                output.append(NUMBER)  # Add number indicator the first time a number is found
                is_number = True  # Stay in number mode until a space is found
            output.append(NUMBER_TO_BRAILLE[char])  # Convert the number to Braille
        elif char == " ":
            output.append(SPACE)  # Add space
            is_number = False  # Reset number mode when a space is encountered
        else:
            output.append(ALPHABET_TO_BRAILLE[char])  # Convert the letter to Braille
            is_number = False  # If a letter is found, reset number mode

    return "".join(output)


# Function to convert Braille to English text
def braille_to_english(text):
    output = []
    is_capital = False
    is_number = False
    braille_chars = [text[i:i+6] for i in range(0, len(text), 6)]

    # Loop through the Braille characters
    for char in braille_chars:
        if char == CAPITAL:
            is_capital = True
            is_number = False  # Reset number mode if a capital indicator is found
        elif char == NUMBER:
            is_number = True
            is_capital = False  # Reset capital mode if a number indicator is found
        elif char == SPACE:
            output.append(" ")
            is_number = False  # Reset number mode when space is encountered
        elif is_number:
            # Ensure the Braille character is valid in the number mapping
            if char in BRAILLE_TO_NUMBER:
                output.append(BRAILLE_TO_NUMBER[char])
            else:
                raise KeyError(f"Unrecognized number Braille pattern: {char}")
        elif is_capital:
            output.append(BRAILLE_TO_ALPHABET[char].upper())
            is_capital = False  # Capital applies only to the next letter
        else:
            output.append(BRAILLE_TO_ALPHABET[char])
    
    return "".join(output)

# Function to check if the input text is Braille
def is_braille(text):
    return all(char in "O." for char in text)

# Main function to handle input and output
if __name__ == "__main__":
    
    input_text = " ".join(sys.argv[1:])

    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))