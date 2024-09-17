
import sys

english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......', 
    'capital': '.....O',  
    'number': '.O.OOO'  
}


number_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings: Braille to English letters and special characters
braille_to_english = {}
braille_to_number = {}

# First for loop for english_to_braille
for char, braille in english_to_braille.items():
    braille_to_english[braille] = char

# Second for loop for number_to_braille
for num, braille in number_to_braille.items():
    braille_to_number[braille] = num

def translate_1(txt):
    braille_text = ""
    isNum = False
    for char in txt:
        if char.isupper():
            braille_text += english_to_braille['capital']
            braille_text += english_to_braille[char.lower()]
        elif char.isdigit():
            if not isNum:
                isNum = True
                braille_text += english_to_braille['number']
            braille_text += number_to_braille[char]
        elif char == ' ':
            braille_text += english_to_braille[' ']
            isNum = False
            
        else:
            braille_text += english_to_braille[char]
    return braille_text

def translate_2(braille):
    
    english_text = []
    i = 0
    capitalize_next = False
    number = False

    while i < len(braille):
        braille_char = braille[i:i+6]
        if braille_char == english_to_braille['capital']:
            capitalize_next = True
            i += 6
            
        elif braille_char == english_to_braille['number']:
            number = True
            i += 6
        elif braille_char == '......':
            char = braille_to_english[braille_char]
            english_text.append(char)
            number = False
            i += 6
        elif number:
            char = braille_to_number[braille_char]
            english_text.append(char)
            i += 6
        else:
            char = braille_to_english[braille_char]
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            english_text.append(char)
            i += 6
    return ''.join(english_text)

def main():
    
    input_text = ' '.join(sys.argv[1:])
    
    isBraille = True

    for char in input_text:
        if char not in 'O.':
            isBraille = False
            break

    if isBraille:
        out = translate_2(input_text)
    else:
        out = translate_1(input_text)

    print(out)

if __name__ == "__main__":
    main()
