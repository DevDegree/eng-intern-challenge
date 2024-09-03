import sys

alpha_to_braille = {
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
}

braille_to_alpha = {v: k for k, v in alpha_to_braille.items()}

numberic_to_braille = {
	'1': 'O.....',
	'2': 'O.O...',
	'3': 'OO....',
	'4': 'OO.O..',
	'5': 'O..O..',
	'6': 'OOO...',
	'7': 'OOOO..',
	'8': 'O.OO..',
	'9': '.OO...',
	'0': '.OOO..',
}

braille_to_numeric = {v: k for k, v in numberic_to_braille.items()}

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE = '......'

# Set of all valid Braille characters, using hashset for O(1) lookup as number of braille characters could potentially increase (symbols, punctuation, etc.) 
valid_braille = set(list(alpha_to_braille.values()) + list(numberic_to_braille.values()) + [CAPITAL_FOLLOWS, NUMBER_FOLLOWS, SPACE])

def parse_args():
	if len(sys.argv) < 2:
		print('Usage: python translator.py <string to convert>')
		sys.exit(1)
	return ' '.join(sys.argv[1:])

def is_braille(string_to_check):
	if len(string_to_check) % 6 != 0:
		return False
	
	# Check if all characters are valid Braille characters
	# Don't use hashset for this as the number of valid characters is small
	allowed_chars = ['.', 'O']
	
	for c in set(string_to_check):
		if c not in allowed_chars:
			return False
		
	for i in range(0, len(string_to_check), 6):
		if string_to_check[i:i+6] not in valid_braille:
			return False

	return True

def braille_to_english(braille):
	english = []
	currently_number = False
	should_capitalize = False

	for i in range(0, len(braille), 6):
		braille_char = braille[i:i+6]

		if braille_char == SPACE:
			currently_number = False
			english.append(' ')
		elif braille_char == NUMBER_FOLLOWS:
			currently_number = True
		elif braille_char == CAPITAL_FOLLOWS:
			should_capitalize = True
		elif currently_number:
			english.append(braille_to_numeric[braille_char])
		elif should_capitalize:
			english.append(braille_to_alpha[braille_char].upper())
			should_capitalize = False
		else:
			english.append(braille_to_alpha[braille_char])
	
	return ''.join(english)

def english_to_braille(english):
	braille = []
	currently_number = False
	
	for i, c in enumerate(english):
		if c == ' ':
			braille.append(SPACE)
			currently_number = False
		elif c.isdigit():
			if not currently_number:
				braille.append(NUMBER_FOLLOWS)
				currently_number = True
			braille.append(numberic_to_braille[c])
		elif c.isalpha():
			if c.isupper():
				braille.append(CAPITAL_FOLLOWS)
				braille.append(alpha_to_braille[c.lower()])
			else:
				braille.append(alpha_to_braille[c])
		else:
			return f'Invalid character {c} at position {i}'
	
	return ''.join(braille)
		
def translate(string_to_convert):
	if is_braille(string_to_convert):
		try:
			return braille_to_english(string_to_convert)
		except:
			# if we ever encounter a Braille character in an incorrect position, assume the original string was in English
			# for example, if we encounter a Z after a NUMBER_FOLLOWS, we should assume the original string was in English
			return english_to_braille(string_to_convert)
	else:
		return english_to_braille(string_to_convert)


if __name__ == '__main__':
	string_to_convert = parse_args()
	translated_string = translate(string_to_convert)
	print(translated_string)
	
