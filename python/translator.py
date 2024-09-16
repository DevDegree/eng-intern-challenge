import argparse

# Dictionaries for translation

# English to Braille
english_to_braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

english_to_braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Braille to English through reversing previous dictionaries
braille_to_english_letters = {braille: english for english, braille in english_to_braille_letters.items()}
braille_to_english_numbers = {braille: english for english, braille in english_to_braille_numbers.items()}

# Special Symbols
capital_follows = '.....O'
number_follows = '.O.OOO'
space = '......'

def braille_to_english(braille: str) -> str:
    """
    Converts a Braille string to English.
    Handles capitalization and numbers based on requirements.

    Params:
    braille (str): The Braille string.

    Return:
    str: The converted English string.
    """
    english = ''
    capital = False 
    number = False
    i = 0 # Indexing the braille

    while i < len(braille):
        symbol = braille[i: i+6]
        
        if symbol == capital_follows: # Check for capital symbol
            capital = True
        elif symbol == number_follows: # Check for number symbol
            number = True
        elif symbol == space: # Check for Space
            english += ' '
            number = False
        else: # It's a letter or number
            if number: # Number
                english += braille_to_english_numbers[symbol]
            else: # Letter
                letter = braille_to_english_letters[symbol]
                if capital:
                    letter = letter.upper()
                    capital = False  # Reset after capital letter
                english += letter
        i += 6

    return english

def english_to_braille(english: str) -> str:
    """
    Converts an English string to Braille.

    Params:
    english (str): The English string.

    Return:
    str: The converted Braille string.
    """
    braille = ''
    number = False

    for char in english:
        if char == ' ': # Space
            braille += space
            number = False
        elif char.isupper(): # Capital Letter
            braille += capital_follows
            braille += english_to_braille_letters[char.lower()]
        elif char.isdigit(): # Number Digit
            if number: # Digit precedes
                braille += english_to_braille_numbers[char]
            else: # First digit
                braille += number_follows
                braille += english_to_braille_numbers[char]
                number = True
        else: # Other Letters
            braille += english_to_braille_letters[char] 
            
    return braille

def main():
    # Get the argument
    parser = argparse.ArgumentParser(description="Converts English to Braille or Braille to English")
    parser.add_argument('text', type=str, nargs='+', help='The English or Braille Text')
    
    args = parser.parse_args()
    text = ' '.join(args.text)

    # Determine if Braille or English, then convert
    if all(char in '.O' for char in text):
        result = braille_to_english(text)
    else:
        result = english_to_braille(text)
    
    # Output result
    print(result)

if __name__ == "__main__":
    main()
