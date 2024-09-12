import sys

# Braille to English mappings
BRAILLE_TO_ENGLISH = {
    'O.....': ['a', '1'], 'O.O...': ['b', '2'], 'OO....': ['c', '3'], 'OO.O..': ['d', '4'],
    'O..O..': ['e', '5'], 'OOO...': ['f', '6'], 'OO..': ['g', '7'], 'O.OO..': ['h', '8'],
    '.OO...': ['i', '9'], '.OOO..': ['j', 'O'], 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 
    'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', 
    '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
    'O..OOO': 'z', 
    
    '.....O': 'cap', '.O...O': 'dec', '.O.OOO': 'num', 
    
    '..OO.O': ".", '..O...': ",", '..O.OO': "?", '..OOO.': "!", '..OO..': ":", '..O.O.': ";", '....OO': "-", 
    '.O..O.': "/", '.OO..O': "<", 'O..OO.': '>', 'O.O..O': "(", '.O.OO.': ")", '......': ' '
}

# English to Braille mappings
ENGLISH_TO_BRAILLE = {}
for braille, english_list in BRAILLE_TO_ENGLISH.items():
    if isinstance(english_list, list):
        for english in english_list:
            ENGLISH_TO_BRAILLE[english] = braille
    else:
        ENGLISH_TO_BRAILLE[english_list] = braille


def is_braille(input_text):
    allowed_braille_chars = {'O', '.'}
    if not all(char in allowed_braille_chars for char in input_text):
        return False  # Contains invalid characters

    return True


def braille_to_english(braille_text):
    # Handle cases where the length of braille_text is not a multiple of 6
    braille_text = braille_text[:len(braille_text) - (len(braille_text) % 6)]  # Trim to the nearest multiple of 6
    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    result = []
    capitalize_next = False
    num_mode = False

    for braille_char in braille_chars:
        if braille_char in BRAILLE_TO_ENGLISH:
            value = BRAILLE_TO_ENGLISH[braille_char]

            if value == 'cap':
                capitalize_next = True
                continue
            elif value == 'dec':
                result.append('.')
                continue
            elif value == 'num':
                num_mode = True
                continue
            elif braille_char == "......":
                num_mode = False

            
            if num_mode:
                translated_char = value[1] if isinstance(value, list) else value
            else:
                translated_char = value[0] if isinstance(value, list) else value

            if capitalize_next:
                translated_char = translated_char.upper()
                capitalize_next = False

            result.append(translated_char)
        else:
            result.append('?')  # Unknown character

    return ''.join(result)



def english_to_braille(english_text):
    result = []
    in_number_mode = False
    
    for char in english_text:
        if char.isupper():
            result.append(ENGLISH_TO_BRAILLE['cap'])
            char = char.lower()

        if char in '0123456789':
            if not in_number_mode:
                result.append(ENGLISH_TO_BRAILLE['num'])
                in_number_mode = True
            result.append(ENGLISH_TO_BRAILLE.get(char, '......'))
        elif char == '.':
            if not in_number_mode:
                result.append(ENGLISH_TO_BRAILLE['dec'])
            result.append(ENGLISH_TO_BRAILLE.get(char, '......'))
        else:
            if char in ENGLISH_TO_BRAILLE:
                result.append(ENGLISH_TO_BRAILLE[char])
                in_number_mode = False
            else:
                result.append('......')
    
    return ''.join(result)
    

def translate(input_text):
    if is_braille(input_text):
        return braille_to_english(input_text)
    else:
        return english_to_braille(input_text)

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <text>")
        sys.exit(1)

    # Join all arguments except the first (which is the script name)
    input_text = ' '.join(sys.argv[1:])
    
    translation = translate(input_text)
    print(f"{translation}")


