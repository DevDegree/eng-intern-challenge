
import sys

# Encoding Letters
ENGLISH_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z']

BRAILLE_LETTERS = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...",
                   "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.",
                   "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.",
                   ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO",
                   "OO.OOO", "O..OOO"]

# Encoding Numbers
ENGLISH_NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

BRAILLE_NUMBERS = [".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..",
                   "OOO...", "OOOO..", "O.OO..", ".OO..."]

# Encoding punctuation
ENGLISH_PUNCTUATION = ['.', ',', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')', ' ']
BRAILLE_PUNCTUATION = ["..OO.O", "..O...", "..O.OO", "..OOO.", "..OO..", "..O.O.",
                       "....OO", ".O..O.", ".OO..O", "O..OO.", "O.O..O", ".O.OO.", "......"]

# Special Braille command encodings
CAPITAL_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O"
NUMBER_FOLLOWS = ".O.OOO"


"""
    Helper function to detect whether the input is English or Braille.
"""
def is_braille(sequence):
    # In the sequence, are there characters different than '.' and 'O'?
    # If others are present, the sequence does not represent Braille but an English sequence.
    for character in sequence:
        if character not in ['.','O']:
            return False
    return True



"""
    Translation from Braille to English.
"""
def to_english(word_list):
    english_version = []
    
    # Edge case
    if len(word_list) % 6 != 0:
        sys.exit()

    # Using separate dictionaries for letters, numbers, and punctuation/signs
    # because Braille encodings (keys) are not always unique, and one encoding may map to multiple 
    # characters in English.

    # Dict for letters
    b_letters = {BRAILLE_LETTERS[i]: ENGLISH_LETTERS[i] for i in range(len(ENGLISH_LETTERS))}
    # Dict for numbers
    b_nums = {BRAILLE_NUMBERS[i]: ENGLISH_NUMBERS[i] for i in range(len(ENGLISH_NUMBERS))}
    # Dict for punctuation and signs
    b_punct = {BRAILLE_PUNCTUATION[i]: ENGLISH_PUNCTUATION[i] for i in range(len(ENGLISH_PUNCTUATION))}

    # Flag variables to track if we need to capitalize or if it is a sequence of number with number follows
    capitalize = False
    is_num = False

    # Decode from Braille to English
    for i in range(0, len(word_list), 6):
        current = word_list[i:i + 6]

        # Handle special cases first
        if current == CAPITAL_FOLLOWS:
            capitalize = True
        elif current == NUMBER_FOLLOWS:
            is_num = True
        else:
            # Check if number follows is true, then it is a number
            if is_num and current in b_nums:
                english_version.append(b_nums[current])

            # Or, it might be a letter
            elif current in b_letters and not is_num:
                if capitalize:
                    english_version.append(b_letters[current].upper())
                    capitalize = False  # Reset capitalization
                else:
                    english_version.append(b_letters[current])
            # Or, it might be punctuation/signs
            elif current in b_punct:
                sign = b_punct[current]
                # If it's a space and number follows is true, it marks the end of the number sequence, not just a space
                if sign == ' ' and is_num:
                    is_num = False
                else:
                    english_version.append(sign)

            # Handle cases where no mapping exists
            else:
                sys.exit()
    
    return ''.join(english_version)



"""
    Translation from English to Braille.
"""    
def to_braille(word_list):
    braille_version = []

    # One dictionary is sufficient since each character in English is unique (unique keys).
    # This method converts characters from English to the matching Braille encodings.
    # Map for letters, numbers, and punctuation
    english_to_braille = {ENGLISH_LETTERS[i]: BRAILLE_LETTERS[i] for i in range(len(ENGLISH_LETTERS))}
    english_to_braille.update({ENGLISH_NUMBERS[i]: BRAILLE_NUMBERS[i] for i in range(len(ENGLISH_NUMBERS))})
    english_to_braille.update({ENGLISH_PUNCTUATION[i]: BRAILLE_PUNCTUATION[i] for i in range(len(ENGLISH_PUNCTUATION))})

    num_sequence = False  # Track if it is a sequence of numbers

    # Translate from English to Braille
    for char in word_list:
        # Check if the character is a capital letter
        if char.isalpha() and char.isupper():
            braille_version.append(CAPITAL_FOLLOWS)
            char = char.lower()
        
        # char is present and is either a letter, number or punctuation/sign
        if char in english_to_braille:
            # Check if the character is a letter
            if char.isalpha() and num_sequence:
                # If it was a sequence of numbers, having 'char' as a letter marks the end of the sequence with space
                num_sequence = False

            # Check if the character is a number
            elif char.isdigit():
                if not num_sequence:
                    braille_version.append(NUMBER_FOLLOWS)
                    num_sequence = True

            # Append the mapping of the character
            braille_version.append(english_to_braille[char])
        else:
            sys.exit()

    return ''.join(braille_version)


if __name__ == "__main__":
    # Get the input from the command line
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
    else:
        sys.exit(1)

    # Detect whether the input is Braille or English and call the corresponding translation function
    if is_braille(input_str):
        output_str = to_english(input_str)
    else:
        output_str = to_braille(input_str)

    # Output the translated string 
    print(output_str)