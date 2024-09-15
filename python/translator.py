import sys

# Braille to English dictionaries
braille_to_english_letters = {
    "O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e', "OOO...": 'f',
    "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i', ".OOO..": 'j', "O...O.": 'k', "O.O.O.": 'l',
    "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o', "OOOO.O": 'p', "OOOOO.": 'q', "O.OOO.": 'r',
    ".OO.O.": 's', ".OOOO.": 't', "O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OOO.OO": 'x',
    "OO.OOO": 'y', "O..OOO": 'z'
}

braille_to_english_numbers = {
    "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4', "O..O..": '5', "OOO...": '6',
    "OO.OO.": '7', "O.OO..": '8', ".OO...": '9', ".OOO..": '0'
}

braille_to_english_symbols = {
    "..O.OO": 'capital', "..O..O": 'number', "......": ' ', 
    "OO..OO": '.', "OO.OO.": ',', "O..O.O": '?', "O.O.O.": '!', "O..O.O": ':', "O..OO.": ';',
    "O..O..": '-', "....O.": '/', "....OO": '<', ".....O": '>', "O.O...": '(', "O.OO..": ')'
}

english_to_braille_letters = {v: k for k, v in braille_to_english_letters.items()}
english_to_braille_numbers = {v: k for k, v in braille_to_english_numbers.items()}
english_to_braille_symbols = {v: k for k, v in braille_to_english_symbols.items()}

def braille_to_eng(braille_input):
    if ' ' not in braille_input:
        braille_input = ' '.join([braille_input[i:i+6] for i in range(0, len(braille_input), 6)])

    words = braille_input.split(' ')
    english_output = []
    number_mode = False
    capitalize_next = False
    
    for word in words:
        if word == ".O.OOO":
            number_mode = True
            continue

        if word == ".....O": 
            capitalize_next = True
            continue

        if word in braille_to_english_symbols:
            char = braille_to_english_symbols[word]
            
            if char == 'number':
                number_mode = True
                continue
            
            if char == 'capital':
                capitalize_next = True
                continue

            if char == ' ':
                number_mode = False 
                english_output.append(char)
                continue

        if word in braille_to_english_numbers and number_mode:
            char = braille_to_english_numbers[word]
            english_output.append(char)
            continue

        elif word in braille_to_english_letters:
            char = braille_to_english_letters[word]
            
            if capitalize_next:
                english_output.append(char.upper())
                capitalize_next = False 
            else:
                english_output.append(char)
        
        else:
            english_output.append("[Invalid Braille pattern: " + word + "]")

    return ''.join(english_output)

def eng_to_braille(english_input):
    braille_output = []
    number_mode = False
    for char in english_input:
        if char.isdigit():
            if not number_mode:
                braille_output.append(".O.OOO")
                number_mode = True
            char_as_braille = english_to_braille_numbers.get(char, "......")
            braille_output.append(char_as_braille)
        elif char.isalpha():
            if char.isupper():
                braille_output.append(".....O")
            char_as_braille = english_to_braille_letters.get(char.lower(), "......")
            braille_output.append(char_as_braille)
        elif char in english_to_braille_symbols:
            braille_output.append(english_to_braille_symbols[char])
        else:
            braille_output.append("......")

    return ''.join(braille_output)

def identify_mode(input_str):
    if all(char in "O." for char in input_str if char != ' '):
        return "braille_to_eng"
    else:
        return "eng_to_braille"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
        mode = identify_mode(input_str)
        
        if mode == "braille_to_eng":
            print(braille_to_eng(input_str))
        elif mode == "eng_to_braille":
            print(eng_to_braille(input_str))
