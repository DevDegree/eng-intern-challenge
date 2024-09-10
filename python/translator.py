import sys

braille_to_english_dict = {
    'O.....': 'a', 'O.O...': 'b', 
    'OO....': 'c', 'OO.O..': 'd', 
    'O..O..': 'e', 'OOO...': 'f', 
    'OOOO..': 'g', 'O.OO..': 'h', 
    '.OO...': 'i', '.OOO..': 'j', 
    'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 
    'O..OO.': 'o', 'OOO.O.': 'p', 
    'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 
    'O...OO': 'u', 'O.O.OO': 'v', 
    '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' '
}

english_to_braille_dict = {value:key for key, value in braille_to_english_dict.items()}

braille_to_number = {
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

number_to_braille = {value:key for key, value in braille_to_number.items()}


def is_braille(input):
    """
    Determines if input string is braille or English

    Args: input (str) - string to be evaluated by function to be either braille or English
    
    Returns: bool - True if the string matches the criteria for being Braille, false if otherwise (inferred to be English)
    """
    return (len(input) % 6 == 0) and (all(c in 'O.' for c in input))

def braille_to_eng(input):
    """
    Converts a braille string (combination of 'O' and '.' where 'O' indicates raised bits) into English string

    Args: input (str) - The braille string, assumes input is braille, handled by is_braille in main function

    Returns: str - English translation of braille input
    """

    result = ''
    numbered_braille = False
    cap_next = False
    i = 0

    # loop through braille symbols in the string (get every 6 characters)
    while i < len(input):

        current_braille = input[i : i+6]

        # handle cases where current symbol results in either a swap to numbers or capitlization of next symbol
        if current_braille == ".O.OOO":
            numbered_braille = True
        elif current_braille == ".....O":
            cap_next = True
        # handle inserting correct character into result string
        else:
            # gets capitilized version of desired character
            if cap_next == True:
                result += braille_to_english_dict[current_braille].capitalize()
                cap_next = False
            # if numbered braille is currently active, get braille translation from seperate dict
            elif numbered_braille == True:
                result += braille_to_number[current_braille]
            # else, handles "normal cases" of insertion
            else:
                # addition of space will turn off numbered braille so next character will go back to alphabet dict
                if current_braille == '......':
                    result += ' '
                    numbered_braille = False
                # gets and inserts char from alphabet dict
                else:
                    result += braille_to_english_dict[current_braille]
        i += 6

    return result

def eng_to_braille(input):
    """
    Given an English String, return Braille translation

    Arg: input (str) - the input English String (assumed, handled by is_braille() in main function)

    Return: str - the Braille translation of the English input
    
    """
    result = ''
    i = 0
    more_number = False

    while i < len(input):
        char = input[i]
        if more_number and char.isnumeric():
            result += number_to_braille[char]
        elif char.isnumeric():
            result += ('.O.OOO' + number_to_braille[char])
            more_number = True
        else:
            more_number = False
            if char.isupper():
                result += ('.....O' + english_to_braille_dict[char.lower()])
            else:
                result += english_to_braille_dict[char]
        i += 1
    
    return result

def main():
    input = " ".join(sys.argv[1:])

    if is_braille(input):
        output = braille_to_eng(input)
    else:
        output = eng_to_braille(input)
    
    print(output)

if __name__ == "__main__":
    main()