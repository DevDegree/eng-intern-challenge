import sys

braille_letter_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}

braille_number_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_special_map = {
    'capital': '.....O',  
    'number': '.O.OOO',   
    ' ': '......'         
}


reverse_braille_letter_map = {v: k for k, v in braille_letter_map.items()}
reverse_braille_number_map = {v: k for k, v in braille_number_map.items()}
reverse_braille_special_map = {v: k for k, v in braille_special_map.items()}

def is_braille(text):
    
    return all(c in 'O.' for c in text)

def english_to_braille(text):
    braille_text = []
    number_mode = False  
    
    for char in text:
        if char.isdigit():  # For numbers
            if not number_mode:
                braille_text.append(braille_special_map['number']) 
                number_mode = True
            braille_text.append(braille_number_map[char])
        elif char.isalpha():  # For letters
            if number_mode:
                number_mode = False 
            if char.isupper():
                braille_text.append(braille_special_map['capital'])  
            braille_text.append(braille_letter_map[char.lower()])  
        elif char == ' ':
            braille_text.append(braille_special_map[' '])  
            number_mode = False  
    
    return ''.join(braille_text)


def braille_to_english(braille):
    
    english_text = []
    index = 0
    number_mode = False
    capital_mode = False
    
    while index < len(braille):
        braille_char = braille[index:index + 6]
        index += 6

        if braille_char == braille_special_map['capital']:
            capital_mode = True
            continue
        elif braille_char == braille_special_map['number']:
            number_mode = True
            continue
        elif braille_char == braille_special_map[' ']:
            english_text.append(' ')
            number_mode = False 
            continue
        
        if number_mode:
            letter = reverse_braille_number_map.get(braille_char, '')
        else:
            letter = reverse_braille_letter_map.get(braille_char, '')
        
        if capital_mode and letter:
            letter = letter.upper()
            capital_mode = False
        
        english_text.append(letter)

    return ''.join(english_text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:]) 
    
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()
