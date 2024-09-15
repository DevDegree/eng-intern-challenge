#!/usr/bin/env python3
#.....O capital follows
# O.OO.. H
# O..O.. E
# O.O.O. L
# O.O.O. L
# O..OO. O
# ...... (space)
# .OOO.O w
# O..OO. o
# O.OOO. r
# O.O.O. l
# OO.O.. d

import sys

# braille to english hashmap
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
}

# english to braille mapping for the above hashmap
english_to_braille = {v: k for k, v in braille_to_english.items()}

# braille to english nums
braille_to_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# english to braille nums
english_to_braille_numbers = {v: k for k, v in braille_to_numbers.items()}

# braille to english punctuation
braille_to_punctuation = {
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<',
    'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')'
}

# english to braille puncutation
english_to_braille_punctuation = {v: k for k, v in braille_to_punctuation.items()}

# capitals, number and decimals (assuming decimal follows is for punctuations, no mention of how to handle punctuation cases at the repo)
capital_follows = '.....O'
number_follows = '.O.OOO'
decimal_follows = '.O...O'

def translate_braille_to_english(braille_str):
    #initialize capitalization, number and punctuation flags as false 
    translated = []
    capitalize = False
    is_number = False
    is_punctuation = False
    
    # splitting the input into 6 segments to get the braille characters
    braille_chars = [braille_str[i:i + 6] for i in range(0, len(braille_str), 6)]
    
    for braille_char in braille_chars:
        if braille_char == capital_follows: 
            capitalize = True
            continue
        elif braille_char == number_follows: 
            is_number = True
            continue
        elif braille_char == decimal_follows: 
            is_punctuation = True
            continue
        elif braille_char == '......':  
            translated.append(' ')
            is_number = False # Reset number mode after a space as instructed
            is_punctuation = False # Reset punctuation mode after a space (assumption)
            continue
        
        # using the mappings instructed to get the english characters
        if is_punctuation:
            character = braille_to_punctuation.get(braille_char, '?')
            is_punctuation = False  # reset punctuation after one character (assumption)
        elif is_number:
            character = braille_to_numbers.get(braille_char, '?')
        else:
            character = braille_to_english.get(braille_char, '?')
        
        # capitalization
        if capitalize and not is_number and not is_punctuation:
            character = character.upper()
            capitalize = False
        
        translated.append(character)
    
    return ''.join(translated).strip()

def translate_english_to_braille(english_str):
    translated = []
    is_number_mode = False
    
    for char in english_str:
        if char.isdigit():
            if not is_number_mode:
                translated.append(number_follows)
                is_number_mode = True
            translated.append(english_to_braille_numbers[char])
        elif char.isupper():
            if is_number_mode:
                is_number_mode = False
            translated.append(capital_follows)
            translated.append(english_to_braille[char.lower()])
        elif char in english_to_braille_punctuation:
            if is_number_mode:
                is_number_mode = False
            translated.append(decimal_follows)
            translated.append(english_to_braille_punctuation[char])
        else:
            if is_number_mode:
                is_number_mode = False
            translated.append(english_to_braille.get(char, '......'))
    
    return ''.join(translated)

def detect_and_translate(input_str):
    # checking if braille or english
    if all(c in 'O. ' for c in input_str):
        return translate_braille_to_english(input_str)
    else:
        return translate_english_to_braille(input_str)
    
    
def main():
    # if len(sys.argv) < 3 or sys.argv[0] != 'python3' or sys.argv[1] != 'translator.py':
    #     print("Error: The script expects to be run with 'python3 translator.py' followed by the input.")
    #     sys.exit(1)
    
    # # Join all arguments after the first two into a single string
    # input_str = ' '.join(sys.argv[2:])
    #  # Translate the input string
    # output_str = detect_and_translate(input_str)
    # # Print the translation result
    # print(output_str)
    # print("Arguments passed:", sys.argv)
    
    """input_str = ' '.join(sys.argv[1:])
    output_str = detect_and_translate(input_str)
    print(f"Raw output: {repr(output_str)}")
    print(output_str.strip())"""
    input_string = " ".join(sys.argv[1:])

    result = detect_and_translate(input_string)

    print(result)
  

if __name__ == "__main__":
    main()


"""
input_str = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
output_str = detect_and_translate(input_str)
print(output_str)
"""
