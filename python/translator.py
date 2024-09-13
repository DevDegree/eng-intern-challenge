import sys

"""
This class's purpose is to convert between English and Braille. For English to Braille, this only supports the alphabet, number (0 - 9), and spaces. 
For Braille, the input must be divisble by 6 and contain only 'O' and '.'


There are 3 functions within this class
    get_key_from_values
    translate_text_to_braille
    translate_braille_to_text

We also have a dictionary defined at the constructor level which holds the braille (key) and alphanumeric equivalent (values). There are also
3 other key/value pair which are meant for special circumstances (is it a number? is it a captial letter?, etc.)  
"""
class Translator:
    def __init__(self) -> None:  
        self.BRAILLE_AND_CHARACTERS_DICTIONARY = {
            "O....." : ["a", "A", "1"],
            "O.O..." : ["b", "B", "2"],
            "OO...." : ["c", "C", "3"],
            "OO.O.." : ["d", "D", "4"],
            "O..O.." : ["e", "E", "5"],
            "OOO..." : ["f", "F", "6"],
            "OOOO.." : ["g", "G", "7"],
            "O.OO.." : ["h", "H", "8"],
            ".OO..." : ["i", "I", "9"],
            ".OOO.." : ["j", "J", "0"],
            "O...O." : ["k", "K"],
            "O.O.O." : ["l", "L"],
            "OO..O." : ["m", "M"],
            "OO.OO." : ["n", "N"],
            "O..OO." : ["o", "O"],
            "OOO.O." : ["p", "P"],
            "OOOOO." : ["q", "Q"],
            "O.OOO." : ["r", "R"],
            ".OO.O." : ["s", "S"],
            ".OOOO." : ["t", "T"],
            "O...OO" : ["u", "U"],
            "O.O.OO" : ["v", "V"],
            ".OOO.O" : ["w", "W"],
            "OO..OO" : ["x", "X"],
            "OO.OOO" : ["y", "Y"],
            "O..OOO" : ["z", "Z"],

            "captial" : ".....O",
            "number" : ".O.OOO",
            " " : "......"
        }

    def get_keys_from_value(self, char_value) -> str:
        """
        Takes in a character value and matches that value with the corresponding key from the BRAILLE_AND_CHARACTERS_DICTIONARY
        returns the first key value from the list 
        
        NOTE:
            The way the dictionary is set up should mean that whenever this function is called only ONE item in the list should be present 
        """
        matching_keys = [key for key, values in self.BRAILLE_AND_CHARACTERS_DICTIONARY.items() if char_value in values]
        return matching_keys[0]

    def translate_text_to_braille(self, input_str: str) -> str:
        """
        Takes the text string and converts it to Braille format. Returns a string of said format.
        (For more information on the Braille system, https://en.wikipedia.org/wiki/Braille)
        """
        output_str = ""
        isNumber = False
        
        for i in range(0, len(input_str)):
            character = input_str[i]

            if(character == " "):
                output_str += self.BRAILLE_AND_CHARACTERS_DICTIONARY[" "]
                if(isNumber): # If current character is a 'space' and isNumber is true, isNumber becomes false (next character could or could not be a number).
                    isNumber = False
                continue

            if(character.isupper()):# Checks to see if the current character is an uppercase 
                output_str += self.BRAILLE_AND_CHARACTERS_DICTIONARY["captial"]

            if(character.isnumeric() and isNumber == False): # isNumber is set one time if number is encountered. The follow characters are assumed to be numbers.
                isNumber = True
                output_str += self.BRAILLE_AND_CHARACTERS_DICTIONARY["number"]

            output_str += self.get_keys_from_value(character)

        return output_str

    def translate_braille_to_text(self, input_str: str) -> str: 
        """
        Takes Braille format and converts it to the English language. returns the English word/phrase as a string.
        """
        output_str = ""
        isNumber = False
        isCaptial = False
        type = 0 # "type" corresponds to the array position in BRAILLE_AND_CHARACTERS_DICTIONARY. the array is ordered in a particular way: lowercase, uppercase, and number (if any)

        # For loop, converts every 6 characters to a character
        for i in range(0, len(input_str), 6):
            substring = input_str[i:i+6]

            if substring == self.BRAILLE_AND_CHARACTERS_DICTIONARY["captial"]:
                isCaptial = True
                type = 1 # sets the dictionary 'get' to upper case letters
                continue 

            if substring == self.BRAILLE_AND_CHARACTERS_DICTIONARY["number"]:
                isNumber = True 
                type = 2 # sets the dictionary 'get' to numbers
                continue

            if substring == self.BRAILLE_AND_CHARACTERS_DICTIONARY[" "]:
                output_str += " "
                if(isNumber):
                    isNumber = False 
                    type = 0 # sets the dictionary 'get' to lower case letters
                continue
            
            if(isCaptial):
                output_str += self.BRAILLE_AND_CHARACTERS_DICTIONARY.get(substring)[type]
                isCaptial = False
                type = 0 # sets the dictionary 'get' to lower case letters
                continue
            
            output_str += self.BRAILLE_AND_CHARACTERS_DICTIONARY.get(substring)[type]

        return output_str

def main():
    msg = "" 
    translator = Translator()
    inputs = sys.argv[1:]
    for i, input_str in enumerate(inputs):

        # we check if it is divisible by 6 and if it contains only 2 characters, 'O' and '.'
        if(len(input_str) % 6 == 0 and set(input_str).issubset({'O', '.'}) and all(c in {'O', '.'} for c in input_str)):
            msg += translator.translate_braille_to_text(input_str)
        else:
            if(len(input_str) % 6 != 0 and set(input_str).issubset({'O', '.'}) and all(c in {'O', '.'} for c in input_str)): # error message for non-Braille input. Assumes input with only O and . is Braille
                msg = "Error, it looks like you tried to enter Braille.\nPlease make sure the message contains only 'O' and '.' and is the right length. "
                break

            if any(not char.isalnum() and char != ' ' for char in input_str): # handles any other input. 
                msg = "Error, inputted string couldn't be converted to Braille.\nPlease make sure the string only contains the English alphabet (upper and or lower),  numbers(0-9), and spaces."
                break

            msg += translator.translate_text_to_braille(input_str)
            if i < len(inputs) - 1: # handles the case where you input multiple strings at runtime, will have spaces between them in Braille. Only does this if more than 1 element and not on the last element
                msg += translator.translate_text_to_braille(" ")

    print(msg) 


if __name__ == "__main__":
    main()
