from braille_data import RAISED_DOT, BLANK_DOT, record_of_chars, record_of_01_braille_letters, record_of_01_braille_numbers

def get_braille_from_list(braille_definition_list):
    '''
    Args:
        A list of the 0 and 1 denotion of a braille character

    Returns:
        Corresponding braille string
    '''

    return ''.join(list(map(lambda x: RAISED_DOT if x else BLANK_DOT, braille_definition_list)))

def construct_braille_char(c):
    '''
    Args: 
        A single character or 'space','numberfollows'
        to be converted to braille

    Returns:
        Corresponding braille for that character
    '''
    ans = ''
    if c.isupper():
        ans += get_braille_from_list(record_of_chars['capitalfollows'])
        c = c.lower()
    braille_list = record_of_chars[c]

    ans += get_braille_from_list(braille_list)
    return ans


def convert_to_parseable_string_list(s):
    '''
    Args:
        The input string in English

    Returns:
        list of String with references to start of number and 'space'
    '''
    ans = []
    i = 0
    while i < len(s):
        if s[i] == ' ':
            ans.append('space')
            i += 1
        elif s[i].isdigit():
            ans.append('numberfollows')
            while i < len(s) and s[i].isdigit():
                ans.append(s[i])
                i += 1
        else:
            ans.append(s[i]) 
            i += 1

    return ans

def string_list_to_braille_string(string_list):
    '''
    Args:
        Parseable string list generated from convert_to_parseable_string_list(s)

    Returns: 
            Entire input string in braille
    '''
    ans = ''
    for i in string_list:
        ans += construct_braille_char(i)

    return ans

def convert_input_string_to_brailled_string(input_string):
    '''
    Args:
    The input string

    Returns:
    The output Braille
    '''
    parseable_string_list = convert_to_parseable_string_list(input_string)
    ans = string_list_to_braille_string(parseable_string_list)
    return ans

def identify_English_or_braille(input_string):
    '''
    Args:
    The input string

    Returns:
    0 for English, 1 for Braille text
    '''
    for char in input_string:
        if char not in [RAISED_DOT, BLANK_DOT]:
            return 0
        
    return 1

def convert_braille_to_chunks(input_string):
    '''
    Args:
        Input string

    Returns:
        List of braille chars
    '''
    return [input_string[i:i+6] for i in range(0, len(input_string), 6)]

def convert_chunks_to_01(l):
    '''
    Args: 
        List of 6 char chunks of input string
    Returns:
        converts raised dot and blank dot to 0 1
    '''
    ans = []
    for i in l:
        s = ''
        for j in i:
            if j == RAISED_DOT:
                s += '1'
            else:
                s += '0'
        ans.append(s)

    return ans

def convert_01_to_chars(l):
    '''
    Args:
        list of 6 char chunks of 01
    Returns:
        corresponsing english char or space or number follows
    '''
    ans = []
    for i in range(len(l)):
        if l[i] not in record_of_01_braille_letters and l[i] not in record_of_01_braille_numbers:
            print("Error")
        else:
            if i == 0 or (ans[i-1] not in '1234567890' and ans[i-1] != 'numberfollows'):
                ans.append(record_of_01_braille_letters[l[i]])
            else:
                ans.append(record_of_01_braille_numbers[l[i]])
            

    return ans

def convert_parseable_string_list_to_output_string(l):
    '''
    Args:
        Parseable string list that is output of convert_01_to_chars

    Returns:
        Output string
    '''

    ans = ''
    i = 0
    while i < (len(l)):
        if l[i] == 'numberfollows':
            pass
        elif l[i] == 'capitalfollows':
            ans += l[i+1].upper()
            i += 1
        elif l[i] == 'space':
            ans += ' '
        else:
            ans += l[i]
        i += 1

    return ans

def convert_braille_to_English(input_string):
    '''
    Args:

    Returns:
    '''
    if len(input_string) % 6:
        return 'Improper Input'
    
    ans = convert_braille_to_chunks(input_string)
    ans = convert_chunks_to_01(ans)
    ans = convert_01_to_chars(ans)
    ans = convert_parseable_string_list_to_output_string(ans)
    return ans
    

    
