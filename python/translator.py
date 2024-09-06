import sys #handling for command-line input
    
# given a text input, return whether the text is braille or not based on its characters
def is_braille(text):
    braille_elements = ['0', '.']
    
    for c in text:
        if c not in braille_elements:
            return False
        else:
            return True

# create a dictionary with braille codes as the key and letters as the values
braille_to_letters = {
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
    ".....O": "capital next", 
    ".O.OOO": "number next", 
    "......": " "
}

# reverse the previous dictionary by swapping the key-value pairs
letters_to_braille = {
    letter: braille for braille, letter in braille_to_letters.items()
}

# make a separate dictionary for numbers since 0-9 follow the same braille encodings as A-J
number_to_braille = {
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...', 
    '0': '.OOO..'
}

# to convert braille input to text output
def braille_to_text(input):

    text = ""
    is_next_char_capital = False
    is_next_char_number = False

    for i in range(0, len(input), 6): # every character is 6 O's or .'s in length
        curr_char = input[i:i+6]

        if curr_char == '.....O': # a capital as the next character
            is_next_char_capital = True
            continue
        elif curr_char == '.O.OOO': # a number as the next character
            is_next_char_number = True
            continue
        elif curr_char == '......':
            text += ' '
            is_next_char_number = False # reset
            continue

        # in the case the next character is a number
        if is_next_char_number == True: 
            for num, braille in number_to_braille.items():
                if braille == curr_char:
                    text += num # append the number
                    break

        # in the case the next character is a capital letter
        elif is_next_char_capital == True:
            for braille, letter in braille_to_letters.items():
                if braille == curr_char:
                    text += letter.upper() # make the character uppercase and append it
                    is_next_char_capital = False # reset
                    break

        # in the case of a direct braille to lowercase text conversion
        else:
            for braille, letter in braille_to_letters.items():
                if braille == curr_char:
                    text += letter
                    break
    return text

# to convert text input to braille output
def text_to_braille(input):

    braille = ""
    carrying_digit = False

    for i in input:
        if i.isdigit(): # when the letter is a number
            if carrying_digit == False:
                braille += '.O.OOO'
                braille += number_to_braille[i]
                carrying_digit = True
            elif carrying_digit == True: # avoiding adding the braille for incoming number multiple times
                braille += number_to_braille[i]
        elif i.isupper(): # when the letter is capitalized
            braille += '.....O'
            braille += letters_to_braille[i.lower()]
        elif i == ' ': # when the letter is a space
            braille += '......'
            carrying_digit = False # reset
        else:
            braille += letters_to_braille[i] # append a letter
            
    return braille

if __name__ == "__main__":
    userinput = ' '.join(sys.argv[1:]) # bringing all command line args together as one string

    if is_braille(userinput):
        print(braille_to_text(userinput))
    else:
        print(text_to_braille(userinput))