import sys

BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO'  , '..OO.O':'.', '..O...':',', '..O.OO':'?', '..OOO.':'!', 
    '..OO..':':', '..O.O.':';', '....OO':'-', '.O..O.':'/', '.OO.O.':'<', 'O..OO.':'>', 
    'O.O..O':'(', '.O.OO.':')',
}

BRAILLE_NUMBERS_MAP = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}


ENGLISH_MAP={v:k for k,v in BRAILLE_MAP.items()}
ENGLISH_NUMBERS_MAP={v:k for k,v in BRAILLE_NUMBERS_MAP.items()}

CAPITAL_MARKER='.....O'
NUMBER_MARKER ='.O.OOO'
SPACE_MARKER='......'


def english_to_braile(input_str:str) -> str :
    """   
    Function to translate English to Braille
    """
    output=''
    first_num_flag=True #Recognize first num in a num sequence
    for char in input_str:
        if(char.isupper()):
            output+=CAPITAL_MARKER + BRAILLE_MAP[char.lower()]
        elif (char.isdigit()):
            if(first_num_flag):
                output+=NUMBER_MARKER + BRAILLE_NUMBERS_MAP[char]
                first_num_flag=False
            else:
                output+=BRAILLE_NUMBERS_MAP[char]
        elif (char==' '):
            first_num_flag=True #End of num sequence
            output+=SPACE_MARKER
        else:
            output+=BRAILLE_MAP[char]
    return output
            


def braille_to_english(input_str:str) -> str:
    """   
    Function to translate Braille to English
    """
    output=''
    is_num=False #Enables num sequence
    i=0 
    while i < len(input_str):
        braille_str=input_str[i:i+6]
        if (braille_str==CAPITAL_MARKER):
            i+=6
            braille_str=input_str[i:i+6]
            output+=ENGLISH_MAP[braille_str].upper()
        elif (braille_str==NUMBER_MARKER):
            is_num=True
        elif (braille_str==SPACE_MARKER):
            output += ' '
            is_num=False #Disables num sequence 
        else:
            if(is_num):
                output+=ENGLISH_NUMBERS_MAP[braille_str]
            else:
                output+=ENGLISH_MAP[braille_str]
        i+=6
    return output

    


if __name__ == "__main__":
    if len(sys.argv)>1:
        input_str=" ".join(sys.argv[1:])
        if (all(char in 'O.' for char in input_str) and len(input_str)%6==0):  # Check if input is Braille
            output_str=braille_to_english(input_str=input_str)
            print(output_str)
        else:
            output_str=english_to_braile(input_str=input_str)
            print(output_str)
            



