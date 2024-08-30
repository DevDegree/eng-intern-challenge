import sys

# Key-value store of English characters mapped to 6-character Braille chunks
character_to_braille_mapping = {
        #Letters
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....',
        'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
        'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
        'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
        's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
        'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO', 
        #Numbers
        '1': 'O.....', '2': 'O.O...', '3': 'OO....',
        '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
        '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
        '0': '.OOO..', 

        # Space
        ' ': '......',

        #Flags for incoming word
        'capital': '.....O',  
        'number': '.O.OOO',
        }
        
       
#Key-value store of 6-character Braille chunks mapped to English characters constructed using the English to Braille mapping dictionary
#IMPORTANT : This dictionary maps 6 character Braille chunks to a list consisting of a letter and number
#IMPORTANT : When working with this dictionary, the first element of the list is always the letter and the second is always the number
braille_to_character_mapping = {} 
for char, braille in character_to_braille_mapping.items():
    if char.isdigit():  # If it's a number
        if braille not in braille_to_character_mapping:
            braille_to_character_mapping[braille] = [None, char]
        else:
            braille_to_character_mapping[braille][1] = char
    elif char.isalpha():  # If it's a letter
        if braille not in braille_to_character_mapping:
            braille_to_character_mapping[braille] = [char, None]
        else:
            braille_to_character_mapping[braille][0] = char
    elif char == ' ':  # Space is treated separately
        braille_to_character_mapping[braille] = [' ', ' ']
        
def braille_to_english(text) -> str: #returns text once translated to Braille
    translated_string = ''
    i = 0
    is_num = False

    while i < len(text):
        braille_chunk = text[i:i+6] #Grab 6 character chunks of Braille to translate

        if braille_chunk == character_to_braille_mapping['capital']:
            is_num = False 
            #Capitalize next chunk
            next_chunk = text[i+6:i+12] 
            if next_chunk in braille_to_character_mapping:
                translated_string += braille_to_character_mapping[next_chunk][0].upper()
            i += 12
        elif braille_chunk == character_to_braille_mapping['number']:
            #Keep flag open for incoming numbers
            is_num = True
            i += 6
        elif braille_chunk == character_to_braille_mapping[' ']:
            is_num = False
            translated_string += ' '
            i += 6
        else:
            if braille_chunk in braille_to_character_mapping:
                if is_num:
                    char = braille_to_character_mapping[braille_chunk][1]
                    if char:
                        translated_string += braille_to_character_mapping[braille_chunk][1]
                    else:
                        is_num = False
                        translated_string += braille_to_character_mapping[braille_chunk][0]
                        
                else:
                    translated_string += braille_to_character_mapping[braille_chunk][0]
            i += 6

    return translated_string
    
def english_to_braille(text) -> str: #returns text once translated to English
    translated_string = ""
    is_number = False
    for char in text:
        if char.isdigit():
            if is_number:
                translated_string += character_to_braille_mapping[char]
            else:
                is_number = True
                translated_string += character_to_braille_mapping['number'] + character_to_braille_mapping[char]
        elif char.isalpha():
            is_number = False
            if char.isupper():
                translated_string += character_to_braille_mapping['capital'] + character_to_braille_mapping[char.lower()]
            else:
                translated_string += character_to_braille_mapping[char]
        elif char == ' ':
            is_number = False
            translated_string += character_to_braille_mapping[char]
    return translated_string

def identify_braille_or_english(text) -> bool: # Returns False for English and True for Braille
    for char in text:
        #Check for characters outside of 'O' or '.'
        if char == "O" or char == "." :
            continue
        else:
            return False
    #If all characters are either 'O' or '.' then text must be Braille
    return True 

def translate(input):
    return braille_to_english(input) if identify_braille_or_english(input) else english_to_braille(input)
    
def main():
    #Parsing Input
    input = ' '.join(sys.argv[1:])
    print(translate(input))

if __name__ == "__main__":
	main()
