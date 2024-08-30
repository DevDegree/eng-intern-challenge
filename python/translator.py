import sys
from utils import is_braille, is_english

english_to_braille_map = {
	'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
	'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
	'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
	'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
	'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

	'.': '..OO.O', 
	',': '..O...', 
	'?': '..O.OO', 
	'!': '..OOO.', 
	':': '..OO..',
	';': '..O.O.', 
	'-': '....OO', 
	'/': '.O..O.', 
	'<': '.OO..O', 
	'>': 'O..OO.',
	'(': 'O.O..O', 
	')': '.O.OO.', 
	' ': '......',
	
	'capital_follows': '.....O', 
	'decimal_follows': '.O...O', 
	'number_follows': '.O.OOO'
}

number_to_braille_map = {
	'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
	'6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

braille_to_english_map = {braille:english for english, braille in english_to_braille_map.items()}

braille_to_number_map = {braille:number for number, braille in number_to_braille_map.items()}

def braille_to_english(braille_input: str) -> str:
	english_output = []
	# Store braille symbols, each containing 6 input characters, of braille_input
	braille_symbols = []
	# Track 'capital follows'
	capital_flag = False
	# Track 'number follows'
	number_flag = False

	for i in range(0, len(braille_input), 6):
		braille_symbols.append(braille_input[i : i + 6])
	
	for symbol in braille_symbols:
		if symbol == english_to_braille_map['capital_follows']:
			capital_flag = True
		elif symbol == english_to_braille_map['number_follows']:
			number_flag = True
		elif symbol == english_to_braille_map[' ']:
			# Set number flag to false after space
			number_flag = False
			english_output.append(' ')
		else:
			if number_flag:
				english_output.append(braille_to_number_map[symbol])
			elif capital_flag:
				# Capitalize braille converted character
				upper_char = braille_to_english_map[symbol].upper()
				english_output.append(upper_char)
				# Only capitalize first character
				capital_flag = False
			else:
				english_output.append(braille_to_english_map[symbol])

	return ''.join(english_output) 

def english_to_braille(english_input: str) -> str:
	braille_output = []
	# Track first number in input
	number_flag = False

	for char in english_input:
		if char.isdigit():
			# Add 'number follows' after detecting first digit
			if number_flag is False:
				# Only set number flag for first digit
				number_flag = True
				braille_output.append(english_to_braille_map['number_follows'])
			braille_output.append(number_to_braille_map[char])

		else:
			# Not a digit, set number flag to False
			number_flag = False
			if char.isupper():
				braille_output.append(english_to_braille_map['capital_follows'])
				char = char.lower()
			braille_output.append(english_to_braille_map[char])
	
	return ''.join(braille_output)

def translate(text: str) -> str:
	if is_braille(text):
		return braille_to_english(text)
	elif is_english(text):
		return english_to_braille(text)
	else:
		raise ValueError('Error: input outside of given Braille/English alphabet')
	
def main():
	if len(sys.argv) < 2:
		print('Error: missing English/Braille input')
		sys.exit(1)

	input_text = ' '.join(sys.argv[1:])
	translation = translate(input_text)
	print(translation)

if __name__ == '__main__':
	main()
