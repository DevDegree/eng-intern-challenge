import sys
import re
str = ' '.join(sys.argv[1:])

hash = {
    97: 'O.....',  # 'a' '1'
    98: 'O.O...',  # 'b' '2'
    99: 'OO....',  # 'c' '3'
    100: 'OO.O..',  # 'd' '4'
    101: 'O..O..',  # 'e' '5'
    102: 'OOO...',  # 'f' '6'
    103: 'OOOO..',  # 'g' '7'
    104: 'O.OO..',  # 'h' '8'
    105: '.OO...',  # 'i' '9'
    106: '.OOO..',  # 'j' '0'
    107: 'O...O.',  # 'k'
    108: 'O.O.O.',  # 'l'
    109: 'OO..O.',  # 'm'
    110: 'OO.OO.',  # 'n'
    111: 'O..OO.',  # 'o'
    112: 'OOO.O.',  # 'p'
    113: 'OOOOO.',  # 'q'
    114: 'O.OOO.',  # 'r'
    115: '.OO.O.',  # 's'
    116: '.OOOO.',  # 't'
    117: 'O...OO',  # 'u'
    118: 'O.O.OO',  # 'v'
    119: '.OOO.O',  # 'w'
    120: 'OO..OO',  # 'x'
    121: 'OO.OOO',  # 'y'
    122: 'O..OOO',  # 'z'
    32: '......',   # ' '

    "capital": '.....O',  # 'Upper case'
    "decimal": '.O...O',  # 'Decimal'
    "number": '.O.OOO',  # 'Digit'

}

numSequence = False
result_string = ''

if (re.search("^[.O]*$", str)):
    len_six_substr = [str[i:i+6] for i in range(0, len(str), 6)]
    reverseHash = dict((v, k) for k, v in hash.items())

    capitalization = False

    for substring in len_six_substr:
        if substring in reverseHash.keys():
            if capitalization:
                result_string += chr(reverseHash[substring] - 32)
                capitalization = False
            elif reverseHash[substring] == "capital":
                capitalization = True
            elif reverseHash[substring] == 'decimal':
                result_string += "."
            elif reverseHash[substring] != 'number':
                result_string += chr(reverseHash[substring])

else:
    ascii_str = [ord(c) for c in str]

    for ascii in ascii_str:
        if (ascii > 47 and ascii < 58 and not numSequence):
            result_string += hash["number"]
            numSequence = True
        if (ascii == 32):
            result_string += hash[ascii]
            numSequence = False
        elif (numSequence):
            if (ascii != 48):
                result_string += hash[97 + (ascii - 49)]
            else:
                result_string += hash[106]
        elif (ascii < 97 and ascii > 64):
            result_string += hash["capital"] + hash[ascii + 32]
        else:
            result_string += hash[ascii]

sys.stdout.write(result_string)
