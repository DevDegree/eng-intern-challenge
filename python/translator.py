import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', ' ': '......', 'cap': '.....O', 'num': '.O.OOO', 'dec':'.O...O'
}

reverse_braille_dict_letters = {v: k for k, v in braille_dict.items() if k.isalpha()}
reverse_braille_dict_numbers = {v: k for k, v in braille_dict.items() if k.isdigit()}


def getCharFromBraille(braille,number_mode):
    if number_mode:
        return reverse_braille_dict_numbers[braille]
    return reverse_braille_dict_letters[braille]

def translate_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isupper():
            result.append(braille_dict['cap'])
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result.append(braille_dict['num'])
                number_mode = True
        else:
            number_mode = False
        
        result.append(braille_dict[char])
    
    return ''.join(result)

def translate_to_english(braille_text):
    result = []
    i = 0
    capital_mode = False
    number_mode = False
    
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        
        if braille_char == braille_dict['cap']:
            capital_mode = True
        elif braille_char == braille_dict['num']:
            number_mode = True
        elif braille_char == '......':
            result.append(' ')
            number_mode = False
        else:
            char = getCharFromBraille(braille_char, number_mode)
            if capital_mode:
                result.append(char.upper())
                capital_mode = False
            else:
                result.append(char)
        
        i += 6
        
    return ''.join(result)

def main():
    ans = ""
    for i,input_text in enumerate(sys.argv[1:]):
        if all(c in 'O.' for c in input_text):
            ans += translate_to_english(input_text)
        else:
            ans += translate_to_braille(input_text)

            if i<len(sys.argv[1:])-1:
                ans += "......"
    print(ans)

if __name__ == "__main__":
    main()
