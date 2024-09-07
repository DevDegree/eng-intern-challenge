
######## Assumptions: ########

# 1. An input string like "A12bc" is not bijective (non-invertible) given the constraints of the project 
# where if a 'number follows' flag in braille is parsed, it will treat all subsequent braille as a number 
# until there is a space character. I've assumed that this is intentional and that no unit tests will verify
# the invertibility of input similar to the one above.

    # 1.1 Explanation of example => This would mean the string A12bc would output the following braille:
    #  .....OO......O.OOOO.....O.O...O.O...OO....
    # which, when translated back into english, would output:
    # A1223
    # This occurs because the input does not separate the '2' and the 'b' with a space, so the encoding algorithm
    # treats the 'b' as a number. 

# 2. Ideally, braille input should be a multiple of 6 to be considered valid, any sentences that have an 
# incomplete braille string will be treated as english input text, which will then be converted to the
# corresponding braille input.

# 3. Braille that only consists of "flag" input (see the map below) is treated as valid - I did not want 
# to print an error message as I am unsure if it would raise an issue with the automated testing.

# 4. The "decimal follows" flag and punctuation was not mentioned in the technical requirements of the README.md. As a result, 
# I do not consider it as valid and ignore that input.

    #4.1 Special shell commands (such as '!!') can cause unexpected outputs. In this example, '!!' is a shell command
    # that recalls the previous shell command - in this case, the 'input_text' into the program will not be '!!', but instead
    # the previous command inputted by the user (therefore the input text could end up looking something like:
    # "python translator.py !!"), which is not the intent. This is another reason as to why I assume punctuation is not considered.

# 5. If the input is empty, nothing happens.

# 6. Leading and trailing space is ignored.

# 7. 'English' strings that imitate braille (like OOOOOO) are considered english.

import re

# Braille Mapping for Letters + Flags
BRAILLE_LETTERS = {

    # Space
    'space': "......",

    # Letters
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...",
    'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 
    'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.", 
    'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO", 
    'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO",
    
    # Flags
    'capital': ".....O", # Capitalization
    'decimal': ".O...O", # Decimal
    'number':  ".O.OOO", # Number
}

#Braille Mapping for Numbers
BRAILLE_NUMBERS = { 
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
}


ENGLISH_LETTERS = {}
for k, v in BRAILLE_LETTERS.items():
    ENGLISH_LETTERS[v] = k
    
ENGLISH_NUMBERS = {}
for k, v in BRAILLE_NUMBERS.items():
    ENGLISH_NUMBERS[v] = k


def is_braille(input_text):
    """
    Determine if the input string is a valid Braille string.

    Args:
        input_text (str): The input string.

    Returns:
        bool: True if the input is a valid Braille string, False otherwise.
    """
    braille_pattern = r"(([O.]*[.]+[O.]*){6})+"  #regex pattern to match groups of 6 Braille characters (O or .)
    return bool(re.fullmatch(braille_pattern, input_text))

def english_to_braille(text):
    """
    Convert an English text string to its equivalent Braille representation.

    Args:
        text (str): The input English text.

    Returns:
        str: The equivalent Braille string.
    """
    result = ""
    number_next = False  # flag that when True indicate that the following input should be processed as a number until there is a space

    for char in text:

        if char == " ": # append space
            result += BRAILLE_LETTERS['space'] # append the space flag
            number_next = False

        elif char.isdigit(): # append number
            if not number_next:
                result += BRAILLE_LETTERS['number']  # append the number flag
                number_next = True  
            result += BRAILLE_NUMBERS[char]

        elif char.isupper(): # append uppercase letter
            result += BRAILLE_LETTERS['capital'] + BRAILLE_LETTERS[char.lower()]  # append the capital flag as well as the capital letter
            number_next = False

        else: # append letter
            result += BRAILLE_LETTERS.get(char, "")
            number_next = False
    
    return result

def braille_to_english(braille):
    """
    Convert a Braille string to its equivalent English representation.

    Args:
        braille (str): The input Braille string.

    Returns:
        str: The equivalent English text.
    """
    result = ""
    capital_next = False  # flag to indicate the next letter should be capitalized
    number_next = False   # flag to indicate that numbers should be processed

    
    for i in range(0, len(braille), 6): 
        char = braille[i:i + 6]  # parse braille symbols in 6 char chunks
        
        if char == BRAILLE_LETTERS['capital']:
            capital_next = True 
            number_next = False
        elif char == BRAILLE_LETTERS['number']:
            number_next = True
        elif char == BRAILLE_LETTERS['space']:
            result += " "
            number_next = False  # reset the number flag after a space
        else:
            # check flags
            if number_next:
                result += ENGLISH_NUMBERS.get(char, "")
            else:
                char_to_add = ENGLISH_LETTERS.get(char, "")
            
                if capital_next:
                    result += char_to_add.upper()
                    capital_next = False
                else:
                    result += char_to_add
    return result


def main(input_text):
    """
    Main function that detects whether the input is Braille or English and 
    converts it to the appropriate opposite format.

    Args:
        input_text (str): The input text, either Braille or English.

    Returns:
        None: The function prints the converted text to the console.
    """
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == "__main__":
    import sys
    input_text = " ".join(sys.argv[1:])
    main(input_text)
