import sys

# Braille representation of the English alphabet and digits, where each character is mapped to a 6-dot string
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
}

# Mapping of Braille symbols to corresponding English letters (for reverse translation)
alpha_dict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

# Mapping of Braille symbols to numbers (for reverse translation)
number_dict = {
    '.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9'
}


# Function to convert English to Braille
# Input: english (str) - a string in English
# Output: str - a Braille representation of the input string
def english_to_braille(english):
    braille = ''
    number = False
    for char in english:
        # Convert lowercase English letters to Braille
        if ('a' <= char <= 'z'):
            if (char not in braille_dict):
                raise Exception(f"Unable to convert character {char}")
            braille += braille_dict[char]
        # Convert uppercase letters to Braille, preceded by the capitalization symbol
        elif ('A' <= char <= 'Z'):
            braille += '.....O'
            if (char.lower() not in braille_dict):
                raise Exception(f"Unable to convert character {char}")
            braille += braille_dict[char.lower()]
        # Convert digits to Braille, preceded by the number symbol
        elif ('0' <= char <= '9'):
            if not number:
                braille += '.O.OOO'
                number = True
            braille += braille_dict[char]
        # Handle spaces between words
        elif (char == ' '):
            number = False
            braille += braille_dict[char]
        else:
            raise Exception(f"Unable to convert character {char}")
    return braille


# Function to convert Braille to English
# Input: braille (str) - a string in Braille (each character is represented by 6 dots)
# Output: str - an English translation of the Braille string
def braille_to_english(braille):
    english = ''
    number = False
    upper = False
    # Process Braille string 6 characters at a time
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i + 6]
        # Handle space symbol in Braille
        if braille_char == '......':
            number = False
            english += ' '
        # Handle number symbol
        elif braille_char == '.O.OOO':
            number = True
        # Convert Braille numbers
        elif number:
            if braille_char not in number_dict:
                raise Exception(f"Unable to convert character {braille_char}")
            english += number_dict[braille_char]
        # Handle capitalization symbol
        elif braille_char == '.....O':
            upper = True
        # Convert Braille letters (uppercase if indicated)
        elif upper:
            if braille_char not in alpha_dict:
                raise Exception(f"Unable to convert character {braille_char}")
            english += alpha_dict[braille_char].upper()
            upper = False
        else:
            if braille_char not in alpha_dict:
                raise Exception(f"Unable to convert character {braille_char}")
            english += alpha_dict[braille_char]
    return english


# Function to determine if the input is in English or Braille
# Input: sentence (str) - a string that may be either English or Braille
# Output: bool - returns True if the string is English, False if it is Braille
def is_english(sentence):
    # If the sentence contains '.' and has length divisible by 6, it is considered Braille
    if '.' in sentence:
        if len(sentence) % 6 != 0:
            raise Exception("Invalid input string, string must be valid Braille or English")
        # Ensure all characters in the string are valid Braille symbols
        for char in sentence:
            if char not in ['.', 'O']:
                raise Exception("Invalid input string, string must be valid Braille or English")
        return False
    # Otherwise, validate that all characters are part of the English alphabet or digits
    for char in sentence:
        if char not in braille_dict and char.lower() not in braille_dict:
            raise Exception("Invalid input string, string must be valid Braille or English")
    return True


# Main function to handle input from the command line and perform translation
def main():
    # Get the input sentence from the command line arguments
    sentence = sys.argv[1]
    for i in range(2, len(sys.argv)):
        sentence += ' ' + sys.argv[i]

    try:
        # Determine if the input is English or Braille
        valid_english = is_english(sentence)
    except Exception as e:
        print(f"Error: {str(e)}")
        return

    # Perform the appropriate translation based on input type
    if valid_english:
        try:
            print(english_to_braille(sentence))
        except Exception as e:
            print(f"Error: {str(e)}")
    else:
        try:
            print(braille_to_english(sentence))
        except Exception as e:
            print(f"Error: {str(e)}")


# Entry point of the program
if __name__ == "__main__":
    main()
