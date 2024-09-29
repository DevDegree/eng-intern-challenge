# Importing the sys module to handle command line arguments
import sys 

# Dictionary mapping Braille representations to English letters
braille_to_english = {
    'O.....' : 'a', 'O.O...' : 'b', 'OO....' : 'c', 'OO.O..' : 'd','O..O..' : 'e', 'OOO...' : 'f', 'OOOO..' : 'g',
    'O.OO..' : 'h','.OO...' : 'i', '.OOO..' : 'j', 'O...O.' : 'k', 'O.O.O.' : 'l','OO..O.' : 'm','OO.OO.' : 'n',
    'O..OO.' : 'o','OOO.O.' : 'p','OOOOO.' : 'q','O.OOO.' : 'r','.OO.O.' : 's','.OOOO.' : 't','O...OO' : 'u',
    'O.O.OO' : 'v','.OOO.O' : 'w','OO..OO' : 'x','OO.OOO' : 'y','O..OOO' : 'z',
    '.....O' : 'capital', # To indicate that a capital letter follows
    '.O.OOO' : 'number', # To indicate that number(s) follow(s)
    '......' : ' ',
}

# Dictionary mapping Braille representations to numbers
braille_to_number = {
    'O.....' : '1','O.O...' : '2','OO....' : '3','OO.O..' : '4',
    'O..O..' : '5','OOO...' : '6','OOOO..' : '7','O.OO..' : '8',
    '.OO...' : '9','.OOO..' : '10',
}

# Dictionary mapping English letters to Braille representations
english_to_braille = {
    'a': 'O.....','b' : 'O.O...','c' : 'OO....','d' : 'OO.O..','e' : 'O..O..','f' : 'OOO...','g' : 'OOOO..',
    'h' : 'O.OO..','i' : '.OO...','j' : '.OOO..','k' : 'O...O.','l' : 'O.O.O.','m' : 'OO..O.','n' : 'OO.OO.',
    'o' : 'O..OO.','p' : 'OOO.O.','q' : 'OOOOO.','r' : 'O.OOO.','s' : '.OO.O.','t' : '.OOOO.','u' : 'O...OO',
    'v' : 'O.O.OO','w' : '.OOO.O','x' : 'OO..OO','y' : 'OO.OOO','z' : 'O..OOO',
    'capital' : '.....O', # To indicate that a capital letter follows
    'number' : '.O.OOO', # To indicate that number(s) follow(s)
    'space' : '......',
}

# Dictionary mapping numbers to Braille representations
number_to_braille = {
    '1' : 'O.....','2' : 'O.O...','3' : 'OO....','4' : 'OO.O..',
    '5' : 'O..O..','6' : 'OOO...','7' : 'OOOO..','8' : 'O.OO..',
    '9' : '.OO...','0' : '.OOO..',
}

# Function to check if the input string is in Braille format
def is_braille(input_string):

    # If input contains only spaces, return False (not Braille)
    if all(c in " " for c in input_string):
        return False
    
    # Check if all characters in the input string are either 'O' or '.' (if yes - Braille - returns True, if no - English - returns False)
    else:
        return all(c in "O." for c in input_string)

# Function to translate a Braille string to English
def translate_braille_to_english(string_braille):

    sep_char = [] # List to store translated, separated English characters
    number_dict = False  # Flag to indicate if currently using the number dictionary 
    cap_letter = False # Flag to indicate if the next character is a capital letter

    # Processing Braille input in chunks of 6 characters
    for i in range(0, len(string_braille), 6):
        braille_char = string_braille[i : i+6] # Extracting a Braille character

        #If in number context
        if number_dict: 
            match braille_char:
                case '......': 
                    number_dict = False # Space signifies end of number context
                case _: 
                    sep_char.append(braille_to_number.get(braille_char, '')) # Translate Braille character to number
            continue # Skip to the next character

        # If next character should be capitalized
        if cap_letter: 
            sep_char.append(braille_to_english.get(braille_char, '').upper()) # Translate Braille character to English capital letter
            cap_letter = False # Reset the capital flag
            continue # Skip to next character

        match braille_char:
            #Capital letter indicator
            case '.....O':
                cap_letter = True
            
            #Number indicator
            case '.O.OOO':
                number_dict = True

            #All other cases - translate normal Braille to English letters
            case _:
                sep_char.append(braille_to_english.get(braille_char, '')) # Translate Braille character to English

    return "".join(sep_char) # Return the joined translated string (in English)

# Function to translate English string to Braille
def translate_english_to_braille(string_english):

    sep_char = [] # List to store translated, separated Braille characters
    number_dict = False # Flag to indicate if currently using the number dictionary 

    # Process each character in the English input string
    for english_char in string_english:
        
        # If character is a digit
        if english_char.isdigit():
            if not number_dict: # If not already in number context
                sep_char.append(english_to_braille.get("number", '')) #Add the number indicator
            sep_char.append(number_to_braille.get(english_char, '')) # Translate the number to Braille
            number_dict = True # Set the number context flag

        # If character is capital
        elif english_char.isupper():
            sep_char.append(english_to_braille.get("capital", '')) # Add the capital indicator
            sep_char.append(english_to_braille.get(english_char.lower(), '')) # Translate to Braille
        
        # For lower case letters and spaces
        else:
            if english_char == ' ':
                sep_char.append(english_to_braille.get("space", '')) # Add space representation
                number_dict = False # Reset the number context
            else:
                sep_char.append(english_to_braille.get(english_char, '')) # Translate lower case letter to Braille
    
    # Return the joined translated string (in Braille)
    return "".join(sep_char) 

# Main function to handle input and initiate translation 
def main():

    #Check if there are command line arguments
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:]) # Join command line arguments into a single input string
    else:
        print("No input provided. If you only entered spaces, please wrap them with double quotes.")
        return # Exit if no input is provided

    # Check if the input string is in Braille or English and translate accordingly
    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))

if __name__ == "__main__":
    main()


