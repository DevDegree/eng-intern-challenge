import sys

# Read in system variables passed that have the needed text
originalText = ' '.join(sys.argv[1:])

# BRAILLE TO ENGLISH
# A dictionary for looking up what braille characters mean in alphabet and special characters
braille_to_english_dict = {
    # LETTERS
    'O.....': 'a',
    'O.O...': 'b',
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
    # SPECIAL CHARACTERS
    '......': ' ',
    '.....O': 0, # CAPITAL FOLLOWS
    '.O.OOO': 1 # NUMBER FOLLOWS
}
# A dictionary to look up what braille characters mean for numbers
braille_to_number_dict = {
    # NUMBERS
    'O.....': '1',
    'O.O...': '2',
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

# ENGLISH TO BRAILLE
english_to_braille_dict = {
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
    " ": "......",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

# Print without spaces
def print_no_line(text):
    print(text, end='')

def english_to_braille(original_text):
    index = 0
    while index < len(original_text):
        # If current character is lowercase, number or space
        if original_text[index] in english_to_braille_dict:
            if original_text[index].isdigit():
                print_no_line('.O.OOO') # NUMBER FOLLOWS
                # Loop and addd numbers until a space is found
                while original_text[index] != ' ' and index < len(original_text):
                    print_no_line(english_to_braille_dict[original_text[index]])
                    index += 1
                continue
            else:
                print_no_line(english_to_braille_dict[original_text[index]])
        else:
            print_no_line('.....O')  # CAPITAL FOLLOWS
            print_no_line(english_to_braille_dict[original_text[index].lower()])
        index += 1

def braille_to_english(original_text):
    index = 0
    # Go through 6 characters at a time instead of 1 because 1 regular character is 6 braille
    while index + 5 < len(original_text):
        bcharacter = original_text[index:index + 6]
        character = braille_to_english_dict[bcharacter]
        if character == 0:
            # CAPITAL FOLLOWS
            index += 6
            # Read in only the next character if there is one
            bcharacter = original_text[index:index + 6]
            if bcharacter in braille_to_english_dict:
                print_no_line(braille_to_english_dict[bcharacter].upper())
            else:
                print_no_line(bcharacter)
        elif character == 1:
            # NUMBERS FOLLOW
            index += 6
            # Read in characters until the end is reached or a space is found to signify no more numbers
            while index + 5 < len(original_text):
                bcharacter = original_text[index:index + 6]
                if bcharacter in braille_to_number_dict:
                    print_no_line(braille_to_number_dict[bcharacter])
                else:
                    print_no_line(' ')
                    break
                index += 6
        else:
            # Regular character
            print_no_line(character)
        index += 6

original_set = set(originalText)
# Check if reading braille or english
if len(original_set)<=2 and len(originalText)%6==0 and '.' in original_set:
    braille_to_english(originalText)
else:
    english_to_braille(originalText)
