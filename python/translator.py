import sys 
from translator_help import *

# gets all the arguments after the file name, and return a string connecting all the arguments with spaces
def get_str_from_args() -> str: 
    list_of_arguments = sys.argv[1:]
    if len(list_of_arguments) == 0: 
        return ""
    else: 
        return " ".join(list_of_arguments)
    
# checks if the text is in english or braille
# the way it checks is to see if there are any characters besides 'O' and '.'
def check_if_english(text: str) -> bool: 
    for char in text: 
        if not (char == 'O' or char == '.'): # detected a character that is not in braille, must be in English
            return True 
    return False 

# if it is in english, convert the text to braille 
def convert_to_braille(text: str) -> str: 
    result_string = "" # keeps adding onto this string to be returned at the end 
    use_number = False # sees if the current and upcoming chars, until the next space, should be false 
    for char in text: 
        if char == ' ': 
            result_string += space_braille 
            use_number = False # resets to english character if it was looking at numbers 
            continue 
        # here, we check if the character is a number, then we should set the is_number variable to be true  
        if char.isnumeric(): 
            if not use_number: # if it is the first time the number has appeared in the word, put in number follows braille
                result_string += number_follows_braille
                use_number = True
        # adds in the corresponding braille code of the character based on whether it is a number or an English letter
        try: 
            if use_number: 
                result_string += number_to_braille_code(number_to_braille_char[char])
            else:
                if char.isupper(): # if the character is an uppercase english letter then add in braille code for capital follows
                    result_string += capital_follows_braille
                result_string += number_to_braille_code(english_to_braille_char[char.lower()])
        except: 
            print("invalid character detected in text when trying to convert to braille")
            sys.exit(1)
        
    return result_string 

# helper function for slicing the text in braille code into braille characters, 6 per each
def get_braille_codes(text: str) -> list: 
    start_index = 0
    list_of_braille_codes = []
    while start_index + 6 <= len(text): 
        list_of_braille_codes.append(text[start_index: start_index + 6])
        start_index += 6
    return list_of_braille_codes

# if it is in braille, convert the text to english 
def convert_to_english(text: str) -> str: 
    result_string = ""
    is_number = False # keeps track of if the next characters until the space would be numbers 
    is_capital = False # keeps track of if the next character is capitalized 
    list_of_braille_codes = get_braille_codes(text)
    
    for braille_code in list_of_braille_codes:
        if braille_code == space_braille: 
            is_number = False
            is_capital = False 
            result_string += ' '
        elif braille_code == capital_follows_braille: # makes the next character capitalized 
            is_capital = True 
        elif braille_code == number_follows_braille: # so that the program knows the next characters are numbers
            is_number = True 
        else: # if the current braille code is either a letter or number
            
            if is_number: 
                try: 
                    result_string += braille_to_number_char[braille_code]
                except: 
                    print("invalid braille code detected when trying to do braille to number conversion")
                    sys.exit(1)
            else: 
                # if there is a capital follows code before it, capitalize it
                try: 
                    if is_capital: 
                        result_string += braille_to_english_char[braille_code].upper()
                        is_capital = False # to ensure only the current character is capitalized
                    else:
                        result_string += braille_to_english_char[braille_code]
                except: 
                    print("invalid braille code detected when trying to do braille to English letter conversion")
                    sys.exit(1)

    return result_string



def main():
    text = get_str_from_args()
    is_english = check_if_english(text)
    if is_english: 
        print(convert_to_braille(text))
    else: 
        print(convert_to_english(text))

if __name__ == "__main__": 
    main()