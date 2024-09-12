import sys

# Braille to English mappings
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital follows', '.O.OOO': 'number follows'
}

# English to Braille mappings
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Number mappings
number_mappings = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

# Letter mappings
letter_mapings = {v: k for k, v in number_mappings.items()}

def braille_to_text(braille):
    text = ""
    i = 0
    capitalize_next = False
    number_mode = False
    
    while i < len(braille):
        char = braille[i:i+6]
        
        if char == '.....O':  # Capital follows
            capitalize_next = True
        elif char == '.O.OOO':  # Number follows
            number_mode = True
        elif char in braille_to_english:
            letter = braille_to_english[char]
            if number_mode:
                text += number_mappings[letter]
                if letter == ' ':
                    number_mode = False
            else:
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                text += letter
                number_mode = False
        
        i += 6
    
    return text

def text_to_braille(text):
    braille = ""
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille += english_to_braille['number follows']
                number_mode = True
            braille += english_to_braille[letter_mapings[char]]
        elif char.isalpha():
            if number_mode:
                braille += '......'  # Space to end number mode
                number_mode = False
            if char.isupper():
                braille += english_to_braille['capital follows']
            braille += english_to_braille[char.lower()]
        elif char == ' ':
            braille += english_to_braille[char]
            number_mode = False
    
    return braille

def translate(input_string):
    if set(input_string).issubset({'O', '.'}):
        return braille_to_text(input_string)
    else:
        return text_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
    else:
        input_string = ' '.join(sys.argv[1:])
        result = translate(input_string)
        print(result)

