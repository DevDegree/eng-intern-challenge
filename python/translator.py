import sys

def reverse_dict(d):
    return {v: k for k, v in d.items()}

def braille_to_string(braille_input, braille_reverse_dict, digit_reverse_dict, capital_indicator, number_indicator):
    # Split the input into chunks of 6 characters (Braille cells)
    chunks = [braille_input[i:i+6] for i in range(0, len(braille_input), 6)]
    
    translated_text = ""
    capitalize_next = False
    number_mode = False
    
    for chunk in chunks:
        if chunk == capital_indicator:
            capitalize_next = True  # Set flag to capitalize next letter
            continue  # Move to the next Braille cell
        elif chunk == number_indicator:
            number_mode = True  # Set flag to number mode
            continue  # Move to the next Braille cell
        elif chunk == '......':  # Reset modes on space
            number_mode = False
            capitalize_next = False
            translated_text += ' '
            continue
        
        if number_mode and chunk in digit_reverse_dict:
            translated_text += digit_reverse_dict[chunk]
        elif chunk in braille_reverse_dict:
            char = braille_reverse_dict[chunk]
            # Apply capitalization if the flag is set
            if capitalize_next:
                translated_text += char.upper()
                capitalize_next = False  # Reset flag after use
            else:
                translated_text += char
        else:
            translated_text += '?'  # Unknown pattern placeholder

    return translated_text

def find_braille(value, braille_dictionary,digt_braille, capital_indicator, number_indicator):
    result = []
    final_str = ''
    isdigit = False
    iscapital = False
    #print(number_indicator)
    #print(value)
    
    for char in value:
        if char.isupper() and iscapital == False:
            #print(number_indicator)
            final_str += capital_indicator
            iscapital = True
        
        elif char.isdigit() and isdigit == False:
            final_str += number_indicator
            isdigit = True
        
        if char.isdigit(): 
            char = char.lower()
            final_str += digt_braille[char]
        
        else:
            char = char.lower()
            final_str += braille_dictionary[char]
    
    return final_str
            
            
if __name__ == '__main__':
    braille_dictionary = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
        "y": "OO.OOO", "z": "O..OOO",' ': "......",
        ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":" : "..O.O.", "-": "....OO", "/": ".O..O.", "<" : ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO."
    }
    
    digit_braille = {
        "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
        "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", 
        "9": ".OO...", "0": ".OO.."}
    
    
    # Special indicators
    capital_indicator = '.....O'
    number_indicator = '.O.OOO'
    
    inputs = sys.argv[1:]
    output = ""
    i = 1
    for user_input in inputs:            
        flag_str = False
        flag_braille = False
        for char in user_input[:6]:
            if char != 'O' and char != '.':
                flag_str = True
            else:
                flag_braille = True
        
        if flag_str:
            output += find_braille(user_input, braille_dictionary, digit_braille, capital_indicator, number_indicator)
            if i < len(inputs):
                i += 1
                output += braille_dictionary[' ']
        else:
            # Reverse the dictionaries
            braille_reverse_dict = reverse_dict(braille_dictionary)
            digit_reverse_dict = reverse_dict(digit_braille)
            output += braille_to_string(user_input, braille_reverse_dict, digit_reverse_dict, capital_indicator, number_indicator)
            if i < len(inputs):
                i += 1
                output += ' '
    
    print(output)