import sys

english_braille_map = {                                 # Dictionary with keys set as english letters and values set as braille
    # Numbers from 0-9
    "0":".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", 
    "8": "O.OO..", "9": ".OO...", 
    # Letters a-z and space
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", 
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", 
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", 
    "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", " ": "......",
}       

braille_english_map = {}                                # Create a new map with keys as braille and values as english letters
for key, value in english_braille_map.items():          # Reverse the values for each entry in english_braille_map
    braille_english_map[value] = key                    # Number keys are removed by corresponding letter keys due to duplicates

def english_to_braille(english):                        # Function to convert English prompts to Braille
    braille = ""
    number_follows = False                              # Check for number follows cell
    for char in english:
        if  char.isupper():                             # If the character is uppercase, add the capital follows cell in front
            braille += ".....O"
        elif char.isnumeric() and number_follows == False:      # If the character is a number, add the number follows cell       
            braille += ".O.OOO"
            number_follows = True                    
        elif char == " ":
            number_follows = False                              # Once the space character is identified, no more numbers are following

        braille += english_braille_map[char.lower()]            # Add the cell corresponding with the key, lowercase if it's a letter
    return braille
    
def braille_to_english(braille):                        # Function to convert Braille cells into English
    english = ""
    number_follows = False                              
    capital_follows = False                             
    braille_list = [(braille[i:i+6]) for i in range(0, len(braille), 6)]    # Split the list into groups of 6 dots
    for cell in braille_list:                           
        if cell == ".O.OOO":                            # Check for number follows cell
            number_follows = True
            continue                                    # If there is the cell, do not add anything to the english string
        if cell == ".....O":                            # Check for capital follows cell
            capital_follows = True                      # If the cell exists, do not add anything to the english string
            continue
        if number_follows:                                  # If there was a number follows cell, convert the corresponding letter
                                                            # into its unicode character using ord
            number = ord(braille_english_map[cell]) - 96
            english += str(number)                          # Add the string of the number onto english string
        elif capital_follows:                               # If there was a capital follows cell, capitalize the corresponding char
            english += braille_english_map[cell].upper()    
            capital_follows = False                         # Turn capital_follows to false so that following letters are not capitalized
        else:
            if cell == "......":                            # If the cell is space, make sure to set number_follows to false
                number_follows = False
            english += braille_english_map[cell]            # Add the english value based on the braille key
    return english 

def main():
    args = " ".join(sys.argv[1:])
    if args.find(".") == -1:                            # if there are no periods, it is english
        print(english_to_braille(args))                 
    else:
        print(braille_to_english(args))
        
if __name__ == "__main__":
    main()
