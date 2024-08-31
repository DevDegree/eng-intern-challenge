import sys

ENGLISH_TO_BRAILLE_MAP = {
 'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
 'y': 'OO.OOO', 'z': 'O..OOO','.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
 ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
 '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
 'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO',
 ' ': '......'
}

BRAILLE_TO_ENGLISH_MAP = {
 'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
 '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
 'OO.OOO': 'y', 'O..OOO': 'z', '..OO.O': '.', '..O...': ',',
 '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '..O.O.': ';',
 '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>',
 'O.O..O': '(', '.O.OO.': ')', '.....O': 'capital',
 '.O...O': 'decimal', '.O.OOO': 'number', '......': ' '
}


NUMBERS_TO_BRAILLE_MAP = {
 '1': 'O.....', '2': 'O.O...','3': 'OO....', '4': 'OO.O..','5': 'O..O..','6': 'OOO...',
 '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

BRAILLE_TO_NUMBERS_MAP = {
 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
 'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
 '.OO...': '9', '.OOO..': '0'
}



def Is_Braille(input_string):
    ## check if all the char in side either 0. and that it is divisible by 6
    return all(s in "O." for s in input_string) and len(input_string) % 6 == 0


def Braille_to_English(Braille_string):
    english_output = ""
    capital_symbol = False
    number_symbol = False

    for i in range(0, len(Braille_string), 6):
        ## getting the english word from braille map
        braille_Char = Braille_string[i:i+6]
        english_word = BRAILLE_TO_ENGLISH_MAP.get(braille_Char)
        
        ## check if prev was capital by the flag
        if english_word == 'capital':
            capital_symbol = True
            continue
        ## check if prev was number by the flag
        if english_word == 'number':
            number_symbol = True
            continue
        ## check if we reached a space to change number flag
        if english_word == ' ':
            number_symbol = False
        
        ## if the prev was capital then make the next letter uppercase or if number to put a number next or put the normal char
        if capital_symbol and not number_symbol:
            english_output += english_word.upper()
            capital_symbol = False
        elif number_symbol:
            english_output += BRAILLE_TO_NUMBERS_MAP.get(braille_Char)
        else:
            english_output += english_word
      
    return english_output

def English_to_Braille(English_string):
    braille_output = ""
    is_number = False

    for char in English_string:
        ## check if it is upper case to add its braille
        if char.isupper():
            braille_output += ENGLISH_TO_BRAILLE_MAP.get('capital')
        
        ## adding the number and setting the flag
        if char.isnumeric() and not is_number:
            is_number = True
            braille_output += ENGLISH_TO_BRAILLE_MAP.get('number')
        if char.isnumeric() and is_number:
            braille_output += NUMBERS_TO_BRAILLE_MAP.get(char)
            continue
        is_number = False
        braille_output += ENGLISH_TO_BRAILLE_MAP.get(char.lower(), '')
    return braille_output


def main():
    result = ""
    for i in sys.argv[1:]:
        input_string = i
        if i != sys.argv[-1]:
            input_string += " "
        
        if Is_Braille(input_string):
            result += Braille_to_English(input_string)
        else:
            result += English_to_Braille(input_string)
        
    print(result)


main()