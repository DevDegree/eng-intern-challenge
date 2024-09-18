# Braille dictionary: Maps Braille symbols to English characters (each symbol is 6 characters long)
BRAILLE_TO_ENGLISH = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "capital",  # Marker to indicate the next character should be capitalized
    ".O.OOO": "number",  # Marker to indicate numbers will follow
    "......": " "        # Space character
}

# Reverse dictionary: Maps English characters back to Braille symbols
ENGLISH_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", 
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", 
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......",  # Space character
    "capital": ".....O",  # Marker for capital letters
    "number": ".O.OOO"   # Marker for numbers
}

# Function to convert English text into Braille
def english_to_braille(english):
    braille = ""  # This will hold the Braille translation
    number_mode = False  # To track if we are in number mode (for consecutive numbers)

    # Process each character in the input text
    for char in english:
        if char.isupper():  # Check if the character is an uppercase letter
            # Add capitalization marker followed by the lowercase version of the character
            braille += ENGLISH_TO_BRAILLE["capital"] + ENGLISH_TO_BRAILLE[char.lower()]
            number_mode = False  # Exit number mode when processing letters
        elif char.islower():  # Check if the character is a lowercase letter
            braille += ENGLISH_TO_BRAILLE[char]
            number_mode = False  # Exit number mode when processing letters
        elif char.isdigit():  # Check if the character is a digit (0-9)
            if not number_mode:  # If we aren't in number mode, add the number marker
                braille += ENGLISH_TO_BRAILLE["number"]
                number_mode = True  # Enter number mode
            braille += ENGLISH_TO_BRAILLE[char]  # Add the Braille representation of the number
        elif char == " ":  # Handle spaces
            braille += ENGLISH_TO_BRAILLE[" "]
            number_mode = False  # Exit number mode when a space is encountered
        else:
            raise ValueError(f"Unsupported character: '{char}'")  # Raise error for unsupported characters
    
    return braille  # Return the full Braille translation

# Function to convert Braille back to English text
def braille_to_english(braille):
    english = ""  # This will hold the English translation
    capital_next = False  # To track if the next letter should be capitalized
    number_mode = False  # To track if we are in number mode (for consecutive numbers)

    # Split the Braille string into chunks of 6 characters, each representing one symbol
    braille_chunks = [braille[i:i+6] for i in range(0, len(braille), 6)]

    # Process each Braille chunk
    for chunk in braille_chunks:
        if chunk == ".....O":  # Capitalization marker
            capital_next = True
            continue
        elif chunk == ".O.OOO":  # Number marker
            number_mode = True
            continue
        elif chunk == "......":  # Space
            english += " "  # Add a space to the English text
            number_mode = False  # Exit number mode when a space is encountered
            continue

        # If the chunk is not in the Braille dictionary, raise an error
        if chunk not in BRAILLE_TO_ENGLISH:
            raise ValueError(f"Braille symbol '{chunk}' not found.")

        char = BRAILLE_TO_ENGLISH[chunk]  # Get the corresponding English character

        if number_mode:
            # Convert letters a-j into numbers (a=1, b=2, ..., j=0)
            if char in "abcdefghij":
                char = str(ord(char) - ord('a') + 1)
                if char == "10":  # Handle 0 (which corresponds to 'j')
                    char = "0"
            else:
                raise ValueError(f"Invalid number character in number mode: '{char}'")
            # Stay in number mode for consecutive digits
        else:
            if capital_next:  # If the previous symbol was a capitalization marker, capitalize the letter
                char = char.upper()
                capital_next = False

        english += char  # Add the character to the English translation

    return english  # Return the full English translation

# Main function to detect if the input is English or Braille, and translate accordingly
def translate(input_text):
    # If the input consists only of 'O', '.', or ' ' (Braille), translate from Braille to English
    if all(c in "O. " for c in input_text):
        return braille_to_english(input_text)
    else:  # Otherwise, assume the input is English and translate to Braille
        return english_to_braille(input_text)

# Entry point for command-line arguments
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:  # Check if there are command-line arguments
        input_text = " ".join(sys.argv[1:])  # Combine all arguments into a single string
        try:
            result = translate(input_text)  # Translate the input
            print(result)  # Output the result
        except ValueError as e:
            print(f"Error: {e}")  # Print error message if an invalid character is found
    else:
        print("Please provide a string to translate.")  # Prompt for input if no arguments are provided
