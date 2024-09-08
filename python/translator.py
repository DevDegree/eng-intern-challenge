import sys


# some constant flags
CAPITAL_FOLLOWS = "caps"
NUMBER_FOLLOWS = "num"
WHITESPACE = " "

# let's define a dictionary for the braille alphabet
# need one for both numbers and letters

braille_letters = {
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

# then some special cases
braille_special = {
    ".....O": CAPITAL_FOLLOWS,
    ".O.OOO": NUMBER_FOLLOWS,
    "......": WHITESPACE
}

# now lets define the functions needed
# we need 3 functions:
# is_braille: checks if input string is braille or english, then we can decide which translation function to run
# braille_to_english: translates input string to english
# english_to_braille: translates input string to braille

# is_braille(message) takes message and dtermines if it is braille or english
# return true for braille, false
# a braille message:
# - only contains '.' and 'O'
# - length divisible by 6
def is_braille(message):
    for c in message:
        if c != '.' and c != 'O':
            return False
    return len(message) % 6 == 0

# braille_to_english(message) translates message in braille to english
# take string 6 letters at a time, and translate
def braille_to_english(message):
    translated_message = ""
    caps = False
    read_dict = braille_letters
    special_dict = braille_special
    index = 0
    next_index = 0
    while next_index < len(message):
        index = next_index
        next_index += 6
        letter = message[index:index+6]
        if braille_special.get(letter) != None:
            if braille_special[letter] == CAPITAL_FOLLOWS:
                caps = True
            elif braille_special[letter] == NUMBER_FOLLOWS:
                read_dict = braille_numbers
            elif braille_special[letter] == WHITESPACE:
                translated_message += " "
                caps = False
                read_dict = braille_letters
        else:
            new_letter = read_dict[letter]
            if caps:
                new_letter = new_letter.capitalize()
            translated_message += new_letter
            caps = False
    
    return translated_message

# english_to_braille(message) translates message in english to braille
# note: since we pass in through arguments, message does not contain whitespace. we add whitespace between calls of english_to_braille
def english_to_braille(message, add_whitespace=False):
    translated_message = ""
    special_dict = {english: braille for braille, english in braille_special.items()}
    read_dict = {english: braille for braille, english in braille_letters.items()}
    if message.isdigit():
        translated_message += special_dict[NUMBER_FOLLOWS]
        read_dict = {english: braille for braille, english in braille_numbers.items()}
    for c in message:
        if c.isupper():
            translated_message += special_dict[CAPITAL_FOLLOWS]
            c = c.lower()
        translated_message += read_dict[c]
    if add_whitespace:
        translated_message += special_dict[WHITESPACE]
    return translated_message

if __name__ == '__main__':
    messages = sys.argv[1:]
    if len(messages) > 0:
        output = ""
        if is_braille(messages[0]):
            output = braille_to_english(messages[0])
        else:
            for message in messages:
                output += english_to_braille(message, True)
            # trim the extra whitespace at the end
            output = output[:-6]
        print(output)