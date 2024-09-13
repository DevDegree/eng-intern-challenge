# This program translates the input to Braille or alphanumeric alphabet.

import sys
# Variable declaration
output=""
nums_lock = False
caps_lock = False
dec_lock = False

#Function to detect if the input is Braille or alphanumeric
def is_braille(value):
    for char in value:
        if (char != "O") & (char != "."):
            return False
    return True

# Dictionary of the Braille alphabet without numbers and special caracters
braille_letters_signs = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}
# Dictionary of numbers of the Braille alphabet
braille_numbers={
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ".": "..OO.O"
}
# Dictionary of specials of the Braille alphabet
braille_specials={
    "CAP": ".....O",
    "DEC": ".O...O",
    "NUM": ".O.OOO"
}

#Prompt
entered_value = sys.argv[1:]
entered_value = ' '.join(entered_value)
# Condition if user wants to translate from Braille
if is_braille(entered_value):
    split = [entered_value[x:x+6] for x in range(0,len(entered_value),6)] # Split the full string into 6-character segments
    for char in split:
        if char == braille_specials["CAP"]:
            caps_lock = True
        elif char == braille_specials["DEC"]:
            dec_lock = True
        elif char == braille_specials["NUM"]:
            nums_lock = True
        elif caps_lock:
            for key, value in braille_letters_signs.items():
                if value==char:
                    output += key
                    caps_lock = False
                    break
        elif dec_lock:
            for key, value in braille_numbers.items():
                if value==char:
                    output += key
                elif char == braille_letters_signs[" "]:
                    output += " "
                    dec_lock = False
                    break
        elif nums_lock:
            for key, value in braille_numbers.items():
                if value==char:
                    output += key
                elif char == braille_letters_signs[" "]:
                    output += " "
                    nums_lock = False
                    break
        else:
            for key, value in braille_letters_signs.items():
                if value==char:
                    output += key.lower()
                    break

# condition if user wants to translate to Braille
else:
    for char in entered_value: # loops over each character
        if char.isnumeric():
            if not nums_lock:
                output += braille_specials["NUM"]
                nums_lock = True # flag to know the following characters will be numbers
            output += braille_numbers[char]
        elif char.isdecimal():
            output += braille_specials["DEC"]
            output += braille_numbers[char]
        elif char.isupper():
            output += braille_specials["CAP"]
            output += braille_letters_signs[char]

        else :
            output += braille_letters_signs[char.upper()]
            if char == " ":
                nums_lock = False
print(output)
