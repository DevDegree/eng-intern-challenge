braille_dict = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
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
    " ": "......",
}

english_dict = {
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
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " "
}

# constants
capital_follows = ".....O"
decimal_follows = ".O...O"
number_follows = ".O.OOO"

def english_to_braille(english):
    braille_output = ""
    is_number = False
    for char in english:
        if char.isdigit() or char == '>': #numerical characters and '>'
            if not is_number:
                braille_output += number_follows
                is_number = True
            if char == '>':
                braille_output += braille_dict[char]
            else:
                braille_output += braille_dict[char]
        else:
            if is_number:
                is_number = False
            
            if char.isalpha(): #alphabetical characters
                if char.isupper():
                    braille_output += capital_follows
                braille_output += braille_dict[char.lower()]
            else: #symbols
                braille_output += braille_dict[char]

    return braille_output

def braille_to_english(braille):
    # print(f"Input Braille: {braille}")
    english_output = ""
    i = 0
    is_number = False
    capitalize_next = False
    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == number_follows:
            is_number = True
            #print("Number mode")
            i += 6
            continue
        
        if symbol == capital_follows:
            capitalize_next = True
            #print("Capital mode")
            i += 6
            continue
        
        if symbol in english_dict:
            char = english_dict[symbol]
            #print(f"Translated to: {char}")
            if is_number:
                if char in "abcdefghij>":
                    if char == 'j':
                        char = '0'
                    elif char == '>':
                        char = '>'
                    else:
                        char = str(ord(char) - ord('a') + 1)
                elif char == " ":
                    is_number = False
                else:
                    is_number = False
            elif capitalize_next:
                char = char.upper()
                capitalize_next = False
                # print(f"Capitalized: {char}")
            
            english_output += char
        
        i += 6
    
    #print(f"Final output: {english_output}")
    return english_output

def detect_translation_type(text):
    if all(char in '.O' for char in text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

user_input = input("")
print(detect_translation_type(user_input))
