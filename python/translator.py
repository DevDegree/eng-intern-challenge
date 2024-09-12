import sys

braille_dict = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',  # space
    ',': '.O....', '?': '.O.OOO', '!': 'OO.O.O', '.': '.O.OO.', 
    '-': '....O.', ':': '.OO...', ';': '.OO.O.', '/': 'O..O.O', 
    '<': 'O..O..', '>': '.OO.OO', '(': 'OO.O..', ')': 'OO.O..'
}

reverse_braille_dict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' ',  # space
    '.O....': ',', '.O.OOO': '?', 'OO.O.O': '!', '.O.OO.': '.', 
    '....O.': '-', '.OO...': ':', '.OO.O.': ';', 'O..O.O': '/', 
    'O..O..': '<', '.OO.OO': '>', 'OO.O..': '(', 'OO.O..': ')'
}
Reverse_braille_nums = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
    '......': ' ' # space
}

capital_next = '.....O'  
number_next = '.O.OOO'
space = '......' 

def translator(input_string):

    english = True
    stripped_input = input_string.replace(' ', '')
    if all(c in 'O.' for c in stripped_input) and len(stripped_input) % 6 == 0: #check if brialle or english
        english = False
    number_mode = False
    answer = []

    if english:
        for char in input_string:
            if char.isdigit():      #if number
                if not number_mode:
                    answer.append(number_next)
                    number_mode = True
                answer.append(braille_dict[char])

            elif char.isalpha():    #if letter
                number_mode = False
                if char.isupper():  #if Capital
                    answer.append(capital_next)
                answer.append(braille_dict[char.upper()])

            elif char in braille_dict:  #if symbol
                number_mode = False
                answer.append(braille_dict[char])
    else:
        capital_mode = False
        for i in range(0, len(input_string), 6):    #For each brialle word
            char_braille = input_string[i:i+6]

            if char_braille == capital_next:    #If Capital Symbol
                capital_mode = True
                continue

            elif char_braille == number_next:   #If Num Symbol
                number_mode = True
                continue

            if capital_mode:        #Capitalize if needed
                answer.append(reverse_braille_dict[char_braille].upper())
                capital_mode = False
            elif number_mode:   #Nums if needed
                answer.append(Reverse_braille_nums[char_braille])
            else:
                answer.append(reverse_braille_dict[char_braille])

            if char_braille == space:   #End nums if space
                number_mode = False
    
    return ''.join(answer)  #make string


if __name__ == "__main__":

    input_string = ' '.join(sys.argv[1:]) 
    output = translator(input_string)
    print(output)  