import sys

english_to_braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    
    'capital follows': '.....O',
    'number follows': '.O.OOO',
    
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    
    'space': '......',
}


def main(val):
    
    key_list = list(english_to_braille.keys())
    val_list = list(english_to_braille.values())

    translation = []

    i = 0
    n = 0

    while n < len(val):
        
        
        try:    
            # Braille to English translation
            # Checks whether n to n+6 match braille values in val_list to begin braille to english translation. Throws error if nothing is found
            if val_list.index(val[n:n+6]):
                
                if val[n:n+6] == english_to_braille['capital follows']:
                    n+=6
                    found = val_list.index(val[n:n+6])
                    translation.append(key_list[found].upper())
                    i+=1
                    n+=6
                
                elif val[n:n+6] == english_to_braille['number follows']:
                    n+=6
                    found = val_list.index(val[n:n+6], 28, 37)
                    translation.append(key_list[found])
                    i+=1
                    n+=6
                    
                elif val[n:n+6] == english_to_braille['space']:
                    found = val_list.index(val[n:n+6])
                    translation.append(' ')
                    i+=1
                    n+=6
                    
                elif translation[i-1].isdigit():
                    found = val_list.index(val[n:n+6], 28, 37)
                    translation.append(key_list[found])
                    i+=1
                    n+=6
                    
                else:
                    found = val_list.index(val[n:n+6])
                    translation.append(key_list[found])
                    i+=1
                    n+=6
        
        except:
            
            # English to Braille translation
            if val[n].isalpha():
                    
                if val[n].isupper():
                    translation.append(english_to_braille['capital follows'])
                    translation.append(english_to_braille[val[n].lower()])
                    n+=1
                    i+=6
                    
                else:
                    translation.append(english_to_braille[val[n]])
                    n+=1
                    i+=6    
                        
            elif val[n].isspace():
                translation.append(english_to_braille['space'])
                i+=6
                n+=1
                
            elif val[n].isdigit():
                if val[n-1].isdigit():
                    translation.append(english_to_braille[val[n]])
                    i+=6
                    n+=1
                    
                else:
                    translation.append(english_to_braille['number follows'])
                    translation.append(english_to_braille[val[n]])
                    i+=6
                    n+=1
                    
            
    return ''.join(translation)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = ' '.join(sys.argv[1:])
        print(main(input.strip()))
    else:
        print("Invalid input. Please try again")