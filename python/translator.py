import sys

translation_dictionary_letters = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.", 
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.", 
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO"
}

translation_dictionary_numbers = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}


def in_braille(string_to_translate) -> bool:
    for i in string_to_translate:
        #if any char that isn't "O" or "." is found, the string is in english
        if i != "O" and i != ".":
            return False
    return True

def translate_to_braille(string_to_translate) -> str:
    list_to_return = []
    currently_number = False
    i = 0

    while i < len(string_to_translate):
        current_char = string_to_translate[i]
        
        if current_char.isnumeric():
            '''
            The program should print the braille character indicating that a number is coming
            only if there isn't a number preceding (this was the rule for braille -> english)
            '''
            if not currently_number:
                list_to_return.append(".O.OOO" + translation_dictionary_numbers[current_char])
            else:
                list_to_return.append(translation_dictionary_numbers[current_char])
            currently_number = True
        else:
            '''
            if current_char is a space symbol then write the equivalent character 
            in braille
            '''
            if current_char == " ":
                list_to_return.append("......")
            #if current_char is a alphabetical character verify if it's in lower and upper case and add the braille equivalent
            elif current_char.upper() == current_char:
                list_to_return.append(".....O" + translation_dictionary_letters[current_char.upper()])
            else:
                list_to_return.append(translation_dictionary_letters[current_char.upper()])
            currently_number = False
        i += 1

    '''
    To avoid a O(n) operation everytime a new char is translated, this function uses a
    list to store the individual chars. Then the list is joined (only one single O(n) operation)
    into a string once the translation has been completed.
    '''
    return "".join(list_to_return)


def translate_to_english(string_to_translate) -> str:
    list_to_return = []
    i = 0
    number_follows = False
    capital_follows = False
    
    while i < len(string_to_translate) - 5:
        #Since braille is represented in a 2 X 3 matrix, each character is given by 6 consecutive values
        current_char = string_to_translate[i : i + 6]
        
        #If the current_char is a space, then simply append it and make sure to reset numbers_follow to False
        if current_char == "......":
            number_follows = False
            list_to_return.append(" ")
        #If the current_char isn't a capital follows or number follows value then there are only 3 possibilities
        elif current_char != ".....O" and current_char != ".O.OOO":
            # (1) Number follows: simply append the english equivalent of the number
            if number_follows:
                list_of_numbers_keys = list(translation_dictionary_numbers.keys())
                list_of_numbers_values = list(translation_dictionary_numbers.values())

                position_of_value = list_of_numbers_values.index(current_char.upper())
                list_to_return.append(list_of_numbers_keys[position_of_value])
            else: 
                list_of_letters_keys = list(translation_dictionary_letters.keys())
                list_of_letters_values = list(translation_dictionary_letters.values())

                position_of_value = list_of_letters_values.index(current_char.upper())

                # (2) Capital follows: simply append the english equivalent of the letter capitalized
                if capital_follows:
                    list_to_return.append(list_of_letters_keys[position_of_value])
                #(3) Letter follows: simply append the english equivalent of the letter
                else:
                    list_to_return.append(list_of_letters_keys[position_of_value].lower())
            #Reset capital_follows to False seeing as this only lasts for one letter
            capital_follows = False
        else:
            #If a capital follows, set the equivalent boolean value to True
            if current_char == ".....O":
                capital_follows = True
            #If a number follows, set the equivalent boolean value to True
            elif current_char == ".O.OOO":
                number_follows = True
        #Increment by the size of braille character
        i += 6

    return "".join(list_to_return) 

def get_string_to_translate() -> str:
    '''
    If the program is used properly, the command line format would be:
      py <name of file> <string_to_translate>
    '''
    if len(sys.argv) >= 2:
        #get argv[1] because this holds the value of the string_to_translate
        i = 1
        list_to_return = []
        while i < len(sys.argv):
            if i + 1 != len(sys.argv):  
                list_to_return.append(sys.argv[i] + " ")
            else:
                list_to_return.append(sys.argv[i])
            i += 1
        return "".join(list_to_return)
    else:
        #return empty string if the format is incorrect
        return ''

def run_program() -> None:
    #fetch the string_to_translate
    string_to_translate = get_string_to_translate()

    #Make sure that the input what appropriate. If not return empty string.
    if string_to_translate != '':
        input_language = in_braille(string_to_translate)

        #Translate the string based on its language
        if input_language:
            print(translate_to_english(string_to_translate))
        else:
            print(translate_to_braille(string_to_translate))
    else:
        print('')

run_program()