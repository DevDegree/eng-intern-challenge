import sys

braille_dict = {   #dict to use
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO'
}

def to_braille(text):
    braille_output = []
    number_mode = False
    
    for char in text:
        if char.isdigit() and not number_mode:
            braille_output.append(braille_dict['number'])
            number_mode = True
        
        if char.isalpha() and number_mode:
            number_mode = False
        
        if char.isupper():
            braille_output.append(braille_dict['capital'])
            char = char.lower()
        
        braille_output.append(braille_dict.get(char, '......'))
    
    return ''.join(braille_output)

def from_braille(braille):
    reverse_braille_dict = {v: k for k, v in braille_dict.items()}
    
    english_output = []
    current_char = ""
    capital_mode = False
    number_mode = False
    
    for i in range(0, len(braille), 6):
        current_char = braille[i:i+6]
        
        if current_char == braille_dict['capital']:
            capital_mode = True
            continue
        elif current_char == braille_dict['number']:
            number_mode = True
            continue
        
        char = reverse_braille_dict.get(current_char, '')
        
        if number_mode and char.isdigit():
            english_output.append(char)
        elif number_mode and char == '':
            number_mode = False
        elif char:
            if capital_mode:
                english_output.append(char.upper())
                capital_mode = False
            else:
                english_output.append(char)
    
    return ''.join(english_output)


def main():
    args = sys.argv[1:]
    if not args:
        print("No input provided.")
        return
    
    text = " ".join(args)
    
    # Check if input is braille or English
    if all(c in 'O.' for c in text):
        print(from_braille(text))
    else:
        print(to_braille(text))

if __name__ == "__main__":
    main()

