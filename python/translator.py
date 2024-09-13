import sys

'''
Encodings
Note: As per the question description, special characters are not included
'''
# Maps digits to their braille encodings
DIGIT_TO_BRAILLE = { 
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Maps alphabet characters to their braille encodings
ALPHABET_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO"
}

# Maps braille encodings to their associated digits
BRAILLE_TO_DIGIT = {braille: digit for digit, braille in DIGIT_TO_BRAILLE.items()}

# Maps braille encodings to their associated alphabet characters
BRAILLE_TO_ALPHABET = {braille: letter for letter, braille in ALPHABET_TO_BRAILLE.items()}

# Special encodings
CAPITAL_FOLLOWS = ".....O"
DIGIT_FOLLOWS = ".O.OOO"
SPACE = "......"


'''
Helper Functions
'''
# is_braille(input) returns true if the input is braille and false if the input is not braille
# Note: This function assumes that the input is braille only if it only consists of the characters O or . and has length divisible by 6
def is_braille(input):
    return len(input) % 6 == 0 and all(char in ['O', '.'] for char in input)


# english_to_braille(english_string) translates the english_string to braille and returns the result
# Note: Assuming that english_string does not contain any special characters other than SPACE; the function will raise an ValueError if so
def english_to_braille(english_string):
    braille_result = ""
    is_reading_digit = False # only true if the translator is assuming a digit as the next char

    for char in english_string:
        if char == " ":
            is_reading_digit = False
            braille_result += SPACE 

        elif char.isdigit():
            if not is_reading_digit:
                braille_result += DIGIT_FOLLOWS
                is_reading_digit = True 
            
            braille_result += DIGIT_TO_BRAILLE[char]

        elif char.isalpha():
            if char.isupper():
                braille_result += CAPITAL_FOLLOWS
            
            braille_result += ALPHABET_TO_BRAILLE[char.lower()]
        
        else: # char is not a digit, space or alphabet characer
            raise ValueError(f"Error: Character '{char}' is invalid. Only digits, spaces, and alphabet letters are allowed.")

    return braille_result


# braille_to_english(braille_string) translates the braille_string to english and returns the result
# Note: Assuming that braille_string is valid and does not contain any encodings of special characters other than SPACE, CAPITAL_FOLLOWS or DIGIT_FOLLOWS; the function will raise a ValueError if so
def braille_to_english(braille_string):
    english_result = ""
    is_capital_next = False # true when the translator is assuming a capital letter as the next char
    is_digit_next = False # true when the translator is assuming a digit as the next char

    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]

        if braille_char == SPACE:
            is_digit_next = False
            english_result += " "
        
        elif braille_char == CAPITAL_FOLLOWS:
            is_capital_next = True
        
        elif braille_char == DIGIT_FOLLOWS:
            is_digit_next = True
        
        elif is_capital_next: # assuming that braille_char is an alphabet character
            capital_letter = BRAILLE_TO_ALPHABET.get(braille_char).upper()
            if capital_letter is None: # could not find letter encoding in BRAILLE_TO_ALPHABET
                raise ValueError(f"Error: Encoding '{braille_char}' is invalid. The braille string must be valid and consist of only encodings of digits, spaces and/or letters of the alphabet")

            english_result += capital_letter
            is_capital_next = False
        
        elif is_digit_next: # assuming that braille_char is a digit
            digit = BRAILLE_TO_DIGIT.get(braille_char)
            if digit is None: # could not find digit encoding in BRAILLE_TO_DIGIT
                raise ValueError(f"Error: Encoding '{braille_char}' is invalid. The braille string must be valid and consist of only encodings of digits, spaces and/or letters of the alphabet")
            
            english_result += digit
        
        else: # braille_char is a lowercase alphabet character
            letter = BRAILLE_TO_ALPHABET.get(braille_char)
            if letter is None: # could not find letter encoding in BRAILLE_TO_ALPHABET
                raise ValueError(f"Error: Encoding '{braille_char}' is invalid. The braille string must be valid and consist of only encodings of digits, spaces and/or letters of the alphabet")

            english_result += letter
    
    return english_result


# Assuming that the input string can have length 0 and the program will return an empty string if that occurs
def main():
    input_string = " ".join(sys.argv[1:]) # join the arguments when the program is run as the input string separated by spaces        

    if is_braille(input_string):
        print(braille_to_english(input_string))
    
    else:
        print(english_to_braille(input_string))


if __name__ == "__main__":
    main()