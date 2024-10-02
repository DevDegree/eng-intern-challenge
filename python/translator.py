import sys

def get_to_braille():
    '''
    Initialize and create dictionary that maps 
    alphanumerals and punctuations to their respective 
    braille translations according to the spec
    
    Args: 
        None
        
    Returns:
        tuple: three dictionaries that map the english alphabet to braille
    '''
    alpha_to_braille = {
        'a':'O.....',
        'b':'O.O...',
        'c':'OO....',
        'd':'OO.O..',
        'e':'O..O..',
        'f':'OOO...',
        'g':'OOOO..',
        'h':'O.OO..',
        'i':'.OO...',
        'j':'.OOO..',
        'k':'O...O.',
        'l':'O.O.O.',
        'm':'OO..O.',
        'n':'OO.OO.',
        'o':'O..OO.',
        'p':'OOO.O.',
        'q':'OOOOO.',
        'r':'O.OOO.',
        's':'.OO.O.',
        't':'.OOOO.',
        'u':'O...OO',
        'v':'O.O.OO',
        'w':'.OOO.O',
        'x':'OO..OO',
        'y':'OO.OOO',
        'z':'O..OOO'
    }
    
    num_to_braille = {
        '1':'O.....',
        '2':'O.O...',
        '3':'OO....',
        '4':'OO.O..',
        '5':'O..O..',
        '6':'OOO...',
        '7':'OOOO..',
        '8':'O.OO..',
        '9':'.OO...',
        '0':'.OOO..',
    }
    
    punct_to_braille = {
        '.':'..OO.O',
        ',':'..O...',
        '?':'..O.OO',
        '!':'..OOO.',
        ':':'..OO..',
        ';':'..O.O.',
        '-':'....OO',
        '/':'.O..O.',
        '<':'.OO..O',
        '>':'O..OO.',
        '(':'O.O..O',
        ')':'.O.OO.',
        ' ':'......',
    }
    
    translations = alpha_to_braille, num_to_braille, punct_to_braille
    
    return translations


def reverse_dict(original: dict):
    '''
    Reverses the input dictionary such that
    the key becomes the value, and the value
    becomes the key
    
    Args:
        original (dict): dictionary that maps alpha to braille
    
    Returns
        dict: dictionary that maps braille to alpha
    '''
    return {value: key for key, value in original.items()}


def get_to_alpha():
    '''
    Retruns dictionaries that map braille
    to english alphabet
    
    Args:
        None
        
    Returns
        tuple: tuple of dictionaries that map braille to letters, numbers, and punctuations
    '''
    a_to_b, n_to_b, p_to_b = get_to_braille()
    
    braille_to_alpha = reverse_dict(a_to_b)
    braille_to_num = reverse_dict(n_to_b)
    braille_to_punct = reverse_dict(p_to_b)
    
    translations = braille_to_alpha, braille_to_num, braille_to_punct
    
    return translations
    
    
def is_braille(string: str):
    '''
    Checks if the input string is in braille
    
    Args:
        string (str): string to be checked if braille

    Returns:
        bool: true if the string is in braille, false otherwise
    '''
    # Check if the string contains only 'O' and '.'
    return all(char in 'O.' for char in string)


def translate_alpha(text: str):
    '''
    Translates the given english text
    into braille
    
    Args:
        text(str): text to be translated to braille
    
    Returns:
        str: braille translated text
    '''
    translation = ""
    isnumber = False
    
    upper = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower = set("abcdefghijklmnopqrstuvwxyz")
    num = set("1234567890")
    punct = set(".,?!:;-/<>() ")
    
    alpha, number, punctuation = get_to_braille()
    
    for char in text:
        # if char is a lowercase letter then append translation
        if char in lower:
            translation += alpha[char]
        # if char is an uppercase letter then lower (for dict mapping) and then append
        elif char in upper:
            translation += ".....O" + alpha[char.lower()]
        # if char is a number
        elif char in num:
            # if it is the first number, then append "number follows" braille
            if not isnumber:
                isnumber = True
                translation += ".O.OOO" + number[char]
            else:
                translation += number[char]
        # check whether char is either a decimal or a period
        elif char == ".":
            if isnumber:
                translation += ".O...O"
            else:
                translation += punctuation[char]
        elif char == ' ':
            # if space is at the end of a number then stop appending numbers
            if isnumber:
                isnumber = False
            translation += punctuation[char]
        elif char in punct:
            translation += punctuation[char]
    
    return translation


def segment_text(text: str):
    '''
    Helper function that separates a braille string
    into individual braille characters
    
    Args:
        text(str): Braille string to be segmented
    
    Returns
        list: array of each separated braille character
    '''
    # Use list comprehension to split the string into segments of size 6
    return [text[i:i+6] for i in range(0, len(text), 6)]

def translate_braille(text: str):
    '''
    Translates the given braille string
    into english alphabet
    '''
    translation = ""
    isnumber = False
    iscapital = False
    
    braille = segment_text(text)
    
    alpha, number, punctuation = get_to_braille()
    
    for x in braille:
        if isnumber:
            # if space, end number
            if x == '......':
                isnumber = False
            # if decimal
            elif x == '..OO.O':
                translation += punctuation[x]
            else:
                translation += number[x]
        else:
            # if number follows
            if x == '.O.OOO':
                isnumber = True
            elif iscapital:
                translation += alpha[x].upper()
                iscapital = False
            elif x == '.....O':
                iscapital = True
            else:
                if x in alpha:
                    translation += alpha[x]
                else:
                    translation += punctuation[x]
    
    return translation

if __name__ == '__main__':
    texts = sys.argv[1:]
    translation = ''
    n = len(texts)   # for adding spaces between separate inputs
  
    for i, text in enumerate(texts):
        if is_braille(text):
            translation += translate_braille(text)
            if i < n-1:
                translation += ' '
        else:
            translation += translate_alpha(text)
            if i < n-1:
                translation += '......'
    
    print(translation)
  
  