## Braille Translator
# In this coding challenge you will create a terminal / command-line application that 
#  can translate Braille to English and vice versa.  
 
# The string to translate will be passed into your application as an argument at runtime.  
# Your application must be smart enough to determine if the string given to it is either Braille or English and automatically convert it to the appropriate opposite.  
 
# For the purposes of this challenge Braille must be displayed as O and . where O  
# represents a raised dot. You must include the entire English alphabet, the ability 
#  to capitalize letters, add spaces, and the numbers 0 through 9 as well.  
 
# After conversion, output the translated string--and nothing else--to the terminal.  
 
## Technical Requirements 
# - Translator 
#   - Given arguments passed into the program at runtime, determine if the given string should be translated to English or Braille. 
#   - For Braille, each character is stored as a series of O (the letter O) or . (a period). 
#   - Store Braille symbols as a 6 character string reading left to right, line by line, starting at the top left. See examples below. 
#   - When a Braille capital follows symbol is read, assume only the next symbol should be capitalized.  
#   - When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol. 
# - Braille Alphabet 
#   - Letters a through z 
#     - The ability to capitalize letters 
#   - Numbers 0 through 9 
#   - The ability to include spaces ie: multiple words 
 
# ## Examples 
# - Launching your application with English or Braille: 
#   - ruby translator.rb Hello world 
#   - ruby translator.rb .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.. 
# --- 
# - Input: Hello world 
# - Output: .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.. 
# --- 
# - Input: 42 
# - Output: .O.OOOOO.O..O.O... 
# --- 
# - Input: .....OO.....O.O...OO...........O.OOOO.....O.O...OO.... 
# - Output: Abc 123 
 
import sys 
 
# Braille to English dictionary 
braille_dict = { 
    # Alphabets 
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO",  
    # Numbers 
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", 
    #Structure 
    "capital_next": ".....O", "decimal_next": ".O...O", "number_next": ".O.OOO", 
    # Symbols 
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",  
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", 
    "(": "O.O..O", ")": ".O.OO.", "space": "......", 
} 
 
# English to Braille dictionary 
english_dict = {v: k for k, v in braille_dict.items()} 
 
def translate_braille_to_english(braille): 
    english = "" 
    for i in range(0, len(braille), 6): 
        braille_char = braille[i:i+6] 
        if braille_char == braille_dict["capital_next"]: 
            english += braille_dict["capital_next"] 
            continue 
        if braille_char == braille_dict["number_next"]: 
            english += braille_dict["number_next"] 
            continue 
        if braille_char == braille_dict["space"]: 
            english += " " 
            continue 
        english += english_dict[braille_char] 
    return english 

def translate_english_to_braille(english):
    braille = ""
    for char in english:
        if char.isupper():
            braille += braille_dict["capital_next"]
            braille += braille_dict[char.lower()]
            continue
        if char.isdigit():
            braille += braille_dict["number_next"]
            braille += braille_dict[char]
            continue
        if char == " ":
            braille += braille_dict["space"]
            continue
        braille += braille_dict[char]
    return braille


def main():
    # Check if the input is Braille or English
    input_text = " ".join(sys.argv[1:])
    # Check if the input is Braille or English
    if "O" in input_text or input_text.startswith("."):
        print(translate_braille_to_english(input_text))
    else:
        print(translate_english_to_braille(input_text))
 
if __name__ == "__main__": 
    main()
