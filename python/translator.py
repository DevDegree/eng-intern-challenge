import sys

def invertDict(dictionary):
	"""Returns inverted dictionary by mapping values to keys. Assumes values are unique in dictionary."""
	return {v: k for k, v in dictionary.items()}

# Maps lowercase English letters and space to their braille equivalent
englishToBraille = {
	'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
	'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
	'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
	'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

# Maps braille characters to their lowercase English equivalent
brailleToEnglish = invertDict(englishToBraille)

# Maps decimal numbers to their braille equivalent
decimalToBraille = {
	'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
	'9': '.OO...', '0': '.OOO..'
}

# Maps braille characters to their decimal number equivalent
brailleToDecimal = invertDict(decimalToBraille)

capitalFollows = '.....O'
numberFollows = '.O.OOO'

def translateEnglishToBraille(english):
	"""Returns translation of string from English to braille. Assumes string is a valid English sentence."""
	# Construct braille sentence letter by letter
	braille = ""

	# Define state variables
	isNumber = False # Whether the current character is a part of a number
	for char in english:
		if char.isnumeric():
			if not isNumber:
				isNumber = True
				braille += numberFollows
			braille += decimalToBraille[char]
		else:
			isNumber = False
			if char.isupper():
				braille += capitalFollows
				char = char.lower()
			braille += englishToBraille[char]

	return braille

def translateBrailleToEnglish(braille):
	"""Returns translation of string from braille to English. Assumes string is a valid braille sentence."""
	# Split braille into 6-character segments, where each segment is a braille letter
	braille = [braille[i:i+6] for i in range(0, len(braille), 6)]
	# Construct english sentence letter by letter
	english = ""
	
	# Define state variables
	isCapital = False # Whether the current character is a capital letter
	isNumber = False # Whether the current character is part of a number
	for char in braille:
		# Special letters
		if char == capitalFollows:
			isCapital = True
			continue
		if char == numberFollows:
			isNumber = True
			continue
		# Letters that map to english letters
		if char == englishToBraille[' ']:
			isNumber = False
			english += ' '
		elif isNumber:
			english += brailleToDecimal[char]
		else:
			englishChar = brailleToEnglish[char]
			if isCapital:
				englishChar = englishChar.upper()
				isCapital = False
			english += englishChar

	return english

def isBraille(string):
	"""Returns whether string is a valid braille string"""
	return all(x == 'O' or x == '.' for x in string) and len(string) % 6 == 0

if __name__ == '__main__':
	string = ' '.join(sys.argv[1:])
	if isBraille(string):
		print(translateBrailleToEnglish(string))
	else:
		print(translateEnglishToBraille(string))
