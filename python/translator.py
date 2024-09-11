import sys

# Braille to English dictionary
BRAILLE_TO_ENGLISH = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
}

# English alphabet to Braille dictionary
ENGLISH_TO_BRAILLE = {letter: braille for braille, letter in BRAILLE_TO_ENGLISH.items()}

# Braille to numbers dictionary
BRAILLE_TO_NUMBERS = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

# Numbers to Braille dictionary
NUMBERS_TO_BRAILLE = {number: braille for braille, number in BRAILLE_TO_NUMBERS.items()}

# Braille symbols constants
BRAILLE_SPACE = "......"
BRAILLE_CAPITAL = ".....O"
BRAILLE_NUMBER_SIGN = ".O.OOO"


def braille_to_english(braille_text):
    """
    Translates Braille to English text.
    """
    braille_chars = []
    for i in range(0, len(braille_text), 6):
        braille_chars.append(braille_text[i : i + 6])

    capitalize_next = False
    number_mode = False
    english_text = []

    for braille_char in braille_chars:
        # Stop numbers mode if we encounter a space
        # Append space and continue to next character
        if braille_char == BRAILLE_SPACE:
            english_text.append(" ")
            capitalize_next = False
            number_mode = False
            continue
        
        if braille_char == BRAILLE_CAPITAL:
            capitalize_next = True
        elif braille_char == BRAILLE_NUMBER_SIGN:
            number_mode = True
        else:
            if number_mode:
                english_text.append(BRAILLE_TO_NUMBERS[braille_char])
            else:
                
                letter = BRAILLE_TO_ENGLISH[braille_char]
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                english_text.append(letter)

    return "".join(english_text)


def english_to_braille(english_text):
    """
    Translates English text to Braille.
    """
    braille_text = []
    number_mode = False
    
    for char in english_text:
        if char == " ":
            braille_text.append(BRAILLE_SPACE)
            number_mode = False
            continue
        
        if char.isdigit():
            if not number_mode:
                braille_text.append(BRAILLE_NUMBER_SIGN)
                number_mode = True
            braille_text.append(NUMBERS_TO_BRAILLE[char])
            continue
        
        if number_mode:
            braille_text.append(BRAILLE_SPACE)
            number_mode = False
        
        braille_char = ENGLISH_TO_BRAILLE[char.lower()]
        
        if char.isupper():
            braille_text.append(BRAILLE_CAPITAL)
        
        braille_text.append(braille_char)
    
    return "".join(braille_text)


# Check if a string is valid Braille
def is_valid_braille(text):
    """
    Checks if a string is valid Braille.
    """
    if len(text) % 6 != 0:
        return False

    for c in text:
        if c not in ".O":
            return False
        
    return True



def translate():
    """
    Translates command-line arguments from English to Braille or vice versa.
    Will print the translated text to the console.
    """
    if len(sys.argv) < 2:
        print("ERROR: Missing arguments")
        return

    input_text = " ".join(sys.argv[1:]).strip()

    if is_valid_braille(input_text):
        output_text = braille_to_english(input_text)
    else:
        output_text = english_to_braille(input_text)

    print(output_text)



if __name__ == "__main__":
    # Run the translator
    translate()
