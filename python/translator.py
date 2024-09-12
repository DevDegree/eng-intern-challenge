import sys

# Dictionary to translate Braille to English letters
BRAILLE_TO_ENGLISH = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",  # Numbers
    "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D", "O..O..": "E", "OOO...": "F", "OOOO..": "G", "O.OO..": "H", ".OO...": "I", ".OOO..": "J",  # Letters (A-J)
    "O...O.": "K", "O.O.O.": "L", "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O", "OOO.O.": "P", "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T",  # Letters (K-T)
    "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X", "OO.OOO": "Y", "O..OOO": "Z"  # Letters (U-Z)
}

# Dictionary to translate English letters and numbers to Braille
ENGLISH_TO_BRAILLE = {
    "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..", "E": "O..O..", "F": "OOO...", "G": "OOOO..", "H": "O.OO..", "I": ".OO...", "J": ".OOO..",  # Letters (A-J)
    "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.", "P": "OOO.O.", "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.",  # Letters (K-T)
    "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO", "Y": "OO.OOO", "Z": "O..OOO",  # Letters (U-Z)
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."  # Numbers
}

# Special characters and modes in Braille
SPECIAL_BRAILLE = {
    "Capital": ".....O",  # Capital letter marker
    "Number": ".O.OOO",   # Number mode marker
    "Space": "......"     # Space marker
}

# Function to handle translation from Braille to English
def braille_to_english(braille_text):
    braille_cells = [braille_text[i:i + 6] for i in range(0, len(braille_text), 6)]
    result, capital_mode, number_mode = [], False, False

    for cell in braille_cells:
        if cell == SPECIAL_BRAILLE["Capital"]:  # Handle capital mode
            capital_mode = True
        elif cell == SPECIAL_BRAILLE["Number"]:  # Handle number mode
            number_mode = True
        elif cell == SPECIAL_BRAILLE["Space"]:  # Handle space
            result.append(" ")
            number_mode = False
        elif number_mode and cell in BRAILLE_TO_ENGLISH:
            result.append(BRAILLE_TO_ENGLISH[cell])  # Append number
        elif capital_mode and cell in BRAILLE_TO_ENGLISH:
            result.append(BRAILLE_TO_ENGLISH[cell].upper())  # Append capital letter
            capital_mode = False  # Reset capital mode
        elif cell in BRAILLE_TO_ENGLISH:
            result.append(BRAILLE_TO_ENGLISH[cell].lower())  # Append lowercase letter

    return ''.join(result)

# Function to handle translation from English to Braille
def english_to_braille(english_text):
    result, number_mode = [], False

    for char in english_text:
        if char.isdigit():  # Handle digits
            if not number_mode:
                result.append(SPECIAL_BRAILLE["Number"])  # Insert number mode marker
                number_mode = True
            result.append(ENGLISH_TO_BRAILLE[char])  # Append Braille for digit
        elif char.isupper():  # Handle capital letters
            result.append(SPECIAL_BRAILLE["Capital"])  # Insert capital marker
            result.append(ENGLISH_TO_BRAILLE[char.upper()])  # Append Braille for capital letter
        elif char == " ":  # Handle spaces
            result.append(SPECIAL_BRAILLE["Space"])
            number_mode = False  # Exit number mode on space
        else:  # Handle lowercase letters
            result.append(ENGLISH_TO_BRAILLE[char.upper()])  # Append Braille for letter

    return ''.join(result)

# Main function to detect input type and perform translation
def translate(input_text):
    if set(input_text).issubset({"O", "."}):  # Detect Braille input
        return braille_to_english(input_text)
    return english_to_braille(input_text)  # Otherwise, assume English

# Command-line interface
if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])  # Concatenate arguments into a single string
    print(translate(input_text))
