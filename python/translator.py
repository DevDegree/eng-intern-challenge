''' Khaliq Minsariya
    Shopify Engineering Intern Challenge Fall - Winter 2025
    Braille Translator
'''

import sys
import textwrap

# A dictionary that maps english alphabet to braille alphabet.
braille_alphabet = {
        'A': 'O.....', 
        'B': 'O.O...', 
        'C': 'OO....', 
        'D': 'OO.O..', 
        'E': 'O..O..', 
        'F': 'OOO...', 
        'G': 'OOOO..', 
        'H': 'O.OO..', 
        'I': '.OO...', 
        'J': '.OOO..', 
        'K': 'O...O.', 
        'L': 'O.O.O.', 
        'M': 'OO..O.',
        'N': 'OO.OO.', 
        'O': 'O..OO.', 
        'P': 'OOO.O.', 
        'Q': 'OOOOO.', 
        'R': 'O.OOO.', 
        'S': '.OO.O.', 
        'T': '.OOOO.', 
        'U': 'O...OO', 
        'V': 'O.O.OO', 
        'W': '.OOO.O', 
        'X': 'OO..OO', 
        'Y': 'OO.OOO', 
        'Z': 'O..OOO', 
        '1': 'O.....', 
        '2': 'O.O...', 
        '3': 'OO....', 
        '4': 'OO.O..', 
        '5': 'O..O..', 
        '6': 'OOO...', 
        '7': 'OOOO..', 
        '8': 'O.OO..', 
        '9': '.OO...', 
        'capital_follows': '.....O', 
        'number_follows': '.O.OOO',
        '.': '..OO.O', 
        ',': '..O...', 
        '?': '..O.OO', 
        '!': '..OOO.', 
        ':': '..OO..', 
        ';': '..O.O.', 
        '-': '....OO', 
        '/': '.O..O.', 
        '<': '.OO..O', 
        '>': 'O..OO.', 
        '(': 'O.O..O', 
        ')': '.O.OO.', 
        ' ': '......'
    }

def is_braille(message):
    '''
    Checks if the given string is in braille or english. 
    It's in braille if it contains '.' or 'O', and the result of the string length modulus 6 is 0 (since braille letters are chunks of 6 characters).

        Parameters: 
            message (str): The text to be translated

        Returns:
            (bool): Boolean value indicating if the message is in brialle or english 
    '''
    if ('.' in message or 'O' in message) and len(message) % 6 == 0:
        return True
    else:
        return False   

def to_braille(message):
    '''
        Translates the message to braille.

            Parameters:
                message (str): The english text to be translated to braille
            
            Returns:
                translation (str): The braille version of the english message
    '''

    # Storing the letters in a list and joining them in the end instead of string concatenation for better performance.
    translation = []
    
    # A flag to indicate a number follows in braille.
    number_prefix_exists = False

    # Loop through each character in the message adding its respective braille equivalent to the above list.
    # Hardcoding braille values to avoid dictionary lookup which hinders performance.
    for character in message:
        if character.isalpha():
            if character.isupper():
                translation.append('.....O')
                translation.append(braille_alphabet[character])
            else:
                translation.append(braille_alphabet[character.upper()])
        elif character.isnumeric():
            if not number_prefix_exists:
                translation.append('.O.OOO') 
                translation.append(braille_alphabet[character]) 
                number_prefix_exists = True
            else:
                translation.append(braille_alphabet[character])
        elif character == ' ':
            translation.append('......')
            number_prefix_exists = False
        else:
            translation.append(braille_alphabet[character])

    return ''.join(translation)

def to_english(message):
    '''
        Translates the message to english.

            Parameters:
                message (str): The braille text to be translated to english
            
            Returns:
                translation (str): The english version of the braille message
    '''
    
    # Separate each braille letter and store it in list form.
    message = textwrap.wrap(message, 6)

    # Reverse the 'braille_alphabet' keys and values instead of manually creating another dictionary and, 
    # create separate dictionaries for alphabets, numbers, and special characters since the keys of braille alphabets and numbers are the same.
    # These dictionaries are created within the function for better efficiency as this function is ran only once during the execution of this file, hence,
    # reduces complexity when not called which is the case when translating to braille instead.
    english_alphabet = {}
    for key, value in list(braille_alphabet.items())[0:26]:
        english_alphabet[value] = key

    english_numbers = {}
    for key, value in list(braille_alphabet.items())[26:35]:
        english_numbers[value] = key

    english_special = {}
    for key, value in list(braille_alphabet.items())[35:50]:
        english_special[value] = key
    
    # Flags to indicate when to assume captial letters and numbers. 
    capital_follows = False
    number_follows = False

    # List that stores the translated text.
    translation = []

    # Loop through each braille and convert to respective english version.
    # Hardcoding braille values to avoid dictionary lookup that would've reduced performance.
    for braille in message:
        if braille == '.....O':
            capital_follows = True
            continue
        elif braille == '.O.OOO':
            number_follows = True
            continue
        elif braille == '......':
            number_follows = False
            translation.append(english_special[braille]) 
            continue

        if capital_follows:
            translation.append(english_alphabet[braille]) 
            capital_follows = False
            continue

        if number_follows:
            translation.append(english_numbers[braille]) 
            continue

        # If braille is neither uppercase letter nor number nor blankspace, then it is either lowercase letter or a special character.
        try:
            # Try to search in alphabet dictionary for lowercase letter.
            translation.append(english_alphabet[braille].lower())
        except:
            # If above search fails then search in special characters dictionary.
            translation.append(english_special[braille])

    return ''.join(translation)

if __name__ == "__main__":
    # Read message from command-line arguments combining them into one if multiple given.
    arguments = sys.argv
    message = ' '.join(arguments[1:]).rstrip()

    # Ensure message is given and call appropriate function to translate it, displaying it back to the user in the terminal.
    if not message:
        print('Error! Translation message is missing.')
    elif is_braille(message):
        print(to_english(message))
    else:
        print(to_braille(message))