import sys

braille_to_english = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c", 
    "OO.O..": "d", 
    "O..O..": "e",
    "OOO...": "f", 
    "OOOO..": "g", 
    "O.OO..": "h", 
    ".OO...": "i", 
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",
    ".....O": "CAPITAL",            # capital follows symbol
    ".O.OOO": "NUMBER"              # number follows symbol
}

braille_numbers = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3", 
    "OO.O..": "4", 
    "O..O..": "5",
    "OOO...": "6", 
    "OOOO..": "7", 
    "O.OO..": "8", 
    ".OO...": "9", 
    ".OOO..": "0"
}



numbers_to_braille = {v: k for k, v in braille_numbers.items()} # Reverse mapping for numbers

english_to_braille = {v: k for k, v in braille_to_english.items()} # Reverse mapping for letters

def main():

    input_string = ' '.join(sys.argv[1:]) #getting the input string
    first_six = input_string[:6] #getting the first six characters
    is_Braile = True    
    if all(char in ['O', '.'] for char in first_six): #checking if the first six characters are in the braille format, if yes then it is a braille
        is_Braile = True
    else:
        is_Braile = False
    
    if is_Braile == True: #if it is a braille then convert it to english

        segments = [input_string[i:i+6] for i in range(0, len(input_string), 6)]  # Split the input string into segments of 6 characters each
        result = []
        capitalize_next = False
        number_mode = False
        
        for segment in segments:
            if segment == ".....O":  # Capital follows symbol
                capitalize_next = True
                continue
            elif segment == ".O.OOO":  # Number follows symbol
                number_mode = True
                continue
            elif segment == "......":  # Space resets number mode
                result.append(" ")
                number_mode = False
                continue
            
            if number_mode:
                # If in number mode, use the number mapping
                result.append(braille_numbers.get(segment, "?"))
            else:
                # Otherwise, use the letter mapping
                letter = braille_to_english.get(segment, "?")
                if capitalize_next:
                    letter = letter.upper()  # Capitalize the next letter
                    capitalize_next = False
                result.append(letter)
        print("".join(result))
    else:
        # Convert from English to Braille
        braille_translation = []
        number_mode = False

        for char in input_string:
            if char.isupper():
                braille_translation.append(".....O")  # Capital follows symbol
                braille_translation.append(english_to_braille.get(char.lower(), "......"))
                number_mode = False
            elif char.isdigit():
                if not number_mode:  # Only append number follows symbol if not already in number mode
                    braille_translation.append(".O.OOO")  # Number follows symbol
                    number_mode = True
                braille_translation.append(numbers_to_braille.get(char, "......"))
            elif char == " ":
                braille_translation.append("......")  # Space
                number_mode = False  # Reset number mode on space
            else:
                braille_translation.append(english_to_braille.get(char, "......"))
                number_mode = False  # Reset number mode on letter

        print(''.join(braille_translation))






if __name__ == "__main__":
    main()