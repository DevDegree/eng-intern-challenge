from main import converter
from sys import argv


if __name__ == "__main__":

    inp_string = ' '.join(argv[1:])
    
    if converter().checker(inp_string):
        output = converter().english_to_braille(inp_string)
    else:
        output = converter().braille_to_english(inp_string)

    print(output)
