import sys

## Dictionaries ##

# Created dictionaries to store the mapping between English and Braille
e_to_b = {"a": "O.....","b": "O.O...","c": "OO....","d": "OO.O..","e": "O..O..","f": "OOO...","g": "OOOO..","h": "O.OO..",
 "i": ".OO...","j": ".OOO..","k": "O...O.","l": "O.O.O.","m": "OO..O.","n": "OO.OO.","o": "O..OO.","p": "OOO.O.","q": "OOOOO.", "r": "O.OOO.","s": ".OO.O.","t": ".OOOO.","u": "O...OO","v": "O.O.OO","w": ".OOO.O","x": "OO..OO","y": "OO.OOO","z": "O..OOO","SPA": "......","CAP": ".....O", "NUM": ".O.OOO" }
# Since the numbers have the same Braille coding as the first 9 letters of the alphabet, create a mapping
let_to_num = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"}
# Create the inverse mappings between Braille and English and numbers to letters
num_to_let = {v: k for k, v in let_to_num.items()}
b_to_e = {v: k for k, v in e_to_b.items()}

def input_language(words):
    '''Takes in the input string and outputs the original language'''
    # Find the unique characters in the given words
    unique_chars = ''.join(set(words))

    # If string is a multiple of 6 and there's at most 2 unique characters,
    # and the unique characters are either O or . return Braille
    if len(words) % 6 == 0 and len(unique_chars) <= 2:
            if unique_chars in ['O', '.', '.O', 'O.']:
                return 0

    # return English otherwise
    return 1

# Function to translate from English to Braille
def english_to_braille(words):
    '''Takes in English string and translates to Braille'''
    translated = ''
    num_flag = 0

    for char in words:
        # If the English character is uppercase, then insert the 'capital follows' and then the letter
        if char.isupper():
            translated += e_to_b['CAP']
            translated += e_to_b[char.lower()]
        
        # If the character is a space, insert a space in Braille and reset the number flag
        elif char.isspace():
            translated += e_to_b['SPA']
            num_flag = 0

        # If the character is a number, and it's the first encountered number, set the flag, and insert 'number follows'
        # Then find the mapping between the number and alphabet, and insert the Braille for that letter
        elif char.isnumeric():
            if num_flag == 0:
                translated += e_to_b['NUM']
            letter = num_to_let[char]
            translated += e_to_b[letter]
            num_flag = 1

        # Otherwise, insert the translated character in Braille
        else:
            translated += e_to_b[char]
    return translated


def braille_to_english(words):
    '''Takes in Braille string and translates to English'''
    # Find how many letters are represented by the Braille string
    loops = len(words) // 6
    translated = ''
    cap_flag, num_flag = 0, 0

    # Translate each letter
    for i in range(loops):
        section = words[i*6:(i+1)*6]
        
        # If string represents 'capital follows', set a capital flag so that the following letter is capitalized 
        if b_to_e[section] == "CAP":
            cap_flag = 1

        # If string represents 'number follows', set a number flag so that the following alphabet Braille is mapped to numbers
        elif b_to_e[section] == "NUM":
            num_flag = 1
        
        # If string represents a space, ensure to reset the number flag
        elif b_to_e[section] == "SPA":
            translated += " "
            num_flag = 0

        # Handle any capital and/or number flags. Reset the capital flag immediately. Wait for space for the number flag.
        elif cap_flag == 1:
            translated += b_to_e[section].upper()
            cap_flag = 0
        
        elif num_flag == 1:
            let =  b_to_e[section]
            translated += let_to_num[let]

        # Otherwise, insert the translated letter in English
        else:    
            translated += b_to_e[section]
    return translated

if __name__ == "__main__":
    # Get the words to be translated in string format (need to join with a space if multiple arguments)
    to_translate = " ".join(sys.argv[1:])
    # Determine the language of the input string
    lang = input_language(to_translate)
    # Carry out the appropriate translation
    if lang == 1:
        translated = english_to_braille(to_translate)
    else:
        translated = braille_to_english(to_translate)
    # Print to the terminal
    print(translated)
