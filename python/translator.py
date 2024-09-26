import sys

# Braille mappings 
braille_to_eng_map = {
    'O.....': 'A', 
    'O.O...': 'B', 
    'OO....': 'C', 
    'OO.O..': 'D', 
    'O..O..': 'E',
    'OOO...': 'F', 
    'OOOO..': 'G', 
    'O.OO..': 'H', 
    '.OO...': 'I', 
    '.OOO..': 'J',
    'O...O.': 'K', 
    'O.O.O.': 'L', 
    'OO..O.': 'M', 
    'OO.OO.': 'N', 
    'O..OO.': 'O/>', #Conflicted letter O and symbol >
    'OOO.O.': 'P', 
    'OOOOO.': 'Q', 
    'O.OOO.': 'R', 
    '.OO.O.': 'S', 
    '.OOOO.': 'T',
    'O...OO': 'U', 
    'O.O.OO': 'V', 
    '.OOO.O': 'W', 
    'OO..OO': 'X', 
    'OO.OOO': 'Y',
    'O..OOO': 'Z', 
    '.....O': '^', # Capital follows
    '.O...O': '_', # Decimal follows
    '.O.OOO': '#', # Number follows
    '..OO.O': '.',
    '..O...': ',', 
    '..O.OO': '?', 
    '..OOO.': '!',
    '..OO..': ':', 
    '..O.O.': ';', 
    '....OO': '-', 
    '.O..O.': '/',
    '.OO..O': '<', 
    'O.O..O': '(', 
    '.O.OO.': ')',
    '......': ' ' # Space
}


eng_to_braille_map = {v: k for k, v in braille_to_eng_map.items() if v != 'O/>'} 
eng_to_braille_map['O'] = 'O..OO.'
eng_to_braille_map['>'] = 'O..OO.'

# Number mappings
num_map = {'A': '1', 
           'B': '2', 
           'C': '3', 
           'D': '4', 
           'E': '5',
           'F': '6', 
           'G': '7', 
           'H': '8',
           'I': '9',
           'J': '0'
             }


def br_to_eng(braille):
    result = []
    i = 0
    cap_next = False
    num_mode = False

    while i < len(braille):
        char = braille[i:i+6]
        
        if char == '.....O':  # Capital follows
            cap_next = True
            i += 6
            continue
    
        elif char == '.O.OOO':  # Number follows
            num_mode = True
            i += 6
            continue
            
        elif char == '.O...O':  # Decimal follows
            result.append('.')
            i += 6
            continue
            
        elif char == '......':  # Space Follows
            result.append(' ')
            num_mode = False 
            i += 6
            continue
            
        elif char in braille_to_eng_map:
            letter = braille_to_eng_map[char]
            
        # Context-based decision for '>' or 'O'
            if letter == 'O/>':
                if num_mode:
                    letter = '>'
                else:
                    if i > 0 and result and result[-1] in [' ', '.', ',', '!', '?', ':', ';', '']:
                        letter = '>'
                    else:
                        letter = 'O'
                                                            
                    
            if num_mode and letter in num_map:
                result.append(num_map[letter]) 
                
            else:
                num_mode = False 
                if cap_next:
                    result.append(letter.upper())
                    cap_next = False
                else:
                    result.append(letter.lower())

        i += 6
    
    return ''.join(result) 



def eng_to_br(txt):
    result = []
    num_mode = False
    
    for char in txt:
        if char.isdigit():
            if not num_mode:
                result.append(eng_to_braille_map['#'])   #Handle numbers
                num_mode = True
            letter = [k for k, v in num_map.items() if v == char][0]
            result.append(eng_to_braille_map[letter])
        elif char == '.':
            if num_mode:
                result.append(eng_to_braille_map['_'])  # Handle decimals 
            else:
                result.append(eng_to_braille_map['.'])  # Regular period
        else:
            if char == ' ':
                result.append(eng_to_braille_map[' '])  # Handle spaces
                num_mode = False
            elif char.isupper():
                result.append(eng_to_braille_map['^'])  # Handle capital sign
                result.append(eng_to_braille_map[char])
                num_mode = False
            elif char.upper() in eng_to_braille_map:
                result.append(eng_to_braille_map[char.upper()])
                num_mode = False
            else:
                if char in eng_to_braille_map:
                    result.append(eng_to_braille_map[char])
                    num_mode = False
    
    
    return ''.join(result)



def translate(txt):  # Detect if the input is Braille or English
    if set(txt).issubset({'O', '.'}):
        return br_to_eng(txt)
    else:
        return eng_to_br(txt)

    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_txt = ' '.join(sys.argv[1:])
        result = translate(input_txt)
        print(result)
