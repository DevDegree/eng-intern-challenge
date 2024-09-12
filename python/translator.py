# Braille <-> English translator in Python by Syed Asad Hussian 
# Steps: 	
	# 1. Read in runtime arg
  # 2. Determine if the arg is valid 
	# 3. If invalid arg, return 
	# 4. If valid, determine if the arg is English or Braille
	# 5. If English, output translated corresponding Braille
	# 6. Else, output translated corresponding English

# notes: 
# 	1. A bidirectional dict to store Braille <-> English mappings would have
# 		 worked best in this case, however, I did not use an external library for it
# 		 just in case it wasn't allowed
# 	2. A valid Braille MUST be semantically and syntactically valid to some degree
# 		 i.e if a B_CAPITAL_FOLLOWS symbol exists, then the next symbol must be an alphabet
# 	3. Not checking if english word/sentence is valid semantically and syntactically

import sys

# Braiile "constants"
B_CAPITAL_FOLLOWS = '.....O'
B_DECIMAL_FOLLOWS = '.O..O'
B_NUMBER_FOLLOWS = '.O.OOO'
B_SPACE = 	'......'
B_CHARS = {'.', 'O'}

B_ALPHA = {
  'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
  'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
  '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
	'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
  'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
  'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
  'OO.OOO': 'y', 'O..OOO': 'z'
}

B_NUM = {
  'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 
  'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
  '.OO...': '9', '.OOO..': '0'
}

B_SPECIAL = {
  '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
  '..OO..': ':', '..O.O.': ';', '....OO': '_', '.O..O.': '/',
	'.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')'
}

# English constants
E_ALL = {
	'.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',  
  ';': '..O.O.', '_': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', 
	'(': 'O.O..O', ')': '.O.OO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....',  
	'4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
  '9': '.OO...', '0': '.OOO..', 'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
  'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
  'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 
  'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
	's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 
  'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', ' ': '...... '
}


# check valid  for braille
def check_valid_braille(contender_braille):
	return (
		len(contender_braille) % 6 == 0 and 
		all(char in B_CHARS for char in contender_braille)
	)
	
# convert braille to english
def convert_to_english(braille):
	english = ''
	i = 0
	next_capital = False
	next_number = False
	next_decimal = False

	for i in range(0, len(braille), 6):
		current_braille = braille[i: i + 6]

		if (current_braille == B_CAPITAL_FOLLOWS):
			next_capital = True
		elif (current_braille == B_NUMBER_FOLLOWS):
			next_number = True
		elif (current_braille == B_DECIMAL_FOLLOWS):
			next_decimal = True
		elif next_capital:
			if current_braille in B_ALPHA:
				english += B_ALPHA[current_braille].upper()
				next_capital = False
			else:
				return None
		elif next_decimal:
			english +=  '.'
			next_decimal = False
		elif next_number:
			if current_braille in B_NUM:
				english += B_NUM[current_braille]
			else:
				return None
		else: 
			if current_braille in B_ALPHA:
				english += B_ALPHA[current_braille]
			elif current_braille in B_SPECIAL:
				english += B_SPECIAL[current_braille]
			elif current_braille == B_SPACE:
				english += ' '
				next_number = False
			else:
				return None
			
	return english

# check valid english
def check_valid_english(contender_english):
	# Assume valid english for this project 
	return True

# convert english to braille
def convert_to_braille(english):
	brialle = ''
	added_number_symbol = False

	for char in english:
		if char.isalpha():
			if char.isupper():
				# assume 26 alphabet english, the character must be in E_ALL
				brialle += B_CAPITAL_FOLLOWS + E_ALL[char.lower()]
			else:
				brialle += E_ALL[char.lower()]
		elif char.isdigit():
			if added_number_symbol:
				brialle += E_ALL[char]
			else:
				brialle += B_NUMBER_FOLLOWS + E_ALL[char]
				added_number_symbol = True
		elif char == ' ':
			brialle += B_SPACE
			added_number_symbol = False
		elif char == '.' and added_number_symbol: 
			# this check is for decimal follows
			brialle += B_DECIMAL_FOLLOWS
		elif char in E_ALL:
			#check if char is a special symbol
			brialle += E_ALL[char]
		else:
				return None
			
	return brialle


def main():    
	# error checking
	if len(sys.argv) < 2:
		print('No input given!')
		sys.exit(1)

	arg = ' '.join(sys.argv[1:])

	#check if input is braille
	if check_valid_braille(arg):
		english = convert_to_english(arg)
		if english is None:
			print("Invalid Braille")
			sys.exit(1)
		else: 
			print(english)

	else:
		# valid input can only be english
		if check_valid_english(arg):
			braille = convert_to_braille(arg)

			if braille is None:
				print("Invalid English")
				sys.exit(1)
			else:
				print(braille)
	

if __name__ == "__main__":
    main()