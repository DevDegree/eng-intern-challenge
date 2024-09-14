import sys

#mode flags
english_mode = 0
braille_mode = 0

arguments = sys.argv


if not all(character in {'.', 'O'} for character in arguments[1]):
    english_mode = 1
else:
    braille_mode = 1

#braille dictionary (English to Braille)
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    ' ': '......',  # Space
    'capital': '.....O',  # Capital symbol
    'number': '.O.OOO'  # Number symbol
}

#separate reverse dictionaries for numbers, lowercase, and uppercase letters
reverse_braille_dict_lower = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z'
}

reverse_braille_dict_upper = {
    'O.....': 'A', 'O.O...': 'B', 'OO....': 'C', 'OO.O..': 'D', 'O..O..': 'E',
    'OOO...': 'F', 'OOOO..': 'G', 'O.OO..': 'H', '.OO...': 'I', '.OOO..': 'J',
    'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': 'O',
    'OOO.O.': 'P', 'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T',
    'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 'OO.OOO': 'Y', 'O..OOO': 'Z'
}

reverse_braille_dict_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}


def translate_to_braille(text):
    result = []
    number_mode = False
    
    words = text.split()  
    for idx, word in enumerate(words):
        for letter in word:
            if letter.isdigit() and not number_mode:
                result.append(braille_dict['number']) 
                number_mode = True
            
            if letter.isdigit():
                result.append(braille_dict[letter]) 
            elif letter.isalpha():
                if letter.isupper():
                    result.append(braille_dict['capital']) 
                result.append(braille_dict[letter.lower()])  
                number_mode = False 
            else:
                continue
        
        if idx < len(words) - 1:
            result.append(braille_dict[' '])  
    
    return ''.join(result)

def translate_to_english(braille_text):
    result = []
    number_mode = False
    capital_mode = False

    #split the Braille input into chunks of 6 characters each
    braille_chunks = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]

    for braille_char in braille_chunks:

        if braille_char == braille_dict['number']:  
            number_mode = True
            continue  

        # Detect capital mode ('.....O')
        elif braille_char == braille_dict['capital']:  
            capital_mode = True
            continue  

        # Detect Braille space ('......')
        elif braille_char == '......':  
            result.append(' ') 
            number_mode = False  
            capital_mode = False  
            continue

        #handle number mode: treat next characters as digits
        if number_mode:
            character = reverse_braille_dict_numbers.get(braille_char, '')
            if character:
                result.append(character)  
            else:
                number_mode = False 
                character = reverse_braille_dict_lower.get(braille_char, '')
                result.append(character)

        elif capital_mode:
            character = reverse_braille_dict_upper.get(braille_char, '')
            result.append(character)  
            capital_mode = False  

        else:
            character = reverse_braille_dict_lower.get(braille_char, '')
            result.append(character)

    return ''.join(result)

if len(arguments) > 1:
    input_text = ' '.join(arguments[1:]) 

    if english_mode:
        braille_output = translate_to_braille(input_text)
        print(braille_output)
    elif braille_mode:
        english_output = translate_to_english(input_text)
        print(english_output)
else:
    sys.exit(1)




