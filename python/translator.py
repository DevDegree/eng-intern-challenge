import sys

# Define dictionaries for translation 
english_to_braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOO.O',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOO.O',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',

    ' ': '......',
}


digits_to_braille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
} 

CAP_SYMBOL = '.....O'
NUMBER_FOLLOWS_SYMBOL = '.O.OOO'

braille_to_english = {value: key for key, value in english_to_braille.items()}
braille_to_digits = {value: key for key, value in digits_to_braille.items()}

def translate_to_english(braille_string):
    """Translates a Braille string to English."""

    english_output = ""
    capitalize_next = False
    number_mode = False

    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]

        if braille_char == CAP_SYMBOL:  
            capitalize_next = True
            continue
        elif braille_char == NUMBER_FOLLOWS_SYMBOL: 
            number_mode = True
            continue

        if braille_char in braille_to_english:

            if number_mode:
                char = braille_to_digits[braille_char]
            else:

                char = braille_to_english[braille_char]

                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False

                if number_mode and char.isalpha():  # End number mode if we encounter a letter
                    number_mode = False

            english_output += char

    return english_output

def translate_to_braille(english_string):
    """Translates an English string to Braille."""

    braille_output = ""

    FOLLOWS_DIGIT = False 

    for char in english_string:
        if char.isupper():
            braille_output += CAP_SYMBOL  # Add capitalization symbol
            char = char.lower()
            FOLLOWS_DIGIT = False
        elif char.isdigit():
            if not FOLLOWS_DIGIT:  # digit is first in sequence
                braille_output += NUMBER_FOLLOWS_SYMBOL  # Add number follows symbol
            FOLLOWS_DIGIT = True
        else:
            FOLLOWS_DIGIT = False 

        if char.isdigit():
            braille_output += digits_to_braille[char]
        else:
            braille_output += english_to_braille[char]

    return braille_output

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input string provided.")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:]) 

    if any(char in 'O.' for char in input_string):  # Heuristic to detect Braille
        output_string = translate_to_english(input_string)
    else:
        output_string = translate_to_braille(input_string)

    print(output_string)
