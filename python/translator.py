# Braille to English and English to Braille Translator

# Braille Translator Mappings
BRAILLE_ENGLISH = {
    "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..", "E": "O..O..", 
    "F": "OOO...", "G": "OOOO..", "H": "O.OO..", "I": ".OO...", "J": ".OOO..",
    "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.",
    "P": "OOO.O.", "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.",
    "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO", "Y": "OO.OOO", 
    "Z": "O..OOO"
}

BRAILLE_NUMBERS = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Special symbols for capitalization and numbers
BRAILLE_CAPITAL = ".....O"
BRAILLE_NUMBER = ".O.OOO"
BRAILLE_SPACE = "......"

# Reverse mapping for Braille to English
ENGLISH_BRAILLE = {v: k for k, v in BRAILLE_ENGLISH.items()}
ENGLISH_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}


# Function to translate English to Braille
def english_to_braille(text):
    braille_output = []
    number_mode = False
    
    for char in text:
        if char.isdigit() and not number_mode:
            braille_output.append(BRAILLE_NUMBER)
            number_mode = True
        elif char.isalpha() and number_mode:
            number_mode = False  # Reset after space or non-number char
        
        if char == " ":
            braille_output.append(BRAILLE_SPACE)
        elif char.isupper():
            braille_output.append(BRAILLE_CAPITAL)
            braille_output.append(BRAILLE_ENGLISH[char.upper()])
        elif char.isdigit():
            braille_output.append(BRAILLE_NUMBERS[char])
        else:
            braille_output.append(BRAILLE_ENGLISH[char.upper()])
    
    return ''.join(braille_output)


# Function to translate Braille to English
def braille_to_english(braille_text):
    english_output = []
    i = 0
    number_mode = False
    capitalize_next = False

    while i < len(braille_text):
        braille_char = braille_text[i:i+6]

        if braille_char == BRAILLE_SPACE:
            english_output.append(" ")
        elif braille_char == BRAILLE_CAPITAL:
            capitalize_next = True
        elif braille_char == BRAILLE_NUMBER:
            number_mode = True
        else:
            if number_mode:
                english_char = ENGLISH_NUMBERS.get(braille_char, "")
            else:
                english_char = ENGLISH_BRAILLE.get(braille_char, "")
            
            if capitalize_next:
                english_output.append(english_char.upper())
                capitalize_next = False
            else:
                english_output.append(english_char.lower())
        
        i += 6  # Move to the next Braille character
    
    return ''.join(english_output)


# Main function to determine input type and translate accordingly
def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text>")
        return
    
    input_text = sys.argv[1]

    # Check if the input is in Braille (contains only O's and .s)
    if all(c in "O." for c in input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))


if __name__ == "__main__":
    main()

