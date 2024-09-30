import sys

# could definitely merge into one map, but feel like this is easier to read/maintain
# especially when reversing key:values for braille to english translations
	# there could be duplicates if it was all one map

letters = {
	'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
	'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
	'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
	'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
	'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
	'z': 'O..OOO'
}

numbers = {
	'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
	'6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

symbols = {
	'.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
	';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
	'(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

flags = {
	'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
}

# if braille -- 
	# (string length mod 6) == 0
	# string will only contain "." or "O"
def is_braille(txt):
	if ((len(txt) % 6) != 0):
		return False
	for char in txt:
		if ((char != '.') and (char != 'O')):
			return False
	return True

def english_to_braille(txt):
	txt_in_braille = ""
	numeric_flag = False

	# 'decimal follows' flag?
	# ambiguous in the spec

	# according to actual braille language -- 
	# if something like 0.50 -- just add the decimal point in between
	# if .50 -- numeric mode flag -> decimal point -> numbers

	# according to spec -- 
	# 'When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.'
		# ^ probably means not to worry about it
		# if we assume only true for braille to english, converting the same thing back-and-forth would be messed up
		# i'll leave it unimplemented for now 

	for char in txt:
		if (char.isdigit()):
			if (numeric_flag == False):
				numeric_flag = True
				txt_in_braille += flags['number'] + numbers[char]
			else:
				txt_in_braille += numbers[char]
			continue

		if (char.islower()):
			txt_in_braille += letters[char]
		elif (char.isupper()):
			txt_in_braille += flags['capital'] + letters[char.lower()]
		elif (char in list(symbols.keys())):
			txt_in_braille += symbols[char]
		else:
			sys.exit('Invalid character in input')

	return txt_in_braille
		

		
		

def main():
	input_arr = sys.argv[1:]
	if not input_arr:
		sys.exit('Invalid input')
	input_str = ' '.join(input_arr)
	if (is_braille(input_str)):
		print("Not implemented yet")
	else:
		print(english_to_braille(input_str))

if __name__ == "__main__":
	main()
    