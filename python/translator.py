import sys
from bidirectional_dict import BidirectionalDict

'''
Comments:

Bidirectional Dictionary
I decided to use 2 bidirectional dictionary one for the alphabet to braille and other for numbers to braille. Both these dicstionaries are one-to-one correspondence
Meaning for every input there is only one output and vice versa
I am using bidirectional dictionary to quickly(O(1) time) find the keys value or the values key. ex ("a" -> "o.....") and ("o....." -> "a")
I could have used 4 dictionaries to replicate what the bidirectional dictionary is doing but, doing so would have been more complicated for the task at hand.
'''
# Constants
CAPITAL_PREFIX = ".....O"
NUMBER_PREFIX = ".O.OOO"
SPACE = "......" # ' '
BRALLIE_SIZE = 6

def create_braille_alphabet_bidict():
    braille_alphabet_bidict = BidirectionalDict()
    braille_alphabet_bidict.add("a", "O.....")
    braille_alphabet_bidict.add("b", "O.O...")
    braille_alphabet_bidict.add("c", "OO....")
    braille_alphabet_bidict.add("d", "OO.O..")
    braille_alphabet_bidict.add("e", "O..O..")
    braille_alphabet_bidict.add("f", "OOO...")
    braille_alphabet_bidict.add("g", "OOOO..")
    braille_alphabet_bidict.add("h", "O.OO..")
    braille_alphabet_bidict.add("i", ".OO...")
    braille_alphabet_bidict.add("j", ".OOO..")
    braille_alphabet_bidict.add("k", "O...O.")
    braille_alphabet_bidict.add("l", "O.O.O.")
    braille_alphabet_bidict.add("m", "OO..O.")
    braille_alphabet_bidict.add("n", "OO.OO.")
    braille_alphabet_bidict.add("o", "O..OO.")
    braille_alphabet_bidict.add("p", "OOO.O.")
    braille_alphabet_bidict.add("q", "OOOOO.")
    braille_alphabet_bidict.add("r", "O.OOO.")
    braille_alphabet_bidict.add("s", ".OO.O.")
    braille_alphabet_bidict.add("t", ".OOOO.")
    braille_alphabet_bidict.add("u", "O...OO")
    braille_alphabet_bidict.add("v", "O.O.OO")
    braille_alphabet_bidict.add("w", ".OOO.O")
    braille_alphabet_bidict.add("x", "OO..OO")
    braille_alphabet_bidict.add("y", "OO.OOO")
    braille_alphabet_bidict.add("z", "O..OOO")

    return braille_alphabet_bidict

def create_braille_numerical_bidict():
    braille_numerical_bidict = BidirectionalDict()
    braille_numerical_bidict.add("1", "O.....")
    braille_numerical_bidict.add("2", "O.O...")
    braille_numerical_bidict.add("3", "OO....")
    braille_numerical_bidict.add("4", "OO.O..")
    braille_numerical_bidict.add("5", "O..O..")
    braille_numerical_bidict.add("6", "OOO...")
    braille_numerical_bidict.add("7", "OOOO..")
    braille_numerical_bidict.add("8", "O.OO..")
    braille_numerical_bidict.add("9", ".OO...")
    braille_numerical_bidict.add("0", ".OOO..")

    return braille_numerical_bidict

# Gets input from terminal
def get_system_arguments(args):
    text = ""
    for i in range(1,len(args) - 1):
        text += args[i] + " "
    text += args[len(args) - 1]

    if text == "":
        return(args[0])
    
    return text

'''
In Braille Alphabet in the technical requirements it does not state that '.' can be a vaild alphabet input in this program

Valid Braille Alphabet are:
    1. Letters a through z(lowercase and uppercase)
    2. Numbers 0 through 9
    3. Spaces

This means if '.' is found in a string it is a braille and not a vaild braille alphabet
'''
def vaild_braille(text):
    for c in text:
        if (c != '.') and (c != 'O'):
            return False
        
    return len(text) % 6 == 0

'''
Criteria needed for a vaild english text(Braille Alphabet) are:
    1. Letters a through z(lowercase and uppercase)
    2. Numbers 0 through 9
    3. Spaces
'''
def vaild_english(text):
    for c in text:
        if not (c.isalpha() or c.isdigit() or c == " "):
            return False
        
    return True

