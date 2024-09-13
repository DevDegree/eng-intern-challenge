import sys

'''
ASSUMPTIONS:
1) There will be no mix of Braille and English in the input. It will either be strictly Braille or strictly English.
2) The input will be fully valid (e.g. For English input, there will always be a space between a number and the next letter as in "123 abc", not "123abc)
'''

# Define constants for Braille representations
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"

# Maps English lowercase letters (and space) to Braille representations
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    ' ': '......',  # Space
}

# Maps Braille representations to corresponding English lowercase letters
braille_to_english = {x : y for y, x in english_to_braille.items()}

# Maps numbers to Braille representations
numbers_to_braille = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Maps Braille representations to corresponding numbers
braille_to_numbers = {x : y for y, x in numbers_to_braille.items()}


# Determines if a given string is in Braille or not
def isBraille(text: str) -> bool:
    # If the text length is not a multiple of 6, it cannot be Braille
    if len(text) % 6 != 0: return False

    # Also check if the text only contains "." and "O" characters
    for letter in text:
        if letter not in (".", "O"):
            return False

    return True


# Translates given Braille string into English
def toEnglish(text: str) -> str:

    # Consider substrings of length 6 with each iteration
    left, right = 0, 5 # Define starting values for left and right pointers which span across 6 characters
    result = "" # Variable to store final result
    number_mode = False # Used to track if we are working with numbers or letters

    # Iterate through the entire string, working with substring of length 6 in each iteration
    while(right < len(text)):
        substring = text[left:right+1]
        
        if substring == CAPITAL_FOLLOWS: # Capital follows
            left, right = left + 6, right + 6 # Get the next letter
            result += (braille_to_english[text[left:right+1]]).upper() # Capitalize the letter

        elif substring == NUMBER_FOLLOWS: # Number follows
            number_mode = True
            left, right = left + 6, right + 6 # Get the next character, which will be a number
            result += (braille_to_numbers[text[left:right+1]]) # Add the number to the result

        elif substring == SPACE: # When a space is encountered, disable number mode if it is on
            number_mode = False
            result += " "

        else: # If no condition is met, simply add the corresponding letter or number to the result
            if number_mode:
                result += (braille_to_numbers[text[left:right+1]])
            else:
                result += (braille_to_english[text[left:right+1]])

        # Update pointers
        left, right = left + 6, right + 6

    return result


# Translates given English string into Braille
def toBraille(text: str) -> str:
    result = "" # Variable to store final result

    number_mode = False # Used to track if we are working with numbers or letters

    # Iterate through the entire string, working with each character at a time
    for character in text:

        if character == " ": # Character is a space
            result += SPACE
            number_mode = False # Turn off number mode if it is on since we encountered a space

        elif character.isupper(): # Character is a capital letter
            result += CAPITAL_FOLLOWS # Add capital follows Braille representation to result
            result += english_to_braille[character.lower()] # Add the letter's Braille representation to result

        # Char is a number
        elif character.isnumeric(): # Character is a number
            if (not number_mode): # If not in number mode, turn it on, and add the Braille representation of number follows
                number_mode = True
                result += NUMBER_FOLLOWS
            
            result += numbers_to_braille[character] # Add the braile representation of the number to the result
        
        else: # Else, the character will be a lower case letter, so add its corresponding Braille representation to result
            result += english_to_braille[character]

    return result


def main():
    # Get command line args, excluding python3 and file name
    inputs = sys.argv[1:]

    # Join the input args into one string
    text = " ".join(inputs)

    # Check if the input is in Braille or English, and translate accordingly
    if isBraille(text):
        result = toEnglish(text)
    else:
        result = toBraille(text)

    # Print the output
    print(result)

if __name__ == "__main__":
    main()
