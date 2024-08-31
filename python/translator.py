import sys

# Create all the key-value pairs
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' '
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

BRAILLE_TO_NUMBERS = {
    '.OOO..': '1', 'O.OO..': '2', 'OOO...': '3', 'OOO.O.': '4', 'O..OO.': '5',
    'OOOO..': '6', 'OOOOO.': '7', 'O.OOO.': '8', '.OOOO.': '9', '.OO.O.': '0'
}

NUMBERS_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_NUMBERS.items()}

# Special Case characters
CAPITALIZE = '.....O'

NUMBER_FOLLOWS = '.O.OOO'

def is_braille(input_string):
    '''
    Function to check if a string is a valid braille string

    Args:
    input_string: string to check if it is a valid braille string

    Returns:
    bool: True if the string is a valid braille string, else false
    '''
    #Check if all characters are either 0 or .
    valid_chars = all(char in "O." for char in input_string)
    
    #Check if the braille string is divisible by 6
    valid_length = len(input_string) % 6 == 0
    
    return valid_chars and valid_length    

def translate_to_english(input_string):
    '''
    Function that takes in a valid braille input string and translates it to english

    Args:
    input_string: string to translate to english

    Returns:
    output_string: translated string
    '''
    translated_chars = []
    number_follows = False
    capitalize_next = False

    for i in range(0, len(input_string), 6):
        braille_char = input_string[i:i+6]

        #Toggle switches for number or capitalize
        if braille_char == CAPITALIZE:
            capitalize_next = True
            continue
        elif braille_char == NUMBER_FOLLOWS:
            number_follows = True
            continue

        #Determine the translated character based on number toggle (ie 'j' or 1)
        if number_follows:
            translated_character = BRAILLE_TO_NUMBERS[braille_char]
        else:
            translated_character = BRAILLE_TO_ENGLISH[braille_char]

        #if the character is a letter, toggle capitalize is on capitalize it
        if capitalize_next and translated_character.isalpha():
            translated_character = translated_character.upper()
            capitalize_next = False
        
        translated_chars.append(translated_character)

        #if a space is found, reset the number toggle
        if translated_character == ' ':
            number_follows = false

    return ''.join(translated_chars)
            


    def translate_to_braille(input_string):
        print('Its english')
        pass



def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:]) 

    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        translate_to_braille(input_string)

if __name__ == '__main__':
    main()
