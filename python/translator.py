import sys

alphabet_to_braille = {
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
    'capital_follows': '.....O',
    'number_follows': '.O.OOO'
}

number_to_braille = {
    '1' : 'O.....', 
    '2' : 'O.O...',
    '3' : 'OO....',
    '4' : 'OO.O..',
    '5' : 'O..O..',
    '6' : 'OOO...',
    '7' : 'OOOO..',
    '8' : 'O.OO..',
    '9' : '.OO...',
    '0' : '.OOO..'
}

braille_to_alphabet = {value: key for key, value in alphabet_to_braille.items()}
braille_to_number = {value: key for key, value in number_to_braille.items()}


def detect_language(tokens):
    '''
    Detects if a sequence of tokens is an english or braille sequence
    '''
    if len(tokens) % 6 != 0:
        return "english"
    
    else:
        alphabet = set()

        for c in tokens:
            alphabet.add(c)

        if len(alphabet) == 2:
            if 'O' in alphabet and '.' in alphabet:
                return "braille"
            else:
                return "english"
        else:
            return "english"


def braille_to_english(tokens):
    '''
    Translates an array of braille tokens to an array of english tokens
    '''
    
    braille_tokens = []
    english_tokens = []

    for i in range(0, len(tokens), 6):
        braille_tokens.append(tokens[i:i+6])
    
    is_capital = False
    is_number = False
    
    for braille_token in braille_tokens:
        char = braille_to_alphabet[braille_token]

        # check if space first
        if char == ' ':
            is_number = False
            is_capital = False
        elif char == 'capital_follows':
            is_capital = True
            is_number = False
        elif char == 'number_follows':
            is_number = True
            is_capital = False
        else:
            if is_capital:
                char = braille_to_alphabet[braille_token].capitalize()
                is_capital = False

            elif is_number:
                char = braille_to_number[braille_token]
        
        
        english_tokens.append(char)
    
    # clean up english array
    for token in english_tokens:
        if token == 'capital_follows' or token == 'number_follows':
            english_tokens.remove(token)
            
    
    
    return english_tokens


def english_to_braille(tokens):

    
    braille_tokens = []

    is_number = False
    
    for token in tokens:
        if str.isspace(token):
            is_number = False
            braille_tokens.append(alphabet_to_braille[" "])
        elif str.isalpha(token):
            is_number = False
            if str.isupper(token):
                token = token.lower()
                braille_tokens.append(alphabet_to_braille['capital_follows'])
                braille_tokens.append(alphabet_to_braille[token])
            else:
                braille_tokens.append(alphabet_to_braille[token])
        elif str.isdigit(token):
            if is_number == True:
                braille_tokens.append(number_to_braille[token])
            else:
                is_number = True
                braille_tokens.append(alphabet_to_braille['number_follows'])
                braille_tokens.append(number_to_braille[token])
        

    #print(braille_tokens)
    return braille_tokens
            
            
def main():
    tokens = ' '.join(sys.argv[1:])
    
    translation = ''

    # determine whether it's an alphanumeric string or braille string
    # print(detect_language(tokens))

    language = detect_language(tokens)

    if language == "braille":
        translation = braille_to_english(tokens)
        
    elif language == "english":
        translation = english_to_braille(tokens)

    translation =''.join(translation)
    print(translation)

   



if __name__ == '__main__':
    main()
