import sys
english_to_braille_dict = {
    #letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.O.O', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    #numbers
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..',
    #special characeters
    ' ': '......'
}

braille_to_english_dict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', 
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.O.O': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 
    'OO.OOO': 'y', 'O..OOO': 'z', 
    #special characters
    '......': ' '}

braille_to_numbers_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', 
    '.OO...': '9', '.OOO..': '0'
    }

capital_follows = '.....O' 
number_follows = '.O.OOO'
# #english to braille
def english_to_braille(string):
    capital_follows = '.....O' 
    number_follows = '.O.OOO'  

    output = []

    num_follow = False
    for char in string:
        if char.isupper():
            output.append(capital_follows)
            char = char.lower()
        if char.isdigit() and not num_follow:
            output.append(number_follows)
            num_follow = True
        if char == ' ':
            num_follow = False

        output.append(english_to_braille_dict.get(char, ""))

    return ''.join(output)

#Braille to English
def braille_to_english(braille_string):
    capital_follows = '.....O' 
    number_follows = '.O.OOO'
    output = []
    i = 0
    num_follow = False
    capital_follow = False

    while i < len(braille_string):
        braille_char = braille_string[i:i+6]
        i += 6
        if braille_char == capital_follows:
            capital_follow = True
            continue
        if braille_char == number_follows:
            num_follow = True
            continue
        if num_follow:
            output.append(braille_to_numbers_dict.get(braille_char, ""))
        elif capital_follow:
            output.append(braille_to_english_dict.get(braille_char, "").capitalize())
            capital_follow = False
        else:
            output.append(braille_to_english_dict.get(braille_char, ""))
            if output[-1] == ' ':
                num_follow = False
                capital_follow = False
    return ''.join(output)

#Main
if len(sys.argv) > 1:
    input_string = ' '.join(sys.argv[1:]).strip()
    if all(char in 'O.' for char in input_string) and len(input_string) % 6 == 0:
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))
