import sys

def detect_input_format(input_string):
    if all(c in 'O.' for c in input_string):  #contains only (O, .)
        return "Braille"
    elif all(c.isalnum() or c.isspace() for c in input_string):  #eng letters, nums, and spaces
        return "English"
    else:
        return "Unknown"

eng_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO",
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
    ' ': "......" 
}

braille_to_eng = {
    "O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e',
    "OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i', ".OOO..": 'j',
    "O...O.": 'k', "O.O.O.": 'l', "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o',
    "OOO.O.": 'p', "OOOOO.": 'q', "O.OOO.": 'r', ".OO.O.": 's', ".OOOO.": 't',
    "O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x', "OO.OOO": 'y', "O..OOO": 'z',
    "......": ' '  
}

braille_to_nums = {
    "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4', "O..O..": '5',
    "OOO...": '6', "OOOO..": '7', "O.OO..": '8', ".OO...": '9', ".OOO..": '0'
}

capital_prefix = ".....O"
number_prefix = ".O.OOO" 

def english_to_braille(english_text):
    braille_output = []
    number_mode = False
    
    for char in english_text:
        if char.isdigit():
            if not number_mode:  # if we're not already in number mode
                braille_output.append(number_prefix)
                number_mode = True
            braille_output.append(eng_to_braille[char])
        elif char.isalpha():
            if number_mode:  #reset number mode if a letter is encountered
                number_mode = False
            if char.isupper():  #add capitalization prefix if letter is uppercase
                braille_output.append(capital_prefix)
            braille_output.append(eng_to_braille[char.lower()])
        elif char == ' ':
            braille_output.append(eng_to_braille[' '])
    
    return ''.join(braille_output)

def braille_to_english(braille_text):
    english_output = []
    capital_mode = False
    number_mode = False
    
    #process the input string in chunks of 6 characters (each braille is 6 dots)
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]
        
        if braille_char == capital_prefix:
            capital_mode = True
            number_mode = False  #exit num mode when capital mode is entered
        elif braille_char == number_prefix:
            number_mode = True
            capital_mode = False  #exit capital mode when num mode is entered
        elif number_mode:
            #use num dictionary when in num mode
            if braille_char in braille_to_nums:
                char = braille_to_nums[braille_char]
                english_output.append(char)
        else:
            #use the eng dictionary when not in num mode
            if braille_char in braille_to_eng:
                char = braille_to_eng[braille_char]
                
                #capitalization
                if capital_mode:
                    if char.isalpha():
                        char = char.upper()
                    capital_mode = False  #only the next letter
                
                english_output.append(char)
            
        #exit num mode if found a space
        if braille_char == "......":
            number_mode = False
    
    return ''.join(english_output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])  # combines all input into one
    
    #detect input type
    if detect_input_format(input_string) == "Braille":
        result = braille_to_english(input_string)
    else:
        result = english_to_braille(input_string)
    
    print(result)