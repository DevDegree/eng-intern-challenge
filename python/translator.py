import sys

# Dictionary to convert English to Braille
braille_dict = {
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
    
    # Numbers
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    
    # Indicators
    'capital_follows': '.....O',
    'number_follows': '.O.OOO',

    # Space
    ' ': '......'
}

# Dictionary to convert Braille to English
english_dict = {
    'O.....': ['a','1'],
    'O.O...': ['b','2'],
    'OO....': ['c','3'],
    'OO.O..': ['d','4'],
    'O..O..': ['e','5'],
    'OOO...': ['f','6'],
    'OOOO..': ['g','7'],
    'O.OO..': ['h','8'],
    '.OO...': ['i','9'],
    '.OOO..': ['j','0'],
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',

    # Indicators
    '.....O': 'capital_follows',
    '.O.OOO': 'number_follows',

    # Space
    '......': ' ',
}


def brailleToEnglish(s):
    # Converts a Braille string into its English Equivalent
    englishString = ""
    n = len(s)//6
    is_number = False
    is_capital = False

    if len(s)%6 != 0:
        print("Incorrect braille input. The length of the input should be a multiple of 6.")
        return 0
    try:
        for i in range(n):
            # Gets the 6 digit braille code
            sub_str = s[i*6: i*6+6]
            
            # If space is identified, then add space and change is_number to True
            if(english_dict[sub_str] == " "):
                englishString += " "
                is_number = False
                continue
            
            # If number_follows code is identified, sets is_number to True 
            if english_dict[sub_str] == "number_follows":
                is_number = True
                continue
            
            # if capital_follows is identified, sets is_capital to True
            if english_dict[sub_str] == "capital_follows":
                is_capital = True
                continue
            
            # if is_number is True, then all the following codes are numbers, until we hit a space
            if is_number == True:
                englishString += english_dict[sub_str][1]
                continue
            
            # This adds the aplhabets to the string. If is_capital is True, only the next alphabet is capitalized. 
            if is_capital == True:
                englishString += english_dict[sub_str][0].upper()
                is_capital = False
            else:
                englishString += english_dict[sub_str][0]

        print(englishString)
    except Exception as e:
        print(f"Input was incorrect. {e} is not a correct braille syntax")

def engToBraille(s):
    
    # Converts an English String into its Braille Equivalent
    brailleString = ""
    slist = s.split()
    n = len(slist)
    try: 
        for i in range(n):
            
            if slist[i][0].isalpha():
                brailleString += stringToBraille(slist[i])
            elif slist[i][0].isdigit():
                brailleString += numberToBraille(slist[i])
            
            if i!=n-1:
                brailleString += braille_dict[' ']
        print(brailleString)
    except Exception as e:
        print(f"Input string incorrect: {e} was used")

def stringToBraille(string):
    # Converts a given string into its Braille equivalent
    s = ""
    for i in range(len(string)):
        if string[i].isupper():
            s += braille_dict['capital_follows']

        s += braille_dict[string[i].lower()]
    return s

def numberToBraille(number):
    # Converts a given number into its Braille equivalent
    s = ""
    s += braille_dict['number_follows']
    for i in range(len(number)):
        s += braille_dict[number[i]]
    return s


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Create input_string, by taking input from user through standard input
        input_string = ' '.join(sys.argv[1:])
        
        if '.' in input_string:
            brailleToEnglish(input_string)
        else:
            engToBraille(input_string)
    else:
        print("Please run the code as follows: python translator.py <String to covert>")
        