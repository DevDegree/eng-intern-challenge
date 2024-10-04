import sys

braille_to_english = {
    # Alphabet
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ', # space
    # Capital and number follow symbols
    '.O.....': 'capital follows', '.O.OOO': 'number follows',
}

braille_to_numbers = {
    # Numbers
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

def check_input(input_string):
    return all(c in 'O.' for c in input_string) and len(input_string) % 6 == 0

def translate(input_string):
    # Braille to English
    if check_input(input_string):
        result = []
        index = 0
        is_number = False
        while index < len(input_string):
            char = input_string[index:index+6]
            if char == '.O.....':
                index += 6
                next_char = input_string[index:index+6]
                result.append(braille_to_english[next_char].upper())
            elif char == '.O.OOO':
                is_number = True
            else:
                if is_number:
                    translation = braille_to_numbers.get(char, '')
                else:
                    translation = braille_to_english.get(char, '')

                result.append(translation)

                if translation == ' ':
                    is_number = False
            
            index += 6
        return ''.join(result)
    else:
        return input_string


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
        translated_string = translate(input_string)
        print(translated_string)