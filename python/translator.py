
import sys
# Braille Mappings for letters and numbers
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOOOO', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', 
    ' ': '......', # Space
    'capital': '.....O', # Capitalization
    'number': ".O.OOO" # Number follow symbol
}

# Number mappings specifically
number_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}
# Reverse mapping from Braille to English
english_dict = {v: k for k, v in braille_dict.items()}
# Reverse mapping from Braille to the corresponding Number
number_reverse_dict = {v: k for k, v in number_dict.items()}
def is_braille(input):
    #Determine if the input string is in Braille
    return all(c in "O. " for c in input.strip())
#The strip() method removes any whitespace from the beginning or the end that may have been put by the user

def english_to_braille(text): #Convert English to Braille, handling capitalization and numbers
    result = [] # the translation will be stored in this array
    is_number = False
    for char in text:
        if char.isdigit():
            if not is_number:  #If the number symbol hasn't been added yet, add it
                result.append(braille_dict['number'])
                is_number = True
            result.append(number_dict[char])
        else:
            if is_number: # Reset the number flag if a non-digit is encountered
                is_number = False
            if char.isupper(): # Handle capitalization by appending the capital symbol
                result.append(braille_dict['capital'])
            result.append(braille_dict[char.lower()])
    return "".join(result) #Used to return a string composed of the elements of the Array result
def braille_to_english(braille): #Convert Braille to English, handling capitalization and numbers
    result = []
    i = 0 #variable used to jump to the next braille letter
    is_number = False
    while i < len(braille):
        chunk = braille[i:i+6]
        if chunk == braille_dict['capital']:
            i += 6
            result.append(english_dict[braille[i:i+6]].upper())
        elif chunk == braille_dict['number']:
            is_number = True
            i += 6
            continue
        else:
            if is_number:
                result.append(number_reverse_dict[chunk])
            else:
                result.append(english_dict[chunk])
        i += 6
    return ''.join(result)
def main():
    if len(sys.argv) < 2:
        print("INCORRECT USAGE: The correct form is: python translator.py <string>")
        return

    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()
