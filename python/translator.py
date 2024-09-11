import sys

braille_to_char = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital follows', '.O.OOO': 'number follows'
}

number_match = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0' 
}

char_to_braille = dict((value, key) for key, value in braille_to_char.items())

letter_match = dict((value, key) for key, value in number_match.items())

def braille_to_text(braille):
    text = []
    i = 0
    capitalize_next = False
    number_mode = False
    
    while i < len(braille):
        char = braille[i:i+6]
        
        if char == '.....O':  # Capital follows
            capitalize_next = True
        elif char == '.O.OOO':  # Number follows
            number_mode = True
        elif char in braille_to_char:
            letter = braille_to_char[char]
            if number_mode:
                text.append(number_match[letter])
                if letter == ' ':
                    number_mode = False
            else:
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                text.append(letter)
                number_mode = False
        
        i += 6
    
    return ''.join(text)

def text_to_braille(text):
    braille = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille.append(char_to_braille['number follows'])
                number_mode = True
            braille.append(char_to_braille[letter_match[char]])
        elif char.isalpha():
            if number_mode:
                braille.append('......')  # Space to end number mode
                number_mode = False
            if char.isupper():
                braille.append(char_to_braille['capital follows'])
            braille.append(char_to_braille[char.lower()])
        elif char == ' ':
            braille.append(char_to_braille[char])
            number_mode = False
    
    return ''.join(braille)

def is_braille(input):
    return all(c in {'O', '.'} for c in input) and len(input) % 6 == 0


def translate(input):
    if is_braille(input):
        return braille_to_text(input)
    else:
        return text_to_braille(input)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
    else:
        input = ' '.join(sys.argv[1:])
        result = translate(input)
        print(result)