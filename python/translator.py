import sys

# Char to Braille
charToBrai = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'cap': '.....O', 'num': '.O.OOO', '.': '..OO.O', ' ': '......'
}

# Braille to Char
braiToNum = {charToBrai[key]: key for key in charToBrai if key.isnumeric()}
braiToAlp = {charToBrai[key]: key for key in charToBrai if key.isalpha() and len(key) == 1}
braiToOther = {'.O.OOO': 'num', '......': ' ', '.....O': 'cap', '..OO.O': '.'}

# Create a function called englishToBraille() to translate Braille to English. 
def brailleToEnglish(inp_str):
    res = ""
    isUpper = False
    isNum = False
    for i in range(0, len(inp_str), 6):
        pattern = inp_str[i: i + 6]
        # In case of number starts
        if pattern in braiToOther and braiToOther[pattern] == 'num':
            isNum = True
        # In case of number ends or space between words
        elif pattern in braiToOther and braiToOther[pattern] == ' ':
            isNum = False
            res = res + ' '
        # In case of capital letter indicator
        elif pattern in braiToOther and braiToOther[pattern] == 'cap':
            isUpper = True
        # In case of dot
        elif pattern in braiToOther and braiToOther[pattern] == '.':
            res = res + '.'
        # In case of aphpabet.
        elif not isNum:
            # Check whether it is upper case or not. If so, use upper case and set isUpper = False
            if isUpper:
                isUpper = False
                res = res + braiToAlp[pattern].upper()
            # If it is not upper case, add it directly
            else:
                res = res + braiToAlp[pattern]
        # In case of number
        else:
            res = res + braiToNum[pattern]

    return res

# Create a function called englishToBraille() to translate English to Braille. 
def englishToBraille(inp_str):
    isNum = False
    res = ""
    ind = 0
    for ch in inp_str:
        # Handle single english letter
        if ch.isalpha():
            # In case of upper case letter
            if ch.isupper():
                res = res + charToBrai['cap'] + charToBrai[ch.lower()]
            # In case of lower case letter
            else:
                res = res + charToBrai[ch]
        # In case of space: this is a sign of number ending -> set isNum to False. It does not make any difference if it is just a regular space between two words.
        elif ch == ' ':
            isNum = False
            res = res + charToBrai[ch]
        # In case of numeric.
        else:
            # isNum is True -> directly adding the Braille code to the string.
            if isNum:
                res = res + charToBrai[ch]
            # isNum is False -> Assign an indicator in the Braille code to label the start of a number. Set isNum to True
            else:
                isNum = True
                res = res + charToBrai['num'] + charToBrai[ch]
    return res

# Check whether is given string is Braille or not
def isBraille(inp_str):
    if len(inp_str) % 6 != 0: return False
    brai_codes = [charToBrai[key] for key in charToBrai]
    return all(inp_str[i: i + 6] in brai_codes for i in range(0, len(inp_str), 6))

# Check the type of inputs (English or Braille) and call the corresponding function for translation.
def brailleTranslator(inputs):
    # Store the result for each input in a list
    res = []
    # Label type of input
    translateToEng = False
    toBraille = False
    for inp in inputs:
        # If the input is Braille, we translate it to English
        if isBraille(inp):
            translateToEng = True
            res.append(brailleToEnglish(inp))
        # If the input is English, we translate it to Braille
        else:
            res.append(englishToBraille(inp))
    # If the output is English, use ' ' to seperate each result
    if translateToEng:
        return ' '.join(res)
    # If the output is Braille, use '......' to seperate each result
    return '......'.join(res)

if __name__ == '__main__':
    # Read argument
    inputs = sys.argv[1:]
    # Check whether input is provided
    if not inputs:
        print('Please offer inputs!')
        sys.exit(0)
    res = brailleTranslator(inputs)
    print(res)
        
