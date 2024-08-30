import sys
from constants import BRAILLE, char_dict, num_dict, special_char_dict

def translate_to_braille(text):
    braille_text = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_text.append(BRAILLE['num'])
                number_mode = True
            braille_text.append(BRAILLE[char])
        elif char.isalpha():
            if char.isupper():
                braille_text.append(BRAILLE['caps'])
            braille_text.append(BRAILLE[char.lower()])
            number_mode = False 
        else:
            braille_text.append(BRAILLE.get(char, ''))
            number_mode = False 

    return ''.join(braille_text)

def translate_from_braille(braille_text):
    english_text = []
    i = 0
    while i < len(braille_text):
        char = braille_text[i:i+6]
        if char == BRAILLE['caps']:
            next_char = braille_text[i+6:i+12]
            english_text.append(char_dict.get(next_char, '').upper())
            i += 12
        elif char == BRAILLE['num']:
            i += 6
            while i < len(braille_text):
                num_char = braille_text[i:i+6]
                if num_char == BRAILLE[' ']:
                    break
                english_text.append(num_dict.get(num_char, ''))
                i += 6
        else:
            if char in char_dict:
                english_text.append(char_dict[char])
            elif char in special_char_dict:
                english_text.append(special_char_dict[char])
            i += 6

    return ''.join(english_text)

def is_braille(input_text):
    return all(c in 'O.' for c in input_text)

if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        translation = translate_from_braille(input_text)
    else:
        translation = translate_to_braille(input_text)
    
    print(translation)
