import sys 
from mappings import *

def is_english(arg: str):
    if "." not in arg: 
        return True 
    return False 

def main():
    arg_len = len(sys.argv)
    if arg_len < 2:
        return "word/braille not provided"
    
    res = ""
    for i in range(1, arg_len):
        arg = sys.argv[i]
        if is_english(arg):
            is_numbers = False
            if arg[0] in numbers and not is_numbers:
                    res = res + special_characters_to_braille['number']
                    is_numbers = True 
            for char in arg:
                # if there is a mixture of numbers and letters then the input should be invalid according to our rules
                if char not in numbers and is_numbers: 
                    print("ERROR: cannot mix numbers and letters in the same continous string")
                    return 
                if char.isupper():
                    res = res + special_characters_to_braille['capital']
                res = res + english_to_braille[char.upper()]
            if i != arg_len - 1: 
                res = res + special_characters_to_braille['space']
        else:
            char = ""
            is_number = False
            is_capital = False
            for i in range(len(arg)):
                char = char + arg[i]
                if (i + 1) % 6 == 0 and i != 0: 
                    if char in braille_to_special_characters:
                        if braille_to_special_characters[char] == "number":
                            is_number = True
                        if braille_to_special_characters[char] == "capital":
                            is_capital = True
                        if braille_to_special_characters[char] == "space":
                            res = res + " "
                    else:
                        if is_number: 
                            res = res + braille_to_numbers[char]
                        elif is_capital:
                            res = res + braille_to_letters[char]
                            is_capital = False
                        else:
                            res = res + braille_to_letters[char].lower()
                    char = ""
    print(res)


if __name__ == "__main__":
    main()
