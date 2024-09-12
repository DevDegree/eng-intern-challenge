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
    return True 

# if it is in english, convert the text to braille 
def convert_to_braille(text: str) -> str: 
    return text

# if it is in braille, convert the text to english 
def convert_to_english(text: str) -> str: 
    return text 

def main():
    text = get_str_from_args()
    is_english = check_if_english(text)
    if is_english: 
        print(convert_to_braille(text))
    else: 
        print(convert_to_english(text))

# if __name__ == "__main__": 
#     main()

print(get_str_from_args())