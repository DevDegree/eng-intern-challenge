import sys

# 1. determine if string is in english or braille
#       -> iterate through each character
#       -> if character is not 'O' or '.' string is in braille
#       -> else string is in english

def is_braille(string):
    for c in string:
        if c != 'O' and c != '.':
            return to_english(string)
    return to_braille(string)

# 2. If string is in braille
#       -> create dict variable 'BRAILLE-ENGLISH-LETTER-MAP' that has the braille character letters as the keys, and english characters as the values
#       -> create dict variable 'BRAILLE-ENGLISH-NUMBER-MAP' that has the braille numbers as the keys, and english numbers as the values
#       -> create list variable 'braille-characters'
#       -> create string variable 'english-str'
#       -> create bool variable number = False
#       -> iterate through every sixth character
#       -> store characters in string from position i - 6 to position i as item in list
#       -> iterate through 'braille-characters'
    #       -> if item is 'capital follows'
    #           -> search for item in 'BRAILLE-ENGLISH-LETTER-MAP' keys
    #           -> add CAPITALIZED corresponding value to 'english-str'
    #       -> if number == True and item is 'space'
    #           -> set number = False
    #           -> add space to 'english-str'
    #       -> if item is 'number follows' or number == True
    #           -> set number = True
    #           -> search for item in 'BRAILLE-ENGLISH-NUMBER-MAP' keys
    #           -> add corresponding value to 'english-str'
#       -> return 'english-str'

def to_english(string):
    BRAILLE_ENGLISH_LETTER_MAP = {
        "O.....": 'a',
        "O.O...": 'b',
        "OO....": 'c',   
        "OO.O..": 'd',   
        "O..O..": 'e',  
        "OOO...": 'f',  
        "OOOO..": 'g',  
        "O.OO..": 'h',  
        ".OO...": 'i',  
        ".OOO..": 'j',   
        "O...O.": 'k',   
        "O.O.O.": 'l',   
        "OO..O.": 'm',   
        "OO.OO.": 'n',   
        "O..OO.": 'o',  
        "OOO.O.": 'p',  
        "OOOOO.": 'q',   
        "O.OOO.": 'r',  
        ".OO.O.": 's',  
        ".OOOO.": 't',   
        "O...OO": 'u', 
        "O.O.OO": 'v',  
        ".OOO.O": 'w',  
        "OO..OO": 'x', 
        "OO.OOO": 'y',  
        "O..OOO": 'z',
        "..OO.O": '.',
        "..O...": ',',
        "..O.OO": '?',
        "..OO..": ':',
        "..O.O.": ';',
        "....OO": '-',
        ".O..O.": '/',
        ".OO..O": '<',
        "O..OO.": '>',
        "O.O..O": '(',
        ".O.OO.": ')',
        "......": ' '
}
    BRAILLE_ENGLISH_NUMBER_MAP = {
        "O.....": '1',
        "O.O...": '2',
        "OO....": '3',
        "OO.O..": '4',
        "O..O..": '5',
        "OOO...": '6',
        "OOOO..": '7',
        "O.OO..": '8',
        ".OO...": '9',
        ".OOO..": '0',
    }
    braille_characters = []
    english_str = ''
    number = False
    

# 3. If string is in english
#       -> create dict variable 'ENGLISH-BRAILLE-MAP' that has the english characters as the keys, and braille characters as the values
#           -> 
#       -> create string variable 'braille-str'
#       -> iterate through every character of string
#           -> if character is number, add 'number-follows'
#           -> if character is capital, add 'capital-follows'
        #   -> if previous character is number and current character is '.' add 'decimal follows' and continue to next iteration
    #       -> search for item in 'ENGLISH-BRAILLE-MAP' keys, add corresponding value to 'braille-str'
#       -> return 'braille-str'



if __name__ == "__main__":
    args = sys.argv[1:]
    input = ' '.join(args)
    print(is_braille(input))
