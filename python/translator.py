import sys
import re


#Store the letters/numbers and the braile value in a dictionary.
BRAILLE_DICT = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", 1: "O.....", 2: "O.O...", 3: "OO....", 4: "OO.O..", 
    5: "O..O..", 6: "OOO...", 7: "OOOO..", 8: "O.OO..", 9: ".OO...", 
    0: ".OOO..", ' ': "......", 'capital': ".....O", 
    'number': ".O.OOO"
}

def english_to_braile(test_var):
    """
    Converts English text to Braille.
    - Uppercase letters are preceded by the "capital" Braille symbol.
    - Numbers are represented by the "number" Braille symbol followed by digits.
    
    Parameters:
    text (str): The English text to be converted to Braille.
    
    Prints:
    The corresponding Braille representation.
    """
    return_val = ""
    for letter in test_var:
        if letter.lower() in BRAILLE_DICT.keys():
            #If the letter is in upper case add the capital symbol before it.
            if str(letter).isupper():
                return_val += BRAILLE_DICT["capital"]+BRAILLE_DICT[str(letter.lower())]
            else:
                return_val += BRAILLE_DICT[str(letter)]
            
    
    print(return_val)

def braile_to_english(test_var):
    """
    Converts Braille text to English.
    - Handles capitalization and numeric mode.
    
    Parameters:
    braille_text (str): The Braille string to be converted to English.
    
    Prints:
    The corresponding English text.
    """
    braile_letters = []
    return_val = ""
    is_number = False
    is_caps = False


    # Split the Braille string into chunks of 6 (each representing a letter or symbol)
    for i in range(0, len(test_var), 6):
        braile_letters.append(test_var[i:i+6])
    
            
        
    for bl in braile_letters:
        # Detect the number sign
        if bl == '.O.OOO':
            is_number=True
            continue
            
        if is_number:
            # Handle spaces in numbers if found the next set of braile symbols are no longer a number
            if bl == '......':
                return_val += " "
                is_number = False
                continue
            # Convert Braile to digits
            letter = {i for i in BRAILLE_DICT if BRAILLE_DICT[i] == bl }
            for i in list(letter):
                # Only add numbers
                if isinstance(i,int): 
                    return_val += str(i)
        
        elif bl == '.....O':
            # Detect capitalization
            is_caps=True
            continue
            
        else:
            # Convert Braille to letter
            if not is_caps:
                letter = {i for i in BRAILLE_DICT if BRAILLE_DICT[i] == bl }
                for i in list(letter):
                    if isinstance(i,str):
                        return_val += i
                
            elif is_caps:
                # Handle uppercase letters
                letter = {i for i in BRAILLE_DICT if BRAILLE_DICT[i] == bl }
                for i in list(letter):
                    if isinstance(i,str):
                        return_val += i.upper()
                is_caps=False
                
    print(return_val)
        


def main():
    """
    The main function that processes the command-line arguments to convert either 
    from Braille to English or English to Braille.
    """
    if len(sys.argv) < 2:
        print("Please Add a word in Braile or English")
        return
    
    args = sys.argv[1:]
    
    for arg in args:
        # If the argument matches only Braille symbols ('.' and 'O'), assume it's Braille
        if re.match(r'^[\.O]+$', arg):
            braile_to_english(arg)
        else:
            # Otherwise, assume it's English
            english_to_braile(arg)
    

if __name__ == "__main__":
    main()
        
