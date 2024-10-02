from typing import List
import sys

B_TO_E_MAP = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "CAP",
    ".O.OOO": "NUM",
    "......": " "
}
BRL_NUM_MAP = {
    "O.....": "1",  
    "O.O...": "2",  
    "OO....": "3",  
    "OO.O..": "4",  
    "O..O..": "5",  
    "OOO...": "6",  
    "OOOO..": "7",  
    "O.OO..": "8",  
    ".OO...": "9",  
    ".OOO..": "0",
    "......": " "
}
E_to_B_MAP = {
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
    ' ' : '......',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'CAP': '.....O',
    'NUM': '.O.OOO'
}
ENG_NUM_MAP = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

def is_braille(str_input: str) -> bool:
    """
    Returns True if passed string is in Braille
    Checks if input string only consists of "O" and "." chars. Could be a better/more efficient way of checking this condition
    """
    return len(str_input) == str_input.count('O') + str_input.count('.')

def parse_braille(str_input: str) -> List[str]:
    """
    Returns braille string input parsed into chunks of 6 char strings as a list
    """
    return [str_input[i: i+6] for i in range(0, len(str_input), 6)]

def braille_to_english(b_list: List[str]) -> str:
    """
    main Braille to English translator function
    """
    n = len(b_list)
    i = 0 # wanted to use n, but that would likely annoy someone
    res = "" # Translated string to be returned

    try:
        while(i < n):
            val = B_TO_E_MAP[b_list[i]]
            if val == "CAP" and i != n-1:
                # read next string is as upper case, move counter up by two
                res += B_TO_E_MAP[b_list[i+1]].upper()
                i += 2
            elif val == "NUM":
                #set temp counter to i + 1 to begin reading numbers until space is hit or end of input
                k = i + 1
                while k < n and BRL_NUM_MAP[b_list[k]] != " ":
                    res += BRL_NUM_MAP[b_list[k]]
                    k += 1
                i = k
            else:
                res += B_TO_E_MAP[b_list[i]]
                i += 1
    except KeyError:
        raise KeyError("Please only enter alphanumeric characters/strings or Braille encoding (O's and .'s)")

    return res.strip()

def english_to_braille(e_str: str) -> str:
    """
    Main English to Braille translator function
    """
    n = len(e_str)
    i = 0
    res = ""

    try:

        while(i < n):

            val = e_str[i]
            if val.isupper():
                # Pre-empt capital letter with Braille flag, then add caps letter
                res += E_to_B_MAP['CAP'] + E_to_B_MAP[val.lower()]
                i += 1
            elif val.isnumeric():
                #Pre-empt numbers with Braille flag, process until " " hit or string terminated
                res += E_to_B_MAP['NUM']
                while i < n and e_str[i].isnumeric():
                    res += ENG_NUM_MAP[e_str[i]]
                    i += 1
            else: 
                res += E_to_B_MAP[e_str[i]]
                i += 1

    except KeyError:
        raise KeyError("Please only enter alphanumeric characters/strings or Braille encoding (O's and .'s)")

    return res.strip()

def main():
    """
    Primary caller function
    """
    if (len(sys.argv) > 1):
        user_in = " ".join([ x for x in sys.argv[1:]]).strip()
        if is_braille(user_in):
            test = parse_braille(user_in)
            print(braille_to_english(test))
        else:
            output = english_to_braille(user_in)
            print(output)

if __name__ == "__main__":
    main()