from braille_dict import braille_dict
from english_dict import english_dict
import pdb

def translate(input_args): 
    if(is_english(input_args)):
        translated_string = "".join(english_to_braille(input_args)) 
    else:
        translated_string = "".join(braille_to_english(input_args))
    print (translated_string)      
    return translated_string    

def is_english(input_args):
    if len(input_args) % 6 != 0 or any(char not in ['O', '.'] for char in input_args):
        return True 
    else:
        return False 
   

def english_to_braille(string):
    translated_string = []
    chars_to_translate = list(string)
    is_in_number_sequence = False
    for i, char in enumerate(chars_to_translate):
        if char.isupper():
            translated_string.append(english_dict["CF"])
            char = char.lower()
        elif char.isdigit() and not is_in_number_sequence:
            translated_string.append(english_dict["NF"])
            is_in_number_sequence = True
        if not char.isdigit():
            is_in_number_sequence = False
        translated_string.append(english_dict[char])
        

    return translated_string

def braille_to_english(string):
 #   pdb.set_trace()
    translated_string = []
    chars_to_translate = [string[i:i+6] for i in range(0, len(string), 6)]
    print(chars_to_translate)
    i = 0
    numbers = False
    while i <len(chars_to_translate):
        if chars_to_translate[i] == ".....O":
            if numbers == False:
                translated_string.append(braille_dict[chars_to_translate[i+1]][0].upper())
                i = i + 1
        elif chars_to_translate[i] == ".O.OOO":
            numbers = True
        elif chars_to_translate[i] == "......":
            numbers = False
            translated_string.append(braille_dict[chars_to_translate[i]])
        else:
            if isinstance(braille_dict[chars_to_translate[i]], list):
                if numbers == True:
                    translated_string.append(braille_dict[chars_to_translate[i]][1])
                else:
                    translated_string.append(braille_dict[chars_to_translate[i]][0])
            else:
                translated_string.append(braille_dict[chars_to_translate[i]])
        i = i+1
    return translated_string


def main():
    import sys
    input_args = ' '.join(sys.argv[1:])
    translate(input_args)

if __name__ == "__main__":
    main()