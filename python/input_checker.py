import sys
from matrix_dict import matrix_dict

def input_checker(s):
    
    md = matrix_dict()

    if len(s) % 6 != 0:
        return 'english'
    else:
        substrings = [s[i:i+6] for i in range(0, len(s), 6)]
        for i in substrings:
            if i not in list(md.values()):
                return 'english'
        
        return 'braille'
