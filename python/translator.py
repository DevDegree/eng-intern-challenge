import sys
#Mahdi Metwally
#Mahdimetwally@gmail.com

# Define Braille translation dictionary
# This dictionary maps English letters, digits, and punctuation marks to their corresponding Braille patterns.
english_to_braille = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..',
    'I': '.OO...', 'J': '.OOO..', 'K': 'O...O.',
    'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.',
    'T': '.OOOO.', 'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O',
    'X': 'OO..OO', 'Y': 'OO.OOO', 'Z': 'O..OOO', ' ': '......',
    'O': '.OOOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '.': 'OO..O.', ',': '..O...', '?': '..O.OO',
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO',
    '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O',
    ')': '.O.OO.', 1: '.....O', 2: '.O...O', 3: '.O.OOO'
}

def braille_translation(english_string):
    """
    Converts an English string to its corresponding Braille representation.

    Args:
        english_string (str): The input string to be translated to Braille.

    Returns:
        str: The translated Braille string.
    """
    braille_output = ""
    digSen = False  # Flag to track whether the previous character was a digit.

    # Iterate through each character in the input string.
    for char in english_string:
        if char.isdigit():  # Check if the character is a digit.
            if digSen:  # Prevent unnecessary repetition of the number signifier.
                braille_output += english_to_braille.get(3)
                digSen = True
            braille_output += english_to_braille.get(char, '')
        elif char == '.':  # Handle punctuation.
            braille_output += english_to_braille.get(2)
        elif char.isupper():  # Check if the character is uppercase.
            digSen = False
            braille_output += english_to_braille.get(1)  # Add uppercase signifier.
            braille_output += english_to_braille.get(char, '')
        else:  # Handle lowercase letters.
            digSen = False
            braille_output += english_to_braille.get(char.upper(), '')

    return braille_output

def main():
    """
    Main function to handle input and output for the Braille translator.
    """
    # Ensure correct program usage.
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string_to_translate>")
        return

    # Convert all input arguments to a single string.
    input_string = " ".join(sys.argv[1:])

    # Translate the input string to Braille.
    braille_output = braille_translation(input_string)

    # Print the Braille translation to the terminal.
    print(braille_output)

if __name__ == "__main__":
    main()


