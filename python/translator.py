import sys
import re

# Define mapping from English to Braille
braille_dict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......"
}

braille_number_dict = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

capt_follows = ".....O"
number_follows = ".O.OOO"

# Define inverse mapping
english_dict = {value:key for key, value in braille_dict.items()}

english_number_dict = {value:key for key, value in braille_number_dict.items()}

def convert_list_to_string(lst):

    """
    Function that will convert list to string with spaces between the elements
    """

    string = " ".join(str(element) for element in lst)

    return string

def english_to_braille(text):

    """
    Function that converts english to braille
    """

    braille = ""
    
    i = 0
    
    while i < len(text):
        
        if text[i].isupper():
            
            braille += capt_follows + braille_dict[text[i].lower()]
                        
        elif text[i].isdigit():
            
            braille += number_follows
            
            while i < len(text) and text[i].isdigit():
                
                braille += braille_number_dict[text[i]]
                
                i += 1
                
            continue
                            
        else:
            
            braille += braille_dict[text[i]]
            
        i +=1
            
    return braille

def braille_to_english(braille):

    # Split braille string into list
    braille = [braille[i:i+6] for i in range(0, len(braille), 6)]

    english = ""

    i = 0

    while i < len(braille):

        if braille[i] == capt_follows:

            if i+1 < len(braille):

                english += english_dict[braille[i+1]].capitalize()

                i += 2

            else:

                i += 1

            continue

        if braille[i] == number_follows:

            i += 1

            while i < len(braille) and braille[i] != "......":

                english += english_number_dict[braille[i]]

                i += 1

            if i < len(braille) and braille[i] == "......":
                
                english += " "

                i += 1
            
        else: 

            english += english_dict[braille[i]]

            i += 1

    return english

def main():

    # Convert program input into single string
    prog_input  = convert_list_to_string(sys.argv[1:])

    # check if its english or braille then convert to opposite and print
    english_cond = bool(re.fullmatch(r"[a-zA-Z0-9 ]*", prog_input))
    braille_cond = bool(re.fullmatch(r"[O.]*", prog_input))

    if english_cond:

        braille_output = english_to_braille(prog_input)
        
        print(braille_output)

    elif braille_cond:

        english_output = braille_to_english(prog_input)

        print(english_output)

if __name__ == "__main__":
    
    main()
