import sys

# Braille mappings
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.....O': 'capital_follows', '.O.OOO': 'number_follows'
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

number_map = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

def braille_to_english_text(braille):
    result = []
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
            if letter == ' ':
                number_mode = False
                result.append(' ')
            else:
                if number_mode and letter in number_map:
                    result.append(number_map[letter])
                else:
                    if capitalize_next:
                        letter = letter.upper()
                        capitalize_next = False
                    result.append(letter)
        i += 6
    
    return ''.join(result)

def english_to_braille_text(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isupper():
            result.append(english_to_braille['capital_follows'])
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille['number_follows'])
                number_mode = True
            char = list(number_map.keys())[list(number_map.values()).index(char)]
        elif number_mode:
            number_mode = False
        
        result.append(english_to_braille[char])
    
    return ''.join(result)

def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def translate(text):
    if is_braille(text):
        return braille_to_english_text(text)
    else:
        return english_to_braille_text(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(translate(input_text), end='')
    else:
        print("Please provide a string to translate.")