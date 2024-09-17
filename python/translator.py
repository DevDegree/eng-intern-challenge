#!/usr/bin/env/python3
import sys
def is_braille(text):
	braille_chars = {'O','.'}
	for char in text:
		if char not in braille_chars:
			return False
	return True
chartoBrailleDict = {
    'a': 'O.....',  # Braille for 'A'
    'b': 'O.O...',  # Braille for 'B'
    'c': 'OO....',  # Braille for 'C'
    'd': 'OO.O..',  # Braille for 'D'
    'e': 'O..O..',  # Braille for 'E'
    'f': 'OOO...',  # Braille for 'F'
    'g': 'OOOO..',  # Braille for 'G'
    'h': 'O.OO..',  # Braille for 'H'
    'i': '.OO...',  # Braille for 'I'
    'j': '.OOO..',  # Braille for 'J'
    'k': 'O...O.',  # Braille for 'K'
    'l': 'O.O.O.',  # Braille for 'L'
    'm': 'OO..O.',  # Braille for 'M'
    'n': 'OO.OO.',  # Braille for 'N'
    'o': 'O..OO.',  # Braille for 'O'
    'p': 'OOO.O.',  # Braille for 'P'
    'q': 'OOOOO.',  # Braille for 'Q'
    'r': 'O.OOO.',  # Braille for 'R'
    's': '.OO.O.',  # Braille for 'S'
    't': '.OOOO.',  # Braille for 'T'
    'u': 'O...OO',  # Braille for 'U'
    'v': 'O.O.OO',  # Braille for 'V'
    'w': '.OOO.O',  # Braille for 'W'
    'x': 'OO..OO',  # Braille for 'X'
    'y': 'OO.OOO',  # Braille for 'Y'
    'z': 'O..OOO',  # Braille for 'Z'
}
punctuatetoBrailleDict = {
    '.': '..OO.O',  # Braille for period
    ',': '..O...',  # Braille for comma
    '?': '..O.OO',  # Braille for question mark
    '!': '..OOO.',  # Braille for exclamation mark
    ':': '..OO..',  # Braille for colon
    ';': '..O.O.',  # Braille for semicolon
    '-': '....OO',  # Braille for hyphen
    '/': '.O..O.',  # Braille for slash
    '(': 'O.O..O',  # Braille for open parenthesis
    ')': '.O.OO.',  # Braille for close parenthesis
    ' ': '......',  # Braille for space
}
mathOperatorsToBraille = {
    '-': '....OO',  # Braille for hyphen
    '/': '.O..O.',  # Braille for slash
    '<': '.OO..O',  # Braille for less than
    '>': 'O..OO.',  # Braille for greater than
    ' ': '......',  # Braille for space
}
numtoBrailleDict = {
  '0': '.OOO..',
  '1' : 'O.....',
  '2' : 'O.O...',
  '3' : 'OO....',
  '4' : 'OO.O..',
  '5' : 'O..O..',
  '6' : 'OOO...',
  '7' : 'OOOO..',
  '8' : 'O.OO..',
  '9' : '.OO...'
}
    
def BrailletoEng (input_str):
    brailleToNum = {v: k for k, v in numtoBrailleDict.items()}
    brailleToMathOperator = {v: k for k, v in mathOperatorsToBraille.items()}
    brailleToChar = {v: k for k, v in chartoBrailleDict.items()}
    brailleToPunctuate = {v: k for k, v in punctuatetoBrailleDict.items()}
    braillelist = []
    for i in range (0,len(input_str),6):
        chunk = input_str[i : i + 6]
        braillelist.append(chunk)
    results = []
    i = 0
    while i < len(braillelist):
        print(braillelist[i])
        chunk = braillelist[i]
        if chunk == '.O.OOO':
            # For numerical input
            while i < len(braillelist)-1 :
                #for decimal
                i+=1
                if chunk == '.O...O':
                    results.append('.')
                else:
                    next_chunk = braillelist[i]
                    if next_chunk in brailleToNum:
                        results.append(brailleToNum[next_chunk])
                    elif next_chunk in brailleToMathOperator.keys():
                        results.append(brailleToMathOperator[next_chunk])

                        
        # For capitalization
        elif chunk == '.....O':
            next_chunk = braillelist[i+1]
            if next_chunk in brailleToChar.keys():
                results.append(brailleToChar[next_chunk].capitalize())
            i+=1
        else:
            if chunk in brailleToChar.keys():
                results.append(brailleToChar[chunk])
            elif chunk in brailleToPunctuate.keys():
                results.append(brailleToPunctuate[chunk])

        i+=1
        
    result_str = ''.join(results)

    return result_str

def EngtoBraille (input_str):
    englist = []
    for i in range (len(input_str)):
        if input_str[i].isalpha():
            if input_str[i].isupper():
                englist.append('.....O')

            if input_str[i].lower() in chartoBrailleDict:
                englist.append(chartoBrailleDict[input_str[i].lower()])

        elif input_str[i].isdigit():
            if '.O.OOO' not in englist or englist[-1] == '......':
                englist.append('.O.OOO')

            if input_str[i] in numtoBrailleDict:
                englist.append(numtoBrailleDict[input_str[i]])
        else: 
            if input_str[i] in punctuatetoBrailleDict:  
                englist.append(punctuatetoBrailleDict[input_str[i]])
            elif input_str[i] in mathOperatorsToBraille:
                englist.append(mathOperatorsToBraille[input_str[i]])


    result_str = ''.join(englist)

    return result_str

if len(sys.argv) < 2:
	print("incorrect usage")
	sys.exit(1)
input_str = ' '.join(sys.argv[1:])
if is_braille(input_str):
	result =  BrailletoEng(input_str)
	print(result)
else:
	result =  EngtoBraille(input_str)
	print(result)
