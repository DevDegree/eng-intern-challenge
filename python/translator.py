# O is raised dot, . is an unraised dot

# ENGLISH TO BRAILLE MAP
BRAILLE = {
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

# BRAILLE TO ENGLISH MAP
BRAILLE_REV = {
    'O.....': 'a', 
    'O.O...': 'b', 
    'OO....': 'c', 
    'OO.O..': 'd', 
    'O..O..': 'e',
    'OOO...': 'f', 
    'OOOO..': 'g', 
    'O.OO..': 'h', 
    '.OO...': 'i', 
    '.OOO..': 'j',
    'O...O.': 'k', 
    'O.O.O.': 'l', 
    'OO..O.': 'm', 
    'OO.OO.': 'n', 
    'O..OO.': 'o',
    'OOO.O.': 'p', 
    'OOOOO.': 'q', 
    'O.OOO.': 'r',
    '.OO.O.': 's', 
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v', 
    '.OOO.O': 'w', 
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' '
}

# BRAILLE TO NUMBER
NUMS = {
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

# NUMBER TO BRAILLE
NUMS_REV = {
    '.OOO..': '0',  
    'O.....': '1',  
    'O.O...': '2',  
    'OO....': '3',  
    'OO.O..': '4',  
    'O..O..': '5',  
    'OOO...': '6',  
    'OOOO..': '7',  
    'O.OO..': '8',  
    '.OO...': '9'   
}

def english_to_braille(text):
    braille = []
    number_mode = False

    for char in text:
        if char.isupper():
            braille.append('.....O')  # Braille capital indicator
            char = char.lower()  # Convert to lowercase for the Braille mapping

        if char.isdigit():
            if not number_mode:
                braille.append('.O.OOO')  # Braille number sign
                number_mode = True
            braille.append(NUMS.get(char, 'error'))  # Convert digit to Braille
        else:
            if number_mode:
                number_mode = False  
            braille.append(BRAILLE.get(char, 'error')) 
    
    return ''.join(braille)



def braille_to_english(braille_text):
    english = []
    i = 0  # index to keep track of Braille letter count
    number_mode = False  # This flag will track if braille is being converted to numbers or letters

    while i < len(braille_text):
        current_char = braille_text[i:i+6] 

        # Check if upper case indicator
        if current_char == '.....O': 
            i += 6  
            next_char = braille_text[i:i+6]  
            english.append(BRAILLE_REV.get(next_char, 'error').upper())  # Convert to capital english letter 
        # Check if number sign indicator
        elif current_char == '.O.OOO':
            i += 6  # Move to the next 6 characters
            number_mode = True  # Start interpreting follwoing characters as numbers
            next_char = braille_text[i:i+6]  # Get the next Braille character
            english.append(NUMS_REV.get(next_char, 'error'))  
        # Check if the current character is a space
        elif current_char == '......':
            if number_mode:
                number_mode = False
            english.append(' ')
        else:
            # For regular Braille characters (letters and spaces)
            if number_mode:
                english.append(NUMS_REV.get(current_char, 'error'))  # Convert to English number
            else:
                english.append(BRAILLE_REV.get(current_char, 'error'))  # Convert to English letter or space

        i += 6
    return ''.join(english)  


def find_input_type(input_string):
    # Check if every character in the input string 
    # if all O or . then input message must be in braille
    # else the message is in english
    for char in input_string:
        if char not in "O.":
            return 'english'  
    return 'braille'


def main():
    import sys

    if len(sys.argv) < 2: ## if command line argument does not include as message, then prints error
        print("Provide a valid input to translate")
        return
    
    # concats all inputs after the commandline call into a single string seperated by spaces
    input_string = ' '.join(sys.argv[1:])
    
    # Detect whether input is Braille or English
    input_type = find_input_type(input_string)

    if input_type == 'english':
        result = english_to_braille(input_string)
    else:
        result = braille_to_english(input_string)
    print(result)

if __name__ == '__main__':
    main()


