import sys

# English to Braille
a_br = 'O.....'
b_br = 'O.O...'
c_br = 'OO....'
d_br = 'OO.O..'
e_br = 'O..O..'
f_br = 'OOO...'
g_br = 'OOOO..'
h_br = 'O.OO..'
i_br = '.OO...'
j_br = '.OOO..'
k_br = 'O...O.'
l_br = 'O.O.O.'
m_br = 'OO..O.'
n_br = 'OO.OO.'
o_br = 'O..OO.'
p_br = 'OOO.O.'
q_br = 'OOOOO.'
r_br = 'O.OOO.'
s_br = '.OO.O.'
t_br = '.OOOO.'
u_br = 'O...OO'
v_br = 'O.O.OO'
w_br = '.OOO.O'
x_br = 'OO..OO'
y_br = 'OO.OOO'
z_br = 'O..OOO'

# Braille Numbers
br_1 = a_br
br_2 = b_br
br_3 = c_br
br_4 = d_br
br_5 = e_br
br_6 = f_br
br_7 = g_br
br_8 = h_br
br_9 = i_br
br_0 = j_br

# Braille Special Characters
br_cf = '.....O'  # Capital Follows
br_df = '.O...O'  # Decimal Follows
br_nf = '.O.OOO'  # Number Follows
br_dot = '..O.O'
br_comma = '..O...'
br_ques = '..O.OO'
br_excl = '..OOO.'
br_colon = '..OO..'
br_semicolon = '..O.O.'
br_dash = '....OO'
br_fwdslsh = '.O..O.'
br_lessthan = '.OO..O'
# Code was same as O, wasn't sure how to differentiate O and >
br_greaterthan = 'O..O.O'
br_leftround = 'O.O..O'
br_rightround = '.O.OO.'
br_space = '......'


engToBraille = {
    'a': a_br,
    'b': b_br,
    'c': c_br,
    'd': d_br,
    'e': e_br,
    'f': f_br,
    'g': g_br,
    'h': h_br,
    'i': i_br,
    'j': j_br,
    'k': k_br,
    'l': l_br,
    'm': m_br,
    'n': n_br,
    'o': o_br,
    'p': p_br,
    'q': q_br,
    'r': r_br,
    's': s_br,
    't': t_br,
    'u': u_br,
    'v': v_br,
    'w': w_br,
    'x': x_br,
    'y': y_br,
    'z': z_br,
    '0': br_0,
    '1': br_1,
    '2': br_2,
    '3': br_3,
    '4': br_4,
    '5': br_5,
    '6': br_6,
    '7': br_7,
    '8': br_8,
    '9': br_9,
    'cf': br_cf,
    'df': br_df,
    'nf': br_nf,
    '.': br_dot,
    ',': br_comma,
    '?': br_ques,
    '!': br_excl,
    ':': br_colon,
    ';': br_semicolon,
    '-': br_dash,
    '/': br_fwdslsh,
    '<': br_lessthan,
    '>': br_greaterthan,
    '(': br_leftround,
    ')': br_rightround,
    ' ': br_space,
}


# Braille to Numbers, letters a-j have same code as 0-9 (dictionary key overlap)
brailleToNumMap = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
}


def buildBrailleToEngMap(dictionary: dict) -> dict:
    # Create a Map to translate from Braille to English
    brailleToEng = {}
    keys = dictionary.keys()

    for key in keys:
        if not key.isnumeric():
            brailleToEng[engToBraille[key]] = (key)

    return brailleToEng


def isBraille(text: str) -> bool:
    # Check if text is Braille
    for char in text:
        if char != 'O' and char != '.':
            return False
    return True


def convertToEnglish(toEngMap: dict, braille: str, nextLetterCap: bool, nextNumFollows: bool, result) -> str:
    # recursive function that translates text from Braille to English

    if len(braille) == 0:
        return result

    else:
        # Get the 6 digit Braille string
        brailleKey = ''
        for i in range(6):
            brailleKey += braille[i]

        if nextLetterCap == True:
            result += toEngMap[brailleKey].upper()
            nextLetterCap = False

        elif nextNumFollows == True:
            result += brailleToNumMap[brailleKey]

        elif brailleKey == br_cf:
            nextLetterCap = True

        elif brailleKey == br_nf:
            nextNumFollows = True

        elif brailleKey == br_space:
            result += toEngMap[brailleKey]
            nextNumFollows = False

        else:
            result += toEngMap[brailleKey]

        # recurse the function for the next 6 digits using slicing method
        return convertToEnglish(toEngMap, braille[6:], nextLetterCap, nextNumFollows, result)


def convertToBraille(english: str) -> str:
    # function that translates from English to Braille
    result = ''

    # Number Follows found
    numIsLocated = False

    for char in english:
        if char.isupper():
            result += engToBraille['cf']
        if char == '.':
            result += engToBraille['df']

        if numIsLocated == False:
            if char.isnumeric():
                result += engToBraille['nf']
                numIsLocated = True

        if char == ' ':
            numIsLocated = False

        if char.isalpha():
            result += engToBraille[char.lower()]
        else:
            result += engToBraille[char]

    return result


if __name__ == '__main__':

    #text = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO....'
    #text = 'Abc 123 xYz'
    text = ''

    # get command line args as text
    for i in range(1, len(sys.argv)):
        text += sys.argv[i] + ' '
    text = text.strip()

    if (isBraille(text)):
        # Convert to English
        brailleToEngMap = buildBrailleToEngMap(engToBraille)
        englishTranslation = convertToEnglish(
            brailleToEngMap, text, False, False, '')
        print(englishTranslation)

    else:
        # Convert to Braille
        brailleTranslation = convertToBraille(text)
        print(brailleTranslation)






