
import sys
from matrix_dict import matrix_dict
from input_checker import input_checker
from english_to_braille import e2b
from braille_to_english import b2e

def main(input_string):

    input_type = input_checker(input_string)

    if input_type == 'english':
        translated_string = e2b(input_string)
    else:
        translated_string = b2e(input_string)

    return translated_string

if __name__ == "__main__":
        
    # Get the input argument
    input_string = ' '.join(sys.argv[1:])
    
    # Call the main function with the input
    main(input_string)

    print(main(input_string))