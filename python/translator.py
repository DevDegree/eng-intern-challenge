import sys

# Gather arguments from command line (not getting script name)
args = sys.argv[1:] 

# Create dictionary for the Braille Alphabet
eng_to_braille_map = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO',

    'capital' : '.....O',
    'decimal' : '.O...O',
    'number' : '.O.OOO',
    ' ' : '......'
}

nums_map = {
    'O' : '.OOO..',
    '1' : 'O.....',
    '2' : 'O.O...',
    '3' : 'OO....',
    '4' : 'OO.O..',
    '5' : 'O..O..',
    '6' : 'OOO...',
    '7' : 'OOOO..',
    '8' : 'O.OO..',
    '9' : '.OO...'
}


# Invert maps to Braille to English
braille_to_eng_map = {v:k for k, v in eng_to_braille_map.items()}
braille_nums_map = {v:k for k, v in nums_map.items()}

# Checks input command and determines whether it is in English or Braille then translate it
def check_input(input): 
    if len(input) >= 1 and all(char in '.O' for char in input[0]):
        print(braille_to_text(input[0]))
    else:
        translation = ''
        for value in input:
            translation += text_to_braille(value)
        print(translation) 

# Translates Braille input and outputs English string
def braille_to_text(braille):
    result = []

    # Seperate braille input into the 6 symbol blocks representing each character
    braille_6block = []
    for i in range(0, len(braille), 6):
        chunk = braille[i:i + 6]  # Slice the braille string from index i to i + 6
        braille_6block.append(chunk)

    i = 0
    while i < len(braille_6block):
        current_char = braille_6block[i]

        # check for braille capital then get next 6block and append character
        if current_char == eng_to_braille_map['capital']:
            i+=1
            result.append(braille_to_eng_map.get(braille_6block[i], '').upper())
        # check for braille number then get next 6block and append the number
        elif current_char == eng_to_braille_map['number']:
            i+=1
            # check when there is a space at the end of number
            while i < len(braille_6block) and i != braille_6block[i] and i != eng_to_braille_map[' ']:
                result.append(braille_nums_map.get(braille_6block[i], ''))
                i+=1
        # regular characters
        else:
            result.append(braille_to_eng_map.get(current_char, ''))
        i+=1
    return ''.join(result)

# Translate text input and outputs braille string
def text_to_braille(text):
    b_result = []
    # check if there are multiple numbers in a row
    num_flag = False 

    for char in text: 
        if char.isdigit():
            if not num_flag:
                b_result.append(eng_to_braille_map['number'])
                num_flag = True
            b_result.append(nums_map[char])  
        else:
            # switch num_flag back if it is true
            if num_flag:
                num_flag = False
                b_result.append(eng_to_braille_map[' '])
            if char.isupper():    
                b_result.append(eng_to_braille_map['capital'] + eng_to_braille_map[char.lower()])
                print(char + 'upper')
            elif char.islower():
                b_result.append(eng_to_braille_map[char])
                print(char + 'lower')
            #get characters that are symbols (. , > < / etc)   
            else:
                b_result.append(eng_to_braille_map.get(char, ''))
                print(char + 'else')        
    return ''.join(b_result)

check_input(args)
