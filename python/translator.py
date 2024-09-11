#Thought Process while coding:
#For the Braille Translator, a mapping needs to be made for the alphabet and braille which when reversed can be used when braille is
#inputted. The mapping will also need to include the follows symbols for capitalization, numbers, spaces, and the decimal point.
#To determine if the input is braille or english, we can check if all that the input is O/. and is divisible by 6.
#To handle the part that says assume all characters that follow a number will be number, I will use a toggle called number mode till a
# space is encountered or input ends 

#While coding I realised that 1-0 and a-j have identical symbols, which is why Hello world when reverse input was giving 85ll> w>rl4
#I decided after a while, the easiest solution would be to just create 2 separate mappings for number and alphabet
#I also realised > and o have the same character and was bamboozled for a while until I realised they did not ask us to factor special
# characters. So all the special characters were immediately thrown out the window. "." looked at me with puppy eyes and i decided it 
# would stay as I needed a decimal point for numbers. (you're on thin ice ".")

# I started writing the individual functions for english to braille and realised for the "follows" characters we need to skip 6 characters
# I also coded the number mode getting reset after space. I realised there should also be a failsafe system and just decided to add a
# ? when it was unintelligible.

#For Braille to English, I realised I needed to skip 12 characters for the capitalization after converting the character to english.
#(I'm imagining someone reading braille and saying all the follows out loud like a cat jumped over an i<characterfollows>Phone)
#^ I just realised to avoid that happening since these are indicators and don't need to be converted, i will exclude them from the
#reverse dictionary.

#After a lot of thought I added a failsafe for the input incase nothing is provided.


#IT WORKS, PRAISE BE TO THE CODING LORDS

#said it too early as always, the spaces are not preserved unless the whole input is in quotes or the spaces are in quotes. I have a 
#solution to fix that but it won't work for python 3.8 so I will be sticking with this.


# To Do List before coding:
# Create a dictionary for the Braille alphabet
# Create a function to convert English to Braille
# Create a function to convert Braille to English
# Create a function to handle the input and output
# Create a function to handle the capitalization and numbers
# Create a function to handle the spaces
# Create a function to handle the new lines
# Create a function to handle the tabs
# Create a function to handle the punctuation (update: not needed anymore)

import sys

#note in this code I will be ignoring the special characters except the decimal place because > shares the same braille as o and
#the requirements do not specify anything about special characters

# Mapping for the alphabet and follow symbols + decimal symbol
#note I will only be using "." for decimal numbers
braille_dict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.",
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", " ": "......",
    "cap": ".....O", "num": ".O.OOO", "dec": ".O...O", ".": "..OO.O"  # "." is treated as decimal point
}

# Separate dictionary for numbers in Braille which I will use in number mode
braille_num_dict = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", 
    "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Reverse dictionary for combined alphabet (removed the indicators as we dont want it to be translated as capHello)
letter_dict = {v: k for k, v in braille_dict.items() if k not in ["num", "cap", " "]}

# Reverse dictionary for number mapping
num_dict = {v: k for k, v in braille_num_dict.items()}

# Function to determine if input is Braille or English
def is_braille(input_string):
    return all(c in "O." for c in input_string) and len(input_string) % 6 == 0

# Function to convert Braille to English
def braille_to_english(braille):
    english_text = ""
    i = 0
    number_mode = False # Initially not in number mode
    
    while i < len(braille):
        char_braille = braille[i:i+6]
        
        if char_braille == braille_dict["cap"]:
            # Handle capitalization, so look at the next 6 characters for the letter
            next_char_braille = braille[i+6:i+12]
            if next_char_braille in letter_dict:
                english_text += letter_dict[next_char_braille].upper()  # Capitalize the next character
            i += 12  # Move the index forward by 12 characters (6 for "cap" and 6 for the letter)
        elif char_braille == braille_dict["num"]:
            # Switch to number mode
            number_mode = True
            i += 6
        elif char_braille == braille_dict[" "]:
            # Handle space and reset number mode
            english_text += " "
            number_mode = False
            i += 6
        elif number_mode:
            # Handle numbers in number mode
            if char_braille == braille_dict["dec"]:
                next_char_braille = braille[i+6:i+12]
                if next_char_braille == braille_dict["."]:
                    english_text += "."  # Decimal point in number mode
                    i += 12  # Move past both "dec" and "."
            elif char_braille in num_dict:
                english_text += num_dict[char_braille]
                i += 6
            else:
                english_text += "?"
                i += 6
        else:
            # Handle letters in character mode
            if char_braille in letter_dict:
                english_text += letter_dict[char_braille]
            i += 6

    return english_text

# Function to convert English to Braille
def english_to_braille(text):
    braille_text = ""
    number_mode = False  # Initially not in number mode
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_text += braille_dict["num"]  # Switch to number mode
                number_mode = True
            braille_text += braille_num_dict[char]  # Convert number to Braille
        elif char.isalpha():
            if char.isupper():
                braille_text += braille_dict["cap"]  # Add "capital follows" symbol
                char = char.lower()  # Convert to lowercase for Braille translation
            braille_text += braille_dict[char]  # Convert letter to Braille
            number_mode = False  # Reset number mode when encountering a letter
        elif char == " ":
            braille_text += braille_dict[" "]  # Add space
            number_mode = False  # Reset number mode after space
        elif char == ".":
            braille_text += braille_dict["dec"]  # Add "decimal follows" symbol
            braille_text += braille_dict["."]  # Add actual decimal point symbol in Braille
            number_mode = True  # Stay in number mode for decimal
        else:
            braille_text += "?"  # Handle unknown characters

    return braille_text

# Main function to handle input and output
def main():
    #case to handle no input
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    input_string = ' '.join(sys.argv[1:])
    
    if is_braille(input_string):
        # Convert Braille to English
        print(braille_to_english(input_string))
    else:
        # Convert English to Braille
        print(english_to_braille(input_string))
        
if __name__ == "__main__":
    main()

