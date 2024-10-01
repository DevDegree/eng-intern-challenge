import sys # imports the sys module to take command line arguments

line = sys.argv[1:] # takes the arguments and puts them into a set

def is_braille(text):
    return all(char in {'O', '.', ' '} for char in text) # checks if the text is in braille

def is_english(text):
    return all(char.isalnum() or char.isspace() for char in text) # checks if the text is in english

# braille dictionary (converting from english to braille)
braille_dict = {
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
    'p': 'OOOO..',
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
    ' ': '......'
}

# braille dictionary (converting from braille to english letters)
# setting keys to values and vice versa only for letters and the space character
braille_to_char = {v: k for k, v in braille_dict.items() if k.isalpha() or k == ' '}

# braille dictionary (converting from braille to numbers)
# we need a separate dictionary for numbers, because the numbers are represented by the 
# same braille characters as the letters
braille_to_char_num = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
}
# joins the arguments into a single string (for english to braille conversion)
combined = ' '.join(line)


conv = '' # create empty string for the converted text
capital_follows = False # boolean to check if the next character is uppercase
number_follows = False # boolean to check if the next character is a number

# if the text is in english, translate it to braille
if is_english(combined):
    # loop through each character in the combined string
    for char in combined:
        # if the character is uppercase, add the braille for 'capital follows' rule and the braille for the lowercase version of the character 
        if char.isupper():
            conv += '.....O' + braille_dict[char.lower()]
        
        # if the character is a digit (number), add the braille for the 'number follows' rule and the braille for the digit itself
        elif char.isdigit():
            if not number_follows:
                conv += '.O.OOO'
                number_follows = True
            conv += braille_dict[char]
        
        # if the character is a space, add the braille for 'space'
        elif char == ' ':
            conv += '......'
            # reset the number_follows rule to False
            number_follows = False
        else:
            # add the braille for the character itself
            conv += braille_dict[char.lower()]

# if the text is in braille
else:
    # split the braille into words
    words = []
    # create an empty string for the current word
    current_word = ''

    # loop through the combined string with a step size of 6
    # since an alphanumeric character is 6 characters of 'O's and '.'s long
    for i in range(0, len(combined), 6):
        # get the current character
        char = combined[i:i+6]
        # if the character is a space, add the current word to the words list 
        # and reset the current word
        if char == '......':
            if current_word:
                words.append(current_word)
                current_word = ''
        
        # if the character is the braille for 'capital follows' rule, set the capital_follows rule to True
        elif char == '.....O':
            capital_follows = True
        
        # if the character is the braille for 'number follows' rule, set the number_follows rule to True
        elif char == '.O.OOO':
            number_follows = True
        
        # if the character is in the braille_to_char dictionary, add the corresponding character to the current word
        elif char in braille_to_char:
            
            # if the preceding character was a number and the character is in the braille_to_char_num dictionary, 
            # add the corresponding number to the current word
            if number_follows and char in braille_to_char_num:
                current_word += braille_to_char_num[char]
            
            # if the preceding character was a capital letter, add the corresponding uppercase character to the current word
            elif capital_follows:
                current_word += braille_to_char[char].upper()
                capital_follows = False
            
            # if the character is not in the braille_to_char_num dictionary, add the corresponding lowercase character to the current word
            else:
                current_word += braille_to_char[char]


    # if the current word is not empty, add it to the words list
    if current_word:
        words.append(current_word)

    # join the words list into a single string with spaces between each word
    conv = ' '.join(words)

# print the converted text without a newline
print(conv, end='')