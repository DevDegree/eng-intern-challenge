import sys

# *** The following code only implements the functionality mentioned in the technical requirements (no support for symbols) ***

# Braille to English letter mappings
b2e_letters = {
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
    "O..OOO": "z"
}

# Braille to English number mappings
b2e_numbers = {
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

# Other special Braille to English conversions
space = "......"
capital = ".....O"
decimal = ".O...O"
number = ".O.OOO"


def check_braille_str(string):
    """
    Checks whether the input string consists only of 'O' and '.' characters.

    Args:
        string (str): The input string to be checked.

    Returns:
        bool: True if the string contains only 'O' and '.', False otherwise.
    """

    for letter in string:
        if letter != 'O' and letter != '.':
            return False
    return True


def convert_braille_to_text(string):
    """
    Converts a braille string (represented as a sequence of 'O' and '.') into its corresponding English text.

    Args:
        string (str): The braille string where each 6-character segment represents a braille cell.

    Returns:
        string (str): The translated English string.
    """

    output_str = ""
    curr = 0

    while curr < len(string):
        # Get the current braille cell
        lookup_pattern = string[curr: curr+6]

        if lookup_pattern == space:
            output_str += " "

        elif lookup_pattern == capital:
            # Get the next braille cell and convert to capital
            curr += 6
            lookup_pattern = string[curr: curr+6]

            output_str += b2e_letters[lookup_pattern].upper()
            #Skip over next covered cell
            curr += 6
            continue

        elif lookup_pattern == number:
            # Go to next number cell
            curr += 6
            # Keep track of all numbers encountered until the ' ' char
            cells = 1
            for i in range(curr, len(string), 6):
                lookup_pattern = string[i: i+6]
                cells += 1

                if lookup_pattern == space:
                    output_str += ' '
                    break
                elif lookup_pattern == decimal:
                    output_str += '.'
                else:
                    output_str += b2e_numbers[lookup_pattern]
            # Skip over all covered cells
            curr += 6 * cells
            continue

        else:
            output_str += b2e_letters[lookup_pattern]

        curr += 6 # Move to next braille cell 

    return output_str



def convert_text_to_braille(string):
    """
    Converts an English text string into its corresponding braille string (represented as a sequence of 'O' and '.').

    Args:
        string (str): The English text to be converted.

    Returns:
        string (str): The translated braille string.
    """

    # Create the Braille to English mappings
    e2b_letters = {val: key for key, val in b2e_letters.items()}
    e2b_numbers = {val: key for key, val in b2e_numbers.items()}

    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"

    output_str = ""
    curr = 0
    while curr < len(string):
        if string[curr] == ' ':
            output_str += space

        elif string[curr] in upper_alpha:
            # Convert the capital letter into its braille capitalization and lowercase letter representations
            output_str += capital
            output_str += e2b_letters[string[curr].lower()]
        
        elif string[curr] in nums:
            # Convert the next sequence of numbers until the ' ' char
            output_str += number
            while curr < len(string) and string[curr] != ' ':
                # Check for decimals
                if string[curr] == '.':
                    output_str += decimal
                    curr += 1
                    continue
                
                output_str += e2b_numbers[string[curr]]
                curr += 1

            if curr < len(string) and string[curr] == ' ':
                output_str += space

        else:
            output_str += e2b_letters[string[curr]]

        curr += 1

    return output_str
                


# Get the first arguement from command line
input_str = sys.argv[1:]

if len(input_str) == 1:
    string = input_str[0]
else:
    # Convert args array into space-separated string
    string = ""
    for word in input_str:
        string += word + " "
    string = string[:-1]

# Determine whether to convert braille-to-english or vice-versa
is_braille = check_braille_str(string)

# Convert input text
if is_braille:
    print(convert_braille_to_text(string))
else:
    print(convert_text_to_braille(string))