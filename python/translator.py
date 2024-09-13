import sys

# Mapping for Braille to English letters
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
}

# Reverse mapping for English to Braille letters
english_to_braille = {letter: braille for braille, letter in braille_to_english.items()}

# Mapping for Braille to numbers
braille_to_number = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '10',
}

# Reverse mapping for numbers to Braille
number_to_braille = {number: braille for braille, number in braille_to_number.items()}


input_words = sys.argv[1:]
if not len(input_words):
    quit()  

# Check if the input is in Braille or regular text
is_braille_input = True
for character in input_words[0]:
    if character not in ['.', 'O']:
        is_braille_input = False
        break

# String to store the output
translated_string = ''

# If the input is not Braille, translate from English to Braille
if not is_braille_input:
    for word in input_words:
        is_number_mode = False
        for char in word:
            if char.isnumeric() and not is_number_mode:  
                is_number_mode = True
                translated_string += '.O.OOO'  
            if is_number_mode:
                translated_string += number_to_braille[char.lower()]  
            if char.isupper():
                translated_string += '.....O'  
            if not is_number_mode:
                translated_string += english_to_braille[char.lower()]  
        if word is not input_words[-1]:
            translated_string += '......' 

# If the input is Braille, translate from Braille to English
else:
    braille_message = input_words[0]
    braille_chunks = []
    for i in range(0, len(braille_message), 6):
        braille_chunks.append(braille_message[i:i+6])
    
    is_number_mode = False
    is_capital_mode = False
    
    for braille_chunk in braille_chunks:
        if braille_chunk == '.O.OOO':  
            is_number_mode = True
            continue
        if braille_chunk == '......': 
            translated_string += ' '
            is_number_mode = False
            continue
        if is_number_mode:
            translated_string += braille_to_number[braille_chunk]  
            continue
        if braille_chunk == '.....O': 
            is_capital_mode = True
            continue
        if not is_number_mode:
            if is_capital_mode:
                translated_string += braille_to_english[braille_chunk].upper()  
                is_capital_mode = False
            else:
                translated_string += braille_to_english[braille_chunk] 

# Output the translated string
print(translated_string)
