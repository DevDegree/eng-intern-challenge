## Braille Translator in Python. 
import sys
test = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO'
input_str = ' '.join(sys.argv[1:])
global_dict = {'a':"O.....", 'b':'O.O...', 'c':'OO....', 'd':'OO.O..', 'e':'O..O..', 'f':'OOO...', 
               'g':'OOOO..', 'h':'O.OO..', 'i':'.OO...', 'j':".OOO..", 'k':'O....O', 'l':'O.O.O.', 
               'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.', 'p':'OOO.O.', 'q':'OOOOO.', 'r':'O.OOO.', 
               's':'.OO.O.', 't':'.OOOO.', 'u':'O...OO', 'v':'O.O.OO', 'w':'.OOO.O', 'x':'OO..OO', 
               'y':'OO.OOO', 'z':'O..OOO', '1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', 
               '7':'g', '8':'h', '9':'i', '0':'j', 'CAP':'.....O', ' ':'......', 'NUM':'.O.OOO'}
keys = list(global_dict.keys())
values = list(global_dict.values()) # use this string to index the translation of the characters. Example: 'O.....' indexes 0, thrown into keys[0] gives 'a'. 

def main(val):
    if val == '':
        return ''
    final_msg = lang_converter(lang_detect(val), val) # 1 for braille, 0 for english. 
    print(final_msg)
    return final_msg

def lang_detect(string):
    if set(['O','.']) == set(string): # This means it is in braille
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

            if snippet == '......': # Catches space after numlock and disables num flag
                if mode == 2:
                    mode = 0
                char_start += 6
                char_end += 6
                message += char_retrieval(snippet, mode)

            elif snippet == '.....O': # sets the mode for an uppercase 
                mode = 1
                if (char_end + 6) <= len(val):
                    char_end += 6 
                    char_start += 6

            elif mode == 1:
                message += char_retrieval(snippet, mode)
                char_end += 6
                char_start += 6
                mode = 0

            elif snippet == '.O.OOO': ## Needs to stay num's locked until a space occurs
                mode = 2
                if (char_end + 6) <= len(val):
                    char_end += 6
                    char_start += 6
            elif snippet in values:
                char_end += 6
                char_start += 6
                message += char_retrieval(snippet, mode)
            else:
                char_end += 6
                char_start += 6

        return message

    else:
        message = ''
        eng_text = list(val)
        i = 0
        mode = 0
        while i < len(eng_text): ## Processes english alphanum into braille

            if str(eng_text[i]) == ' ':
                mode = 0
                message += str(global_dict[' '])

            if eng_text[i].isupper() == True:
                message += str(global_dict['CAP'])
                message += str(global_dict[eng_text[i].lower()])
                i += 1

            elif eng_text[i].isnumeric() == True:
                if mode == 1:
                    message += str(global_dict[global_dict[eng_text[i]]])
                    i += 1
                
                else:
                    message += str(global_dict['NUM'])
                    message += str(global_dict[global_dict[eng_text[i]]])
                    mode = 1
                    i += 1

            elif eng_text[i].isalpha():
                message += str(global_dict[eng_text[i]])
                i += 1 
            else:
                i += 1

        return message

def char_retrieval(snippet, mode):
    if mode == 1: # returns uppercase
        return keys[values.index(snippet)].upper()
    elif mode == 2: #returns numeric value
        return keys[values.index(keys[values.index(snippet)])]
    else: # base case
        return keys[values.index(snippet)]


main(input_str)

