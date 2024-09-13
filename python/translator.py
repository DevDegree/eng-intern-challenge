import sys  

special_chars ={
    ".":"..OO.O",
    ",":"..O...",
    "?":"..O.OO",
    "!":"..OOO.",
    ":":"..OO..",
    ";":"..O.O.",
    "-":"....OO",
    "/":".O..O.",
    "<":".OO..O",
    ">":"O..OO.",
    "(":"O.O..O",
    ")":".O.OO.",
}
translation_dict = {
    "capital_follows":".....O",
    "decimal_follows":".O...O",
    "number_follows" :".O.OOO",
    "a":"O.....",
    "b":"O.O...",
    "c":"OO....",
    "d":"OO.O..",
    "e":"O..O..",
    "f":"OOO...",
    "g":"OOOO..",
    "h":"O.OO..",
    "i":".OO...",
    "j":".OOO..",
    "k":"O...O.",
    "l":"O.O.O.",
    "m":"OO..O.",
    "n":"OO.OO.",
    "o":"O..OO.",
    "p":"OOO.O.",
    "q":"OOOOO.",
    "r":"O.OOO.",
    "s":".OO.O.",
    "t":".OOOO.",
    "u":"O...OO",
    "v":"O.O.OO",
    "w":".OOO.O",
    "x":"OO..OO",
    "y":"OO.OOO",
    "z":"O..OOO",
    " ":"......"
}

number_dict = {
    "1":"O.....",
    "2":"O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    "0":".OOO..",
    }

braille_dict = dict(zip(translation_dict.values(), translation_dict.keys()))
braille_number_dict = dict(zip(number_dict.values(), number_dict.keys()))


def input_string_braille(input):    
    return all(c in {'.', 'O'} for c in input)

def split_braille(braille_string):
    return [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]

def braille_to_english(input_braille_string):
    assert (len(input_braille_string) % 6 == 0) # checks if input string is braille
    braille_chars = split_braille(input_braille_string) # splits braille string into each braille character
    next_char_capital = False # flag for capital
    next_char_num = False # flag for number 

    for char in braille_chars:
        translated_value = braille_dict[char] 


        if translated_value == 'capital_follows': # checks for if next char should be a capital
            next_char_capital = True
            continue
        elif translated_value == 'number_follows': # checks if next chars should be numbers
            next_char_num = True
            continue
        elif translated_value == ' ': # prints space out and ends number printing if applicable
            next_char_num = False
            print(translated_value, end='')
            continue
        
        if not next_char_num: # if not number, prints out capitalized or normal letter
            if next_char_capital:
                print(translated_value.upper(), end='')
                next_char_capital = False
            else:
                print(translated_value, end='')
        else:
            print(braille_number_dict[char], end='')



def english_to_braille(input):
    currently_parsing_number = False # creates flag to see if number is currently being parsed to know if number_follows needs to be printed
    for char in input:
        if char.isalpha():
            if char.isupper(): # print capital_follows before char if char is capital
                print(translation_dict['capital_follows'], end='') 
                print(translation_dict[char.lower()], end='')
                continue
            print(translation_dict[char], end='')
        elif char.isdigit(): 
            if not currently_parsing_number: # check if currently parsing a number, if not print number_follows before printing character
                print(translation_dict['number_follows'], end='')
                currently_parsing_number = True
            print(number_dict[char], end='')
        elif char == ' ': # ends parsing of number if it was positive, then prints space string
            currently_parsing_number = False
            print(translation_dict[' '], end='')

def main():
    input_string = ' '.join(sys.argv[1:]) # creates joint input string

    if input_string_braille(input_string):
        braille_to_english(input_string)
    else:
        english_to_braille(input_string)
if __name__ == '__main__':
    main()