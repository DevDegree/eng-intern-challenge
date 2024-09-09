import sys

NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"
CAPITAL = ".....O"

# Dictionary that contains each english character's lowercase braille equivalent
eng_lwr_to_brle = {
    "a" : "O.....", "b" : "O.O...", "c" : "OO....", "d" : "OO.O..", "e" : "O..O..", "f" : "OOO...",
    "g" : "OOOO..", "h" : "O.OO..", "i" : ".OO...", "j" : ".OOO..", "k" : "O...O.", "l" : "O.O.O.",
    "m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.", "p" : "OOO.O.", "q" : "OOOOO.", "r" : "O.OOO.",
    "s" : ".OO.O.", "t" : ".OOOO.", "u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO",
    "y" : "OO.OOO", "z" : "O..OOO"
}
# Dictionary that contains each english character's uppercase braille equivalent
eng_uppr_to_brle = {
    "A" : "O.....", "B" : "O.O...", "C" : "OO....", "D" : "OO.O..", "E" : "O..O..", "F" : "OOO...",
    "G" : "OOOO..", "H" : "O.OO..", "I" : ".OO...", "J" : ".OOO..", "K" : "O...O.", "L" : "O.O.O.",
    "M" : "OO..O.", "N" : "OO.OO.", "O" : "O..OO.", "P" : "OOO.O.", "Q" : "OOOOO.", "R" : "O.OOO.",
    "S" : ".OO.O.", "T" : ".OOOO.", "U" : "O...OO", "V" : "O.O.OO", "W" : ".OOO.O", "X" : "OO..OO",
    "Y" : "OO.OOO", "Z" : "O..OOO"
}
# Dictionary that contains each english character's numerical braille equivalent
eng_nums_to_brle = {
    "0" : ".OOO..", "1" : "O.....", "2" : "O.O...",
    "3" : "OO....", "4" : "OO.O..", "5" : "O..O..",
    "6" : "OOO...", "7" : "OOOO..", "8" : "O.OO..",
    "9" : ".OO..."
}

# Inverted dictionary that contains all lowercase english equivalents for braille inputs
brle_lwr_to_eng = dict(map(reversed, eng_lwr_to_brle.items()))
# Inverted dictionary that contains all uppercase english equivalents for braille inputs
brle_uppr_to_eng = dict(map(reversed, eng_uppr_to_brle.items()))
# Inverted dictionary that contains all numerical english equivalents for braille inputs
brle_nums_to_eng = dict(map(reversed, eng_nums_to_brle.items()))

# Function to determine if input is braille or not
def CheckIfBraille(input):
    for i in input:
        if(i == "o" or i == "."):
            return True
        else:
            return False
        
# Function to determine if braille input is a number or not
def CheckIfBrleNum(input):
    if(input == NUMBER_FOLLOWS):
        return True
    else:
        return False
        
# Function to determine if English input is a number or not
def CheckIfEngNum(input):
    if(input in eng_nums_to_brle.keys()):
        return True
    else:
        return False


# Function that converts the english alphabet to its braille equivalent
def EnglishAlphabetToBraille(input):
    braille_value = ""
    # Counter for numbers found, only need to print "number follows" once
    num_count = 0
    # Parse through each character, find char in dict, store converted value
    for i in input:
        # Check to see if character is capital or not, if capital add capital follows
        if(i.isupper()):
            braille_value = braille_value + CAPITAL + eng_uppr_to_brle[str(i)]
        elif(CheckIfEngNum(i)):
            if(num_count == 0):
                braille_value = braille_value + NUMBER_FOLLOWS + eng_nums_to_brle[str(i)]
                num_count += 1
            else:
                braille_value = braille_value + eng_nums_to_brle[str(i)]
        else:
            braille_value = braille_value + eng_lwr_to_brle[str(i)]
    return braille_value

# Function that convers the braille alphabet to its English equivalent
def BrailleAlphabetToEnglish(input):
    english_value = ""
    # Parse through every 6 characters, convert to english, store converted value 
    # Counter for to keep track of characters that are parsed
    counter = 1
    # String used to store every 6 characters
    input_str = ""
    # Boolean to keep track of whether a letter should be capitalized or not, default is false
    is_caps = False
    # Boolean to keep track of whether a char is a number or not 
    is_num = False
    for i in input:
        # If 6 characters have not been parsed, store the next character in the current input
        if(counter % 6 != 0):
            input_str = input_str + i
        # Else, check if caps, add space if necessary store translated value
        else:
            # Last chracter gets missed in modulus check, store to complete the string then do conversion
            input_str = input_str + i
            if(CheckIfBrleNum(input_str)):
                is_num = True
                input_str = ""
            elif (input_str == CAPITAL):
                is_caps = True
                input_str = ""
            else:
                if(is_caps):
                    english_value = english_value + brle_uppr_to_eng[input_str]
                    is_caps = False
                elif(is_num):
                    english_value = english_value + brle_nums_to_eng[input_str]
                else:
                    english_value = english_value + brle_lwr_to_eng[input_str]
            ## Clear the input string so next character set can be stored
            input_str = ""
        counter += 1
    return english_value

def main():
    # Count the number of arguments to be translated (for the while loop)
    args_len = len(sys.argv) - 1

    # Output string array 
    translated_output = ""
    # Counter for while loop
    arg_count = 1
    # Temporary output (to be used for each argument)
    output = ""
    
    # iterate through each argument 
    while(args_len >= arg_count):
        input = sys.argv[arg_count]
        # if the first argument has passed, a space needs to be added, check if the input is braille or not to add the correct language space
        if(arg_count > 1):
            if(CheckIfBraille(input)):
                translated_output = translated_output + " "
                # Run translation function
                output = BrailleAlphabetToEnglish(input)
                translated_output = translated_output + output
            else:
                translated_output = translated_output + SPACE
                # Run translation function
                output = EnglishAlphabetToBraille(input)
                translated_output = translated_output + output
        else:
            # Determine if input is braille or not
            if(CheckIfBraille(input)):
                # Run translation function
                output = BrailleAlphabetToEnglish(input)
                translated_output = translated_output + output
            else:
                # Run translation function
                output = EnglishAlphabetToBraille(input)
                translated_output = translated_output + output
        arg_count += 1
    
    print(translated_output)

if __name__ == "__main__":
    main()