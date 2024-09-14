import sys

lettersToBraille = {
    
		'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
		'e': 'O..O..','f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
		'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
		'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
		'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
		'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
		'y': 'OO.OOO', 'z': 'O..OOO'}

numToBraille = {
		'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
		'5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
		'9': '.OO...', '0': '.OOO..'
}

brailleToLetters = {value: key for key, value in lettersToBraille.items()}
brailleToNum = {value: key for key, value in numToBraille.items()}

capitalFollowsSymbol = '.....O'
numbersFollowsSymbol = '.O.OOO'
spaceSymbol = '......'


def is_braille(text):
		return ((len(text) % 6 == 0) and all(char in ['O', '.'] for char in text))

def english_to_braille(englishText):
		brailleText = ''
		numberMode = False
		for char in englishText:
				if char.isalpha():
						if numberMode:
								numberMode = False 
						if char.isupper():
								brailleText += capitalFollowsSymbol
						brailleText += lettersToBraille[char.lower()]
				elif char.isdigit():
						if not numberMode:
								brailleText += numbersFollowsSymbol
								numberMode = True
						brailleText += numToBraille[char]
				elif char == ' ':
						brailleText += spaceSymbol
						numberMode = False  
		return brailleText

def braille_to_english(brailleText):
		englishText = ''
		capitalLetter = False
		numberFollows = False
		for i in range(0, len(brailleText), 6):
				brailleChar = brailleText[i:i+6]
				if brailleChar == capitalFollowsSymbol:
						capitalLetter = True
				elif brailleChar == numbersFollowsSymbol:
						numberFollows = True
				elif numberFollows:
						englishText += brailleToNum[brailleChar]
						numberFollows = False
				elif brailleChar == spaceSymbol:
						englishText += ' '
				else:
						if capitalLetter:
								englishText += brailleToLetters[brailleChar].upper()
								capitalLetter = False
						else:
								englishText += brailleToLetters[brailleChar]

		return englishText


def main():
		input_string = ' '.join(sys.argv[1:])
		if is_braille(input_string):
				print(braille_to_english(input_string))
		else:
				print(english_to_braille(input_string))


if __name__ == "__main__":
		main()
