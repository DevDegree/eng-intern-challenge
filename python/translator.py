
import sys

'''
The Braille system uses patterns of raised dots in a 2x3 grid to represent characters. 
In our translation, we have separated Braille data into different categories for clarity and efficiency.

The `braille_basics` list contains the 2x2 grid of Braille representations
for the first 20 English letters (a-t), as well as the numbers 1-9 and 0.

The first four dots of the Braille characters are consistent across these groups. 
The only difference lies in the last two dots of the pattern:
 - For letters a-j, the last two dots are ".."
 - Letters k-t have "O." in the last two positions

Numbers 1-9 and 0 use the same Braille pattern after 'number follows' signal is entered
'''

braille_basics = [
    "O...",
    "O.O.",
    "OO..",
    "OO.O",
    "O..O",
    "OOO.",
    "OOOO",
    "O.OO",
    ".OO.",
    ".OOO"
]


# The `braille_u_to_z` list contains Braille patterns for letters u-z.
# These characters are mapped separately as they don't follow the same 2x2 grid patterns

braille_u_to_z = [
    "O...OO",
    "O.O.OO",
    ".OOO.O",
    "OO..OO",
    "OO.OOO",
    "O..OOO"
]

# Special characters are mapped with their specific Braille patterns

braille_special_chars = {
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}

'''
 Braille command indicators are used for specific formatting instructions:
 - "capital" indicates that the following letter is capitalized.
 - "decimal" indicates the presence of a decimal point in numbers.
 - "number" indicates that the following characters are numbers.
'''

braille_commands = {
    "capital":".....O",
    "decimal":".O...O",
    "number":".O.OOO"
}



# Function to check if a string is a valid Braille string
def braille_string_checker(text):
    # checks the first 6 characters of the given string
    if len(text) != 6:
        return False

    # Braille strings can only contain 'o' or '.'
    braille_characters = {'.', 'O'}
    unique_chars = set(text)

    if unique_chars.issubset(braille_characters):
        return True
    else:
        return False


# Function to retrieve the key from a value in a dictionary (used for special characters)
def get_key_from_value(value, dictionary):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Return None if the value is not found

# Function to translate a Braille string to English text
def translate_to_english(text):
    is_capital = False
    is_number = False
    output = ""

    # Split the input text into substrings of 6 characters each (one Braille character per substring)
    substrings = [text[i:i+6] for i in range(0, len(text), 6)]

    for substring in substrings:
        # Check for a number indicator
        if substring == braille_commands["number"]:
            is_number = True

        # Check for a decimal indicator
        elif substring == braille_commands["decimal"]:
            output += "."

        # Handle numbers
        elif is_number:
            if substring == ".OOO..": # Special case for 0
                output += "0"
            elif substring[0:4] in braille_basics:
                output += str(braille_basics.index(substring[0:4]) + 1)
            else: # Space detected; reset number indicator
                is_number = False
                output += " "

        # Check for a capital letter indicator
        elif substring == braille_commands["capital"]:
            is_capital = True

        # Handle alphabet characters
        elif substring[0:4] in braille_basics:
            if substring[4:6] == "..":  # a-j
                ascii_val = 97 + braille_basics.index(substring[0:4])

            elif substring[4:6] == "O.": # k-t
                ascii_val = 107 + braille_basics.index(substring[0:4])

            elif substring in braille_u_to_z: # u-z
                ascii_val = 117 + braille_u_to_z.index(substring)

            # Convert the ASCII value to a character, handling capitalization if needed
            if is_capital:
                output += chr(ascii_val).upper()
                is_capital = False

            else:
                output += chr(ascii_val)

        # Handle special characters
        elif substring in braille_special_chars.values():
            special_char = get_key_from_value(substring, braille_special_chars)
            if special_char is not None:
                output += special_char
    print(output)

# Function to translate English text to Braille
def translate_to_braille(text):
    output = ""
    is_number = False

    # Iterate over each character in the input text
    for i in range(len(text)):
        if text[i].isspace() and is_number == True: # Reset is_number flag when space is encountered
            is_number = False

        if text[i].isalpha(): # Handle alphabetic characters
            ascii_num = ord(text[i].lower())

            # Add capital letter indicator if the character is uppercase
            if text[i].isupper():
                output += braille_commands["capital"]
            # Handle characters a-j
            if ascii_num >= 97 and ascii_num < 107:
                output += (braille_basics[ascii_num - 97] + "..")
            # Handle characters k-t
            elif ascii_num >= 107 and ascii_num < 117:
                output += (braille_basics[ascii_num - 107] + "O.")
            # Handle characters u-z
            elif ascii_num >= 117 and ascii_num < 123:
                output += braille_u_to_z[ascii_num - 117]


        elif text[i].isdigit(): # Handle numeric characters
            # Add number indicator if the first number is encountered
            if not is_number:
                output += braille_commands["number"]
                is_number = True

            if int(text[i]) == 0: # Special case for 0
                output += (braille_basics[-1] + "..")
            else: # Handle digits 1-9
                output += (braille_basics[int(text[i]) - 1] + "..")

        elif text[i] == '.': # Handle decimal point
            output += braille_commands["decimal"]  # Add decimal point

        elif text[i] in braille_special_chars: # Handle special characters
            output += braille_special_chars[text[i]]
    print(output)




def main():
    if len(sys.argv) < 2:
        print("No input provided")
        return

    input_string = " ".join(sys.argv[1:])

    if braille_string_checker(input_string[0:6]):
        translate_to_english(input_string)
    else:
        translate_to_braille(input_string)

if __name__ == "__main__":
    main()