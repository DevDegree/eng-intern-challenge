# Dictionary for English to Braille (letters)
english_to_braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    ' ': '......', 
    '.': '......',   
    ',': '..O...',    
    '?': '..O.O.',   
    '!': '..OO.O',        
    '-': '....OO',    
    ':': '..OO..',    
    ';': '..O.OO',
    '/': '..O..O',    
    '<': 'O..O.O',   
    '>': '.OO.O.',    
    '(': 'O...OO',    
    ')': 'O..OOO'  
}

# Dictionary for numbers (1-9, 0)
english_to_braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse dictionaries for Braille to English
braille_to_english_letters = {brai: eng for eng, brai in english_to_braille_letters.items()}
braille_to_english_numbers = {brai: num for num, brai in english_to_braille_numbers.items()}

# Capitalization and number indicators
capital_indicator = '.....O'
number_indicator = '.O.OOO'


# Check if an input is in braille 
def is_braille(input_string):
    for char in input_string:
        if char not in "O.":
            return False
    return True


# Translate Braille to English
def translate_braille_to_english(braille_string):
    translation = []
    capital_mode = False  
    number_mode = False  

    # Process the Braille string in chunks of 6 characters
    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]  

        # Handle capital and number indicators
        if braille_char == capital_indicator:
            capital_mode = True 
            continue  
        elif braille_char == number_indicator:
            number_mode = True  
            continue  

        if number_mode:
            letter = braille_to_english_numbers.get(braille_char, '')  
        else:
            letter = braille_to_english_letters.get(braille_char, '')  

        # Handle capitalization
        if capital_mode and letter.isalpha():
            translation.append(letter.upper()) 
            capital_mode = False 
        else:
            translation.append(letter) 

       
        if letter == ' ':
            number_mode = False
        elif not letter.isdigit(): 
            number_mode = False

    return ''.join(translation)


# Translate English to Braille
def translate_english_to_braille(english_string):
    translation = []
    number_mode = False  

    for char in english_string:
        if char.isupper():
            translation.append(capital_indicator)  
            translation.append(english_to_braille_letters[char.lower()])  
        elif char.isdigit():
            if not number_mode:  
                translation.append(number_indicator)
                number_mode = True  
            translation.append(english_to_braille_numbers[char])  
        elif char == ' ':  
            translation.append(english_to_braille_letters[char])  
            number_mode = False  
        else:
            translation.append(english_to_braille_letters[char])  
            number_mode = False  

    return ''.join(translation)


def main():
    import sys
    input_strings = sys.argv[1:]  

    #print(f"Input strings: {input_strings}")  

    if not input_strings:
        #print("No input provided.")
        return

    translations = []

    for input_string in input_strings:
        if is_braille(input_string):
            #print(f"Translating Braille: {input_string}")  
            translations.append(translate_braille_to_english(input_string))  
        else:
            #print(f"Translating English: {input_string}") 
            translations.append(translate_english_to_braille(input_string))  

    final_translation = '......'.join(translations)

    print(final_translation) 

if __name__ == '__main__':
    main()



