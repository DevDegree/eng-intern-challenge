import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='+', type=str) # Let's you write a line without quotations marks
    args = parser.parse_args()
    input = ' '.join(args.input)

    if not input:
        print('No string was given')
        return
    
    if is_braille(input):
        result = translate_to_english(input)
        print(result)

    elif is_english(input):
        result = translate_to_braille(input)
        print(result)
    
    else:
        print('Invalid input format')
        return
    
def is_braille(input):
    chars = {'O', '.'}
    return all(char in chars for char in input) 

def is_english(input):
    return input.replace(" ", "").isalnum()

def translate_to_english(input):
    chars = [input[i:i+6] for i in range(0, len(input), 6)]
    output = ''
    caps_flag = False
    num_flag = False

    for char in chars:
        if char == '.....O':
            caps_flag = True
        elif char == '.O.OOO':
            num_flag = True
            continue
        elif num_flag and char in braille_digits:
            output += braille_digits[char]
        elif char in braille_punctuation:
            output += braille_punctuation[char]
        elif char in braille_to_english:
            letter = braille_to_english[char]
            if caps_flag:
                letter = letter.upper()
                caps_flag = False
            output += letter
            num_flag = False
        else:
            print('Unknown character. Leaving program.')
            return output

    return output

def translate_to_braille(input):
    output = ''
    in_number = False

    for char in input:
        if char.isupper(): 
            output += english_to_braille['capital']
            output += english_to_braille[char.lower()]
            in_number = False
        elif char.isdigit():
            if in_number is False:
                output += english_to_braille['number']
                in_number = True
            output += {v: k for k, v in braille_digits.items()}[char]
        elif char in english_to_braille:
            output += english_to_braille[char.lower()]
            in_number = False
        elif char in braille_punctuation.values():
            output += {v: k for k, v in braille_punctuation.items()}[char]
            in_number = False
        else:
            print('Unknown character. Leaving program.')
            return
    
    return output

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '.O...O': 'decimal' ,'.O.OOO': 'number'
}


braille_digits = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

braille_punctuation = {
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':',
    '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>',
    '.OO..O': '(', 'O..OO.': ')', '......': ' '
}

english_to_braille = {value: key for key, value in braille_to_english.items()}

if __name__ == "__main__":
    main()

