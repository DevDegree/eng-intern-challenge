#!/usr/bin/env python
# coding: utf-8

# In[286]:


alphabet = {'a': 'O.....',
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
            ' ': '......',}

part_1 = {'a': 'O.....',
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
                    ' ': '......',}

braille_alphabet = {v: k for k, v in part_1.items()}

part_2 = {'1': 'O.....',
                   '2': 'O.O...',
                   '3': 'OO....',
                   '4': 'OO.O..',
                   '5': 'O..O..',
                   '6': 'OOO...',
                   '7': 'OOOO..',
                   '8': 'O.OO..',
                   '9': '.OO...',
                   '0': '.OOO..',}

braille_numeric = {v: k for k, v in part_2.items()}


# In[287]:


def english_to_braille(english):
    

    braille = ''
    first_numeric = False
    for i in english:
        if i.isupper() == True:
            braille += ''.join(['.....O', alphabet[i.lower()]])
        elif i == '.':
            braille += ''.join(['.O...O', alphabet[i]])
        elif i.isnumeric() == True and first_numeric == False:
            braille += ''.join(['.O.OOO', alphabet[i]])
            first_numeric = True
        else:
            braille += alphabet[i]
            
    return braille


# In[291]:


def braille_to_english(braille):
    
    braille_sliced = [braille[i:i+6] for i in range(0, len(braille), 6)]

    english = ''
    numeric = False
    for i in range(len(braille_sliced)):
        if braille_sliced[i] == '.....O':
            english += braille_alphabet[braille_sliced[i+1]].upper()
            continue
        elif braille_sliced[i] == '.O...O':
            english += braille_alphabet[braille_sliced[i+1]]
            continue
        elif braille_sliced[i] == '.O.OOO':
            numeric = True
            continue
        elif braille_sliced[i] == '......':
            numeric = False
            continue
    
        if numeric == True:
            if braille_sliced[i] in braille_numeric:
                english += braille_numeric[braille_sliced[i]]
        else: 
            if braille_sliced[i] in braille_alphabet:
                english += braille_alphabet[braille_sliced[i+1]]
    
    return english


# In[292]:


def main():
    
    try:
        user_input = input()
    
        if set(user_input).issubset({'.', 'O'}) == True:
            answer = braille_to_english(user_input)
        else:
            answer = english_to_braille(user_input)
        
        print(answer)
        
    except KeyError:
        print('Invalid input')

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




