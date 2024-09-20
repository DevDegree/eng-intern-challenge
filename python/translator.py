import sys

braille_to_letters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c',
    'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i',
    '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u',
    'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', '......': ' ',
    '.O...O': '.','.....O': 'capital_follows', '.O.OOO': 'number_follows'
}

braille_to_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3',
    'OO.O..': '4', 'O..O..': '5', 'OOO...': '6',
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9',
    '.OOO..': '0'
}

letters_to_braille = {v: k for k, v in braille_to_letters.items()}
numbers_to_braille = {v: k for k, v in braille_to_numbers.items()}

def translate_braille_to_english(braille_input) -> str:
    """
    Translate a Braille string to English.

    braille_input: string

    returns: string
    """
    translated_text = ""
    capitalize_next = False
    treat_as_number = False
    
    # translate each braille symbol (set of 6 characters) in the input
    for i in range(0, len(braille_input), 6):
        current_braille = braille_input[i:i+6]
        if current_braille == letters_to_braille['capital_follows']:
            capitalize_next = True
            continue
        elif current_braille == letters_to_braille['number_follows']:
            treat_as_number = True
            continue
        elif current_braille == '......':
            treat_as_number = False
        
        if capitalize_next:
            translated_text += braille_to_letters[current_braille].upper()
            capitalize_next = False
        elif treat_as_number:
            translated_text += braille_to_numbers[current_braille]
        else:
            translated_text += braille_to_letters[current_braille]

    return translated_text

def translate_english_to_braille(english_input) -> str:
    """
    Translate an English string to Braille.

    english_input: string

    returns: string
    """
    translated_braille = ""
    is_previous_number = False
    
    # translate each character in the input to braille
    for char in english_input:
        if char.isupper(): 
            is_previous_number = False
            translated_braille += letters_to_braille['capital_follows']
            translated_braille += letters_to_braille[char.lower()]
        elif char.isdigit():
            if not is_previous_number:
                translated_braille += letters_to_braille['number_follows']
                is_previous_number = True
            translated_braille += numbers_to_braille[char]
        else:
            is_previous_number = False
            translated_braille += letters_to_braille[char]
    return translated_braille

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    
    # get input from command line arguments
    input_args = sys.argv[1:]
    input_str = " ".join(input_args)
    
    result = " "
    
    # check if input is braille or english and translate
    if all(char in ['O', '.'] for char in input_str) and (len(input_str) % 6 == 0):
        res = translate_braille_to_english(input_str)
    else:
        res = translate_english_to_braille(input_str)

    print(res)
    
if __name__ == "__main__":
    main()
    