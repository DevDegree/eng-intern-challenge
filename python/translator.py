import sys

brailleToEnglish = {
	'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
	'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
	'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
	'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
	'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
	'O..OOO': 'z', '..OO.O': '.', '..O...': ',' , '..O.OO': '?', '..OOO.': '!',
	'..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', 'O.O..O': '(',
	'.O.OO.': ')'
}

englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O',
    ')': '.O.OO.'
}

convertNums = {
	'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
	'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
	'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
	'6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
	'.0...0': '.', '.': '.0...0'
}


def isBraille(inputText):
    for c in inputText:
        if (c != '.') and (c != 'O'):
            return False
    return True
	
def convertBraille(inputText):
	full = inputText
	translation = ''
	numbers = False
	cap = False
	while(full != ''):
		temp = full[:6]
		full = full[6:]
		if (temp == '......'):
			numbers = False
			translation += ' '
		elif (temp == '.....O'):
			cap = True
		elif (temp == '.O.OOO'):
			numbers = True
		elif (numbers == True):
			translation += convertNums.get(temp, 'error')
		elif (cap == True):
			translation += brailleToEnglish.get(temp, 'error').upper()
			cap = False
		else:
			translation += brailleToEnglish.get(temp, 'error')	
	return translation

def convertEnglish(inputText):
	full = inputText
	translation = ''
	numbers = False
	while (full != ''):
		temp = full[:1]
		full = full[1:]
		if (temp == ' '):
			numbers = False
			translation += '......'
		elif (temp.isnumeric()):
			if (numbers == False):
				numbers = True
				translation += '.O.OOO'
			translation += convertNums.get(temp, 'error')
		elif (temp.isupper()):
			translation += '.....O' + englishToBraille.get(temp.lower(), 'error')
		else:
			translation += englishToBraille.get(temp, 'error')
	return translation
		

def main():
	if (len(sys.argv) < 2): sys.exit(1)
	args = sys.argv[1:]
	# I'm making an assumption that inputs braille XOR english, and not a mix
	# If they were a mix, I would just run through the args and translate based on type
	# which is what I had originally but based off the test file, it looks like inputs
	# should be considered as one larger input. 
	# Also symbols < > are not included as one of them was identical to a letter and
	# causing issues.
	if (isBraille(args[0])):
		translationText = '......'.join(args)
		print(convertBraille(translationText))
	else:
		translationText = ' '.join(args)
		print(convertEnglish(translationText))

if __name__ == "__main__":
    main()
