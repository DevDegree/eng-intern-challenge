import sys

# Mapping of letters to braile characters
LETTER_TO_BRAILLE = {
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
}

# Mapping of numbers to character
NUMBER_TO_BRAILLE = {
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
}

# Mapping of braile character to numbers by inverting existing mapping
BRAILE_TO_NUMBER = {braile: number for number, braile in NUMBER_TO_BRAILLE.items()}

# Mapping of braile character to characters by inverting existing mapping
BRAILE_TO_CHAR = {braile: letter for letter, braile in LETTER_TO_BRAILLE.items()}

SPACE = "......"
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"

ASCII_MIN_NUMBER_VALUE = 48 # ascii value for 0
ASCII_MAX_NUMBER_VALUE = 57 # ascii value for 9
ASCII_MIN_UPPERCASE_VALUE = 65 # ascii value for 'A'
ASCII_MAX_UPPERCASE_VALUE = 90 # ascii value for 'Z'

def braile_to_english(user_input):
    """
    Converts a Braille string to its English equivalent.
    
    Input: A Braille string where characters are represented by 'O' and '.' in 6-dot format.
    Output: Prints the translated English string.
    """
    result = []
    number_mode = False
    capital_added = False
    
    # iterate from 0 to end of input, incremeting index by 6 each iteration
    for index in range(0, len(user_input), 6):
        braile_sequence = user_input[index : index + 6]

        # If the current braile is a braile space character 
        if braile_sequence == SPACE:
            number_mode = False # disable number translation

        # If the current braile is a capital follows character
        elif braile_sequence == CAPITAL_FOLLOWS:
            index += 6
            braile_sequence = user_input[index : index + 6] # get the next brailie character
            result.append(BRAILE_TO_CHAR[braile_sequence].upper()) # add the uppercase version of the character
            index += 6
            capital_added = True # enable flag so that character isnt double added
            continue
        
        # If the current braile is a number follows character 
        elif braile_sequence == NUMBER_FOLLOWS:
            number_mode = True
            continue

        if number_mode:
            result.append(BRAILE_TO_NUMBER[braile_sequence]) # Use braile to number mapping for adding to result
        else:
            if not capital_added:
                result.append(BRAILE_TO_CHAR[braile_sequence]) # Use braile to character mapping for adding to result
            capital_added = False

    print("".join(result))


def english_to_braile(user_input):
    """
    Converts an English string to its Braille equivalent.
    
    Input: English string containing letters, spaces, and numbers.
    Output: Prints the Braille translation of the input string.
    """
    result = []
    numberMode = False
    
    for char in user_input:
        
        # if space and number mode on
        if char == " " and numberMode:
            numberMode = False   # disable number flag
            result.append(LETTER_TO_BRAILLE[char]) # append space
            continue
        
        # if it is a number
        if ord(char) >= ASCII_MIN_NUMBER_VALUE and ord(char) <= ASCII_MAX_NUMBER_VALUE:
            if not numberMode:
                # turn on number flag
                numberMode = True
                # append NUMBER_FOLLOWS add number representation
                result.append(NUMBER_FOLLOWS)
            result.append(NUMBER_TO_BRAILLE[char])

        # else it is a letter
        else:
            # if capital letter
            if ord(char) >= ASCII_MIN_UPPERCASE_VALUE and ord(char) <= ASCII_MAX_UPPERCASE_VALUE:
                # append CAPITAL_FOLLOWS + braile represenation of the char
                result.append(CAPITAL_FOLLOWS)
                result.append(LETTER_TO_BRAILLE[char.lower()])
            else:
                result.append(LETTER_TO_BRAILLE[char])

    print("".join(result))


def main():
    """
    Determines whether to translate an input string from Braille to English or vice versa.
    
    Input: A string passed as command-line arguments (either Braille or English text).
    Output: Calls the appropriate translation function and prints the result.
    """
    user_input = None
    
    # if command line has more than 2 args, combine all input for translation
    if len(sys.argv) >= 2:
        user_input = " ".join(sys.argv[1:])
    else:
        return
    
    braile_chars = {"O", ".", " "} # the allowed braile character
    nonBraileCharDetected = False 
    
    for c in user_input:
        # check if we have proper braile, if we receive an unexpected char, enable flag and break
        if c not in braile_chars: 
            nonBraileCharDetected = True
            break
        
    if nonBraileCharDetected:
        english_to_braile(user_input)
    else:
        braile_to_english(user_input)


if __name__ == "__main__":
    main()