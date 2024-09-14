import sys

braille = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
		   'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
		   'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
		   's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
		   'y': 'OO.OOO', 'z': 'O..OOO', '0': '.OOO..', '#': '.OOOOO', ',': '..O...', ';': '..OO..',
		   ':': '...O..', '.': '...OO.', '!': '..OOO.', '?': '..O.O.', '(': '..OO.O', ')': '..OO.O',
		   "'": '....O.', '-': '....OO', ' ':"......"}

NUMBERFOLLOWS = '.O.OOO'
CAPITALFOLLOWS = '.....O'
SPACE = '......'
key_list = list(braille.keys())
value_list = list(braille.values())


def BrailleEncoder(message: str) -> None: 
	isNumber: bool = False
	result: str = ""
	for char in message:
		if char.isnumeric():
			if not isNumber:
				isNumber = True
				result += NUMBERFOLLOWS
			result += braille.get(chr(int(char) + 96))
		else:
			if char == ' ':
				isNumber = False
			elif char.isupper():
				result += CAPITALFOLLOWS
			result += braille.get(char.lower())
	sys.stdout.write(result)


def BrailleDecoder(message: str) -> None:
	isNumber: bool = False
	capitalizeNext: bool = False
	result: str = ''

	for i in range(0, len(message), 6):
		char = message[i:i+6]
		if char == NUMBERFOLLOWS:
			isNumber = True
		elif char == CAPITALFOLLOWS:
			capitalizeNext = True
		elif char == SPACE:
			isNumber = False
			result += ' '
		else:
			if isNumber:
				result += str(ord(key_list[value_list.index(char)]) - 96)
			elif capitalizeNext:
				result += key_list[value_list.index(char)].upper()
				capitalizeNext = False
			else:
				result += key_list[value_list.index(char)]
	sys.stdout.write(result)


message: str = ' '.join(sys.argv[1:])

for char in message:
	if len(message) % 6 != 0:
		BrailleEncoder(message)
		exit()
	elif char != 'O' and char != '.':
		BrailleEncoder(message)
		exit()

BrailleDecoder(message)