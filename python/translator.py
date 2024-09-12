import sys 
from translator_help import *

def get_str_from_args() -> str: 
    list_of_arguments = sys.argv[1:]
    if len(list_of_arguments) == 0: 
        return ""
    else: 
        return " ".join(list_of_arguments)
    
def check_if_english(text: str) -> bool: 
    return True 

def convert_to_braille(text: str) -> str: 
    return text

def convert_to_english(text: str) -> str: 
    return text 

def main():
    text = get_str_from_args()
    is_english = check_if_english(text)
    if is_english: 
        print(convert_to_braille(text))
    else: 
        print(convert_to_english(text))

if __name__ == "__main__": 
    main()