def convert_brallie_to_english(text, braille_alphabet_bidict, braille_numerical_bidict):
    english = ""
    capital_letter = False
    number_next = False
    for i in range(0,len(text),BRALLIE_SIZE):
        brallie = text[i:i + BRALLIE_SIZE]
        if brallie == CAPITAL_PREFIX:
            capital_letter = True
        elif brallie == NUMBER_PREFIX:
            number_next = True
        elif brallie == SPACE:
            number_next = False
            english += " "
        else:
            if number_next:
                english += braille_numerical_bidict.get_by_value(brallie)
            elif capital_letter:
                english += braille_alphabet_bidict.get_by_value(brallie).upper()
                capital_letter = False
            else:
                english += braille_alphabet_bidict.get_by_value(brallie)
                
    return english

def convert_english_to_brallie(text, braille_alphabet_bidict, braille_numerical_bidict):
    full_brallie = ""
    number_switch = False
    for c in text:
        if c == " ":
            full_brallie += SPACE
            number_switch = False
        elif c.isdigit():
            if not number_switch:
                full_brallie += NUMBER_PREFIX
                full_brallie += braille_numerical_bidict.get(c)
                number_switch = True
            else:
                full_brallie += braille_numerical_bidict.get(c)
        else:
            if c.isupper():
                full_brallie += CAPITAL_PREFIX
                full_brallie += braille_alphabet_bidict.get(c.lower())
            else:
                full_brallie += braille_alphabet_bidict.get(c)
    
    return full_brallie

# Runs the Translator
def main():
    text = get_system_arguments(sys.argv)
    braille_alphabet_bidict = create_braille_alphabet_bidict()
    braille_numerical_bidict = create_braille_numerical_bidict()
    if vaild_braille(text):
        print(convert_brallie_to_english(text, braille_alphabet_bidict, braille_numerical_bidict))
    elif vaild_english(text):
        print(convert_english_to_brallie(text, braille_alphabet_bidict, braille_numerical_bidict))
    else:
        print("Invaild input in terminal")

if __name__ == "__main__":
    main() 

'''
Test Cases:

English to Braille:
1. "Hello world" -> ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."  -> Correct
2. "42"          -> ".O.OOOOO.O..O.O..."                                                        -> Correct
3. "Abc 123"     -> ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."                    -> Correct
4. "HeLLo"       -> ".....OO.OO..O..O.......OO.O.O......OO.O.O.O..OO."                          -> Correct
5. "123 456"     -> ".O.OOOO.....O.O...OO...........O.OOOOO.O..O..O..OOO..."                    -> Correct
6. "1 "          -> ".O.OOOO..........."                                                        -> Correct NOTE: Make sure to quote it the input like 'python3 translator.py "1 "'. If you don't do that it will skip the trailling space. The actually quotes "" wont't be included in the input argumnets due to the way Python3 handles it.
7. " "           -> "......"                                                                    -> Correct NOTE: Make sure to quote it the input like 'python3 translator.py " "'. If you don't do that it will skip the space. The actually quotes "" wont't be included in the input argumnets due to the way Python3 handles it.                            

Braille to English:
1. ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.." -> "Hello world"  -> Correct
2. ".O.OOOOO.O..O.O..."                                                       -> "42"           -> Correct
3. ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."                   -> "Abc 123"      -> Correct
4. ".....OO.OO..O..O.......OO.O.O......OO.O.O.O..OO."                         -> "HeLLo"        -> Correct
5. ".O.OOOO.....O.O...OO...........O.OOOOO.O..O..O..OOO..."                   -> "123 456"      -> Correct
6. ".O.OOOO..........."                                                       -> "1 "           -> Correct
7. "......"                                                                   -> " "            -> Correct

Invaild Inputs:                                                | Why is it invaild?
1. "Hello .....OO"   -> "Invaild input in terminal" -> Correct | Both english and Braille were inputed
2. "23/ 97g"         -> "Invaild input in terminal" -> Correct | Invaild charaters("/")
3. ""                -> "Invaild input in terminal" -> Correct | Empty input(I am assuming that is invaild) NOTE: Works regardless if input is like "python3 translator.py  " or 'python3 translator.py ""'
4. ".....O....."     -> "Invaild input in terminal" -> Correct | Had 11 characters which is not divisible by 6. It is not a vaild braille
5. "O.O. .."         -> "Invaild input in terminal" -> Correct | Should not be a vaild braille becuase of the space
'''