import sys

BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

CAPITAL_SYMBOL = '.....O'
NUMBER_SYMBOL = '.O.OOO'

NUMBERS = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

def braille_to_english(braille):
    result = ""
    capitalize_next = False
    number_mode = False
    
    # Process the braille string 6 characters at a time
    for i in range(0, len(braille), 6):
        char = braille[i:i+6]
        if char == CAPITAL_SYMBOL:
            capitalize_next = True
        elif char == NUMBER_SYMBOL:
            number_mode = True
        else:
            # Get the English letter corresponding to the Braille character
            letter = BRAILLE_TO_ENGLISH.get(char)
            if letter:
                # if in number mode, convert Braille letter to number
                if number_mode and letter in NUMBERS:
                    result += NUMBERS[letter]
                else:
                    # capitalize the next letter if needed
                    letter = letter.upper() if capitalize_next else letter
                    result += letter
                    # exit number mode after processing a non-number character
                    number_mode = False
                # reset capitalization flag after using it
                capitalize_next = False
    
    return result

def english_to_braille(english):
    result = ""
    number_mode = False
    
    # Process each character in the English string
    for char in english:
        if char.isupper():
            result += CAPITAL_SYMBOL
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result += NUMBER_SYMBOL
                number_mode = True
            # convert digit to corresponding Braille letter
            char = list(NUMBERS.keys())[list(NUMBERS.values()).index(char)]
        else:
            number_mode = False
        
        result += ENGLISH_TO_BRAILLE.get(char, '')
    
    return result

def translate(input_string):
    """
    Determine whether the input string is in English or Braille and translate it accordingly.
    """
    if all(c in 'O.' for c in input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
    else:
        input_string = ' '.join(sys.argv[1:])
        print(translate(input_string))
