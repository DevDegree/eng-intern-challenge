from sys import argv

# Define constants
BRL_SYM_LEN = 6

BRAILLE_TO_ENGLISH_LETTERS = {
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

BRAILLE_TO_ENGLISH_NUMBERS = {
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


ENGLISH_TO_BRAILLE = {
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

    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
 
    # Special characters
    "capital follows": ".....O",
    "number follows": ".O.OOO",
    " ": "......",
}


# Function takes in a string of Braille text
# and returns a string of English text
def translate_braille_to_english(braille_text):
    translation = ""
    i = 0
    while i < len(braille_text):
        current_symbol = braille_text[i : i + BRL_SYM_LEN]

        # Handle numbers
        if current_symbol == (ENGLISH_TO_BRAILLE["number follows"]):
            # Advance iterator to next symbol
            i += BRL_SYM_LEN
            while i < len(braille_text):
                current_symbol = braille_text[i : i + BRL_SYM_LEN]

                # Check for space to stop number handling
                if current_symbol == (ENGLISH_TO_BRAILLE[" "]):
                    break

                # Assume valid number input 
                translation += BRAILLE_TO_ENGLISH_NUMBERS[current_symbol]
                i += BRL_SYM_LEN

            # Stopped on space, need to translate to English without advancing past it
            continue

        # Handle letters
        elif current_symbol in BRAILLE_TO_ENGLISH_LETTERS:
            translation += BRAILLE_TO_ENGLISH_LETTERS[current_symbol]

        # Handle capital letters
        elif current_symbol == ENGLISH_TO_BRAILLE["capital follows"]:
            # Advance iterator and translate capital letter which follows
            i += BRL_SYM_LEN
            current_symbol = braille_text[i : i + BRL_SYM_LEN]
            translation += BRAILLE_TO_ENGLISH_LETTERS[current_symbol].upper()

        # Must be a space
        else:
            translation += " "

        i += BRL_SYM_LEN

    return translation


# Function takes in a string of English text
# and returns a string of Braille text
def translate_english_to_braille(english_text):
    translation = ""
    i = 0
    while i < len(english_text):

        # Handle letters
        if english_text[i].isalpha():
            # Handle uppercase letter
            if english_text[i].isupper():
                translation += ENGLISH_TO_BRAILLE["capital follows"]
                translation += ENGLISH_TO_BRAILLE[english_text[i].lower()]

            # Handle lowercase letter
            else:
                translation += ENGLISH_TO_BRAILLE[english_text[i]]

        # Handle numbers
        elif english_text[i].isdigit():
            translation += ENGLISH_TO_BRAILLE["number follows"]

            # Continue processing digits
            while i < len(english_text) and english_text[i].isdigit():
                translation += ENGLISH_TO_BRAILLE[english_text[i]]
                i += 1
            
            # Stopped on space, need to translate to Braille without incrementing past it
            continue

        # Must be a space
        else:
            translation += ENGLISH_TO_BRAILLE[" "]

        # Increment the loop
        i += 1

    return translation


# Main function handles input of Braille or English from command line
# and prints translated result to terminal
def main():
    user_input = " ".join(argv[1:])

    # Process as Braille
    if "." in user_input:
        translated_text = translate_braille_to_english(user_input)

    # Process as English
    else:
        translated_text = translate_english_to_braille(user_input)
        
    print(translated_text)

if __name__ == "__main__":
    main()
