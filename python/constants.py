CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
BRAILLE_SPACE = '......'

ALPHABET_TO_BRAILLE = {
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
	' ': '......',
}

for i in range(0, 26):
	upper_case = chr(i + ord('A'))
	lower_case = chr(i + ord('a'))
	ALPHABET_TO_BRAILLE[upper_case] = CAPITAL_FOLLOWS + ALPHABET_TO_BRAILLE[lower_case]

BRAILLE_TO_ALPHABET = {v: k for k, v in ALPHABET_TO_BRAILLE.items()}

# NOTE: THE BELOW SYSTEM SEEMS TO BE USED FOR LAST TEST CASE
# NUMBER_TO_CHAR = {
# 	'0': 'a',
# 	'1': 'b',
# 	'2': 'c',
# 	'3': 'd',
# 	'4': 'e',
# 	'5': 'f',
# 	'6': 'g',
# 	'7': 'h',
# 	'8': 'i',
# 	'9': 'j',
# }
NUMBER_TO_CHAR = {
	'1': 'a',
	'2': 'b',
	'3': 'c',
	'4': 'd',
	'5': 'e',
	'6': 'f',
	'7': 'g',
	'8': 'h',
	'9': 'i',
	'0': 'j',
}

CHAR_TO_NUMBER = {v: k for k, v in NUMBER_TO_CHAR.items()}
