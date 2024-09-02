#python linter

## Braille Translator in Python. 

import sys

#input_str = sys.argv[1]

global_dict = {'a':"0.....", 'b':'0.0...', 'c':'00....', 'd':'00.0..', 'e':'0..0..', 'f':'000...', 
               'g':'0000..', 'h':'0.00..', 'i':'.00...', 'j':".000..", 'k':'0....0', 'l':'0.0.0.', 
               'm':'00..0.', 'n':'00.00.', 'o':'0..00.', 'p':'000.0.', 'q':'00000.', 'r':'0.000.', 
               's':'.00.0.', 't':'.0000.', 'u':'0...00', 'v':'0.0.00', 'w':'.000.0', 'x':'00..00', 
               'y':'00.000', 'z':'0..0000', '1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', 
               '7':'g', '8':'h', '9':'i', '0':'j', 'CAP':'.....0', ' ':'......', 'NUM':'.0.000'}

test_str_e = "XOXOXO" ## --> 00..00 0..00. 00..00 0..00. 00..00 0..00. 
test_str_b = "0.....0.0....0.0000....." ## --> ab1

keys = list(global_dict.keys())
values = list(global_dict.values()) # use this string to index the translation of the characters. Example: '0.....' indexes 0, thrown into keys[0] gives 'a'. 


def main(val):
    ## Main segment:
    ## TO-DO: Language detection [_], English -> Braille [_], Braille -> English [_], output handlerself.
    
    final_msg = lang_converter(lang_detect(val), val) # 1 for braille, 0 for english. 
   
    print(final_msg)
    return final_msg



def lang_detect(string):

    if set(['0','.']) == set(string): # This means it is in braille
#        print(str(set(['0','.'])) + " and " + str(set(string)))
        return 1 

    else: # This means it is in english
        return 0 

def lang_converter(convertee, val): # receives 0 or 1 and terminal value
    
    if convertee == 1:
        char_end = 6 
        char_start = 0
        message = ''
        mode = 0 # 0 is lowercase alpha, 1 is uppercase alpha, 2 is numeric. 

        while char_end <= len(val): # grabs set of 6 characters to be converted from braille to english
            snippet = val[char_start:char_end]
            
            if snippet == '.....0':
                mode = 1
                if (char_end + 6) <= len(val):
                    char_end += 6 
                    char_start += 6


            elif snippet == '.0.000':
                mode = 2
                if (char_end + 6) <= len(val):
                    char_end += 6 
                    char_start += 6


            else:
                char_end += 6 
                char_start += 6
                message += char_retrieval(snippet, mode)
                mode = 0
        return message


def char_retrieval(snippet, mode):
    if mode == 1: # returns uppercase
        return keys[values.index(snippet)].upper()
    elif mode == 2: #returns numeric value
        return keys[values.index(keys[values.index(snippet)])]
    else: # base case
        return keys[values.index(snippet)]


main(test_str_b)


