import sys

english_to_braille_dictionary = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    
    'capital': '.....O',
    'number': '.O.OOO',
    'decimal': '.O...O',
    'space': '......',
    '.': '..OO.O',
    ',': '..O...',
    ';': '..OO..',
    ':': '..OO.O',
    '!': '..OOO.',
    '?': '..O.O.',
    '-': '..O..O', 
    '/': '..O..O',  
    '<': '.O....',  
    '>': '..O..O',  
    '(': '.O..O.',  
    ')': '..O..O',  
}

braille_to_english_dictionary = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    
    '.....O': 'capital',
    '.O.OOO': 'number',
    '.O...O': 'decimal' ,
    '......': ' ',

    '..OO.O': '.',
    '..O...': ',',
    '..OO..': ';',
    '..OO.O': ':',
    '..OOO.': '!',
    '..O.O.': '?',
    '..O..O': '-',
    '.O....': '<',
    '..O..O': '>',
    '.O..O.': '(',
    '..O..O': ')',
}

def braille_to_english(braille: str) -> str:
    """
    Conver Braille to English

    Args: 
    braille (str): Braille string to convert

    Returns:
    complete(str): The coverted English string
    """

    # Divide string by 6 digit block
    divided = [ braille[i:i+6] for i in range(0, len(braille), 6)]

    complete = ''

    capital_flag = False

    number_flag = False

    letter_to_number = "abcdefghij"

    for block in divided:
        if(braille_to_english_dictionary[block] == 'capital'):
            capital_flag = True

        elif(braille_to_english_dictionary[block] == 'number'):
            number_flag = True

        elif (capital_flag == True):
            capitalized = braille_to_english_dictionary[block].capitalize()
            complete += capitalized
            capital_flag = False

        elif (number_flag == True):
            corresponding_number = letter_to_number.find(braille_to_english_dictionary[block]) + 1
            if corresponding_number == 10:
                complete += '0'
            else:
                complete += str(corresponding_number)

        elif (braille_to_english_dictionary[block] == 'space'):
            number_flag = False

        else:
            english = braille_to_english_dictionary[block]
            complete += english

    return complete

def english_to_braille(English: str) -> str:
    """
    Conver English to Braille

    Args: 
    English (str): English string to convert

    Returns:
    complete(str): The coverted Braille string
    """

    complete = ''

    number_flag = False
    
    for alphabet in English:
        if alphabet.isupper() == True:
            complete += english_to_braille_dictionary['capital']
            complete += english_to_braille_dictionary[alphabet.lower()]

        elif alphabet.isnumeric() == True and number_flag == False:        
            complete += english_to_braille_dictionary['number']
            complete += english_to_braille_dictionary[alphabet]
            number_flag = True

        elif alphabet == ' ':
            complete += english_to_braille_dictionary['space']
            number_flag = False

        else:
            complete += english_to_braille_dictionary[alphabet]

    return complete

# Check if it is braille or english
def is_braille(argument: str) -> str:
    """
    Check if the string is braille
    
    Args:
    argument(str): string to check
    
    Returns:
    bool: True if the string is braille, False if not
    """
    for character in argument:
        if character not in 'O.':
            return False
    return True



def translate(argument: str) -> str:
    """
    Translate the given argument to Braille or English

    Args:
    argument(str): The string to translate

    Returns:
    answer(str): The translated string
    """

    # check if the given argument is English or Braille
    if is_braille(argument) == True:
         # Check if the Braille is incomplete
        if ((len(argument)%6) != 0):
            answer = english_to_braille(argument)
            
        else:
            answer = braille_to_english(argument)
       
    else:
        answer = english_to_braille(argument)
    return answer

def main() -> str:
    """
    main function control the command line input
    
    Returns:
    result(str): The translated string
    """
    if len(sys.argv) < 2:
        print("Please provide the text that you would like to translate braille or english")
        sys.exit(1)

    argument = ' '.join(sys.argv[1:])

    try:
        result = translate(argument)
        print(result)
        return result
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()

        



