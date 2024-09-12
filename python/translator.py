import sys

'''
Encodings
Note: As per the question description, special characters are not included
'''
# Maps numbers to their braille encodings
NUMBER_TO_BRAILLE = { 
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

# Maps braille encodings to their associated numbers
BRAILLE_TO_NUMBER = {braille: number for number, braille in NUMBER_TO_BRAILLE.items()}

# Maps braille encodings to their associated alphabet characters
BRAILLE_TO_ALPHABET = {braille: letter for letter, braille in ALPHABET_TO_BRAILLE.items()}

# Special encodings
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"


'''
Helper Functions
'''
# is_braille(input) returns true if the input is braille and false if the input is not braille
# Note: This function assumes that the input is braille only if it only consists of the letters O or . and has length divisible by 6
def is_braille(input):
    return len(input) % 6 == 0 and all(char in ['O', '.'] for char in input)


# english_to_braille(english_string) translates the english_string to braille and returns the result
# Note: Assuming that english_string does not contain any special characters other than SPACE
def english_to_braille(english_string):
    braille_result = ""
    is_reading_number = False # true if the translator is assuming digits as the next char

    for char in english_string:
        if char == " ":
            is_reading_number = False
            braille_result += SPACE 


        elif char.isdigit():
            if not is_reading_number:
                braille_result += NUMBER_FOLLOWS
                is_reading_number = True 
            
            braille_result += NUMBER_TO_BRAILLE[char]

        else: # char is an alphabet character
            if char.isupper():
                braille_result += CAPITAL_FOLLOWS
            
            braille_result += ALPHABET_TO_BRAILLE[char.lower()]
    
    return braille_result





# Assuming that the input string can have length 0 and the program will return an empty string if that occurs
if __name__ == "__main__":
    input_string = " ".join(sys.argv[1:]) # join the arguments when the script is run as the input string separated by spaces        

    if not is_braille(input_string):
        print(english_to_braille(input_string))
