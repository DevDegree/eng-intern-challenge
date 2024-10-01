import sys


# english to braille mappings
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
    'q': 'OOOOO.', 
    'r': 'O.OOO.', 
    's': '.OO.O.', 
    't': '.OOOO.',
    'u': 'O...OO', 
    'v': 'O.O.OO', 
    'w': '.OOO.O', 
    'x': 'OO..OO', 
    'y': 'OO.OOO',
    'z': 'O..OOO', 
    ' ': '......'
}

# english to braille numbers
english_to_braille_numbers = {
    '0': '.OOO..', 
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..',
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...'
}

# indicator constants
capital_indicator = '.....O'
number_indicator = '.O.OOO'
space_indicator = '......'

# braille to english mappings
braille_to_english = {}

# braille to english numbers
braille_to_english_numbers = {}

# function to initialize braille to english mappings
def init_braille_to_english():
    for char, braille in english_to_braille.items():
        braille_to_english[braille] = char

    for char, braille in english_to_braille_numbers.items():
        braille_to_english_numbers[braille] = char

# function to detect if input is braille
def is_braille(input_str):
    return all(c in 'O.' for c in input_str)

# function to translate braille to english
def english_to_braille_translation(input_str):
    result = ""

    for c in input_str:
        if c.isupper():
            result += capital_indicator
            c = c.lower()
        if c.isdigit():
            result += number_indicator
            result += english_to_braille[c]
        else:
            result += english_to_braille[c]

    return result

# function to translate english to braille
def braille_to_english_translation(input_str):
    result = ""
    capital_letter_flag = False
    number_flag = False

    for i in range(0, len(input_str), 6):
        braille_char = input_str[i:i+6]

        if braille_char == capital_indicator:
            capital_letter_flag = True
            continue
        elif braille_char == number_indicator:
            number_flag = True
            continue
        else:
            translated_char = ""

            if braille_char == space_indicator:
                translated_char = braille_to_english.get(braille_char)
                number_flag = False
            elif number_flag == True:
                translated_char = braille_to_english_numbers.get(braille_char)
            elif capital_letter_flag == True:
                translated_char = braille_to_english.get(braille_char).upper()
                capital_letter_flag = False
            else:
                translated_char = braille_to_english.get(braille_char)

            result += translated_char

    return result


# main
def main():
    if len(sys.argv) < 2:
        print("Error: No input given")
        return
    
    # initialize mappings
    init_braille_to_english()

    # get input from command line
    input_string = sys.argv[1]

    # check if input is braille
    if is_braille(input_string):
        print(braille_to_english_translation(input_string))
    else:
        print(english_to_braille_translation(input_string))


if __name__ == "__main__":
    main()

