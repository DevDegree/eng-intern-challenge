
# Dictionary for translating letters from Braille to English
BRAILLE_TO_ENGLISH = {
    'O.....' : 'a',
    'O.O...' : 'b',
    'OO....' : 'c',
    'OO.O..' : 'd',
    'O..O..' : 'e',
    'OOO...' : 'f',
    'OOOO..' : 'g',
    'O.OO..' : 'h',
    '.OO...' : 'i',
    '.OOO..' : 'j',
    'O...O.' : 'k',
    'O.O.O.' : 'l',
    'OO..O.' : 'm',
    'OO.OO.' : 'n',
    'O..OO.' : 'o',
    'OOO.O.' : 'p',
    'OOOOO.' : 'q',
    'O.OOO.' : 'r',
    '.OO.O.' : 's',
    '.OOOO.' : 't',
    'O...OO' : 'u',
    'O.O.OO' : 'v',
    '.OOO.O' : 'w',
    'OO..OO' : 'x',
    'OO.OOO' : 'y',
    'O..OOO' : 'z',
    '.....O' : 'capital follows',
    '.O.OOO' : 'number follows',
}

BRAILLE_TO_ENGLISH_NUM ={
    'O.....' : '1',
    'O.O...' : '2',
    'OO....' : '3',
    'OO.O..' : '4',
    'O..O..' : '5',
    'OOO...' : '6',
    'OOOO..' : '7',
    'O.OO..' : '8',
    '.OO...' : '9',
    '.OOO..' : '0',
}
BRAILLE_SPECIAL_CHARS = {
    '..OO.O' : '.',
    '..O...' : ',',
    '..O.OO' : '?',
    '..OOO.' : '!',
    '..OO..' : ':',
    '..O.O.' : ';',
    '....OO' : '-',
    '.O..O.' : '/',
    '.OO..O' : '<',
    'O..OO.' : '>',
    'O.O..O' : '(',
    '.O.OO.' : ')',
    '......' : ' ',
}
# Converting the above dictionary into a english by reversing the values of keys and values
ENGLISH_TO_BRAILLE = {eng_alphabet: braille for braille, eng_alphabet in BRAILLE_TO_ENGLISH.items()}
ENGLISH_TO_BRAILLE_NUM = {num: braille for braille, num in BRAILLE_TO_ENGLISH_NUM.items()}
ENGLISH_TO_BRAILLE_SPECIAL = {spec: braille for braille, spec in BRAILLE_SPECIAL_CHARS.items()}

# function to check if the input is only braille '.0'
def check_if_braille(string):
    for char in string:
        if char == '.':
            continue
        elif char == 'O':
            continue
        else:
            return False
    return True

# function to translate braille to english
def braille_to_english(string):
    english_output = ''
    num_follows = False
    capital_follows = False
    i = 0
    
    while i < len(string):
        braille_text = string[i:i+6]
        # Check for capital follows symbol
        if braille_text in BRAILLE_TO_ENGLISH and BRAILLE_TO_ENGLISH[braille_text] == 'capital follows':
            capital_follows = True
            i += 6
            continue
        # Check for number follows symbol
        elif braille_text in BRAILLE_TO_ENGLISH and BRAILLE_TO_ENGLISH[braille_text] == 'number follows':
            num_follows = True
            i += 6
            continue
        # Check if it's a letter or number
        if num_follows and braille_text in BRAILLE_TO_ENGLISH_NUM:
            # add number to the output
            english_output += BRAILLE_TO_ENGLISH_NUM[braille_text]
        elif braille_text in BRAILLE_TO_ENGLISH:
            # add letter to the output
            if capital_follows:
                # capitalize the letter
                english_output += BRAILLE_TO_ENGLISH[braille_text].upper()
                # reset capital follows so that only one capital letter is added
                capital_follows = False
            else:
                english_output += BRAILLE_TO_ENGLISH[braille_text]
        
        # Check if it's a special character
        elif braille_text in BRAILLE_SPECIAL_CHARS:
            english_output += BRAILLE_SPECIAL_CHARS[braille_text]
        i += 6
        # Reset number mode when a space is encountered
        if braille_text in BRAILLE_SPECIAL_CHARS and BRAILLE_SPECIAL_CHARS[braille_text] == ' ': 
            num_follows = False
    
    return english_output

# function to translate english to braille

def english_to_braille(string):
    braille_output = ''
    num_follows = False

    for char in string:
        # Check for capital letter
        if char.isupper():
            # add capital follows and letter to the output
            braille_output += ENGLISH_TO_BRAILLE['capital follows'] + ENGLISH_TO_BRAILLE[char.lower()]
        # Check for number
        elif char.isnumeric():
            # add number follows to the output
            if not num_follows:
                braille_output += ENGLISH_TO_BRAILLE['number follows']
                num_follows = True
            # add number to the output
            braille_output += ENGLISH_TO_BRAILLE_NUM[char]
        # Check for special character
        elif not char.isalnum():
            # check if it's a space if it is add the space to the output and number follows is reset
            if char == ' ':
                braille_output += ENGLISH_TO_BRAILLE_SPECIAL[' ']
                num_follows = False
            else:
                # add special character to the output
                braille_output += ENGLISH_TO_BRAILLE_SPECIAL[char]
        else:
            # add letter to the output
            braille_output += ENGLISH_TO_BRAILLE[char]
    return braille_output


#use the above two functions to translate
def braille_and_english_translator(string):
    if check_if_braille(string):
        # if the input is only braille '.0'
        return braille_to_english(string)
    else:
        # if the input is english
        return english_to_braille(string)

if __name__ == '__main__':
    import sys
    input_string = " ".join(sys.argv[1:])
    print(braille_and_english_translator(input_string))

    

