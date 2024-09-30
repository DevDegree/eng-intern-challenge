import sys

CHAR_BRAILLE_MAP = {
	'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
	'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
	'o':  'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
	'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}

NUMBERS_BRAILLE_MAP = {
	'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
	'6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_CHAR_MAP = {v: k for k, v in CHAR_BRAILLE_MAP.items()}
BRAILLE_NUMBERS_MAP = {v: k for k, v in NUMBERS_BRAILLE_MAP.items()}

CAPITAL_FOLLOWS = '.....O'
DECIMAL_FOLLOWS = '.O...O'
NUMBER_FOLLOWS = '.O.OOO'

WHITESPACE_BRAILLE = '......'

def translate_braille(str):
	split_braille = [str[i:i + 6] for i in range(0, len(str), 6)]

	readNumbers = False
	capitalizeNext = False

	translated_output = ''
	for chunk in split_braille:
		if chunk == WHITESPACE_BRAILLE:
			translated_output += ' '
			readNumbers = False	
		elif chunk == CAPITAL_FOLLOWS:
			capitalizeNext = True
		elif chunk == DECIMAL_FOLLOWS:
			translated_output += '.'
		elif chunk == NUMBER_FOLLOWS:
			readNumbers = True
		elif readNumbers and chunk in BRAILLE_NUMBERS_MAP:
			translated_output += BRAILLE_NUMBERS_MAP[chunk]
		elif chunk in BRAILLE_CHAR_MAP:
			charASCII = ord(BRAILLE_CHAR_MAP[chunk])
			if capitalizeNext:
				capitalizeNext = False
				charASCII -= 32
			translated_output += chr(charASCII)
	return translated_output

def translate_english(str):
	translated_output = ''

	writeNumbers = False

	for char in str:
		if char == ' ':
			translated_output += WHITESPACE_BRAILLE
			writeNumbers = False
		elif char == ".":
			translated_output += DECIMAL_FOLLOWS
		elif char.isalpha():
			translated_output += (CAPITAL_FOLLOWS + CHAR_BRAILLE_MAP[chr(ord(char) + 32)]) if char.isupper() else CHAR_BRAILLE_MAP[char]
		elif char in NUMBERS_BRAILLE_MAP:
			if not writeNumbers:
				translated_output += NUMBER_FOLLOWS
				writeNumbers = True
			translated_output += NUMBERS_BRAILLE_MAP[char]
	return translated_output

if __name__ == "__main__":
	# testing

	# makes sure the portion of each pair containing the braile has 6 characters
	# print(all(len(v) == 6 for v in CHAR_BRAILLE_MAP.values()))
	# print(all(len(v) == 6 for v in NUMBERS_BRAILLE_MAP.values()))
	# print(all(len(k) == 6 for k in BRAILLE_CHAR_MAP.keys()))
	# print(all(len(k) == 6 for k in BRAILLE_NUMBERS_MAP.keys()))
	
	# print(BRAILLE_CHAR_MAP['OOO...'])
	# print(BRAILLE_NUMBERS_MAP['OOO...'])

	# errors if missing letter or number
	# for i in range(97, 97 + 26):
	# 	test_char = chr(i)
	# 	char = CHAR_BRAILLE_MAP[test_char]

	# for i in range(48, 48 + 9):
	# 	test_char = chr(i)
	# 	char = NUMBERS_BRAILLE_MAP[test_char]

	input_args = ' '.join(sys.argv[1:])
	
	print(translate_braille(input_args) if all(c in '.O' for c in input_args) else translate_english(input_args))