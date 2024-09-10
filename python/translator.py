import sys
from collections import Counter

# Initializing an English to Braille map for alphabets and digits, string for capital and number
english_to_braille_alphabet_map = {
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "q" : "OOOOO.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO",
    " " : "......"
}

english_to_braille_digits_map = {
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "0" : ".OOO..",
}

capital = ".....O"
number = ".O.OOO"

# Initializing Braille to English map for alphabets and digits
braille_to_english_alphabet_map = {v: k for k, v in english_to_braille_alphabet_map.items()}
braille_to_english_digits_map = {v: k for k, v in english_to_braille_digits_map.items()}


def translate(input):
    """
    Detect and translate English to Braille or vice versa

    @param input : str
    @return result : str
    """

    n = len(input)
    if(n == 0): 
        return ""

    # Counting the characters to determine if the input string is Braille or English
    counts = Counter(input)
    characters = counts.keys()
    size = len(characters)

    # Condition 1: the length of the string must be divisible by 6
    # Condition 2: the number of unique character can be 1 or 2 but they must be either O or .
    if((n % 6 == 0) and ((size == 1 and ('O' in characters or '.' in characters)) or (size == 2  and 'O' in characters and '.' in characters))):
        return braille_to_english(input)
    else:
        return english_to_braille(input)

def english_to_braille(input):
    """
        Translate English to Braille

        @param input : str
        @return result : str
    """
    result = ""
    i = 0

    # Loop through every character of the input string and convert to Braille character
    while(i < len(input)):
        c = input[i]

        if (c.isupper()):
            # If character is an upper case, add a capitalized character
            result += capital + english_to_braille_alphabet_map[c.lower()]
            i += 1
        elif(c.isnumeric()):
            # If character is a digit, continue the loop until space
            result += number
            j = i
            while (j < len(input) and input[j] != " "):
                result += english_to_braille_digits_map[input[j]]
                j += 1
            i = j
        else:
            # If character is lower case
            result += english_to_braille_alphabet_map[c]
            i += 1
    return result

def braille_to_english(input):
    """
        Translate Braille to English

        @param input : str
        @return result : str
    """
    result = ""
    i = 0
    while(i < len(input)):
        # Read the next 6 characters
        code = input[i:i+6]

        if(code == capital):
            # If code is a capital symbol, the next character should be capitalized
            i += 6
            code = input[i:i+6]
            result += braille_to_english_alphabet_map[code].upper()
        elif(code == number):
            # If code is a number symbol, keep reading until space
            i += 6
            while(code != "......" and i < len(input)):
                code = input[i:i+6]
                result += braille_to_english_digits_map[code]
                i += 6
        else:
            # If code is a normal character, add it to the result
            result += braille_to_english_alphabet_map[code]
        i += 6
    return result

# Extract input from the command line
input_string = " ".join(sys.argv[1:])
print(translate(input_string))
