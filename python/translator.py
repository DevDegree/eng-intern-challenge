import sys 
from translation_maps import english_to_braille, braille_to_english, braille_to_english_numbers

#Get input string
user_input = " ".join(sys.argv[1:])

input_language = "English"

if set(user_input) == {"O", "."}:
    input_language = "Braille"

output_string = ""
number_mode = False 

#Translating English to Braille
if input_language == "English":

    for char in user_input:
        #Numbers
        if char.isdigit():
            if number_mode:
                output_string += english_to_braille[char]
            else:
                output_string += english_to_braille["number"] + english_to_braille[char]
                number_mode = True
        #Lowercase letters and spaces
        elif char in english_to_braille:
            if char == " ":
                number_mode = False
            output_string += english_to_braille[char]

        #Capital letters
        elif char.lower() in english_to_braille:
            output_string += english_to_braille["capital"] + english_to_braille[char.lower()]

#Braille to English
else:
    capital_mode = False
    for i in range(0, len(user_input), 6):
        #Loop through each 6 characters
        char = user_input[i: i + 6]

        #Number follows
        if char == ".O.OOO":
            number_mode = True
        #Capital follows
        elif char == ".....O":
            capital_mode = True
        #Numbers
        elif number_mode:
            output_string += braille_to_english_numbers[char]
        #Capital letters
        elif capital_mode:
            output_string += braille_to_english[char].upper()
            capital_mode = False
        #Space
        elif char == "......": 
            output_string += " "
            number_mode = False
        #Lowercase letters
        elif char in braille_to_english:
            output_string += braille_to_english[char]

print(output_string)