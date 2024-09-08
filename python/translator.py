import sys

# English to Braille / Braille to English dictionaries
ENGLISH_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", 
    "A": ".....OO.....", "B": ".....OO.O...", "C": ".....OOO....", "D": ".....OOOO...", "E": ".....O..O..", 
    "F": ".....OOOO...", "G": ".....OOOOO..", "H": ".....OOO...", "I": ".....O..OO..", "J": ".....O..OOO.", 
    "K": ".....OO...O", "L": ".....OO.O.O", "M": ".....OOOO.O", "N": ".....OOOOO.", "O": ".....O..O.", 
    "P": ".....OOOO.O", "Q": ".....OOOOO.", "R": ".....OOO.O.", "S": ".....O..OO.", "T": ".....O..OOO.", 
    "U": ".....OO...OO", "V": ".....OO.OOO", "W": ".....O..OOO", "X": ".....OOOO..O", "Y": ".....OOOOO.O", 
    "Z": ".....O..OOO", 
    "1": ".O.....", "2": ".O.O...", "3": ".OO....", "4": ".OO.O..", "5": ".O..O..", 
    "6": ".OOO...", "7": ".OOOO..", "8": ".O.OO..", "9": "..OO...", "0": "..OOO..", 
    " ": "......"
}

BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}

# Function to determine if the input is English or Braille
def is_braille(input_string):
    return all(c in "O." for c in input_string)

# Function to translate English to Braille
def english_to_braille(text):
    braille = ""
    number_mode = False

    for char in text:
        if char.isupper():
            braille += ".....O"  # Capital letter prefix
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                braille += ".....O"  # Number mode prefix
                number_mode = True
        else:
            number_mode = False  # Reset number mode for non-digit characters
        
        translated_char = ENGLISH_TO_BRAILLE.get(char, "")
        braille += translated_char

    return braille

# Function to translate Braille to English
def braille_to_english(text):
    english = ""
    i = 0
    while i < len(text):
        if text[i:i+6] == ".....O":  # Capital or number prefix
            i += 6
            if i + 6 <= len(text):
                braille_char = text[i:i+6]
                english_char = BRAILLE_TO_ENGLISH.get(braille_char, "")
                if english_char.isdigit():
                    english += english_char
                else:
                    english += english_char.upper()
            i += 6
        else:
            braille_char = text[i:i+6]
            english += BRAILLE_TO_ENGLISH.get(braille_char, "")
            i += 6
    return english

# Main function to handle input and output
def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <string_to_translate>")
        return

    input_string = sys.argv[1]
    
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()


#continue