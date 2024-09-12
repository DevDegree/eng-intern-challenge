import sys

# Special markers
CAPITAL_MARKER = '.....O'
NUMBER_MARKER = '.O.OOO'

# Braille dictionary for letters and special characters
braille_translator = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', 
}

# Number dictionary for handling numeric conversions
number_translator = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

#not really used in any of the examples so didnt include much functionality for it
#translated anyways for clarity purposes
punct_translator = {
    '.O....': '.', '..O...': ',', '..OO..': '?', '..O.O.': '!', '.O..O.': '(', 
    '.O..OO': ')', '.O..O.': '/', '....O.': ':', '....OO': ';', '...O..': '-', 
    '...OO.': '*', 'OO....': '<', 'OOO...': '>'
}

#English to Braille, needs to be separate because of conflicts in defining caps, num, etc. 
english_translator = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', ' ': '......', '.': '.O....', ',': '..O...', '?': '..OO..',
    '!': '..O.O.', '(': '.O..O.', ')': '.O..OO', '/': '.O..O.', ':': '....O.',
    ';': '....OO', '-': '...O..', '*': '...OO.', '<': 'OO....', '>': 'OOO...'
}


def b_to_e(b_str):
    #Braille to English
    result = []
    i = 0
    while i < len(b_str):
        if i + 6 <= len(b_str):
            segment = b_str[i:i+6]
        else:
            break

        if segment == CAPITAL_MARKER:
            i += 6
            if i + 6 <= len(b_str):
                next_char = braille_translator.get(b_str[i:i+6], '?')
                result.append(next_char.upper())
            i += 6
            continue
        elif segment == NUMBER_MARKER:
            i += 6
            while i + 6 <= len(b_str) and b_str[i:i+6] in number_translator:
                result.append(number_translator[b_str[i:i+6]])
                i += 6
            continue
        
        result.append(braille_translator.get(segment, '?'))
        i += 6

    return ''.join(result)

def e_to_b(e_str):
    #English to Braille
    result = []
    capital_mode_added = False
    number_mode_added = False 

    for char in e_str:
        if char.isupper():
            if not capital_mode_added:
                # Add the CAP marker only once
                result.append('.....O')
                capital_mode_added = True
            result.append(english_translator[char.lower()])
        elif char.isdigit():
            if not number_mode_added:
                # Add the NUM marker only once
                result.append('.O.OOO')
                number_mode_added = True
            result.append(english_translator[char])
        elif char == ' ':
            result.append('......')  # space char
            capital_mode_added = False  # reset caps
            number_mode_added = False  # reset nums
        else:
            result.append(english_translator[char])
            capital_mode_added = False  # reset caps

    return ''.join(result)

def input_type(input_string):
    #detect Braille or English
    if set(input_string).issubset({'O', '.'}):
        return "b"
    else:
        return "e"

def main():
    #both take user input, once at execution or if nothing is input then leave it
    if len(sys.argv) > 1:
        inp_str = " ".join(sys.argv[1:])  # Taking input from command-line argument
    else:
        inp_str = input("")  #User input
    
    inp = input_type(inp_str)
    
    if inp == "b":
        translated_str = b_to_e(inp_str)
    else:
        translated_str = e_to_b(inp_str)
    
    print(translated_str)

# Command-line execution: Provide the string as an argument
if __name__ == "__main__":
    main()

