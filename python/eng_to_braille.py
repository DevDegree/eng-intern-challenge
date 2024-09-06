english_to_braille_dict = {
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
    ' ': '......',
}

def translate_english(text):
    '''
    expects a text argument of type str
    print a string containing the braille translation of the given text
    '''

    # approach:
    # iterate over each character in the text
    # check for flags: number after text, capital letter, decimal value etc
    # add the necessary braille for the flags to the result 
    # add the value of the character to the result
    # return the result

    result = ''

    for i, char in enumerate(text):
        # process a letter
        if char.isalpha():
            # there is a capital letter, append the "capital follows" braille to the result
            if char.isupper():
                result = result + '.....O'

            result = result + english_to_braille_dict[char.lower()] # append the actual character braille.

        elif char.isdigit(): # process a number
            # if the proccesed character is not a digit, append the number follows braille 
            if result == '' or not text[i-1].isdigit():
                result = result + '.O.OOO'

            val = chr(ord(char)-ord('1')+ord('a')) # letters A-J are used are used to represent digits 0-9
            result = result + english_to_braille_dict[val] # append the resulting braille number to the result
        else:
            result = result + english_to_braille_dict[char] # append all other characters
            
    print(result)