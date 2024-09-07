'''
Name: Oluwasina Olowookere,
Email: oluwsinaalex@gmail.com,
'''
import sys

'''
My thought process is to create a dictionary 
that maps each letter to its corresponding Braille pattern.
I wanted to see if I could do this programmatically without hardcoding the patterns,
because I researched and found that the Braille alphabet are repeating patterns. i.e 
A-J only use a combination of the first 4 dots in the 3x2 matrix.
K-T repeat the pattern of A-J but with an added dot in the bottom left corner.
U-Z repeat the pattern of A-J but with the last row filled out.
W is unique and has a different pattern altogether.
Numbers are also repeating the A-J pattern but follow a number decorator.

In the end, I aimed for readability and simplicity of the code.
'''

# Braille patterns for each letter and special characters excluding punctuations as per the technical requirements.
braille_patterns = {
    'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
    'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
    'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
    'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
    'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
    'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
    'y': 'OO.OOO',    'z': 'O..OOO',    ' ': '......',
    'capital': '.....O',  'number': '.O.OOO'
}

# Create reverse dictionary for Braille to English
english_patterns = {v: k for k, v in braille_patterns.items()}


def english_to_braille(text):
    result = []
    number_mode = False #Flag to indicate the start of a number sequence
    
    for char in text:
        if char.isupper():
            result.append(braille_patterns['capital'])
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result.append(braille_patterns['number'])
                number_mode = True
            result.append(braille_patterns[chr(ord(char) - ord('0') + ord('a'))])
        elif char.isalpha() or char == ' ':
            if number_mode:
                number_mode = False
            result.append(braille_patterns[char])
    
    return ''.join(result)
