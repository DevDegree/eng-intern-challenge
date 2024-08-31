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

# Function to check what the input language is
def input_language(words):
    # Find the unique characters in the given words
    unique_chars = ''.join(set(words))

    # If string is a multiple of 6 and there's only 2 unique characters, return Braille
    if len(words) % 6 == 0 and len(unique_chars) <= 2:
        return 0

    # return English otherwise
    return 1

# Function to translate from English to Braille
def english_to_braille(words):
    translated = ''
    num_flag = 0

    for char in words:
        if char.isupper():
            translated += e_to_b['CAP']
            translated += e_to_b[char.lower()]
        
        elif char.isspace():
            translated += e_to_b['SPA']
            num_flag = 0

        elif char.isnumeric():
            if num_flag == 0:
                translated += e_to_b['NUM']
            letter = num_to_let[char]
            translated += e_to_b[letter]
            num_flag = 1
        else:
            translated += e_to_b[char]

    return translated


# Function to translate from Braille to English
def braille_to_english(words):
    loops = len(words) // 6
    translated = ''
    cap_flag, num_flag = 0, 0

    for i in range(loops):
        section = words[i*6:(i+1)*6]
        if b_to_e[section] == "CAP":
            cap_flag = 1

        elif b_to_e[section] == "NUM":
            num_flag = 1
        
        elif b_to_e[section] == "SPA":
            translated += " "
            num_flag = 0

        elif cap_flag == 1:
            translated += b_to_e[section].upper()
            cap_flag = 0
        
        elif num_flag == 1:
            let =  b_to_e[section]
            translated += let_to_num[let]

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