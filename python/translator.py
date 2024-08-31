'''
Braille Translator

A terminal / command-line application that can translate Braille to English and vice versa

How to run:
python3 translator.py <input>
e.g. 
python3 translator.py Hello world
python3 translator.py "Hello" "world"
python3 translator.py "Hello world"
python3 translator.py .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
python3 translator.py ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."

Output:
only the translated Braile or English string
e.g. 
.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
Hello world

Exceptional output:
no input -> "No input was given. Use: python3 translator.py <input>"
invalid Braille -> "Invalid input. Invalid Braille character: <invalid Braille character>"
invalid English -> "Invalid input. English text can only include numbers, spaces, and English characters"

Author:
Fengting Tang
fengtingtang1065@gmail.com
'''

import sys

# Braille to English dictionary
braille_dict = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "capital", ".O.OOO": "number", "......": " "
}

# English to Braille dictionary
english_dict = {v: k for k, v in braille_dict.items()}

# char to number dictionary
char_to_number = {
    "a": '1', "b": '2', "c": '3', "d": '4', "e": '5',
    "f": '6', "g": '7', "h": '8', "i": '9', "j": '0'
}

# number to char dictionary
number_to_char = {v: k for k, v in char_to_number.items()}

# Translate Braille to English
def braille_to_english(braille_str):
    translated_str = ""
    capitalize_next = False
    is_number = False
    
    for i in range(0, len(braille_str), 6): # Split the Braille string into chunks of 6 characters
        braille_char = braille_str[i:i+6]
        if braille_char in braille_dict:
            curr_english_char = braille_dict[braille_char]
            if curr_english_char == "capital":
                capitalize_next = True
            elif curr_english_char == "number":
                is_number = True # always effective until a space is encountered
            else:
                if curr_english_char == " ":
                    is_number = False # numbers end with a space
                elif capitalize_next:
                    capitalize_next = False # capital char is only effective for one char
                    curr_english_char = curr_english_char.upper()
                elif is_number:
                    curr_english_char = char_to_number[curr_english_char]

                translated_str += curr_english_char
        else:
            return "\nInvalid input:\nInvalid Braille character: " + braille_char
        
    return translated_str

# Translate English to Braille
def english_to_braille(english_str):
    translated_str = ""
    number_encountered = False

    for char in english_str:
        if char.lower() in english_dict:
            if char == " ":
                number_encountered = False # another number char needed for later numbers
            if char.isupper():
                translated_str += english_dict["capital"] # add capital char before every capital letter
                char = char.lower() # no capital char in the dictionary
            translated_str += english_dict[char]
        elif char in number_to_char:
            if not number_encountered: # if this is the first of a consecutive numbers
                translated_str += english_dict["number"]
                number_encountered = True # then the rest are not the first of a consecutive numbers
            translated_str += english_dict[number_to_char[char]]
        else:
            return "\nInvalid input\nEnglish text can only include numbers, spaces, and English characters"

    return translated_str

# Translate Braille or English
def translate(input_str):
    if len(input_str) >= 6 and '.' in input_str[:6]: # Check if the input is Braille
        return braille_to_english(input_str)
    else:
        return english_to_braille(input_str)

def main():
    args = sys.argv

    if len(args) < 2:
        print("\nNo input was given\nUse: python3 translator.py <input>")
    else:
        input_str = " ".join(args[1:]) # Join all the arguments into a single string
        output_str = translate(input_str)
        print(output_str)

if __name__ == '__main__':
    main()