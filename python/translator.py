import sys

digit_to_braille = {
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....", 
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...", 
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO.."
}

letter_to_braille = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....", 
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...", 
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.", 
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.", 
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O", 
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
}

braille_to_english_letter = {
    "O.....": 'a',
    "O.O...": 'b',
    "OO....": 'c', 
    "OO.O..": 'd',
    "O..O..": 'e',
    "OOO...": 'f', 
    "OOOO..": 'g',
    "O.OO..": 'h',
    ".OO...": 'i',
    ".OOO..": 'j',
    "O...O.": 'k',
    "O.O.O.": 'l',
    "OO..O.": 'm', 
    "OO.OO.": 'n',
    "O..OO.": 'o',
    "OOO.O.": 'p', 
    "OOOOO.": 'q',
    "O.OOO.": 'r',
    ".OO.O.": 's',
    ".OOOO.": 't',
    "O...OO": 'u',
    "O.O.OO": 'v',
    ".OOO.O": 'w', 
    "OO..OO": 'x',
    "OO.OOO": 'y',
    "O..OOO": 'z'
}

braille_to_digit = {
    "O.....": '1',
    "O.O...": '2',
    "OO....": '3', 
    "OO.O..": '4',
    "O..O..": '5',
    "OOO...": '6', 
    "OOOO..": '7',
    "O.OO..": '8',
    ".OO...": '9',
    ".OOO..": '0',
}

def main():
    
    #get message from command line
    num_args = len(sys.argv) - 1
    message = sys.argv[1]
    for i in range(2, num_args+1):
        message = message + " " + sys.argv[i]

    #first, check for braille vs english. all braille comes in sets of 6, so check the length of the message mod 6
    #additionally, check that only braille characters exist, that is, only '.' and 'O' are in the string
    is_braille = 0 == (len(message) % 6)
    for character in message:
        if (character != '.' and character != 'O'):
            is_braille = False
            break

    if is_braille:
        print(braille_to_english(message))
    else: 
        print(english_to_braille(message))

def get_braille_digit(digit):
    return digit_to_braille[digit]

def get_braille_letter(letter):
    return letter_to_braille[letter]

def get_english_letter(braille_character):
    return braille_to_english_letter[braille_character]

def get_english_digit(braille_character):
    return braille_to_digit[braille_character]

def english_to_braille(message):
    status = "nothing"
    translated = ""
    for character in message:   
        if character == ' ':
            #if there is a space, reset the "status" which represents whether or not we are set to print numbers
            translated = translated + "......"
            status = "nothing"
        elif character.isdigit():
            #if we have a digit, set status to number if it was not already and start printing numbers
            if status == "nothing":
                translated = translated + ".O.OOO"
                status = "number"
                translated = translated + get_braille_digit(character)
            else: 
                translated = translated + get_braille_digit(character)
        else:
            if character != character.lower():
                #must be a capital letter
                translated = translated + ".....O"
            #regardless, print the lower case letter
            translated = translated + get_braille_letter(character.lower())
    
    return translated

def braille_to_english(message):
    english_text = ""
    status = "nothing"

    #loop through the braille characters and translate them, use status to know what type each character is
    for i in range(0, len(message), 6):
        braille_character = message[i:i+6]

        if braille_character == "......":
            english_text = english_text + " "
            status = "nothing"
        elif braille_character == ".....O":
            status = "capital"
        elif braille_character == ".O.OOO":
            status = "number"
        else:
            #actual character, number/letter
            if status == "number":
                english_text = english_text + get_english_digit(braille_character)
            else:
                letter = get_english_letter(braille_character)
                if status == "capital":
                    letter = letter.upper()
                    status = "nothing"
                english_text = english_text + letter

    return english_text


if __name__ == "__main__":
    main()