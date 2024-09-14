import re
import sys
engchar_to_braille = {
    'a': "O.....", 'b': "O.O...",'c': "OO....",'d': "OO.O..",'e': "O..O..",
    'f': "OOO...",'g': "OOOO..",'h': "O.OO..",'i': ".OO...",'j': ".OOO..",
    'k': "O...O.",'l': "O.O.O.",'m': "OO..O.",'n': "OO.OO.",'o': "O..OO.",
    'p': "OOO.O.",'q': "OOOOO.",'r': "O.OOO.",'s': ".OO.O.",'t': ".OOOO.",
    'u': "O...OO",'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",'y': "OO.OOO",
    'z': "O..OOO", ' ': "......"}
digits_to_braille = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."}

capital_flag = ".....O"
number_flag = ".O.OOO"

braille_to_engchar = {v: k for k, v in engchar_to_braille.items()}
braille_to_digits = {v: k for k, v in digits_to_braille.items()}


def valid_braille_value(braille):
    braille_list = list(braille_to_engchar.keys()) + list(braille_to_digits.keys())
    if braille in braille_list:
        return True
    return False

def english_to_braille(given_string):

    try:
        brailleResult = []
        number_follows = False

        for c in given_string:
            
            if c.isupper():
                brailleResult.append(capital_flag)
                c = c.lower()
            elif c == ' ':
                brailleResult.append(engchar_to_braille[' '])
                number_follows = False
                continue
            elif c.isdigit():
                if not number_follows:
                    brailleResult.append(number_flag)
                    number_follows = True
        
            if number_follows:
                brailleResult.append(digits_to_braille[c])
            else: 
                brailleResult.append(engchar_to_braille[c])

        return "".join(brailleResult)
    except:
        return ""

def is_braille(inputArg):
    if len(inputArg) % 6 != 0:
        return False
    for val in inputArg:
        if val == '.' or val == 'O':
            continue
        else:
            return False
    return True



def braille_to_english(givenBraille):
    try:
        english_result = []
        next_capital = False
        next_number = False
        braille_chars = re.findall('.{1,6}', givenBraille) #uses regex to get braille chars

        for braille in braille_chars:
            if braille == capital_flag:
                next_capital = True
                continue # no character will be added
            elif braille == number_flag:
                next_number = True
                continue 
            if not valid_braille_value(braille):
                return ""
            charValue = braille_to_digits[braille] if next_number else braille_to_engchar[braille]
            if next_capital:
                charValue = charValue.upper()
                next_capital = False
            if charValue == ' ':
                next_number = False
            english_result.append(charValue)
        return "".join(english_result)
    except:
        return ""



        
def translate(input_string):
    input_string = input_string.strip()
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))
if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:]) 
    translate(input_string)
    
    