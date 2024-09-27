import sys

# Check if there is at least one input string provided
if len(sys.argv) <= 1:
    print("Usage: python translator.py <string>")
    sys.exit(1)

# Determining input type: Braille or English

input_string = ' '.join(sys.argv[1:])
if all(char in 'O.' for char in input_string):
    input_type = "Braille"
else:
    input_type = "English"


############ Braille-To-English section ################
def braille_to_English(input_string):
    # Using dictionary to map Braille characters to English
    braille_dict = {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
        "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
        "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
        "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
        "O..OOO": "z", ".....O": "capital", ".O.OOO": "number", "......": " ",
        "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", 
        "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">", 
        "O.O..O": "(", ".O.OO.": ")"}

    braille_Num = {
        "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
        "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"}

    while input_string:
        # Join the first 6 characters into one string
        braille_char = ''.join(input_string[:6])
        input_string = input_string[6:]

        # Check if the character is a special indicator (capital or number)
        if braille_char in braille_dict:
            value = braille_dict[braille_char]

            if value == "capital":
                braille_char = ''.join(input_string[:6])
                input_string = input_string[6:]
                if braille_char in braille_dict:
                    print(braille_dict[braille_char].upper(), end='')

            elif value == "number":
                # Translate the following characters as numbers
                while input_string:
                    braille_char = ''.join(input_string[:6])
                    input_string = input_string[6:]
                    if braille_char == "......":
                        print(" ", end='')
                        break
                    elif braille_char in braille_Num:
                        print(braille_Num[braille_char], end='')

            else:
                # Print the corresponding English characters
                print(value, end='')

# if input is Braille call the function braille_to_English()
if input_type == "Braille":
    braille_to_English(input_string)

############ English-To-Braille section ################

# Used the same approach as in braille but in reverse order
def english_to_Braille(input_string):
    # Using dictionary to map English characters to Braille
    english_dict = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
        "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
        "z": "O..OOO", " ": "......", ".":"..OO.O",  ",":"..O...",
        "?":"..O.OO", "!":"..OOO.", ":":"..OO..", ";":"..O.O.",
        "-":"....OO", "/":".O..O.", "<":".OO..O", ">":"O..OO.",
        "(":"O.O..O", ")":".O.OO."
        }

    english_Num = {
        "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
        "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."}

    # Track state for numbers
    number_mode = False

    # Iterate through each character in the input string
    for char in input_string:
        if char.isupper():
            # Print the capitalization indicator only once before a capital letter
            print(".....O", end='')
            
            braille_char = english_dict[char.lower()]
            print(braille_char, end='')

        elif char.isdigit():
            if not number_mode:
                # Print the number indicator if switching to number mode
                print(".O.OOO", end='')
                number_mode = True
            
            braille_char = english_Num[char]
            print(braille_char, end='')

        elif char == " ":
            # Reset number mode on encountering a space
            number_mode = False
            print("......", end='')

        else:
            
            number_mode = False
            # Convert the lowercase letter or space to Braille and print it
            braille_char = english_dict[char]
            print(braille_char, end='')


# if input is English call the function english_to_Braille()
if input_type == "English":
    english_to_Braille(input_string)
