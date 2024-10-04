#import sys

#body = str(sys.argv[1])
##Tried to do the function in one line, but it could not handle spaces.

body = str(input())

bdict_alpha = {"a":"O.....",
               "b":"O.O...",
               "c":"OO....",
               "d":"OO.O..",
               "e":"O..O..",
               "f":"OOO...",
               "g":"OOOO..",
               "h":"O.OO..",
               "i":".OO...",
               "j":".OOO..",
               "k":"O...O.",
               "l":"O.O.O.",
               "m":"OO..O.",
               "n":"OO.OO.",
               "o":"O..OO.",
               "p":"OOO.O.",
               "q":"OOOOO.",
               "r":"O.OOO.",
               "s":".OO.O.",
               "t":".OOOO.",
               "u":"O...OO",
               "v":"O.O.OO",
               "w":".OOO.O",
               "x":"OO..OO",
               "y":"OO.OOO",
               "z":"O..OOO"}

bdict_num = {"1":"O.....",
             "2":"O.O...",
             "3":"OO....",
             "4":"OO.O..",
             "5":"O..O..",
             "6":"OOO...",
             "7":"OOOO..",
             "8":"O.OO..",
             "9":".OO...",
             "0":".OOO.."}
             
def braille_check(text):
    """Helper function to determine if given text
    is in Braille (True) or English (False).
    
    >>> braille_check(Ohio)
    False
    
    >>> braille_check(.....OO.....)
    True
    """
    trail = [str(char) for char in text]
    if len(text) % 6 == 0 and set(trail).issubset({"O", "."}):
        return True
    return False

def braille_to_eng(text):
    """Helper function to translate Braille to English.
    
    >>> braille_to_eng(.....OO.O...)
    B
    
    >>> braille_to_eng(.O.OOO0...........OO....)
    1 c
    """
    trail = [str(text[i:i + 6]) for i in range(0, len(text), 6)]
    count = len(trail)
    bdict_alpha_rev = {braille:eng for eng, braille in bdict_alpha.items()}
    bdict_num_rev = {braille:eng for eng, braille in bdict_num.items()}
    cap = 0
    num_flag = 0
    output = ""
    for i in trail:
        if num_flag == 0:
            if i == "......":
                output = output + " "
            elif i in bdict_alpha_rev:
                if cap == 1:
                    output = output + bdict_alpha_rev[i].upper()
                    cap = 0
                else:
                    output = output + bdict_alpha_rev[i]
            elif i == ".....O":
                cap = 1
            elif i == ".O.OOO":
                num_flag = 1
        elif num_flag == 1:
            if i == "......":
                output = output + " "
                num_flag = 0
            elif i in bdict_num_rev:
                output = output + bdict_num_rev[i]
    return print(output)
  
def eng_to_braille(text):
    """Helper function to translate English to Braille.
    
    >>> eng_to_braille(A)
    .....OO.....
    
    >>> eng_to_braile(42)
    .O.OOOOO.O..O.O...
    """
    trail = [str(i) for i in str(text)]
    num_flag = 0
    output = ""
    for i in trail:
        if num_flag == 0:
            if i == " ":
                output = output + "......"
            elif i.lower() in bdict_alpha:
                if i.isupper():
                    output = output + ".....O" + bdict_alpha[i.lower()]
                else:
                    output = output + bdict_alpha[i]
            elif i.isnumeric():
                num_flag = 1
                output = output + ".O.OOO" + bdict_num[i]
        elif num_flag == 1:
            if i == " ":
                output = output + "......"
                num_flag = 0
            elif i in bdict_num:
                output = output + bdict_num[i]
    return print(output)

def braille_eng_translator(text):
    """Detects if text is Braille or English and
    translates it to the other language.
    
    >>> braille_eng_translator(ABC 623)
    .....OO.....O.O...OO...........O.OOOOOO...O.O...OO....
    
    >>> braille_eng_translator(.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..)
    Hello World
    """
    if braille_check(text):
        braille_to_eng(text)
    else:
        eng_to_braille(text)
pass

braille_eng_translator(body)
