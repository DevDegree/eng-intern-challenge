"""

A translator module that converts English text to Braille and vice versa.

Supports uppercase letters, numbers, and spaces.

"""



import sys



# Constants

CHUNK_SIZE = 6



# Lookup dictionaries



braille_to_english_no_digits = {

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

    '.....O': 'capital follows',

    '.O.OOO': 'number follows',

    '......': 'space',

}



braille_to_english_digits = { 

    'O.....': '1',

    'O.O...': '2',

    'OO....': '3',

    'OO.O..': '4',

    'O..O..': '5',

    'OOO...': '6',

    'OOOO..': '7',

    'O.OO..': '8',

    '.OO...': '9',

    '.OOO..': '0',

}



english_to_braille_no_digits = {

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

    'capital follows': '.....O',

    'number follows': '.O.OOO',

    'space': '......'

}



english_to_braille_digits = {

    '1': 'O.....',

    '2': 'O.O...',

    '3': 'OO....',

    '4': 'OO.O..',

    '5': 'O..O..',

    '6': 'OOO...',

    '7': 'OOOO..',

    '8': 'O.OO..',

    '9': '.OO...',

    '0': '.OOO..'

}





def translate_braille_to_english(input_string: str) -> str:

    """Translates Braille to English."""

    braille_chunks = []

    translated_characters = []



    # Split the Braille string into chunks of CHUNK_SIZE

    for i in range(0, len(input_string), CHUNK_SIZE):

        braille_chunks.append(input_string[i:i+CHUNK_SIZE])

        translated_characters.append(braille_to_english_no_digits[input_string[i:i+CHUNK_SIZE]])

    



    # Identify indices of special characters

    capital_follows_indices = [index for index, value in enumerate(translated_characters) if value == 'capital follows']

    number_follows_indices = [index for index, value in enumerate(translated_characters) if value == 'number follows']



    # Indices for capitalized letters and numbers

    capitalized_letters_indices  = [(index+1) for index in capital_follows_indices]

    numbers_indices = []

    

    # Find indices for numbers following 'number follows' until a space is encountered

    for count, idx in enumerate(number_follows_indices):

        j = idx + 1

        while(j < len(translated_characters) and translated_characters[j] !=  'space'):

            numbers_indices.append(j)

            j += 1





    # Capitalize letters at the identified indices

    for idx in capitalized_letters_indices:

        translated_characters[idx] = translated_characters[idx].capitalize()



    # Replace Braille chunks with corresponding digits

    for idx in numbers_indices:

        translated_characters[idx] = braille_to_english_digits[braille_chunks[idx]]

    

    

    # Build the final translated string, skipping control characters

    returned_string = ''



    for i in range(len(translated_characters)):

        if(translated_characters[i] == 'space'):

            returned_string += ' '

        elif(translated_characters[i] == 'capital follows' or translated_characters[i] == 'number follows'):

            continue

        else:

            returned_string += translated_characters[i]



    return returned_string 





def translate_english_to_braille(input_string: str) -> str:

    """Translates English to Braille."""



    returned_string = ''



    for i in range(len(input_string)):

        if(input_string[i] == ' '):

            returned_string += english_to_braille_no_digits['space']

        elif(input_string[i].isalpha()):

            if(input_string[i].isupper()):

                # Add 'capital follows' indicator for uppercase letters

                returned_string += english_to_braille_no_digits['capital follows'] + english_to_braille_no_digits[input_string[i].lower()]

            else:

                returned_string += english_to_braille_no_digits[input_string[i]]

        else:

            # Add 'number follows' indicator before a sequence of digits

            if i == 0 or not input_string[i - 1].isdigit():

                returned_string += english_to_braille_no_digits['number follows'] + english_to_braille_digits[input_string[i]]

            else:

                returned_string += english_to_braille_digits[input_string[i]]

    

    return returned_string





def translate(input_string: str) -> str:

    """

    Translates an input string from English to Braille or Braille to English.



    Parameters:

    input_string (str): The string to translate.



    Returns:

    str: The translated string.

    """



    # Determine if the input is Braille or English

    is_braille = all((char == 'O' or char == '.') for char in input_string) 





    if(is_braille):

        return translate_braille_to_english(input_string)

    else:

        return translate_english_to_braille(input_string)

        

    

if __name__ == "__main__":

    # Join the command-line arguments into a single string

    input_string = " ".join(sys.argv[1:])

    # Print the translated output to stdout

    print(translate(input_string))
