#python linter

## Braille Translator in Python. 

import sys

input_str = sys.argv[1]

global_dict = {'a':"0.....", 'b':'0.0...', 'c':'00....', 'd':'00.0..', 'e':'0..0..', 'f':'000...', 'g':'0000..', 'h':'0.00..', 'i':'.00...', 'j':".000.."\
               'k':'0....0', 'l':'0.0.0.', 'm':'00..0.', 'n':'00.00.', 'o':'0..00.', 'p':'000.0.', 'q':'00000.', 'r':'0.000.', 's':'.00.0.', 't':'.0000.', \
               'u':'0...00', 'v':'0.0.00', 'w':'.000.0', 'x':'00..00', 'y':'00.000', 'z':'0..0000', \
               '1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '0':'j', 'CAP':'.....0', 'DEC':'.0....0', 'NUM':'.0.000', \
               '.':'..00.0', ',':'..0...', '?':'...000', '!':'..000.', ':':'..00..', ';':'..0.0.', '_':'....00', '/':'.0..0.', '<':'.0.0.0', '>':'0.0.0.', \
               '(':'0.0..0', ')':'.0.00.', ' ':'......'}

test_str_e = "XOXOXO" ## --> 00..00 0..00. 00..00 0..00. 00..00 0..00. 
test_str_b = "0.....0.0....0.0000....." ## --> ab1



def main(val):
    ## Main segment:
    ## TO-DO: Language detection [_], English -> Braille [_], Braille -> English [_], output handlerself.
    
    final_lang = lang_converter(lang_detect(val)) # 1 for braille, 0 for english. 
   
    print(final_lang)
    return final_lang



def lang_detect(string):

    base_set = set{'0','.'}
    unique_vars = len(set(string))

    if base_set == unique_vars: # This means it is in braille
        print(base_set + " and " + unique_vars)
        return 1 

    else: # This means it is in english
        return 0 

def lang_converter(): # receives 1 or 2



main(val)


