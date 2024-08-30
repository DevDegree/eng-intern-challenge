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
    'decimal follows': '.O...O',
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
    
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    
    'space': '......',
}

key_list = list(english_to_braille.keys())
val_list = list(english_to_braille.values())

val = input()
translation = ""

i = 0
n = 0

# .....OO.....O.O...OO....
# numbers = 29 to 38
# decimals = 39 to 50

while n < len(val):
    # print(val[i:i+6])
    if val_list.index(val[n:n+6]):
        
        if val[n:n+6] == english_to_braille['capital follows']:
            n+=6
            found = val_list.index(val[n:n+6])
            translation+= key_list[found].upper()
            i+=1
            n+=6
        
        elif val[n:n+6] == english_to_braille['number follows']:
            n+=6
            found = val_list.index(val[n:n+6], 29, 38)
            translation+= key_list[found]
            i+=1
            n+=6
            
        elif val[n:n+6] == english_to_braille['space']:
            found = val_list.index(val[n:n+6])
            translation+= ' '
            i+=1
            n+=6
            
        elif translation[i-1].isdigit():
            found = val_list.index(val[n:n+6], 29, 38)
            translation+= key_list[found]
            i+=1
            n+=6
        
        elif val[n:n+6] == english_to_braille['decimal follows']:
            n+=6
            found = val_list.index(val[n:n+6])
            translation+= key_list[found]
            i+=1
            n+=6
            
        
        else:
            found = val_list.index(val[n:n+6])
            translation+= key_list[found]
            i+=1
            n+=6
    
    else:
        
        if n.isalpha():
            if n.isspace():
                translation += english_to_braille['space']
                i+=1
            elif n.isupper():
                translation += english_to_braille['capital follows']
                translation += english_to_braille[n.lower()]
                i+=1
            else:
                translation += english_to_braille[n]
                i+=1
            n+=1
        
        elif n.isdigit():
            if val[n-6:n] == english_to_braille['number follows']:
                translation += english_to_braille['number follows']
                translation += english_to_braille[n]
                i+=1
            elif n.isspace():
                translation += english_to_braille['space']
                i+=1
            else:
                translation += english_to_braille[n]
                i+=1
            n+=1
        



    
print(translation)

