import sys

# **NOTE**
# The dictionaries were defined in this file to prevent issues from reading from another file (not sure what environment it will be tested in and read/write privileges)

# English characters and space to braille
ENG_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", " ": "......"
}
# Numbers to braille 
NUMS_TO_BRAILLE = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO.."
}
# Special characters capital follows and number follows to braille
SPEC_TO_BRAILLE = { "capital": ".....O", "number": ".O.OOO" }

# Static string declaration to prevent using strings in comparisons
CAPITAL = "capital"
NUMBER = "number"
SPACE = " "

# Function to check if the input is Braille
def isBraille(str):
    braille = ["O", "."]
    for char in str:
        if char not in braille:
            return False
    return True

# Function to check if the input is english (our accepted version with letters, numbers, and space)
def isEnglish(str):
    for char in str:
        if not char.isalpha() and not char.isnumeric() and char != SPACE:
            return False
    return True

# Function to convert braille inputs into english given an input string str
def brailleToEnglish(str):
    # Only accept inputs that are multiples of 6 (a complete braille input)
    if len(str) % 6 != 0:
        print("Incorrect length input, must be a multiple of 6")
        exit()

    # Reverse the english/special/numbers to braille mapping (both keys and values are unique in all dictionaries)
    BRAILLE_TO_ENG = {value: key for key, value in ENG_TO_BRAILLE.items()}
    BRAILLE_TO_SPEC = {value: key for key, value in SPEC_TO_BRAILLE.items()}
    BRAILLE_TO_NUMS = {value: key for key, value in NUMS_TO_BRAILLE.items()}
    # Check just to ensure the mapping was valid
    if len(BRAILLE_TO_ENG) != len(ENG_TO_BRAILLE) and len(BRAILLE_TO_SPEC) != len(SPEC_TO_BRAILLE) and len(BRAILLE_TO_NUMS) != len(NUMS_TO_BRAILLE):
        print("Error with english/braille mapping")
        exit()

    # Flags used to keep track if 'number follows' or 'capital follows' was used previously
    num_flag = False
    cap_flag = False
    
    # Iterate through the string 6 characteres at a time (representing one braille input)
    for i in range(0, len(str), 6):
        # The substring represents one braille input
        substring = str[i:i+6]
        res = ""

        # If the substring is a special character set their flags to true
        if substring in BRAILLE_TO_SPEC:
            if BRAILLE_TO_SPEC[substring] == NUMBER:
                num_flag = True
            elif BRAILLE_TO_SPEC[substring] == CAPITAL:
                cap_flag = True
            else:
                print("Error in BRAILLE_TO_SPEC")
                exit()
        # If only the num_flag is true (only numbers should follow or a space)
        elif num_flag and not cap_flag:
            # Add the number to the result if it's a number
            if substring in BRAILLE_TO_NUMS:
                res += BRAILLE_TO_NUMS[substring]
            # Add a space to the result if it's a space and set all flags to false
            elif substring in BRAILLE_TO_ENG and BRAILLE_TO_ENG[substring] == SPACE:
                res += BRAILLE_TO_ENG[substring]
                num_flag = False
                cap_flag = False
            else:
                print("Invalid braille for a number")
                exit()
        # If only the cap_flag is true, add the next character to result as an upper case (if it exists)
        # and reset the cap_falg to false
        elif cap_flag and not num_flag:
            if substring in BRAILLE_TO_ENG and BRAILLE_TO_ENG[substring] != SPACE:
                res += BRAILLE_TO_ENG[substring].upper()
                cap_flag = False
            else:
                print("Character after 'capital follows' must be a letter")
                exit()
        # If there are no flags set to true, add a normal letter to the result if it exists
        elif not num_flag and not cap_flag:
            if substring in BRAILLE_TO_ENG:
                res += BRAILLE_TO_ENG[substring]
            else:
                print("Invalid braille for a letter")
                exit()
        else:
            print("Cannot have a number and capital follows next to eachother")
            exit()
        
        print(res, end="")
    # Print a newline at the end
    print()


# Translates english inputs into braille given an input string str
def englishToBraille(str):
    # Flag used to check if number follows has been encountered
    num_flag = False

    # Iterate through each letter in the string
    for char in str:
        res = ""
        # If the character is a letter and uppercase and we have not set the capital flag yet,
        # add the braille for capital, and add the braille character. We have to cast the character to lower
        # when looking it up in our dictionary since it's uppercase currently.
        if char.isalpha() and char.isupper():
            res += SPEC_TO_BRAILLE[CAPITAL]
            res += ENG_TO_BRAILLE[char.lower()]
        # If the character is a digit and it's the first one we've seen, add the braille for 'number follows' and set the num_flag to true.
        # Also, add the number's braille to the result
        elif char.isdigit():
            if not num_flag:
                res += SPEC_TO_BRAILLE[NUMBER]
                num_flag = True
            res += NUMS_TO_BRAILLE[char]
        # If the character is a space or letter, we should add it. We know that it is not a number or capital since those cases have already
        # been checked for above. If the character is a space, we should reset the num_flag to false.
        elif char == SPACE or char.isalpha():
            res += ENG_TO_BRAILLE[char]
            if char == SPACE:
                num_flag = False # Redundant because each argument is separated by a space, useful if we want to accept a single string
        # Print errors and exit if there's an unexpected character
        else:
            print("Error reading character")
            exit()
        # Print the braille for our current iteration
        print(res, end="")
    # Print a newline at the end
    print()

def translate_input():
    # Read the arguments written at runtime. Since all of the spaces are used as separators for the arguments (and removed from the inputs),
    # we can create a concatenated string of the inputs with and without spaces separating them. 
    inputs = sys.argv[1:]
    concat_raw = ''.join(inputs)
    concat_spaced = ' '.join(inputs)

    # If there's no arguments at runtime, exit
    if not concat_raw or concat_raw == "":
        print("Error reading input or no input received")
        exit()

    # If the raw text is braille, call brailleToEnglish using the raw text
    if isBraille(concat_raw):
        brailleToEnglish(concat_raw)
    # If the text is english, call englishToBraille using the spaced text
    elif isEnglish(concat_spaced):
        englishToBraille(concat_spaced)
    else:
        print("Error with inputs. Only braille OR alpha/numeric/space accepted")
        exit()

if __name__ == "__main__":
    translate_input()