import sys

# Create original dictionary from Letters to Braille
letters_to_braille_dict = {
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

# Create dictionary from Numbers to Braille
numbers_to_braille_dict = {
    '1': "O.....",
    '2': "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

# Generate reverse of above dictionaries
braille_to_letters_dict = {v: k for k, v in letters_to_braille_dict.items()}
braille_to_numbers_dict = {v: k for k, v in numbers_to_braille_dict.items()}


# Special indicators
capital_indicator = '.....O'
number_indicator = '.O.OOO'



def isBraille(text: str) -> bool:
    """
    isBraille checks if the given parameter text is Braille or English
    """ 

    # If the length of text is not a multiple of 6, it is English
    if len(text) % 6 != 0:
        return False
    
    # The text should also only contain O or .
    for char in text:
        if char not in ['O', '.']:
            return False

    return True

def english_to_braille(english: str) -> str:
    """
    english_to_braille translates english to Braille
    Args: 
        english (str): A string that contains a-z, A-Z, 0-9, and space
    Returns: 
        str: A string that is formatted in Braille notation
    """

    output = ""
    is_number = False

    # Loop through every character in english
    for char in english:
        # If the character is uppercase, add the uppercase indicator then its lowercase Braille equivalent
        if char.isupper():
            is_number = False
            output += capital_indicator
            output += letters_to_braille_dict[char.lower()]
        
        # If the character is a number, we need to check the numbers dictionary
        elif char.isnumeric():
            # First time the number is seen, thus we turn on is_number and add the number indicator
            if (is_number == False):
                output += number_indicator
                is_number = True

            output += numbers_to_braille_dict[char]
        
        # Base case is that the character is a lowercase letter, in which we just add its Braille equivalent from the letters dictionary
        else:
            is_number = False
            output += letters_to_braille_dict[char]

    return output

def braille_to_english(braille: str) -> str:
    """
    braille_to_english translates Braille to English
    Args: 
        braille (str): A string that is formatted in Braille notation
    Returns: 
        str: A string that contains a-z, A-Z, 0-9, and space
    """

    output = ""
    # Create and array of groups of 6 characters representing a Braille character
    iterable_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]

    is_number = False
    is_capital = False

    # Iterate through the above group of 6
    for char in iterable_chars:
        # If the character is the capital indicator, turn on the flag and turn off the number flag
        if char == capital_indicator:
            is_capital = True
            is_number = False

        # If the character is the capital indicator, turn on the flag
        elif char == number_indicator:
            is_number = True

        # If the character is the Braille equivalent to a space, we need to turn off the capital flag
        elif char == letters_to_braille_dict[" "]:
            is_number = False
            output += " "

        
        # As per above, if the number flag is turned on, check the numbers dictionary
        elif is_number:
            output += braille_to_numbers_dict[char]

        # If the capital flag is turned on, check the letters dictionary then immediately turn off the flag
        elif is_capital:
            output += braille_to_letters_dict[char].upper()
            is_capital = False 
        
        # Base case is that the character is a lowercase letter, in which we just add its English equivalent from the letters dictionary
        else:
            output += braille_to_letters_dict[char]

    return output

    


if __name__ == "__main__":
    # Check to see if the arguments are correctly provided from the command line
    if len(sys.argv) < 2:
        print("Please provide command of the form: python translator.py <inputs>")
        sys.exit(1)
    input_text = ' '.join(sys.argv[1:])

    # If the given input text is Braille, we should call braille_to_english() and vice versa
    if isBraille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))
