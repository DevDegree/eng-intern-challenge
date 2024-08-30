import sys  # Import the sys module to access command-line arguments

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

# English to Braille mapping, reversing the braille_to_english mapping
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Additional mappings for numbers in Braille
number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

def translate_to_braille(text):
    """Translate English text to Braille."""
    result = []  # List to store Braille translation
    number_mode = False  # Flag to check if we are in number mode
    for char in text:  # Iterate over each character in the input text
        if char.isdigit():  # Check if the character is a digit
            if not number_mode:  # If not in number mode, switch to number mode
                result.append(".O.OOO")  # Add "Number follows" indicator
                number_mode = True  # Set number mode to True
            result.append(number_to_braille[char])  # Add the Braille pattern for the number
        elif char.isalpha():  # Check if the character is an alphabet letter
            if number_mode:  # If we were in number mode, exit number mode
                result.append("......")  # Add a space to exit number mode
                number_mode = False  # Set number mode to False
            if char.isupper():  # Check if the character is uppercase
                result.append(".....O")  # Add "Capital follows" indicator
            result.append(english_to_braille[char.lower()])  # Add the Braille pattern for the letter
        else:  # For punctuation or spaces
            if number_mode:  # If we were in number mode, exit number mode
                #result.append("......")  # Add a space to exit number mode
                number_mode = False  # Set number mode to False
            result.append(english_to_braille[char])  # Add the Braille pattern for the punctuation/space
    return ''.join(result)  # Join the list into a single string and return it

def translate_to_english(braille):
    """Translate Braille to English text."""
    result = []  # List to store English translation
    i = 0  # Index for traversing the Braille string
    while i < len(braille):  # Iterate over the Braille string
        chunk = braille[i:i+6]  # Extract the next 6 characters (a Braille pattern)
        if chunk == ".....O":  # Check if it's the "Capital follows" indicator
            i += 6  # Move to the next 6 characters
            next_chunk = braille[i:i+6]  # Extract the next Braille pattern
            result.append(braille_to_english[next_chunk].upper())  # Convert to uppercase and add to result
        elif chunk == ".O.OOO":  # Check if it's the "Number follows" indicator
            i += 6  # Move to the next 6 characters
            while i < len(braille) and braille[i:i+6] != "......":  # Continue until a space is found
                result.append(str(list(number_to_braille.values()).index(braille[i:i+6]) + 1))  # Convert Braille to a digit and add to result
                i += 6  # Move to the next Braille pattern
            continue  # Skip adding "......" (space) to result
        else:  # For regular Braille patterns
            result.append(braille_to_english[chunk])  # Convert to English and add to result
        i += 6  # Move to the next Braille pattern
    return ''.join(result)  # Join the list into a single string and return it

def main():
    """Main function to run the translator."""
    input_text = ' '.join(sys.argv[1:])  # Join all command-line arguments into a single string

    # Determine if the input is Braille or English
    if all(char in 'O.' for char in input_text):
        # If all characters are 'O' or '.', assume it's Braille
        print(translate_to_english(input_text))  # Translate from Braille to English
    else:
        # Otherwise, assume it's English
        print(translate_to_braille(input_text))  # Translate from English to Braille

if __name__ == "__main__":
    main()  # Call the main function when the script is run
